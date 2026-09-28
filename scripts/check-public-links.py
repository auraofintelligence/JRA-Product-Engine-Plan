from pathlib import Path
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.error import HTTPError
import json
root=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self):super().__init__();self.urls=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href','').startswith('https://'):self.urls.add(a['href'].split('#')[0])
p=Links()
for file in (root/'dist').glob('*.html'):p.feed(file.read_text(encoding='utf-8'))
def check(url):
    try:
        with urlopen(Request(url,headers={'User-Agent':'JRA-public-link-check/1.0'},method='HEAD'),timeout=25) as r:return {'url':url,'status':r.status,'final':r.url}
    except HTTPError as e:return {'url':url,'status':e.code}
    except Exception as e:return {'url':url,'error':str(e)}
with ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(check,sorted(p.urls)))
(root/'qa').mkdir(exist_ok=True)
(root/'qa'/'public-links.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for r in results:
    if r.get('status')!=200: print(json.dumps(r))
print(f'{sum(r.get("status")==200 for r in results)}/{len(results)} public links returned HTTP 200')
