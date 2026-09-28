from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
root=Path(__file__).resolve().parents[1]/'dist'
class Page(HTMLParser):
    def __init__(self): super().__init__();self.links=[];self.ids=set();self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='h1': self.h1+=1
        for key in ['href','src']:
            if a.get(key): self.links.append(a[key])
        if tag=='img': assert 'alt' in a,'Image missing alt'
pages={p.name:Page() for p in root.glob('*.html')}
for name,p in pages.items():
    content=(root/name).read_text(encoding='utf-8');p.feed(content)
    assert p.h1==1,(name,'expected one h1',p.h1)
    assert 'lang="en-AU"' in content and 'name="description"' in content,name
    assert 'aria-label="Previous and next page"' in content,name
    assert 'aria-label="Back to top"' in content,name
for name,p in pages.items():
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        path=unquote(u.path) or name
        assert (root/path).is_file(),(name,link,'missing file')
        if u.fragment and path in pages:assert u.fragment in pages[path].ids,(name,link,'missing anchor')
assert (root/'assets/hero.png').stat().st_size>10000
assert (root/'assets/favicon.png').stat().st_size>100
print(f'PASS: {len(pages)} pages, local links, anchors, images, page navigation and metadata')
print('Source PDF SHA256:',hashlib.sha256((root/'sources/JRA-Product-Engine-Plan.pdf').read_bytes()).hexdigest())
