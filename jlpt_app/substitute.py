
import json, csv
from pathlib import Path
DIR = Path(r"C:\Users\cprie\Documents\Japanisch\kanji_study_helper")
with open(DIR / "grammar_entries.json", encoding="utf-8") as f:
    gdata = json.load(f)
vdata = []
for fn in ["n5.csv", "n4.csv", "n3.csv"]:
    with open(DIR / fn, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            vdata.append(row)
gj = json.dumps(gdata, ensure_ascii=False)
vj = json.dumps(vdata, ensure_ascii=False)
# Read template and substitute
template = (DIR / "jlpt_app" / "template3.html").read_text(encoding="utf-8")
html = template.replace("{{GRAMMAR_JSON}}", gj).replace("{{VOCAB_JSON}}", vj)
(DIR / "jlpt_app" / "index.html").write_text(html, encoding="utf-8")
size = len(html.encode("utf-8")) // 1024
print(f"Built: {size} KB, {len(gdata)} grammar, {len(vdata)} vocab")
