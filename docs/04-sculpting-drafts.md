# Chapter 4 — Sculpting Spoken Drafts into Readable Prose

Dictation gives you raw ore. This chapter is the refinery. The art: turn honest-but-messy spoken text into prose a reader never flinches at, in minutes — not hours — using the AI editor of your choice. Cloud editors, local editors, Ollama — all work. The workflow is brand-agnostic on purpose.

## 4.1 Why spoken drafts need a different kind of editing

Spoken prose has telltale signatures, and knowing them makes sculpting mechanical instead of mysterious:

- **Filler strokes:** "you know", "kind of", "like", "so basically", "what happened was".
- **Rambly setups:** long wind-ups before the point ("Okay so the thing about this is that…").
- **Sentence spaghetti:** one sentence that was three.
- **Repeated rephrasing:** you said the idea three ways while you warmed up. All three are in the draft.
- **Punctuation drift:** from Chapter 3, some marks will be wrong or missing.

Notice what's *not* on this list: substance. Dictated drafts are usually too talky, **not** too flimsy — your ideas are already there. Sculpting is subtraction, not invention.

## 4.2 The two-pass sculpture (memorize this)

### Pass 1 — Structural, by you, fast, in the text itself (5–10 min)

- Delete a repeated restatement (keep the version you liked hearing).
- Mark with your editor's find tool any word you over-use ("actually", "really").
- Reorder or delete whole paragraphs while they are visible blocks — voice drafts rearrange *best* in units of paragraphs.
- Fix every placeholder from Chapter 3.3 (names, terms) with find-and-replace.

Do this by hand so you stay the architect. Five minutes beats a machine here because *what to keep* is a taste decision that costs you nothing when you're still warm from dictating.

### Pass 2 — Line polish, by your AI editor (10–15 min)

Paste the structurally-cleaned draft into your AI editor and use a **sculpting prompt** (4.3–4.4). The prompt transforms one chapter-shaped block of prose at a time — not your entire book in one gesture, which is how people end up with a voice that isn't theirs.

## 4.3 The master sculpting prompt (paste this one first)

```
You are a book editor for a friendly, plain-English author voice.
Here is a raw DICTATED FIRST DRAFT. It may contain filler words,
tangents, punctuation glitches, repetition, and missing pause marks.

Do all of the following:
1. Fix punctuation, paragraph breaks, and capitalization.
2. Remove filler phrases ("you know", "kind of", "like", "so basically")
   and false starts — do NOT remove substance or examples.
3. Break any sentence longer than ~25 words into plainer sentences.
4. Keep my meaning, my examples, my term choices, and my tone exactly.
5. Never add facts, ideas, or claims that are not in the draft.
6. End with: three short bullets, "Structural Suggestions",
   still nothing invented.

Draft:
[YOUR PASTE HERE]
```

Why the guardrails matter: items 1–3 delete noise; item 4 preserves you; item 5 keeps the AI from *influencing your book by answering a question nobody asked*; item 6 gives you free self-editing feedback for the *next* dictation session.

## 4.4 A small prompt library for book work

Save these as reusable "snippets" in whatever editor you chose; copy-paste, not retyped, every session.

- **Chapter tightening:** "Trim this dictated chapter by 15% without losing any fact, example, or transition. Flag every cut with a one-line rationale."
- **Ending hooks:** "Suggest 3 ending sentences for this section, each under 20 words, each raising a question the reader wants answered. Do not use hype words."
- **Clarity check (the friend test):** "Explain this section back to me in one plain paragraph, as if testing I made my point. Then list any sentence where meaning is ambiguous."
- **Chapter automation handoff:** "Compress this section for a time-pressed reader into 5 bullets. Do not invent. Keep beginner-friendly wording."
- **Local/keyboard-less mode (Ollama, no keys, no cloud):** "Here is a dictated chapter. Return it with punctuation, paragraph breaks, and filler removed. Keep my voice." — Works with any chat-capable local model like the ones Ollama runs: Llama, Mistral, Qwen, etc.

## 4.5 Local editor choice — using Ollama as your AI editor

If you want the sculpting pass local too (private, offline, free forever):

1. **Install Ollama** from ollama.com (Windows/macOS/Linux, free).
2. Pull a chat model sized to your machine: `ollama pull llama3.1:8b` — a strong default for prose work on 8–16 GB laptops.
3. Run it: `ollama run llama3.1:8b`, then paste your Chapter 4.3 prompt and draft.
4. Better yet, point any free Ollama-compatible desktop editor/chat UI at `http://localhost:11434` and keep your prompt snippets as saved presets.

Local models are very good at *cleanup* work (filler, punctuation, sentence splitting) and very capable at the *friend test*. They are somewhat weaker than top cloud models at subtle line-level style. That's fine — your voice is the style; cleanup is arithmetic. If you want sharper phrasing help, that's the one place a cloud editor pulls ahead, and Chapter 5 tells you when that's worth the trade.

## 4.6 The reading-aloud loop (the human algorithm)

AI editors are one instrument. The best "test" of sculpted prose is free and zero-tech:

1. Read your sculpted draft **out loud**, standing up.
2. Every sentence your mouth trips on: shorten it or split it on the spot.
3. Repeat. Three laps usually converge. Sleep is the fourth lap.

This matters double for dictated books: the reader *hears* prose in their head voice. Prose that can't be spoken comfortably is prose that won't *sound* right in your reader's head.

## 4.7 The sculpting session checklist

At your next editing session, run in this order:

- [ ] Structural pass (filler, rephrasing, placeholders) — by hand
- [ ] Paste into AI editor, run the 4.3 prompt for one section
- [ ] Apply line polish; keep your version wherever the AI's sounds less like you
- [ ] Read aloud lap
- [ ] Save, and log your word count into the Chapter 6 tracker

Do that twice a week and your dictated book will outrun your theoretical typing speed by an amount you'll find slightly funny.
