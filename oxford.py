from bs4 import BeautifulSoup
from dataclasses import dataclass
from libs import MdxBuilder
text = MdxBuilder(
    '/home/kongjun/.goldendict/dict/oald/牛津高阶英汉双解词典（第10版）V3.mdx').mdx_lookup('downside')[0]


@dataclass
class Item:
    definition: str
    synonyms: list[str]


soup = BeautifulSoup(text, features="html.parser")

for ul in soup.css.select("ul"):
    if "examples" in ul.get_attribute_list("class"):
        for child in ul.children:
            examples = [c.get_text()
                        for c in child.children if c.get_text() != ""]
            examples = examples[len(examples)-2:]
            print(examples)
            break

phon_node = soup.css.select(".phons_n_am")[0]
attrs = phon_node.find("a").get_attribute_list("href")
assert len(attrs) == 1
sound = attrs[0]
phon = phon_node.get_text().strip("/ ")
print(phon, sound)

items = dict()
entrys = soup.css.select("#entryContent")
for entry in entrys:
    pos = entry.find("span", {"class": "pos"})
    if pos not in items:
        items[pos] = []
    for deft in entry.find_all("deft"):
        # Definition
        definition = deft.find("chn").get_text().split("；")[0]
        span = deft.find_next_sibling("span")
        # Synonyms
        synonyms = []
        if span:
            for s in span.find_all("span"):
                if "xh" in s.get_attribute_list("class"):
                    synonyms.append(s.get_text())
        item = Item(definition, synonyms)
        items[pos].append(item)
        print(item)

