import requests

from bell_county_docket_parser import iterparse_fromstring, extract_docket_text

FIELDS = [
    [(1, 'CAUSE NUMBER'),
    (18, 'CR. NO. P AT'),
    (32, 'DEFENDANTS NAME'),
    (73, 'OFFENSE'),
    (109, 'CAPIAS')],

    [(15, 'ARR DTE'),
    (22, 'ATTORNY'),
    (33, 'BD CO'),
    (39, 'AMT'),
    (46, 'SETTING'),
    (57, 'DISP'),
    (76, 'PTDT/TIME')]
]

page = requests.get('http://www.bellcountytx.com/Countycoor/CSTMR/DOCKET2C.HTM').content

docket = extract_docket_text(page)

try:
  from scraperwiki.sqlite import save    
except:
  def save(a=None,b=None,c=None):
    print b
for result in list(iterparse_fromstring(docket, FIELDS)):#[:10]:
    save([],result)
