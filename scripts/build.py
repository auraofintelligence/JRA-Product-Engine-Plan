"""Build a small, dependency-free public site in independently publishable stages."""
from pathlib import Path
from html import escape
import argparse, json, shutil

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
REPO='https://github.com/auraofintelligence/JRA-Product-Engine-Plan'
BASE='https://auraofintelligence.github.io/JRA-Product-Engine-Plan/'
parser=argparse.ArgumentParser();parser.add_argument('--stage',type=int,default=4);args=parser.parse_args()
pages={}
def add(file,title,description,body): pages[file]=(title,description,body)
def head(title,text): return f'<section class="page-head"><div class="wrap"><h1>{title}</h1><p>{text}</p></div></section>'
def source(p): return f'<p class="source-line">From the original plan, {p}. <a href="sources/JRA-Product-Engine-Plan.pdf">Read the source PDF</a>.</p>'
def card(n,title,text,url): return f'<a class="card card-link" href="{url}"><span class="number">{n}</span><h3>{title}</h3><p>{text}</p></a>'
home='''<section class="hero"><img src="assets/hero.png" alt="Imagined coastal making garden with luminous purple loops, green terraces and shared creative spaces" width="1536" height="1024" fetchpriority="high"><div class="wrap hero-content"><div class="glass-copy"><h1>A joyful future.<br>Made <em>together.</em></h1><p>Turn a good idea into a useful product. Connect with people, earn a living and keep materials in use.</p><div class="actions"><a class="btn" href="#about">Explore the engine <span aria-hidden="true">↗</span></a>WORKBENCH_CTA</div></div></div></section><div class="hero-caption">AI-generated concept artwork. A vision for shared making.</div>
<section class="intro-strip"><div class="wrap strip-inner"><p>Joyful Responsible Abundance</p><p><span>Make useful things. Build relationships. Begin again.</span></p></div></section>
<section class="section" id="about"><div class="wrap split"><div><h2>Good things grow<br>through connection.</h2></div><div><p class="lead">A maker has a skill. Someone has an idea. A community has a need. The product engine helps their paths meet.</p><p>It connects the brief, materials, people, costs, creative work and next use of a product. A change in one place can inform the next step, from the first sample to a refill, repair or new collection.</p><p>Everyone enters through the work that interests them. People agree responsibilities for each activity. No brand, founder, investor or AI agent gains general authority over the network.</p></div></div></section>
<section class="section tint"><div class="wrap"><div class="section-head"><h2>From possibility<br>to something real.</h2><p>One connected process. Many ways in. Start with an idea, a material, a skill or a gathering.</p></div><div class="cards">HOME_CARDS</div></div></section>
<section class="section"><div class="wrap split"><div><h2>Meaning you choose.<br>Products you use.</h2><p>Aura Undies carries a personally chosen virtue. Drinks bring flavour to a shared moment. Club merchandise connects a useful object with a community story.</p><p>These are starting points for making and learning. Each product needs its own samples, costs, maker and practical route to market.</p><div class="tag-row"><span class="tag">Aura expressions</span><span class="tag">Clothing</span><span class="tag">Drinks</span><span class="tag">Club collections</span></div></div><div class="card"><h3>The purpose is in the name.</h3><p><strong>Joyful:</strong> create things people enjoy.</p><p><strong>Responsible:</strong> make clear agreements and follow through.</p><p><strong>Abundance:</strong> widen access to useful products, skills and the means of making them.</p></div></div></section>
<section class="section dark"><div class="wrap split"><div><h2>Built from a plan.<br>Open to participation.</h2><p>Luke Nathan Hayes developed the JRA Product Engine plan within Aura of Intelligence and Strange but True, beginning in Minjerribah and reaching towards Australia and Oceania.</p></div><div><p>This public edition explains the system and provides a practical starting workspace. The full connected marketplace and agent network remain a proposal.</p><div class="actions"><a class="btn gold" href="sources/JRA-Product-Engine-Plan.pdf">Read the original plan ↗</a><a href="https://github.com/auraofintelligence/JRA-Product-Engine-Plan">Explore the repository</a></div></div></div></section>'''
home=home.replace('WORKBENCH_CTA','<a class="btn secondary" href="workbench.html">Try the workbench</a>' if args.stage>=3 else '<a class="btn secondary" href="sources/JRA-Product-Engine-Plan.pdf">Read the plan</a>')
home=home.replace('HOME_CARDS',card('01','Make an offer','Shape a brief, try a sample and connect the design with people who can make it.','how-it-works.html' if args.stage>=2 else '#about')+card('02','Bring people together','Share an experience, tell the product story and agree the work around it.','connections.html' if args.stage>=4 else '#about')+card('03','Keep value in use','Build care, repair, refill and material recovery into the next cycle.','circular-use.html' if args.stage>=4 else '#about'))
add('index.html','JRA Product Engine | A joyful future, made together','A human-readable guide and practical workbench for Joyful Responsible Abundance: products, people and circular economies.',home)

# Later stages add real pages without shipping empty routes.
if args.stage>=2:
    exec((ROOT/'scripts'/'narrative.py').read_text(encoding='utf-8'))
if args.stage>=3:
    exec((ROOT/'scripts'/'workbench_page.py').read_text(encoding='utf-8'))
if args.stage>=4:
    exec((ROOT/'scripts'/'connections.py').read_text(encoding='utf-8'))

licence=(ROOT/'LICENSE.md').read_text(encoding='utf-8').replace('[YEAR]','2026').replace('[PROJECT_NAME]','JRA Product Engine Plan').replace('[PROJECT_URL]',REPO)
(ROOT/'LICENSE.md').write_text(licence,encoding='utf-8')
(DIST/'LICENSE.md').write_text(licence,encoding='utf-8')
licence_body=''.join(f'<h2>{escape(line[3:])}</h2>' if line.startswith('## ') else f'<h1>{escape(line[2:])}</h1>' if line.startswith('# ') else f'<p>{escape(line[2:] if line.startswith("- ") else line)}</p>' for line in licence.splitlines() if line.strip())
add('licence.html','Licence','Strange But True Public Source Licence for the JRA Product Engine.',f'<section class="section"><div class="wrap prose">{licence_body}</div></section>')
map_items=''.join(f'<article><h3><a href="{file}">{escape(title.split(" | ")[0])}</a></h3><p>{escape(desc)}</p></article>' for file,(title,desc,body) in pages.items())
add('sitemap.html','Site map','Find every page in the JRA Product Engine.',head('Find your way.','Explore the idea, try the working tools and follow the sources.')+f'<section class="section"><div class="wrap link-list">{map_items}</div></section>')
order=list(pages)
nav=[('index.html','Home'),('how-it-works.html','The engine'),('products.html','Products'),('connections.html','Connections')]
for file,(title,description,body) in pages.items():
    navigation=''.join(f'<a href="{url}"'+(' aria-current="page"' if file==url else '')+f'>{label}</a>' for url,label in nav if url in pages)
    if 'workbench.html' in pages: navigation+='<a class="btn" href="workbench.html">Open workbench ↗</a>'
    else: navigation+='<a class="btn" href="sources/JRA-Product-Engine-Plan.pdf">Read the plan ↗</a>'
    idx=order.index(file);prev=order[(idx-1)%len(order)];nxt=order[(idx+1)%len(order)]
    turn=f'<div class="wrap"><nav class="page-turn" aria-label="Previous and next page"><a href="{prev}"><span>← Previous</span><strong>{escape(pages[prev][0].split(" | ")[0])}</strong></a><a href="{nxt}"><span>Next →</span><strong>{escape(pages[nxt][0].split(" | ")[0])}</strong></a></nav></div>'
    footer_links=''.join(f'<a href="{url}">{label}</a>' for url,label in [('how-it-works.html','How it works'),('products.html','Product possibilities'),('workbench.html','Product workbench'),('circular-use.html','Circular use'),('media.html','Media and agents'),('connections.html','Connections'),('sources.html','Sources')] if url in pages)
    extra='<link rel="stylesheet" href="assets/workbench.css?v=20260928-journey"><script defer src="assets/journey.js?v=20260928-journey"></script><script defer src="assets/suggestions.js?v=20260928-journey"></script><script defer src="assets/workbench.js?v=20260928-journey"></script>' if file=='workbench.html' else ''
    html=f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(description,quote=True)}"><meta name="theme-color" content="#2b104c"><link rel="canonical" href="{BASE}{'' if file=='index.html' else file}"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:type" content="website"><link rel="icon" type="image/png" href="assets/favicon.png"><link rel="stylesheet" href="assets/site.css?v=20260928-padding"><script defer src="assets/site.js"></script>{extra}</head><body id="top"><a class="skip" href="#main">Skip to content</a><header class="topbar wrap"><a class="brand" href="index.html"><img src="assets/favicon.png" width="43" height="43" alt=""><span>JRA<br>Product Engine</span></a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="navigation">Menu</button><nav class="nav" id="navigation" aria-label="Main">{navigation}</nav></header><main id="main">{body}</main>{turn}<footer class="footer"><div class="wrap"><div class="footer-grid"><div><h2>Make room for<br>good things.</h2><p>Joyful Responsible Abundance connects products, people and the next useful cycle.</p><p>Minjerribah · Australia · Oceania</p></div><div>{footer_links}</div><div><a href="sitemap.html">Site map</a><a href="sources/JRA-Product-Engine-Plan.pdf">Original plan (PDF)</a><a href="{REPO}">Source repository ↗</a><a href="licence.html">Strange But True licence</a></div></div><div class="footer-base"><p>© 2026 Luke Nathan Hayes · Strange But True · Aura of Intelligence</p><p>Public source. Commercial rights reserved.</p></div></div></footer><button class="top-btn" type="button" aria-label="Back to top" hidden>↑</button></body></html>'''
    (DIST/file).write_text(html,encoding='utf-8')
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{f if f!="index.html" else ""}</loc></url>' for f in pages)+'</urlset>',encoding='utf-8')
(DIST/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n',encoding='utf-8')
(DIST/'.nojekyll').touch()
print(f'Built stage {args.stage}: {len(pages)} pages')
