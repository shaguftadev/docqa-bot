from pathlib import Path

from rag.ingest import extract_chunks


SAMPLE_DOCS = Path(__file__).resolve().parents[1] / "data" / "sample_docs"


def test_sample_pdf_chunks_have_valid_size_and_metadata():
    chunks = extract_chunks(SAMPLE_DOCS)

    assert chunks
    assert all(0 < len(chunk["text"]) <= 500 for chunk in chunks)
    assert all(chunk["text"].strip() for chunk in chunks)
    assert all(chunk["source"].endswith(".pdf") for chunk in chunks)
    assert all(chunk["page"] >= 1 for chunk in chunks)
    assert {chunk["source"] for chunk in chunks} == {
        "leave_policy.pdf",
        "remote_work_policy.pdf",
        "expenses_policy.pdf",
        "code_of_conduct.pdf",
    }


def test_sample_pdf_pages_are_numbered_from_one():
    chunks = extract_chunks(SAMPLE_DOCS)
    pages_by_source: dict[str, set[int]] = {}
    for chunk in chunks:
        pages_by_source.setdefault(chunk["source"], set()).add(chunk["page"])

    assert pages_by_source
    assert all(pages == {1, 2, 3, 4} for pages in pages_by_source.values())
