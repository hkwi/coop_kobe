# coding: UTF-8
import sys
import json
import lxml.html
r = lxml.html.parse("http://www.kobe.coop.or.jp/gaiyou/").getroot()
content = r.find('.//div[@id="contentArea"]')
data = []
for e in content.xpath('.//li'):
	h3 = e.find(".//h3")
	a,d = h3.xpath('.//following-sibling::p')
	obj = dict(
		name = "".join(h3.itertext()),
		url = e.find(".//h3/a").get("href"),
		address = "".join(a.itertext()).strip(),
		discount = "".join(d.itertext()).strip()
	)
	data.append(obj)
json.dump(data, sys.stdout, indent=2, ensure_ascii=False)
