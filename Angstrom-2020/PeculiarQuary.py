from pprint import pprint
from html_table_parser import HTMLTableParser
import requests

print("Toute la table")
url = "https://peculiarquery.2020.chall.actf.co/?q=%"
xhtml = requests.get(url).text

p = HTMLTableParser()
p.feed(xhtml)
if len(p.tables[0]) > 1:
        pprint(p.tables)

alpha = "abcdefghijklmnopqrstuvwxyz"
for letter in alpha:
	print("Lettre: " + letter)
	url = "https://peculiarquery.2020.chall.actf.co/?q="+letter+"%"
	xhtml = requests.get(url).text

	p = HTMLTableParser()
	p.feed(xhtml)
	if len(p.tables[0]) > 1:
		pprint(p.tables)
