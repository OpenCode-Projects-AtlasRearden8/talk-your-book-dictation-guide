import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOCS = ROOT / "docs"
CH = [
    "00-introduction.md",
    "01-free-dictation-by-platform.md",
    "02-transcription-endpoints.md",
    "03-punctuation-control.md",
    "04-sculpting-drafts.md",
    "05-privacy.md",
    "06-30-day-word-flow-plan.md",
]


def check_all():
    failures = []

    def expect(cond, msg):
        assert cond, msg

    def test(name, fn):
        try:
            fn()
            print(f"PASS  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}: {e}")
            failures.append(name)

    def doc_files():
        expect((DOCS / "index.md").is_file(), "docs/index.md missing")
        for c in CH:
            expect((DOCS / c).is_file(), f"docs/{c} missing")

    def platform_chapter():
        txt = "\n".join((DOCS / c).read_text(encoding="utf-8") for c in CH)
        for needle in ["win + h", "system settings", "gboard", "whisper.cpp", "ollama",
                       "/v1/audio/transcriptions", "new paragraph", "privacy", "30"]:
            expect(needle in txt.lower(), f"expected coverage of: {needle}")

    def no_secrets():
        pat = re.compile(r"sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|(api[_-]?key[\"'\s:=]{1,4}[A-Za-z0-9]{16,})", re.I)
        files = [ROOT / "README.md", ROOT / "LICENSE", ROOT / "STATUS.md"]
        files += list(DOCS.rglob("*.md"))
        files += list((ROOT / "site").rglob("*.py"))
        files += list((ROOT / "site").rglob("*.css"))
        files += list((ROOT / "site").rglob("*.html"))
        for p in files:
            if not p.is_file():
                continue
            txt = p.read_text(encoding="utf-8", errors="replace")
            m = pat.search(txt)
            expect(m is None, f"secret-like literal in {p.relative_to(ROOT)}: {m.group(0)[:24] if m else ''}")

    def license_ok():
        txt = (ROOT / "LICENSE").read_text(encoding="utf-8")
        expect(txt.startswith("MIT License"), "LICENSE must start with 'MIT License'")
        expect("Copyright (c) 2026 Asdale Dynamics, LLC" in txt,
               "LICENSE must contain exactly: Copyright (c) 2026 Asdale Dynamics, LLC")

    def readme_ok():
        txt = (ROOT / "README.md").read_text(encoding="utf-8")
        expect("Asdale Dynamics, LLC" in txt, "README must credit Asdale Dynamics, LLC")
        expect("python3 site/gen.py" in txt, "README must document the site build command")

    def doc_links():
        for c in CH + ["index.md"]:
            txt = (DOCS / c).read_text(encoding="utf-8")
            for m in re.finditer(r"\]\(([^)#\s]+\.md)\)", txt):
                expect((DOCS / m.group(1)).is_file(), f"{c} links to missing file {m.group(1)}")

    def site_build():
        import importlib.util
        spec = importlib.util.spec_from_file_location("talkbook_gen", ROOT / "site" / "gen.py")
        g = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(g)
        pages = ROOT / "site" / "pages"
        if pages.exists():
            shutil.rmtree(pages)
        g.build()
        problems = g.verify()
        expect(not problems, "; ".join(problems))

    test("docs chapter files present", doc_files)
    test("required coverage (platforms, endpoints, punctuation, privacy, plan)", platform_chapter)
    test("no secrets or keys in files", no_secrets)
    test("LICENSE is MIT with exact copyright line", license_ok)
    test("README credits Asdale Dynamics, LLC", readme_ok)
    test("docs internal links resolve", doc_links)
    test("static site builds with no broken links", site_build)

    print()
    print(f"{7 - len(failures)}/7 checks passed")
    return not failures


if __name__ == "__main__":
    ok = check_all()
    raise SystemExit(0 if ok else 1)
