"""Generate short, synthetic HR policy PDFs for local development."""

from pathlib import Path

import fitz


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "sample_docs"

POLICIES = {
    "leave_policy.pdf": [
        (
            "Leave Policy",
            "Purpose and request process",
            "This fictional policy explains how team members request planned time away. "
            "Submit a request to the scheduling desk at least five working days before "
            "the first day away when practical. The desk records the request and replies "
            "with an approval or a request for clarification.",
        ),
        (
            "Leave Policy",
            "Unexpected absence and return",
            "For an unexpected absence, notify the scheduling desk as soon as reasonably "
            "possible using the usual team contact channel. Share only the expected "
            "availability date; medical details are not required. On return, check the "
            "team calendar and coordinate any handoff with a colleague.",
        ),
    ],
    "remote_work_policy.pdf": [
        (
            "Remote Work Policy",
            "Work location and availability",
            "This fictional policy allows eligible team members to work remotely when "
            "their duties can be completed securely off site. Keep the team calendar "
            "current, join scheduled meetings on time, and let the team lead know when "
            "your working location changes during the day.",
        ),
        (
            "Remote Work Policy",
            "Equipment and information",
            "Use approved devices and a private network connection for work systems. "
            "Store work files only in the designated workspace, lock the screen when "
            "away, and report a lost device or suspected information exposure promptly "
            "to the service desk.",
        ),
    ],
    "expenses_policy.pdf": [
        (
            "Expenses Policy",
            "Eligible purchases",
            "This fictional policy covers reasonable costs made for an assigned work "
            "activity. Get manager approval before making a purchase when approval is "
            "practical. Personal items, fines, and costs unrelated to an assigned "
            "activity are not reimbursable.",
        ),
        (
            "Expenses Policy",
            "Submitting a claim",
            "Submit a claim through the expense desk with the date, business purpose, "
            "amount, and an itemized receipt. If a receipt is unavailable, include a "
            "short explanation. The desk may ask for clarification before recording "
            "the claim as complete.",
        ),
    ],
    "code_of_conduct.pdf": [
        (
            "Code of Conduct",
            "Respectful collaboration",
            "This fictional code asks everyone to communicate respectfully, make room "
            "for different viewpoints, and address disagreements about work without "
            "personal attacks. Give feedback privately when possible and focus on "
            "specific actions and their effect on the work.",
        ),
        (
            "Code of Conduct",
            "Raising a concern",
            "If you see conduct that may conflict with this code, raise the concern "
            "with a team lead or the fictional people support desk. Share relevant "
            "facts and dates, and avoid circulating sensitive details more widely "
            "than needed to address the concern.",
        ),
    ],
}


def make_policy_pdf(path: Path, pages: list[tuple[str, str, str]]) -> None:
    """Write a PDF with one policy section on each page."""
    document = fitz.open()
    for page_number, (title, heading, body) in enumerate(pages, start=1):
        page = document.new_page()
        page.insert_text((72, 72), title, fontsize=20)
        page.insert_text((72, 112), heading, fontsize=14)
        page.insert_textbox(
            fitz.Rect(72, 140, 520, 360), body, fontsize=11, lineheight=1.4
        )
        page.insert_text((72, 760), f"Synthetic sample · Page {page_number}", fontsize=9)
    document.save(path)
    document.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, pages in POLICIES.items():
        make_policy_pdf(OUTPUT_DIR / filename, pages)
        print(f"Created {OUTPUT_DIR / filename}")


if __name__ == "__main__":
    main()
