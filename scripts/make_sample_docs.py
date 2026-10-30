"""Generate detailed, synthetic HR policy PDFs for Aster Vale Works."""

from pathlib import Path

import pymupdf as fitz


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "sample_docs"
COMPANY = "Aster Vale Works Pvt. Ltd."

# Each body is kept within the requested per-page range and printed as selectable text.
POLICIES = {
    "leave_policy.pdf": (
        "Leave Policy",
        [
            (
                "1. Leave year, eligibility and balances",
                """1.1 The leave year at Aster Vale Works Pvt. Ltd. runs from 1 January through 31 December. This policy applies to regular full-time and part-time employees on the India payroll. Agency workers, consultants and fixed-term trainees use the time-off terms in their signed engagement letter; they do not receive the balances below unless that letter says otherwise.

1.2 Regular employees accrue leave from their joining date. They may first use accrued leave after completing 90 calendar days of continuous service. The annual paid balances for a full leave year are:
Type                 Days per year        Main use
Annual leave         18                   Planned personal time away
Sick leave           10                   Illness or medical recovery
Personal leave       3                    Urgent personal matters

1.3 Part-time balances are prorated to the employee's scheduled workdays and shown in the People Support Desk record. Company-declared public holidays and weekly rest days are not deducted from a leave balance. A half-day absence of four scheduled hours or less uses one half-day; a longer absence uses one full day.

1.4 Annual leave accrues at 1.5 days per completed month, up to 18 days in the leave year. Sick and personal leave are credited on 1 January for eligible employees and are prorated for a joining year. Balances are not cash advances: a request cannot use days that have not accrued or been credited. Employees should check the balance before making non-refundable plans.

1.5 The employee portal is the official balance record. If it differs from a payslip or calendar entry, send the dates and screenshot to people@astervaleworks.example. The People Support Desk confirms a correction in writing; a manager's calendar entry alone does not change the recorded balance.""",
            ),
            (
                "2. Notice, submission and approval",
                """2.1 Submit each request in the employee portal and identify the leave type, first and last day, and any handoff plan. For annual leave, give at least five working days' notice for one to five consecutive workdays and ten working days' notice for six to ten days. Requests longer than ten consecutive workdays need 20 working days' notice and the additional approval in section 3. Notice is a planning rule, not an automatic approval.

2.2 Give at least two working days' notice for personal leave when the matter can be planned. For an emergency, notify the manager by the normal team channel as soon as safe, then enter the request by the end of the next working day. A request is pending until the required approver records a decision in the portal. Do not treat silence or a calendar hold as approval.

2.3 Managers should decide ordinary requests within three working days. They may ask for a revised date when two people in the same coverage role would be away, a fixed customer duty would be unstaffed, or a documented deadline cannot be handed over. They must explain the scheduling reason and offer a discussion of nearby dates; they must not ask for private medical details to decide annual leave.

2.4 Employees should wait for written approval before booking travel that cannot be changed. When a request is declined, the portal records the reason and the next available dates discussed. The employee may ask the department head to review the scheduling decision within five working days. The department head replies within five working days or gives an expected decision date.

2.5 A change to approved dates is a new request. Submit it as soon as possible and retain the original approval until the manager confirms the change. If a public holiday or weekly rest day falls within a request, those non-working days are excluded from the balance calculation, but the full calendar span should still be shown in the portal for coverage planning.""",
            ),
            (
                "3. Limits, carry-forward and unpaid leave",
                """3.1 Approval authority is based on consecutive scheduled workdays in one request. The direct manager may approve up to five annual-leave workdays. The department head must approve six to ten days. More than ten and up to 20 consecutive days requires both the department head and the People Operations Director. Split requests that cover one continuous absence are counted together; dividing a request does not change its approval level.

3.2 At 31 December, up to five unused annual-leave days may carry into the next leave year. Carried days must be used by 31 March or they expire. No sick or personal leave carries forward, and those balances have no cash value. Payroll does not pay unused leave during employment. Any final settlement follows applicable law and the employee's written employment terms.

3.3 Once paid leave is exhausted, an employee may request unpaid leave for up to 20 scheduled workdays in a leave year. The manager and department head must both approve it; the People Operations Director must also approve more than ten days. Requests should be submitted 20 working days ahead when foreseeable. Unpaid leave is not guaranteed and may affect pay and benefit calculations under the employee's terms.

3.4 A manager cannot approve an exception to a balance or approval limit. A proposed exception must be sent to people@astervaleworks.example before the absence, with the reason and proposed dates; only the People Operations Director may approve a policy exception in writing, subject to law. No exception can waive an employee's legal rights.

3.5 If two approved absences overlap because of a later operational change, the manager should discuss options with affected employees rather than cancel silently. The People Support Desk can explain the recorded balance but does not replace the designated approver. Keep the approval message until the portal shows the final dates and balance.""",
            ),
            (
                "4. Illness, emergencies and return to work",
                """4.1 For illness, notify the manager at least one hour before the scheduled shift where possible. If symptoms arise later or make contact impractical, send notice as soon as reasonably possible. Enter sick leave in the portal within two working days after returning. State the dates and expected return date; do not include a diagnosis in a team channel or ordinary leave request.

4.2 A medical certificate may be requested only when sick leave covers more than three consecutive scheduled workdays, or when a repeated absence pattern requires a lawful review. Send documentation directly to people@astervaleworks.example, not to the wider team. The desk limits access to staff who administer leave and records only the information needed to confirm the absence period.

4.3 If an employee becomes ill during annual leave, contact the manager promptly and ask the People Support Desk whether the affected days can be reclassified as sick leave. A medical certificate covering the affected dates is required for reclassification. Until the desk confirms the change, the original annual-leave entry remains in effect. This rule does not extend a trip or create additional sick balance.

4.4 For a family or safety emergency, use personal leave if available and notify the manager as soon as it is safe. If there is no balance, ask about unpaid leave; the usual approval limits still apply. No employee must disclose unnecessary personal details to colleagues. The People Support Desk can explain the private channel for documents or a sensitive request.

4.5 On return, update the portal, confirm the first working day with the manager and review urgent handoffs. Managers must not ask an employee to work while recorded as on approved leave. Questions about a missing balance, certificate or return date go to people@astervaleworks.example. For an urgent same-day absence when the manager is unreachable, contact the department head and copy the desk after the immediate notice.""",
            ),
        ],
    ),
    "remote_work_policy.pdf": (
        "Remote Work Policy",
        [
            (
                "1. Eligibility and weekly schedule",
                """1.1 This policy applies to regular employees of Aster Vale Works Pvt. Ltd. whose duties can be performed securely away from an office. An employee becomes eligible after 90 calendar days of continuous service. Agency workers, consultants and trainees follow their signed engagement terms. Eligibility permits a request; it does not guarantee a remote day or change the employee's role, hours or place of employment.

1.2 The standard allowance is up to three remote workdays in a Monday-to-Friday workweek. The employee and manager agree fixed office anchor days for team training, equipment access and shared work. Weekly schedules should be entered in the team calendar by Thursday for the following week. A public holiday or approved leave day is not converted into a replacement remote day.

1.3 An employee may request a temporary fourth remote day for a specific week. The department head must approve it in writing before the week begins; the standard maximum remains four days. A fifth remote day is not allowed under this policy. A manager may ask for an office day when a defined duty requires physical attendance, with as much notice as reasonably practical.

1.4 New employees within their first 90 days work at the assigned office unless the department head approves a short-term exception for a documented access need. The exception must state dates, location and supervision arrangements and cannot extend beyond 30 calendar days without People Operations review.

1.5 Remote work may be performed only from the employee's approved home or another private location within India. Working from another country is prohibited without prior written approval from People Operations and the department head, plus any required immigration, tax and security review. Personal travel does not itself authorize remote work from the destination.""",
            ),
            (
                "2. Request, approval and availability",
                """2.1 Submit a recurring schedule or a one-time location change to the manager at least two working days in advance. Include the requested dates, work location, normal hours and any planned coverage change. The manager should reply within one working day. The request is not approved until the manager updates the calendar or sends written confirmation.

2.2 Managers approve up to three remote days per week when service coverage, training and access needs are met. The department head approves a fourth day for a named week. Managers may temporarily require office attendance for a client session, secure equipment task or planned team workshop; they should give two working days' notice when known in advance and explain the work need.

2.3 Remote employees keep their agreed working hours and remain reachable through the usual team channel during those hours. A meal break is recorded in the calendar if it differs from the normal team schedule. The employee should acknowledge a time-sensitive message within 30 minutes when not in a meeting or break, or set a status with a return time. This is an availability rule, not a requirement to monitor messages outside scheduled hours.

2.4 Attend scheduled meetings with working audio and a private setting. If the connection fails, call in by the approved method or notify the organizer within 10 minutes. For a planned appointment or interruption longer than one hour, tell the manager and update the calendar; use leave if the employee will not work the scheduled hours.

2.5 The manager reviews the arrangement every quarter with the employee. Review points are delivery, team coverage, equipment and any location change. A change should be discussed before the next schedule is published. If approval is declined or withdrawn, the manager records the business reason and effective date, normally at least five working days ahead except for an urgent safety or security concern.""",
            ),
            (
                "3. Workspace, equipment and information",
                """3.1 Work from a stable surface with enough privacy to prevent others from seeing screens or hearing confidential calls. Use a headset in shared spaces. Do not work from a public computer, an open public Wi-Fi network or a location where another person can view company material. If privacy cannot be maintained, pause the task and tell the manager.

3.2 Use only a company-issued or service-desk-approved device. Keep operating system updates enabled, use multi-factor authentication and lock the screen whenever leaving the workspace. Store files in the approved company workspace; do not forward work documents to a personal email, personal cloud drive or removable device. Paper notes containing work information must be kept out of view and securely destroyed when no longer needed.

3.3 A household member or visitor may not use a company device or account. Do not discuss sensitive work in a shared room or on speakerphone. Before a video call, check the visible background for documents, badges and personal information. Recording or transcription requires the same approval as an office meeting and notice to all participants.

3.4 The company supplies the standard laptop and required security tools. A monitor, keyboard or other accessory requires manager approval up to INR 15,000 per item under the Expenses Policy. Higher cost approval follows that policy before purchase. Routine home internet and electricity are personal costs and are not reimbursed unless the department head and Finance Desk approve a written exception in advance.

3.5 Report a lost device, suspected account compromise or accidental disclosure to servicedesk@astervaleworks.example immediately, and no later than one hour after discovery when feasible. Preserve relevant details and follow service desk instructions. Do not investigate by accessing another person's account or delete evidence. The service desk coordinates containment and tells the employee when normal work can resume.""",
            ),
            (
                "4. Safety, expenses and exceptions",
                """4.1 The employee is responsible for a safe home work area, including clear walkways, a suitable chair and reasonable screen height. Report a work-related injury to the manager and People Support Desk on the same working day. The company may arrange a confidential safety review with reasonable notice; the review is limited to the designated work area and does not authorize general access to the home.

4.2 A remote arrangement does not change leave, attendance or expense rules. If illness prevents work, notify the manager and record leave under the Leave Policy. If a manager requests travel to an office or work site, get the travel plan approved before booking and submit eligible costs under the Expenses Policy. A normal commute to an assigned office is not a reimbursable expense.

4.3 An employee who moves home or plans to work regularly from a different address must notify the manager and People Operations at least five working days before the change. Provide the new city and effective date through the private People Support Desk channel; do not place a full home address in a team calendar. People Operations confirms whether the location remains inside the permitted work region.

4.4 A temporary exception to the three-day schedule requires the department head's written approval. A location outside India or an exception involving restricted information also requires People Operations and security review before work begins. No manager can waive device, confidentiality or legal requirements. An exception record names the employee, dates, safeguards and approvers.

4.5 Questions about eligibility, schedule or a work-related injury go to people@astervaleworks.example. For device access, connectivity or suspected disclosure, contact servicedesk@astervaleworks.example. The employee should continue the approved office schedule while a request is under review. People Operations reviews this policy each January and records any revision date on the current controlled copy.""",
            ),
        ],
    ),
    "expenses_policy.pdf": (
        "Expenses Policy",
        [
            (
                "1. Scope, eligibility and approval limits",
                """1.1 This policy covers reasonable business purchases made by employees of Aster Vale Works Pvt. Ltd. for an assigned work purpose. Consultants and agency workers use the reimbursement terms in their engagement agreement. A purchase must have a clear business purpose, be within an approved budget and be supported by an itemized receipt. Personal costs, fines, penalties, alcohol and costs for a companion are not reimbursable.

1.2 Obtain written approval before committing company funds. Approval authority is based on the total price including taxes and delivery for one item or one related purchase:
Approver                    Maximum per purchase
Direct manager              INR 15,000
Department head             INR 75,000
Finance Director             Above INR 75,000, within approved budget

1.3 A purchase above INR 15,000 requires department-head approval; above INR 75,000 also requires Finance Director approval. The Finance Director cannot approve spending outside an approved budget; a budget change must be recorded first. Dividing one order into smaller invoices to avoid an approval limit is prohibited. A purchase with no written pre-approval is normally declined.

1.4 The approver checks business purpose, budget, price reasonableness and whether an existing company asset can be used. Approval must identify the item or trip, expected total and cost center. A chat message is acceptable only if it clearly records these details and is retained with the claim. Silence, a verbal suggestion or an approved purchase order for a different item is not approval.

1.5 Emergency safety purchases may be made only to prevent immediate harm or material damage. Notify the department head as soon as safe and submit the receipt and explanation within two working days. The emergency route does not authorize personal purchases, bypass the Finance Director's budget control or guarantee reimbursement.""",
            ),
            (
                "2. Travel, meals and local transport",
                """2.1 Obtain manager approval before booking business travel and include destination, dates, business purpose and estimated total. Air travel must be economy class and booked through the designated travel desk where available. Rail travel should use the lowest practical class that meets the schedule. A more expensive option requires department-head approval before booking and an explanation of the time or accessibility need.

2.2 For approved domestic travel, lodging is reimbursable up to INR 6,000 per night before taxes, and meals up to INR 1,200 per travel day. These are per-employee limits, not cash allowances. Submit the actual itemized cost; unused limits are not paid. A client-hosted meal counts toward the meal limit and must list attendees and business purpose. Alcohol is never reimbursable.

2.3 Local public transport and app-based rides may be claimed at actual cost when used for an approved business trip. Choose a reasonable route and attach the receipt or trip record. Personal detours, commuting between home and the assigned office, traffic fines and vehicle damage are not reimbursable. A private vehicle requires prior manager approval and a route record; mileage is reimbursed at the rate shown in the current Finance Desk schedule.

2.4 When travel plans change, tell the manager and travel desk as soon as possible. Cancellation charges caused by a company schedule change may be claimed with the original approval and revised itinerary. Charges caused by a personal change are not covered. If an employee combines personal days with a business trip, claim only the cost that would have applied to the business itinerary.

2.5 A trip estimate exceeding INR 15,000 follows the approval table in section 1 before booking. A likely total above INR 75,000 requires department-head and Finance Director approval. Do not assume that approval of the trip purpose also approves an over-limit hotel, fare or itinerary change.""",
            ),
            (
                "3. Claims, evidence and payment deadlines",
                """3.1 Submit an expense claim in the Finance Desk portal within 30 calendar days after the purchase or the final day of a trip, whichever applies. Each line must show date, merchant, amount, currency, cost center and a short business purpose. Attach an itemized receipt and the pre-approval. A card slip without item details is not sufficient when an itemized receipt is available.

3.2 If a receipt is genuinely unavailable, submit a missing-receipt declaration within the same 30-day period. State the merchant, date, amount, items and reason the receipt cannot be obtained. The manager and Finance Desk must approve the declaration. Claims above INR 2,000 without a receipt need department-head approval as well. Repeated missing receipts may result in refusal and a review of purchasing access.

3.3 Claims in foreign currency must include the original currency and amount. Finance converts the approved amount using the corporate card settlement rate or, for a personal card, the exchange rate shown on the card statement. Add the statement line with unrelated transactions redacted. Do not claim a separate conversion fee unless it appears on the statement and was incurred for the approved purchase.

3.4 The manager reviews a complete claim within five working days. Finance checks policy, receipt and budget within five further working days. If information is missing, the claim returns to the employee with a reason; the review clock restarts when the requested information is supplied. Finance pays an approved complete claim within 15 working days, subject to the regular payment cycle.

3.5 Claims submitted after 30 calendar days need a written reason and department-head approval; Finance may reject a late claim. No claim may be altered to hide a personal item or split a purchase. Keep original receipts until payment is confirmed. Questions on status, currency conversion or a missing receipt go to finance@astervaleworks.example.""",
            ),
            (
                "4. Exceptions, prohibited claims and contacts",
                """4.1 An exception to a stated meal or lodging cap must be approved by the department head before the expense is incurred. A total purchase above INR 75,000 also requires Finance Director approval under section 1. Explain the business reason and show the expected cost. An exception cannot authorize a prohibited item, unbudgeted spending or a purchase split to avoid controls.

4.2 The following are not claimable: personal shopping, home internet and electricity under the Remote Work Policy, normal commuting, gifts to public officials, alcohol, traffic or parking fines, late fees caused by personal delay, and costs for family or other companions. A customer meal may be claimed only within the INR 1,200 per-person travel-day meal limit and must record attendees, business purpose and the total amount.

4.3 Report a duplicate charge, mistaken reimbursement or suspected false receipt to finance@astervaleworks.example within two working days of discovery. Do not submit a second claim while the first is pending. Finance will advise whether to repay, correct or attach the item to an existing claim. Employees must cooperate with a reasonable audit and provide the approval, itinerary or original receipt requested.

4.4 Managers must not approve their own claim. The next-level manager approves a manager's claim, and the department head approves the next-level manager's claim. The Finance Director's own claim is reviewed by the Managing Director. Finance may hold a claim that lacks an independent approval and notify the employee of the missing reviewer.

4.5 For claim submission and payment questions, contact finance@astervaleworks.example. For a suspected misuse or pressure to bypass approval, report to the People Operations Director at people@astervaleworks.example or use the confidential concern channel in the Code of Conduct. Retaliation for raising a good-faith concern is prohibited.""",
            ),
        ],
    ),
    "code_of_conduct.pdf": (
        "Code of Conduct",
        [
            (
                "1. Respectful and safe collaboration",
                """1.1 Everyone working with Aster Vale Works Pvt. Ltd. must treat colleagues, applicants, customers and suppliers with dignity. Work discussions should address the issue, evidence and next step; insults, threats, humiliating jokes and repeated unwanted contact are not acceptable. This standard applies in the office, on calls, in work chat, at company events and during approved remote work.

1.2 Make room for colleagues to contribute. Do not interrupt repeatedly, take credit for another person's work, or exclude someone from a work discussion because of a personal characteristic. Give feedback privately where practical, describe the specific behavior or result, and invite a response. Managers must set clear expectations and correct conduct consistently, regardless of seniority or performance rating.

1.3 Disagreement about a decision is allowed. State the concern with relevant facts, listen to the response and use the assigned escalation route if the issue remains unresolved. Do not retaliate, threaten a schedule or rating change, or withhold necessary information because someone disagreed or raised a concern in good faith.

1.4 Keep work communication professional and limited to people who need the information. Do not post a colleague's private details, screenshots of confidential conversations or unverified allegations in a broad channel. If a record is needed to report a concern, preserve it and send it privately to the designated contact rather than editing, forwarding or publicly debating it.

1.5 A person who witnesses immediate risk of physical harm should contact local emergency services first, then notify the manager or People Support Desk when safe. Other concerns may be reported through the channels in section 4. A person may ask People Operations for help without first confronting the person whose conduct is in question.""",
            ),
            (
                "2. Conflicts, gifts and responsible decisions",
                """2.1 Disclose an actual, potential or perceived conflict of interest to the manager and People Operations within five working days of learning about it, and before taking a related decision. Examples include selecting a relative's business as a supplier, supervising a close family member, holding a financial interest in a bidder, or using company information for a personal opportunity. People Operations records the disclosure and may set a recusal or other safeguard.

2.2 Employees may accept an occasional modest business courtesy only when it is lawful, transparent and not intended to influence a decision. A gift, meal or event invitation worth more than INR 2,000 per giver per occasion must be declined or returned. If return is not practical, notify the People Operations Director within two working days and hand the item over for a documented disposition. Cash, gift cards and personal loans must never be accepted.

2.3 Record every accepted courtesy in the gift register within five working days, including giver, estimated value, date and business context. A manager cannot approve an exception to the INR 2,000 threshold. Any courtesy offered during a live tender, hiring decision or contract renewal must be declined regardless of value and reported to the department head.

2.4 Never offer a public official a gift, payment, favor or hospitality to obtain or retain business. Do not use a third party to do something this code prohibits. Ordinary business hospitality must be modest, related to a legitimate meeting and recorded through the Expenses Policy; reimbursement approval does not make an improper gift acceptable.

2.5 Use company property and information for authorized work. Do not copy customer lists, confidential plans or credentials to a personal account, or use them for a side business. Return devices and records when asked or when employment ends. Questions about a proposed outside role or close supplier relationship go to people@astervaleworks.example before the employee participates in the decision.""",
            ),
            (
                "3. Confidentiality, records and use of resources",
                """3.1 Access only the information needed for assigned work. Share confidential material through approved company systems with named recipients who have a business need. Verify recipients before sending, use access controls rather than public links, and follow the retention label on the record. Do not discuss restricted information in public places or leave printed material unattended.

3.2 Work records must be accurate, dated and complete enough for another authorized colleague to understand the decision. Never backdate an approval, falsify a receipt, alter a safety record or delete a record to avoid review. Correct an error by adding a dated correction and explanation through the system that owns the record.

3.3 Use company devices, accounts and funds primarily for work. Limited personal use is acceptable only when lawful, brief, does not create cost or security risk, and does not interfere with duties. Do not install unapproved software, share passwords, bypass security controls or use another employee's access. Report suspicious requests for credentials to servicedesk@astervaleworks.example.

3.4 When working remotely, follow the approved-location, device and privacy rules in the Remote Work Policy. When buying equipment or hosting a business meal, use the advance approvals and receipt requirements in the Expenses Policy. Policy references work together: a manager's verbal request does not override written spending or security controls.

3.5 If information is sent to the wrong recipient, a device is lost, or a record is exposed, notify servicedesk@astervaleworks.example immediately and no later than one hour after discovery when feasible. Preserve the message or device details and follow containment instructions. Do not conceal the incident or contact affected outsiders unless the response lead instructs you to do so.""",
            ),
            (
                "4. Raising concerns and review process",
                """4.1 Raise a concern with a manager, department head, People Operations Director or the confidential People Support Desk at people@astervaleworks.example. If the concern involves the manager, skip that person and contact another listed route. An urgent safety risk should be reported immediately; a non-urgent conduct concern should be reported within ten working days after discovery where practical.

4.2 Share dates, locations, people involved, relevant records and the outcome sought. Separate what was observed from what was heard from someone else. Do not conduct your own interviews, promise a particular outcome or circulate the report. The receiving contact acknowledges a report within two working days and normally provides an update within ten working days, even if the review is not complete.

4.3 People Operations assigns a neutral reviewer, limits access to those who need to assess or resolve the concern, and keeps a record of steps taken. The reviewer may speak separately with the reporter, the person named and relevant witnesses, and may request supporting records. The company aims to complete an ordinary review within 30 calendar days; a complex review may take longer, with an update explaining the delay.

4.4 Retaliation against someone who raises a good-faith concern, participates as a witness or asks for policy guidance is prohibited. A person who believes retaliation occurred should report it through a different contact route. Knowingly fabricated evidence or a deliberately false report may lead to corrective action, but a report is not misconduct merely because it cannot be substantiated.

4.5 Confirmed violations may result in coaching, training, a written warning, removal of access or further action consistent with law and employment terms. The company does not promise a specific outcome or disclose another person's confidential employment action. Ask people@astervaleworks.example for process questions. People Operations reviews this code each January and publishes the current revision date.""",
            ),
        ],
    ),
}


def make_policy_pdf(path: Path, title: str, pages: list[tuple[str, str]]) -> None:
    """Write a four-page policy with a short header and footer on each page."""
    document = fitz.open()
    for page_number, (heading, body) in enumerate(pages, start=1):
        page = document.new_page()
        page.insert_text((48, 34), f"{COMPANY} | {title}", fontsize=9)
        page.insert_text((48, 66), heading, fontsize=14)
        remaining = page.insert_textbox(
            fitz.Rect(48, 82, 564, 746), body, fontsize=9.5, lineheight=1.18
        )
        if remaining < 0:
            raise ValueError(f"Text does not fit on page {page_number} of {path.name}")
        page.insert_text((48, 770), f"{title} | Page {page_number} of 4", fontsize=9)
    document.save(path)
    document.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ordered_policies = sorted(
        POLICIES.items(), key=lambda item: item[0] == "remote_work_policy.pdf"
    )
    for filename, (title, pages) in ordered_policies:
        if len(pages) != 4:
            raise ValueError(f"{filename} must have exactly four pages")
        for page_number, (_, body) in enumerate(pages, start=1):
            if not 1500 <= len(body) <= 2500:
                raise ValueError(
                    f"{filename} page {page_number} body has {len(body)} characters"
                )
            print(f"{filename} page {page_number}: {len(body)} body characters")
        make_policy_pdf(OUTPUT_DIR / filename, title, pages)
        print(f"Created {OUTPUT_DIR / filename}")


if __name__ == "__main__":
    main()
