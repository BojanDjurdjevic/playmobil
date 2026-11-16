# Screenshot source and privacy review

All page references are one-based PDF pages. Original references are `ATENCIÓN AL CLIENTE_FORMACIÓN 2026 (1).pdf` (October 2026) and `Manual Atención al Cliente de Playmobil Ibérica_v03 (1).pdf` (January 2026).

The 19 original PNG assets and 13 new manual PNGs were visually inspected at readable size. Customer names, customer/order/invoice/shipment identifiers, addresses, personal emails, telephone numbers, card details, transaction values, staff usernames and personal contact details were permanently covered in raster pixels. Report rows and operational counts were removed where they were unnecessary for the lesson. Masks are solid opaque fills, not blur, CSS, overlay elements or reversible PDF annotations. PNG files were saved as fresh RGB pixel images without source metadata.

SAP transaction codes, field labels, organizational codes, document types, generic status descriptions and useful arrows were retained. Blank form fields are unchanged. The screenshots retain the real Spanish interface; localized captions and explanations belong in the presentation. No fictional SAP screenshots were generated.

## Original assets

Every filename below is in `assets/`. Original image paths remain valid. Pages 18–21 were reconstructed from the PDF at 3× rendering scale because the input images cut off parts of the workflow. The others retain their original source resolution and are cropped around the useful screenshot regions.

| Filename | October page | Retained content / removal |
| --- | --- | --- |
| sap-page-18.png | 18 | Complete customer lookup workflow; customer table rows, surname search and postal search value masked. |
| sap-page-19.png | 19 | Complete empty customer creation form; no populated personal fields. |
| sap-page-20.png | 20 | Complete ZTA3 workflow; customer values, address and saved document number masked. |
| sap-page-21.png | 21 | Claim registration headers and reply; customer list, recipient and claim identifier masked. |
| sap-page-22.png | 22 | Customer email cropped; sender identity and contact/signature block masked. Product references retained. |
| sap-page-23.png | 23 | Customer lookup; populated rows and search values masked. |
| sap-page-24.png | 24 | Empty creation form; no populated personal fields. |
| sap-page-25.png | 25 | ZTAC controls and rejection reason; customer identifiers and financial values masked. |
| sap-page-26.png | 26 | Quotation message controls; customer IDs, staff usernames and values masked. |
| sap-page-27.png | 27 | Quotation/email example; customer, document and address fields, attachment name and financial line items masked. |
| sap-page-28.png | 28 | Payment instructions table; personal staff contact details masked. Not required by current HTML. |
| sap-page-29.png | 29 | Modification controls; IDs and values masked. Lower source prose cropped out because the payment-link qualification is handled in corrected localized text. |
| sap-page-30.png | 30 | Payment-link controls; title/field IDs, names, address fragments and values masked. |
| sap-page-31.png | 31 | Response guidance; named staff contact masked. Not required by current HTML. |
| sap-page-32.png | 32 | Carrier table; contact values masked. Not required by current HTML; omit from deployment if unused. |
| sap-page-33.png | 33 | Blank return form only; contact block masked and conflicting deadline prose excluded by crop. Not required by current HTML. |
| sap-page-34.png | 34 | Credit-note steps 1–4; customer, invoice and saved document IDs, addresses, financial rows and associated dates masked. |
| sap-page-35.png | 35 | Credit-note steps 5–8; IDs, customer information, values and personal staff contacts masked. |
| sap-page-36.png | 36 | Shipment search and tracking controls; document, customer and tracking IDs, addresses and populated report values masked. |

## New manual crops

All are in `assets/manual/` and rendered at 3× scale before cropping. PDF images may themselves have limited native detail; upscaling does not invent new field detail.

| Filename | January page | Presentation section | Retained content / removal |
| --- | --- | --- | --- |
| sac-statistics.png | 3 | 29 | Statistics worksheet labels/grid; dates, operational counts, totals and averages masked. |
| outlook-previous-day-search.png | 4 | 29 | Outlook date filter with Ayer; message rows excluded. |
| va14l-command.png | 4 | 30 | VA14L command and original arrow. |
| va14l-search-parameters.png | 4 | 30 | Z1, 2090, channel 01 and division 01 with original arrows; blank customer fields. |
| va14l-blocked-orders.png | 5 | 30 | Blocked results headers and block type; customer/order IDs, dates and financial values masked. |
| va14l-remove-delivery-block.png | 5 | 30 | Bloqueo entrega / Comprobación importe and arrows; IDs in titles/fields, names, addresses, card values/expiry and financial rows masked. |
| va14l-save-modified-order.png | 5 | 30 | Original green-button arrow and report controls; populated customer/order/value data masked. |
| va14l-portugal-z0.png | 6 | 31 | Z0 and 2095 example, channel 01, division 01. The text explains repeating Z1 too; no fabricated Z1 screenshot. |
| accounting-report-inbox.png | 6 | 32 | Report subject types; sender identifiers, dates and sizes masked. |
| accounting-block-report.png | 7 | 32 | Report headers, generic statuses, counterpart-error phrase and original arrow; invoice/tax identifiers, names and dates masked. |
| cancellation-report.png | 8 | 33 | Selection headers, organizations, RE document type; document/customer IDs, names, counts, dates and monetary values masked. |
| va05-cancellation-check.png | 8 | 33 | VA05 command; no customer data in this crop. |
| va05-refund-verification.png | 9 | 33 | VA05 list headers and RE/ZTAI document types; customer/document IDs, name, dates and financial values masked. |

## Reproducibility and deployment boundaries

`scripts/redact_assets.py` records all crop and mask rectangles. It uses Pillow and pypdfium2 only for asset maintenance, not as application dependencies. It reads local source PDFs and keeps private original images under `.audit/asset-originals/`; `.audit/` is ignored and must never be published. Re-running the script requires those private sources and is followed by a new visual review.

The deployment package must contain only reviewed referenced PNG files, HTML, CSS, JavaScript and necessary public vendor assets. Do not deploy the original PDFs, `.audit/`, review intermediates, private backups or repository history. A `.gitignore` rule does not remove files already tracked in Git or past commits. The original repository history may still contain unredacted assets and internal PDFs; review that history before making a repository public.

The remaining screenshots disclose internal SAP structure, report names and operational workflow even after personal data removal. Redaction does not grant permission to distribute internal training or PLAYMOBIL material publicly. Human review of intended audience and confidentiality remains necessary before any publication. No publication was performed by this asset task.

## Checks performed

- Visually reviewed every original asset before editing and every resulting asset after masking; refined masks around table rows and window-title identifiers.
- Visually reviewed all 13 manual crops against their source pages, including arrows and SAP field labels.
- Decoded every final PNG and checked fresh RGB mode and absence of PNG metadata.
- Cropped source slide 29 to prevent its general payment-link prose from conflicting with the specific October page 30 rule.

No automated OCR certification or external privacy review was performed. This is a documented visual redaction review, not a claim that internal material is approved for public hosting.
