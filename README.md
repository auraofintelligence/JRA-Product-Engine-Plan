# JRA Product Engine Plan

Joyful Responsible Abundance: a human-readable public explainer and practical product workbench connecting creation, marketing, sales planning, community and circular use.

**Public website:** https://auraofintelligence.github.io/JRA-Product-Engine-Plan/

Ten public pages were released in stages: landing page; engine and case studies; functional workbench; connections, circular use, media and sources. Each completed build is pushed separately.

## The source

Based on Luke Nathan Hayes' 21-page *The Joyful Responsible Abundance Product Engine*, dated 28 September 2026. The original PDF is preserved byte-for-byte in `dist/sources/JRA-Product-Engine-Plan.pdf` and published with Luke's explicit permission.

The document describes a market economy engine with no preset hierarchy. The product ideas remain available as case studies and optional starting points. A starting example does not prescribe people's decisions or grant authority.

## Run locally

Serve `dist` using `python -m http.server 8768 --directory dist`, then visit http://localhost:8768.

Rebuild with `python scripts/build.py --stage 4`. Validate with `python scripts/check.py`, `node --check dist/assets/workbench.js` and `node scripts/test-workbench.cjs`. The page builder uses only Python's standard library. GitHub Actions validates and publishes the checked-in `dist` directory on every push to `main`.

## Working features

Create blank products or start from any of the nine source case studies. Keep brief, making, offers, costs, community participation, circular-use records, contributions and agent scopes together. Product references are stable, connections are many-to-many and no parent or authority is required. New revisions retain earlier field and connection snapshots.

Records are stored locally in the browser, with Markdown release packs and JSON backup/import. No backend receives product data. The optional read-only WebMCP tool returns the current record to an explicitly invoked browser agent where supported. Fonts are served by Google Fonts, and normal hosting access logs may exist.

This edition does not execute AI tasks, send messages, take payments, place orders, manage live inventory or share records between accounts. The site labels these as future integrations. Presets are concepts and editable starting briefs, not confirmed stock or partnerships. Money inputs are blank until supplied by a visitor.

## Verification

Checks cover all page and asset links, anchors, navigation, metadata and JavaScript syntax. Regression checks cover cost arithmetic, incomplete figures, invalid quantities, break-even, backup validation, duplicate references, safe source URLs and historical snapshots. Browser checks cover desktop and phone layouts, saved edits, case selection, linked contributions, returns, downloads and the optional read-only tool's valid/invalid inputs.

The source PDF SHA256 is `0f998e0bb4c74b561193b1bb83b3d8564b6c71e0e09d2ee6635bbf0b75f1c808`.

## Rights and artwork

Strange But True Public Source Licence. This is public source, not an open-source licence. Commercial rights remain reserved to Luke Nathan Hayes. See [LICENSE.md](LICENSE.md).

Four original images were generated using the built-in image generation tool. They depict concepts, not manufactured products or operating facilities. Prompts are in [IMAGE-PROMPTS.md](IMAGE-PROMPTS.md).
