# studying

## Technical Bookmark Library

**[Energy MEDDPICC playbook](https://vincedelatorre.github.io/studying/x-bookmarks/playbook.html)** · **[Oil & Gas territory plan](https://vincedelatorre.github.io/studying/x-bookmarks/territory.html)** · **[Customer brief: Devin and the Agent Shift](https://vincedelatorre.github.io/studying/x-bookmarks/devin-agent-shift.html)** · **[Read the storylines](https://vincedelatorre.github.io/studying/x-bookmarks/storylines.html)** · **[Open the full library](https://vincedelatorre.github.io/studying/x-bookmarks/)**

506 technical X bookmarks saved Aug 18 – Oct 18, 2026, sorted into 12 chapters and 74 topics. Each entry has a summary, a takeaway, the tools it names, the links from the post, and the full saved text. Politics, everyday life, gossip and memes are left out.

| Path | What it is |
| --- | --- |
| [`x-bookmarks/playbook.html`](x-bookmarks/playbook.html) | Internal MEDDPICC playbook for the energy vertical: value framework, question bank, talk track trees, mutual action plan, account plays |
| [`x-bookmarks/data/accounts/`](x-bookmarks/data/accounts/) | Sourced account research: ExxonMobil, Chevron, Halliburton, SLB, Baker Hughes, ConocoPhillips, Enterprise Products |
| [`x-bookmarks/devin-agent-shift.html`](x-bookmarks/devin-agent-shift.html) | Customer-ready brief: seven shifts, what Devin does about each, proof, industrial and energy fit, four-step pilot |
| [`x-bookmarks/storylines.html`](x-bookmarks/storylines.html) | 11 dated storylines with turning points, key numbers and customer talking points, every claim linked to its post |
| [`x-bookmarks/data/storylines.json`](x-bookmarks/data/storylines.json) | The storylines as structured data |
| [`x-bookmarks/index.html`](x-bookmarks/index.html) | The website (one self-contained page with search and month filter) |
| [`x-bookmarks/data/technical-bookmarks.json`](x-bookmarks/data/technical-bookmarks.json) | All 506 entries with chapter, topic, title, summary, takeaway, tools, links and full text |
| [`x-bookmarks/data/excluded.json`](x-bookmarks/data/excluded.json) | The 297 saves that were left out, with the reason for each |
| [`x-bookmarks/posts/`](x-bookmarks/posts/) | The original bookmark files, one folder per chapter |

### Chapters

1. Coding Agents & Harnesses
2. Agent Architecture, Memory & Skills
3. Cognition & Devin
4. Sandboxes, VMs & Cloud Environments
5. 3D, Game Dev & World Models
6. Creative AI: Image, Video & Audio
7. Design, Frontend & Web
8. Models, Releases & Benchmarks
9. AI Infra, Compute & Inference
10. Security & Trust
11. Robotics, Hardware & Science
12. Open Source, Repos & Learning Resources

### Turning on the website link

The link above is served by GitHub Pages. If it shows a 404, turn Pages on once: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main`, folder `/ (root)` → Save**. The site goes live a minute or two later.

## Oil & Gas territory plan

[`x-bookmarks/territory.html`](https://vincedelatorre.github.io/studying/x-bookmarks/territory.html) is a strategic account plan for ExxonMobil, Chevron, Halliburton, SLB and Enterprise Products. It follows MEDDPICC, Command of the Message and McMahon-style territory execution. It has a pipeline generation (PG) plan, publicly stated challenges with sources, pain chains, a stakeholder map with LinkedIn and Sales Navigator search links, mutual action plans and engagement sequences.

To add an account, write `x-bookmarks/data/accounts/<id>.json` (research) and `x-bookmarks/data/territory/<id>.json` (plan), add the id to `order` in `data/territory/territory.json`, then run `python3 x-bookmarks/tools/build_territory.py`.
