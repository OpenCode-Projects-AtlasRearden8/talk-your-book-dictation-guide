# Talk Your Book: A Voice Dictation Manual for Authors

Free dictation across Windows, macOS, and phones, no-key local transcription endpoints (Ollama-friendly), punctuation control tricks, sculpting spoken drafts into readable prose in any AI editor, manuscript privacy, and a 30-day word-flow trial plan.

By **Asdale Dynamics, LLC** — beginner-friendly AI education from Dylan Asdale, author of *The Massive AI Manual*. Plain English, step by step, never condescending.

## What's here

| Path | What it is |
| --- | --- |
| `docs/` | The manual in Markdown — 6 chapters plus an index |
| `site/` | A static, dependency-free website built from `docs/` |
| `site/gen.py` | The site generator (Python 3 standard library only, no installs) |
| `scripts/verify.py` | Checks that the repo is consistent and the site builds |
| `STATUS.md` | What was built, how to run/verify it, known gaps |

## Quick start

Read the manual anywhere you like:

```
docs/index.md
```

Build the static site (requires only Python 3):

```
python3 site/gen.py
python3 -m http.server 8000 --directory site
```

Then open http://localhost:8000 — the site works entirely offline, no build dependencies, no keys, no accounts. Regenerate any time you edit `docs/`.

Verify everything:

```
python3 scripts/verify.py
```

## Design principles

- **Local-first:** every setup in the manual can run with your voice never leaving your machine.
- **No secrets:** no API keys, accounts, or personal data are required anywhere in these docs, and none are embedded in this repo.
- **Free tools only:** each chapter can be followed with tools that cost $0.
- **Beginner-friendly:** plain English, warm, never condescending.
- **Distinct scope:** about *authoring workflow*, not consumer voice assistants (see the Voice Assistants Comfort Guide) and not transcription tooling internals (see the Local Transcription Handbook).

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.
