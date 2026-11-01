# Literature: the open texts the skills may read

Two shelves of source texts travel with the skills, each file a Markdown conversion with its source,
retrieval date and reuse terms in its own header.

- **Shelf 1, `cited/`: the guidance's own sources.** The works `units/references.md` lists under
  "Cited in the units", where the publisher's licence allows the full text to ship. The packager
  copies shelf 1 into every packaged skill.
- **Shelf 2, everything else here: the comparison frameworks** (DORA, the AI Act, NIST and the
  others). They ship with `/check-against-standards` and `/learn-bcm` only.

A source whose licence does not allow the text to ship stays a `references.md` entry and nothing
more. A file here is a conversion; where it and the publisher's copy differ, the publisher's copy
is right.

## Licences

Shelf 1 was checked on 2026-10-02 against the final units' list (vault
`02-Projects/ai4bcm/guidance-rewrite/units/references.md`, which names ISO 22300:2025; this
repository's `units/references.md` still names the 2021 edition until the units sync). Each
licence was read on the publisher's own page or in the document itself, at the address given.
Shelf 2 was checked when the files were added on 2026-09-10 (CSF 2.0 on 2026-09-28) and is not
re-read here; its terms are in each file's header and in `tools/sources.json`.

| Source | Licence | Evidence (read 2026-10-02 unless stated) | Ships | Shelf |
|---|---|---|---|---|
| ISO 22301:2019, BCMS requirements | © ISO, all rights reserved; no reproduction without written permission | The standard's own copyright page ("COPYRIGHT PROTECTED DOCUMENT"). ISO's policy page https://www.iso.org/copyright.html answers 403 from brain and did not load in the connected browser, so it was not read | no | 1 |
| ISO 22300:2025, vocabulary | Not read: iso.org answers 403. ISO sells its standards under the same notice as ISO 22301, but that was not confirmed for this edition | https://www.iso.org/copyright.html (blocked) | no | 1 |
| IMDA, *Model AI Governance Framework for Agentic AI* v1.5 | © IMDA; copy and distribute "solely for personal, internal, non-commercial, informational purposes"; reproduction needs IMDA's written permission. The PDF itself carries no licence | https://www.imda.gov.sg/terms-of-use (last updated 25 May 2026; read in the connected browser, because direct fetches get a bot challenge) | no | 1 |
| NCSC, CISA and partners, *Guidelines for secure AI system development* v1.0 | © Crown copyright 2023, Open Government Licence v3.0 for the text; photographs and infographics excluded | https://www.ncsc.gov.uk/section/about-this-website/terms-and-conditions, and the PDF's last page (https://www.ncsc.gov.uk/sites/default/files/documents/Guidelines-for-secure-AI-system-development.pdf) | yes, text only: `cited/ncsc/` | 1 |
| ETSI EN 304 223 V2.1.1 | © ETSI 2025, all rights reserved; "No part may be reproduced or utilized in any form ... except as authorized by written permission of ETSI" | The standard's Copyright Notification, PDF page 2: https://www.etsi.org/deliver/etsi_en/304200_304299/304223/02.01.01_60/en_304223v020101p.pdf | no | 1 |
| OWASP GenAI Security Project, *Top 10 for Agentic Applications for 2026* | CC BY-SA 4.0 | The document's "License and Usage" page (PDF page 2) and the site footer of https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | yes, the ten entries, under CC BY-SA: `cited/owasp/` | 1 |
| NIST AI 600-1, *Generative AI Profile* | U.S. Government work, not subject to copyright in the U.S. (17 U.S.C. 105); royalty-free worldwide right to reprint granted for foreign rights | https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications | yes: `cited/nist/` | 1 |
| UK GDS, *Artificial Intelligence Playbook for the UK Government* | © Crown copyright 2025, Open Government Licence v3.0 "except where otherwise stated" | The publication's own notice: https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html | yes, text only: `cited/uk-gds/` | 1 |
| SEI and Accenture, *The AI Adoption Maturity Model v1.0* | "Copyright 2026 Carnegie Mellon University"; no reuse grant in the document or on its landing page | The PDF's back matter: https://sei.cmu.edu/documents/6534/The_AI_Adoption_Maturity_Model.pdf | no | 1 |
| Fortune, radiologists article, 19 July 2026 | © 2026 Fortune Media IP Limited, all rights reserved; the terms forbid reproduction and distribution without permission | https://fortune.com/terms-of-use/ | no | 1 |
| Regulation (EU) 2022/2554 (DORA) | Commission Decision 2011/833/EU: reuse authorised with acknowledgement | https://eur-lex.europa.eu/eli/dec/2011/833/oj (2026-09-10) | yes: `eur-lex/` | 2 |
| Delegated Regulation (EU) 2024/1774 | as DORA | as DORA | yes: `eur-lex/` | 2 |
| Regulation (EU) 2024/1689 (AI Act), Articles 4, 26, 50 | as DORA | as DORA | yes: `eur-lex/` | 2 |
| NIST SP 800-34 Rev. 1, chapters 1 to 5 | U.S. Government work (17 U.S.C. 105) | as NIST AI 600-1 (2026-09-10) | yes: `nist/` | 2 |
| NIST AI 100-1, AI RMF 1.0 | U.S. Government work (17 U.S.C. 105) | as NIST AI 600-1 (2026-09-10) | yes: `nist/` | 2 |
| NIST CSWP 29, CSF 2.0 | U.S. Government work; royalty-free reprint right | as NIST AI 600-1 (2026-09-28) | yes: `nist/` | 2 |
| FONES, *Minimum standard for improving ICT resilience* (2023) | CC BY 4.0 | The document's own licence statement, page 43: https://www.bacs.admin.ch/dam/en/sd-web/dJRSfIeFXoTP/ikt-minimalstandard-2023-en.pdf (2026-09-10) | yes: `swiss-fones/` | 2 |
| UK Cabinet Office, *Organisational Resilience Guidance* | Open Government Licence v3.0 | The GOV.UK page's own notice (2026-09-10) | yes: `uk-cabinet-office/` | 2 |
| ESAs Joint Committee, JC 2026 25 statement | ESMA legal notice: reproduction authorised with acknowledgement; a transformation carries ESMA's disclaimer | https://www.esma.europa.eu/legal-notice (2026-09-10) | yes: `esas/` | 2 |

Not shipping is not a judgement on the work: those sources stay cited in the units, with their
editions, and a reader opens them at the publisher.

## How the packages carry them

`tools/build_chatgpt_package.py` copies `README.md` and `cited/` into `skills/<name>/literature/`
for every skill, and the shelf 2 folders too for the two skills that read them. A plugin
install that takes the whole repository has both shelves beside every skill. The connector's chunk
build (`tools/build_chunks.py`) skips this README and `cited/`: shelf 1 enters the served corpus
only when someone registers it in `tools/sources.json`, and the OWASP text, being share-alike, may
not become chunks at all.

## Converters

`tools/literature/`: `pdf_prose_to_md.py` (NIST-style PDFs), `nist_profile_split.py` (the AI 600-1
line breaks), `owasp_top10_to_md.py` (the OWASP entries), `html_to_md.py` (GOV.UK and NCSC pages),
`eurlex_to_md.py` and `ch_ikt_to_md.py`.
