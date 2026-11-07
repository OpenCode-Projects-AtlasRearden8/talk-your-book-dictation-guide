# STATUS — talk-your-book-dictation-guide

Built: 2026-11-07

## What was built

A complete voice-dictation manual for authors who want to draft books by speaking, by **Asdale Dynamics, LLC** (Dylan Asdale's LLC — beginner-friendly AI education, plain English, local-first).

- `docs/index.md` — reading order index
- `docs/00-introduction.md` — who it's for, the four phases, expectations
- `docs/01-free-dictation-by-platform.md` — free built-in dictation for Windows (Win+H Voice Typing, offline Speech Recognition), macOS (on-device dictation), iPhone (walking-and-dictating), Android (Gboard, on-device typing)
- `docs/02-transcription-endpoints.md` — file-based transcription via local, keyless OpenAI-compatible endpoints (whisper.cpp server and Python Whisper-server options), what Ollama does and doesn't do, model sizing, troubleshooting
- `docs/03-punctuation-control.md` — spoken punctuation commands, pause discipline, name/placeholders, dialogue and dashes
- `docs/04-sculpting-drafts.md` — two-pass editing method, a guardrailed master sculpting prompt plus a mini prompt library, Ollama as the local AI editor, reading-aloud loop
- `docs/05-privacy.md` — privacy ladder, sensitivity triage (including HIPAA-mindset for PHI), three zero-cost upgrades
- `docs/06-30-day-word-flow-plan.md` — the 30-day trial: week-by-week sessions, plain-text tracker, failure modes
- `site/` — static website generated *from* the docs: `site/index.html`, seven chapter pages in `site/pages/`, `site/style.css`
- `site/gen.py` — the site generator: Markdown → HTML using only the Python 3 standard library (zero dependencies, runs offline)
- `scripts/verify.py` — repo checks: docs present, substance coverage, secret scan, LICENSE/README requirements, doc links, full site build with broken-link detection and copyright-footer checks
- `README.md` — credits Asdale Dynamics, LLC; documents quick start
- `LICENSE` — MIT, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`

Scope note: this guide is about the *authoring workflow*. It deliberately does not explain consumer voice-assistant features (Voice Assistants Comfort Guide) or transcription tooling internals (Local Transcription Handbook).

## How to run it

Build the static site (Python 3 only, no packages):

```
python3 site/gen.py
python3 -m http.server 8000 --directory site
# then open http://localhost:8000
```

Regenerate after editing anything in `docs/`. The HTML is fully static and works from `file://` as well; `python3 -m http.server` is just the nicest way to view it.

## Verification results

`python3 scripts/verify.py` → **7/7 checks passed**:

- PASS docs chapter files present
- PASS required coverage (platforms, endpoints, punctuation, privacy, plan)
- PASS no secrets or keys in files
- PASS LICENSE is MIT with exact copyright line
- PASS README credits Asdale Dynamics, LLC
- PASS docs internal links resolve
- PASS static site builds with no broken links

Manual serving smoke test: `python3 -m http.server 8741 --directory site` → HTTP 200 for `/`, one chapter page, another chapter page, and `/style.css`. Site build reports `0 broken links, all pages present`, and every generated page carries the MIT/Asdale Dynamics, LLC footer (checked by the verifier).

## Known gaps and honest limitations

- The site generator is a small hand-rolled Markdown converter: it covers exactly the Markdown constructs used in these docs (headings, lists incl. checkboxes, tables, blockquotes, fenced code, inline emphasis/link/code). It is not a general-purpose Markdown engine — exotic Markdown (nested lists, images, footnotes) is not supported and will be silently mis-rendered until supported.
- Chapter 2 gives correct architecture and workflow for running whisper.cpp's server and Python Whisper servers; it intentionally stops short of exact one-line commands per project, since those projects' flags change between releases — instead it names the endpoints and points at each project's own docs (see the Local Transcription Handbook for that depth), and the Ollama model/version examples (`llama3.1:8b`) should be re-checked at install time.
- No built HTML syntax validation beyond link/copyright checks; no screenshot-level visual QA was done in a browser.
- Content is educational only; tool menus and command names drift over time.
