# Chapter 5 — Protecting Manuscript Privacy

Your unpublished manuscript is an asset, and your voice recordings contain your thinking in unfiltered form. This chapter is about keeping both yours. It's written in the spirit Dylan uses everywhere: **local-first by default, cloud only when you knowingly choose it.**

## 5.1 The privacy ladder

Every dictation setup in this manual falls somewhere on one ladder, from most to least private:

1. **Fully local, fully offline.** Ollama chat models + whisper.cpp or a local Whisper server, on an airplane, with no internet. Even a packet sniffer would find nothing. This is the ceiling.
2. **Local hardware, cloud setup tools.** You downloaded Ollama from the internet and pulled a model — but after setup, nothing leaves. Practically the same as level 1 for manuscript content.
3. **On-device cloud-assisted dictation.** Windows Voice Typing, macOS dictation with network setting, phone keyboards: audio or snippets are processed by the platform vendor's cloud service while the tool works, with no audio *file* ever uploaded by you, and pages of an in-progress article are partially in flight.
4. **Explicitly cloud AI editors and transcription services.** Text you paste (or audio you upload) is processed by that company's servers under their privacy policy. Contents invisible to you after that unless the vendor documents otherwise.

Aim for the highest rung your workflow allows — level 1–2 for drafts, levels 3–4 only when you knowingly accept the trade, ideally with drafts already scrubbed of anything sensitive (5.4).

## 5.2 Train yourself to say "cloud marketing silence" out loud

When a tool's documentation doesn't answer *right away* whether your pasted text or uploaded audio is used for model training, treat the silence as a "yes according to their default terms until they update them." Authors of unpublished books should be defensive here for two solid reasons:

- A manuscript copied to a third-party service is a manuscript you've shared, legally, once — before you even knew what you gave away.
- The most common content leak is not a hacker; it's an author pasting early chapters into a tool whose *default* settings changed between versions.

None of this is paranoia. It is informed consent, applied to your words.

## 5.3 Sensitivity triage before the first word

Before you dictate, run a two-question triage on today's intended content:

1. **Does this draft contain anyone's personal data** — patient details, names + conditions, addresses of people who didn't volunteer to be here — or anyone's private matters beyond "my own unedited thoughts"? If yes: **stop** and go to 5.4. Never dictate PHI (protected health information) onto cloud-assisted tools no matter how much faster they are. As a nurse-author, Dylan's rule you should copy: *if it would need HIPAA-style care to share at work, it needs privacy care on the internet.*
2. **Could this draft damage me if it surfaced too early?** Money plans, launch dates, unpublished contract terms. If yes: dictate into the local-only path or a notes app you'd be comfortable handing to a friend — not into clever little apps whose whole privacy answer is buried.

## 5.4 Three no-cost privacy upgrades you can apply today

These take minutes and cover 90% of author risk:

- **Protect the names from the first take.** Write about people you know using pseudonyms or initials from the very first dictation. Chapter 4's find-and-replace pass then swaps them for real names (or not) in one clean motion — something late-day phone cleanup never reliably does.
- **Treat voice memos as short-lived fuel.** Keep one folder for raw voice memos and one for finished transcripts. After a memo is transcribed and saved, delete it and empty the trash — once a week is plenty. Old memos stopped paying rent the day they were transcribed, but they can still embarrass you later — delete them.
- **Back up like an author, not a cloud app user.** Your manuscript needs to exist in two places at all times: your working machine and one physical/encrypted destination (an external drive at minimum). "My drafts are in that one free web app" means somebody else's privacy policy is your backup plan. It works — until it doesn't.

## 5.5 What you don't need to fear

For balance: everyday dictated prose about ideas, characters, opinions, and craft is fine to any level of the ladder. You do not need zero-cloud absolutism to write safely. You need:

- One consistent, mostly-private path for *the manuscript itself* (levels 1–2 recommended).
- A habit of triage before you dictate anything sensitive (5.3).
- Backup discipline (5.4).

That's it. Privacy is a staircase, not a summit — get on the right step, and write.

## 5.6 If you choose to publish…

Once the manuscript has launched, ties to privacy loosen — but two principles stay:

- Old drafts may contain names or details you changed before launch. Keep the clean final draft and one backup of the manuscript file; delete the rest of the intermediate clutter once you've confirmed what survived into the book.
- Beware the "just testing the AI voice-over" step at audiobook production time, which in some tools sends your entire manuscript to a third-party audio service. Read what got sent, once. That's the same reflex you're practicing now; just in a different chapter of the book.
