"""Extract page-aware text chunks from PDF files."""

import argparse
from pathlib import Path
from typing import TypedDict

import pymupdf as fitz


class Chunk(TypedDict):
    text: str
    source: str
    page: int


def split_text(text: str, chunk_size: int = 500, overlap: int = 80) -> list[str]:
    """Split text near word boundaries, retaining a target overlap between chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    text = text.strip()
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        if end < len(text):
            boundary = text.rfind(" ", start, end + 1)
            if boundary > start:
                end = boundary

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break

        next_start = max(start + 1, end - overlap)
        # Move to the start of a word so neither edge cuts through one.
        while next_start < end and not text[next_start - 1].isspace():
            next_start += 1
        start = next_start

    return chunks


def extract_chunks(folder: str | Path, chunk_size: int = 500, overlap: int = 80) -> list[Chunk]:
    """Extract text from each PDF page and return chunks with file/page metadata."""
    folder = Path(folder)
    chunks: list[Chunk] = []
    for pdf_path in sorted(folder.glob("*.pdf")):
        with fitz.open(pdf_path) as document:
            for page_number, page in enumerate(document, start=1):
                for text in split_text(page.get_text(), chunk_size, overlap):
                    chunks.append(
                        {"text": text, "source": pdf_path.name, "page": page_number}
                    )
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract chunks from PDFs in a folder.")
    parser.add_argument("folder", type=Path, help="Folder containing PDF files")
    parser.add_argument("--show", type=int, default=0, metavar="N", help="Print N sample chunks")
    args = parser.parse_args()
    if args.show < 0:
        parser.error("--show must be non-negative")

    chunks = extract_chunks(args.folder)
    counts = {pdf_path.name: 0 for pdf_path in sorted(args.folder.glob("*.pdf"))}
    for chunk in chunks:
        counts[chunk["source"]] = counts.get(chunk["source"], 0) + 1
    for source, count in counts.items():
        print(f"{source}: {count} chunks")
    print(f"Total: {len(chunks)} chunks")

    for chunk in chunks[: args.show]:
        print(f"\n[{chunk['source']} p. {chunk['page']}]\n{chunk['text']}")


if __name__ == "__main__":
    main()
