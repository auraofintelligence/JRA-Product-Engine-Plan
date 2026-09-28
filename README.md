# JRA Product Engine Plan

Joyful Responsible Abundance: a human-readable public explainer and practical product workbench connecting creation, marketing, sales planning, community and circular use.

**Public website:** https://auraofintelligence.github.io/JRA-Product-Engine-Plan/

The site is being released in stages: landing page; engine and case studies; functional workbench; connections, circular use, media and sources. Each completed build is pushed separately.

## The source

Based on Luke Nathan Hayes' 21-page *The Joyful Responsible Abundance Product Engine*, dated 28 September 2026. The original PDF is preserved byte-for-byte in `dist/sources/JRA-Product-Engine-Plan.pdf` and published with Luke's explicit permission.

The document describes a market economy engine with no preset hierarchy. The product ideas remain available as case studies and optional starting points. A starting example does not prescribe people's decisions or grant authority.

## Run locally

Serve `dist` using `python -m http.server 8768 --directory dist`, then visit http://localhost:8768.

Validate with `python scripts/check.py`. Build the current stage using `python scripts/build.py --stage 1`. Later stages require the corresponding page source files. The final build uses stage 4.

## Rights and artwork

Strange But True Public Source Licence. This is public source, not an open-source licence. Commercial rights remain reserved to Luke Nathan Hayes. See [LICENSE.md](LICENSE.md).

Four original images were generated using the built-in image generation tool. They depict concepts, not manufactured products or operating facilities. Prompts are in [IMAGE-PROMPTS.md](IMAGE-PROMPTS.md).
