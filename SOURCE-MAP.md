# Training source map

The authoritative sources are the supplied Spanish documents. All page numbers are **1-based PDF page numbers**, which match the printed page numbering for the cited material.

| Key | Reference document | Edition |
| --- | --- | --- |
| training | ATENCIÓN AL CLIENTE_FORMACIÓN 2026 (1).pdf | October 2026; 37 pages |
| manual | Manual Atención al Cliente de Playmobil Ibérica_v03 (1).pdf | January 2026; 39 pages |

The original PDFs and private extraction files are reference material, not deployment assets. The newer training governs updated general rules; the manual supplies consistent operational detail. See [AUDIT.md](AUDIT.md) for the unresolved contradictions and explicit exclusions from scoring.

## Presentation facts

| Section | Subject | Reference pages |
| --- | --- | --- |
| 1 | Welcome and project identity | Presentation framing; no scored policy |
| 2 | Regular range 6–8 working days; spare parts up to 10 weeks | training 6 |
| 3 | Shipping charges and conditional free-shipping promotions | training 6; manual 3; exact boundaries not scored |
| 4 | Purchase, dispatch and carrier messages; return handling | training 7–9, 33; deadline conflict excluded |
| 5 | Sales organizations, order types and payment terms | training 16; manual 10 |
| 6 | ZTA3 claim sequence | training 17 |
| 7 | Existing-customer search | training 18; manual 12–14 |
| 8 | New customer details | training 19; manual 11–12 |
| 9 | ZTA3 entry | training 20; manual 14–16 |
| 10 | Registering a claim and replying | training 21; manual 35 |
| 11 | ZTAC overview and email-order limits | training 16, 22 |
| 12 | Customer check for ZTAC | training 23; manual 12–14 |
| 13 | New customer for an order | training 24; manual 11–12 |
| 14 | ZTAC entry and payment hold | training 25; manual 17–18 |
| 15 | ZTAC output/quotation controls | training 26; manual 18–19 |
| 16 | Quotation with Terms and Conditions | training 27; manual 33–34 |
| 17 | Bank transfer confirmation and 24-hour payment link | training 28; manual 29–31, 33–34 |
| 18 | Modifying pending orders; restoring payment hold | training 29; manual 22 |
| 19 | Payment-link email and automatic validation | training 30; manual 29–31; October specific rule takes precedence |
| 20 | Response templates and escalation | training 10–11, 31 |
| 21 | Transport incidents and unguaranteed address requests | training 32; manual 32, 35; cancellation deadline not treated as settled |
| 22 | Return reasons, damage reported at delivery, company-paid MRW collection | training 33; disputed cancellation deadline excluded |
| 23 | ZG2R creation with invoice reference | training 34; manual 24–25 |
| 24 | Completing and recording a credit note | training 35; manual 26–27 |
| 25 | Shipment tracking in SAP | training 36; manual 22–24 |
| 26 | Calls, emails and website awareness | manual 2 |
| 27 | Promotion exclusions and telephone restrictions | manual 2–3 |
| 28 | Essential delivery, payment, order and spare-part rules | training 6, 16; manual 3; disputed return deadline excluded |
| 29 | SAC email statistics and Outlook searches | manual 3–4 |
| 30 | VA14L Spain search and removing amount-check delivery block | manual 4–5 |
| 31 | Portugal Z1/Z0 checks; complete daily matrix | manual 6 |
| 32 | Accounting reports and blocked customers | manual 6–7 |
| 33 | VA05 review, ZTAI/RE, same-content ZTA3 and refund checks | manual 8–9, 24 |
| 34 | November–January priorities | training 12; manual 10 |
| 35 | February–October priorities | training 13; manual 10 |
| 36 | Closing and original author credit | Presentation framing; no scored policy |
| 37 | L2 correction and original-invoice reference | manual 27–29 |
| 38 | Demandware investigation, ERROR/CREADO and customer blocks | manual 36–37; financial disposition and promotional recovery not scored |
| 39 | Reactivating an unused code from a failed/unconfirmed attempt | manual 38 |
| 40 | Validation and operational exceptions | training 28–30; manual 14, 22, 31 |

## Assessment items

The bank has 28 questions in seven groups of four. The application selects exactly 20 per attempt and shuffles using stable option IDs. Options are distractors, not additional policy claims. The same IDs, answers and references apply in EN, ES and SR.

| Item ID | Topic | Reference | Training section |
| --- | --- | --- | --- |
| q-delivery-regular | Regular-range delivery | training 6 | 2 |
| q-delivery-parts | Spare-parts delivery | training 6 | 2 |
| q-delivery-mainland-fee | Standard mainland charge, before promotion | training 6 | 3 |
| q-delivery-islands-fee | Standard listed territory charge | training 6 | 3 |
| q-sap-claim | ZTA3 | training 16 | 5 |
| q-sap-portugal | 2095 | training 16 | 5 |
| q-sap-free | DE22 | training 16 | 5 |
| q-sap-order-type | ZTAC | training 16, 22 | 11 |
| q-payment-link-life | Payment-link validity | training 28 | 17 |
| q-payment-bank-confirmation | Accounting confirmation before release | training 28 | 17 |
| q-payment-link-validation | Automatic link validation; no manual removal | training 30 | 19 |
| q-payment-web | Website payment methods | manual 3 | 28 |
| q-email-references | Maximum 40 distinct references | training 16, 22 | 11 |
| q-email-units | Maximum 20 units per reference | training 16, 22 | 11 |
| q-email-promotion | General email-order promotion exclusion | training 16 | 28 |
| q-email-quotation | Terms and Conditions with quotation | training 27 | 16 |
| q-operations-block-search | VA14L daily checks | manual 4–6 | 30 |
| q-operations-customer-block | Accounting handles customer blocking | manual 7 | 32 |
| q-operations-demandware | Advanced search when SAP order is missing | manual 36 | 38 |
| q-operations-code-reactivation | Unused code from failed attempt | manual 38 | 39 |
| q-refunds-history | VA05 and two-month lookback | manual 8 | 33 |
| q-refunds-replacement | Same-content free replacement prevents refund; L2 | manual 9 | 33 |
| q-refunds-l2 | Correct duplicate credit using L2 | manual 27–29 | 37 |
| q-refunds-damage | Damage reported at delivery; return costs | training 33 | 22 |
| q-priorities-christmas | December tracking: priority 1 | manual 10 | 34 |
| q-priorities-regular | May missing part: priority 1 | manual 10 | 35 |
| q-priorities-phone | Website/email for personal order details | manual 3 | 27 |
| q-priorities-safety | Accident/danger escalation | training 31 | 20 |

## Game items

### SAP Memory Match

| Item ID | Code and meaning | Reference | Section |
| --- | --- | --- | --- |
| mem-zta3 | ZTA3 — claim | training 16 | 5 |
| mem-ztac | ZTAC — spare-parts/DS order | training 16 | 5 |
| mem-zg2r | ZG2R — credit note | training 16 | 5 |
| mem-l2 | L2 — invoice | training 16 | 5 |
| mem-de22 | DE22 — free of charge | training 16 | 5 |
| mem-de01 | DE01 — bank transfer | training 16 | 5 |
| mem-pbyl | PBYL — payment by link | training 16 | 5 |
| mem-va14l | VA14L — delivery-block search | manual 4 | 30 |

### Build the Workflow

Only explicitly ordered source sequences are used. `answer` contains stable step IDs in source order; the UI may shuffle the steps, never the answer.

| Item ID | Correct sequence | Reference | Section |
| --- | --- | --- | --- |
| workflow-claim | Check/create customer → enter ZTA3 → record claim → reply | training 17 | 6 |
| workflow-quotation | Check/create customer → enter ZTAC → send quotation and T&C | training 22, 27 | 11 |
| workflow-delivery-block | VA14L search → open result → remove amount-check delivery block and save → return and save | manual 4–5 | 30 |

The quotation overview does not replace the detailed requirement to hold an unpaid order. The VA14L delivery block is distinct from the `Operación por aclarar` rejection reason used for unpaid manual orders.

### SAC Inbox Challenge

All messages are fictional and contain no personal records.

| Item ID | Correct action | Reference | Section |
| --- | --- | --- | --- |
| inbox-missing-part | Customer check and ZTA3 procedure | training 17 | 6 |
| inbox-phone-order | Direct personal order details to website/email | manual 3 | 27 |
| inbox-address | Forward to carrier without guaranteeing change | training 32 | 21 |
| inbox-danger | Escalate to SAC supervisor | training 31 | 20 |
| inbox-missing-order | Demandware history and customer-block investigation | manual 36–37 | 38 |

### Christmas Rush

Every ticket references manual page 10 (and presentation sections 34–35). The two seasonal answers are explicit in the data.

| Item ID | Category | November–January | February–October |
| --- | --- | --- | --- |
| ticket-tracking | Purchase/delivery | 1 | 2 |
| ticket-promotion | Purchase/delivery | 1 | 2 |
| ticket-delivery | Purchase/delivery | 1 | 2 |
| ticket-missing | After-sales | 2 | 1 |
| ticket-defective | After-sales | 2 | 1 |
| ticket-spares | After-sales | 2 | 1 |
| ticket-return | After-sales | 2 | 1 |
| ticket-other | Other requests | 3 | 3 |

### SAP Simulator

These are fictional exercises. They do not connect to SAP and require only documented fields. Spanish interface names are retained alongside localized explanations.

| Item ID | Correct fields | Reference | Section |
| --- | --- | --- | --- |
| sim-spain-z1 | VA14L; sales organization 2090; block Z1; channel 01; division 01 | manual 4–5 | 30 |
| sim-portugal-z0 | VA14L; sales organization 2095; block Z0; channel 01; division 01 | manual 4–6 | 31 |
| sim-free-claim | Type ZTA3; sales organization 2090; payment DE22 | training 16 | 5 |

### Refund Detective

The scenario wording states whether an existing credit needs compensation. This distinguishes “prevent an incorrect refund” from the full L2 correction without allowing two correct options.

| Item ID | Evidence and correct decision | Reference | Section |
| --- | --- | --- | --- |
| refund-valid-return | ZTAI + RE, no previous refund/credit or same-content replacement → request refund | manual 8–9 | 33 |
| refund-replacement | Same-content ZTA3 already sent and credit needing compensation → L2, tell Accounting not to refund and record correction | manual 9 | 33 |
| refund-duplicate-credit | SAC credit plus later German duplicate → L2 with original invoice reference | manual 27–29 | 37 |
| refund-free-claim | Returned free ZTA3, no customer payment and no duplicate credit → prevent an incorrect refund | manual 24 | 33 |

### Rapid Fire

Rapid Fire reuses the shared `questions` bank. Each item retains its assessment ID, stable answer, localized explanation and source pages listed above. It does not introduce separate unreferenced rules.

## Data maintenance and scoring exclusions

All 59 top-level scored items have an ID, topic, section, source, correct answer and EN/ES/SR explanations. Question, inbox and investigation options use stable IDs. Workflows use stable step IDs. Simulator fields have stable IDs and answers; memory pairs match their item ID; tickets map the season to a numeric priority.

Excluded from scored content: disputed cancellation/return deadlines, exact free-shipping boundaries, unresolved Demandware authorization-hold/refund disposition, recovery promotions, personal contacts, real customer/order identifiers and private financial details. New content must meet the same source and localization checks before it is added.
