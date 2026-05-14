"""Build the JLPT Grammar Practice app (index.html with embedded data)."""
import json, csv
from pathlib import Path

DIR = Path(r"C:\Users\cprie\Documents\Japanisch\kanji_study_helper")

# Load grammar
with open(DIR / "grammar_entries.json", encoding="utf-8") as f:
    gdata = json.load(f)

# Load vocab
vdata = []
for fn in ["n5.csv", "n4.csv", "n3.csv"]:
    with open(DIR / fn, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            row["_source"] = fn.replace(".csv", "")
            vdata.append(row)

gj = json.dumps(gdata, ensure_ascii=False)
vj = json.dumps(vdata, ensure_ascii=False)

# Read the template HTML and substitute placeholders
template = (DIR / "app_template.html").read_text(encoding="utf-8")
html = template.replace("{{GRAMMAR_JSON}}", gj).replace("{{VOCAB_JSON}}", vj)

out = DIR / "jlpt_app"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")

print(f"Written: {out / 'index.html'}")
print(f"Grammar: {len(gdata)}, Vocab: {len(vdata)}")
print(f"Size: {(out / 'index.html').stat().st_size // 1024} KB")
