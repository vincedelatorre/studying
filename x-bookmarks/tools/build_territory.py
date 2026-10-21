#!/usr/bin/env python3
"""Build x-bookmarks/territory.html from data/territory/*.json and data/accounts/*.json."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
t = json.loads((root / "data/territory/territory.json").read_text())
accounts = []
for aid in t["order"]:
    plan = json.loads((root / f"data/territory/{aid}.json").read_text())
    plan["research_data"] = json.loads((root / f"data/accounts/{plan.get('research', aid)}.json").read_text())
    accounts.append(plan)
data = json.dumps({"territory": t, "accounts": accounts}, ensure_ascii=False).replace("</", "<\\/")
tpl = (root / "tools/territory.template.html").read_text()
(root / "territory.html").write_text(tpl.replace("/*__DATA__*/null", data))
print(f"wrote territory.html ({len(accounts)} accounts)")
