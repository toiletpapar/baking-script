import requests
from lxml import etree
from io import StringIO

r = requests.get("https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser")
html = etree.HTML(r.text)

# print(html.findall(".//h2"))
# print(etree.tostring(html, pretty_print=True, method="html"))

allElements = html.findall(".//h2")

# Find all elements and split on the first occurrence of a space
for element in allElements:
  print(element.text.split(" ", 1))

# Find all elements and show each elements attributes
# for element in allElements:
#   for attributes in 