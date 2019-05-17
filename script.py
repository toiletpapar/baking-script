import requests
from lxml import etree
from io import StringIO

r = requests.get("https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser")
html = etree.HTML(r.text)

print(etree.tostring(html, pretty_print=True, method="html"))