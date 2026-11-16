# Training center audit and implementation plan

Audit completed against all 36 sections in EN, ES and SR, the 37-page October training PDF and the 39-page January manual. Page numbers below are PDF page numbers (1-based). All pages were extracted as text and rendered for visual review. Private intermediates are in `.audit/` and must never be deployed.

## Findings

- Sections 4–25 have extensive untranslated card bodies in ES/SR, hybrid titles and English image descriptions. Sections 2, 26–33 also contain untranslated fragments. SAP field names need exact Spanish labels with localized explanations.
- Section IDs match; all 19 original assets exist. Section 24 lacks a Next link. Later sections have no screenshots and incomplete reveal initialization; inline stagger delays persist into hover transitions. Missing x-cloak CSS, focus management and responsive overflow handling.
- Missing substantive topics: L2 corrections, Demandware failures, discount-code reactivation and validation exceptions.
- Original screenshots contain actual customer names, identifiers, addresses, emails and financial data. They require permanent raster redaction before inclusion in a deployment package.

## Source decisions and unresolved points

- Use October general policy and January operational detail when consistent.
- Return/cancellation deadline is unresolved: October p5 says 14 days after purchase; p33 says 14 working days; p32 labels the interval after warehouse receipt as cancellation; January p3 starts at customer receipt. Do not present one as settled or score it. Refer agents to approved current terms/supervisor. Refund processing on warehouse receipt is separately described on October p33.
- October p6 describes €60 free shipping as a special promotion; January p3 says over €60. Do not score an exact €60 boundary or promise an unconditional promotion. Similar exact €150 boundary is excluded.
- Payment links: October p30 specifically says automatic validation and no manual removal of Operación por aclarar. Apply this specific rule; bank transfer requires Accounting confirmation (p28). January p31's general validation instruction is not applied to payment links.
- January p34's regular-order template says approximately 10 working days, versus October p6 and January p3's 6–8. Use newer 6–8 days general guidance; spare parts up to 10 weeks.
- January p36 requests an Accounting refund for ERROR/CREADO orders, while p37 describes a card authorization hold rather than a captured payment. Do not score the financial disposition; inspect and escalate to Accounting.
- January p37 offers manual recovery respecting website conditions, while October p16 excludes promotions on email orders. Do not promise reinstated promotions in recovery or score that exception; escalate.
- January templates use formal usted/Su equipo; October p10 prefers tú/Tu equipo PLAYMOBIL. Use the newer tone.

## Implementation sequence

1. Synchronize localized presentation text and add four concise operational sections, preserving original IDs and Bojan Dj. credit.
2. Extract shared presentation behavior/styles; repair navigation, reveals, lightbox, keyboard focus and responsive layout.
3. Crop and permanently redact source screenshots, retaining useful SAP controls and annotations; add localized captions.
4. Add a shared, localized, source-mapped knowledge dataset and dedicated 20-question assessment.
5. Add seven distinct game mechanics with reset/cleanup and optional local progress.
6. Integrate training/quiz/games navigation and language persistence.
7. Package only allowlisted static assets for deployment, document source decisions and confidentiality limits.
8. Run data/path checks and complete browser rounds, then document actual results.
