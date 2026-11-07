# Chapter 3 — Punctuation Control Tricks

Raw dictation sounds like a river with no banks: no pauses marked, no sentences separated, lowercase and unloving. This chapter builds the banks. Master these tricks and your sculpting pass (Chapter 4) gets dramatically easier — sometimes it nearly disappears.

## 3.1 Spoken punctuation commands

The built-in dictation tools (Chapter 1) understand the following voice commands. Say the punctuation *smoothly*, right where you want the mark, and keep speaking. Don't wait for the mark to appear in a pause.

**Windows Voice Typing / macOS / Gboard — widely supported commands:**

| To get | Say |
| --- | --- |
| , | "comma" |
| . | "period" or "full stop" |
| ? | "question mark" |
| ! | "exclamation mark" or "exclamation point" |
| : | "colon" |
| ; | "semicolon" |
| new line | "new line" |
| new paragraph | "new paragraph" |

Platform extras:

- **Windows Voice Typing** with *Auto punctuation* on will guess full stops from pauses; "comma" and "period" still work as explicit commands.
- **Gboard** on Pixel supports quotation marks, parentheses, hyphen, dash; reliability varies by phone and version, so test three marks before you write a whole session with them.
- **macOS dictation** historically has fewer command-marks; lean on the pause-and-cleanup tool next (3.2) or the AI pass in Chapter 4.

## 3.2 The pause discipline (the real trick)

The single best punctuation trick isn't a command at all — it's a **two-beat pause at the end of every sentence**, and a **three-beat pause at the end of every paragraph**.

- With auto-punctuation tools, the pause itself often inserts the missing period.
- With every tool, pauses give the recognizer a boundary, which measurably improves accuracy of the *next* sentence.
- Saying "period" aloud on top of the pause costs two syllables and guarantees the bank against misrecognition. Use "period" during drafting, and let pauses be your paragraphs' punctuation, then the double-newline comes from "new paragraph".

Beginner sentence shape that works beautifully:

> The hero doubted everything. *period* Two-beat. The storm outside was stronger than the argument. *period* New paragraph.

Your ears learn this rhythm in about two sessions. After a week you won't hear it — you'll *speak* it.

## 3.3 Naming things (dictating tricky words)

Recognizers stumble on proper nouns — medical vocabulary, character names, FFXIV terms, internet words. Tricks:

1. **Spelling out now, fixing later:** dictate a clearly-marked placeholder like "wolfheart" and fix all placeholders in one find-replace pass at the desk. Chapter 4's AI pass also resolves these with a quick prompt.
2. **Text Replacements / AutoCorrect:** every platform has a shortcut-expansion feature (iOS **Settings → General → Keyboard → Text Replacement**; macOS **Keyboard → Text Replacements**; Word autocorrect). Add entries so that typing (or dictation on iOS) expands "fxy" to "Fyrewyrm" automatically. This is a superpower for character names and repeated technical phrases.
3. **Numbers:** say digits plainly ("ten-point-five" versus any clever spelled-out effort) and let your sculpting pass decide the style for your book. Consistency comes from Chapter 4's style sheet.

## 3.4 Quoting, dialogue, and markup by voice

Book work has punctuation Voice Typing doesn't guess: dialogue quotes, em-dashes, italics. Two policies:

- **Dialogue substitution policy:** draft dialogue by saying "quote… unquote" around spoken lines, then clean it up in one pass in your editor (Chapter 4 has a ready-made prompt). Second-best policy, fine for a *first draft*: skip the quotes and let the sculpting pass add them — it can identify who is speaking almost every time.
- **Em-dash hack:** say "dash" where you want one and let Chapter 4 regularize which style your book uses. Or skip dashes entirely while dictating; where a dash would go, just breathe and keep talking. Dashes are easy to add in the sculpting pass, and easy to over-use for months after.

## 3.5 A one-minute test session

Do this right now, whichever device you're on:

1. Open a notes app. New note.
2. Dictate exactly: "Dictation loves long, honest first drafts. It punishes nobody. I am going to talk through one chapter of my book — starting now."
3. Speak with periods and one new paragraph. Tap stop. Read it.

Count problems: likely 0–2, not ten. That's the whole trick demonstrated. When your *raw* dictation is this close, the editorial distance to "readable prose" is short, which is exactly Chapter 4's promise.

## 3.6 When marks go wrong

- A spoken "comma" appearing as the word "comma" in the draft text: the recognizer was in a mode that didn't hear commands. Toggle **Voice commands / Auto punctuation** off and on in that tool's settings; re-test with the one-minute session above.
- Run-on walls of text with no marks: your devices swapped to a *no-command* mode, or you forgot the pause discipline for two paragraphs. Never re-dictate — fix it in seconds in Chapter 4's sculpting pass instead.
- Wrong-but-adjacent marks (period got typed as comma): *don't* fight the tool mid-flow. Continue drafting; a final pass converts punctuation wholesale by search or by AI instruction ("turn comma + 2 spaces at sentence ends into periods" style prompts).
