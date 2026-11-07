# Chapter 1 — Free Dictation on Every Device

Every device you already own can take dictation for free. Start here, download nothing, and upgrade later only if you want to.

## 1.1 Windows 11 — Windows Speech Recognition & Voice Typing

Two tools live on modern Windows. Voice Typing is the one you'll use daily.

### Voice Typing (Windows 11, free, built in)

1. Click into any text box — Word, Notepad, your browser, your AI editor.
2. Press **Win + H**. A small listening bar appears at the top of the screen.
3. Speak. Normal talking speed is fine; it transcribes as you go.
4. Punctuation commands such as "period", "comma", "new paragraph" work (see Chapter 3).
5. Press **Win + H** again, or Esc, to stop.

First-time setup: Voice Typing asks for permission to use your microphone and connects to Microsoft's online speech service. There is a settings gear on the toolbar where you can toggle **Auto punctuation** and **Voice commands** on — turn both on before book work. Voice Typing needs an internet connection because the modern version is cloud-based; if you need fully offline Windows dictation, see Chapter 2's local server, which is the privacy-first alternative anyway.

### Legacy Speech Recognition (Windows 10 & 11, offline, built in)

Older but fully offline: **Settings → Ease of Access (or Accessibility) → Speech → Speech Recognition**, then follow the wizard and start it with **Win + Ctrl + S**. It is finicky, and accuracy trails Voice Typing, but it works with no internet. Good to know it exists as a backup, not your daily driver.

## 1.2 macOS — free built-in dictation

1. **Apple menu → System Settings → Keyboard → Dictation**, toggle it on. With "Siri & Dictation" set to *on-device*, recent Macs transcribe locally with no internet.
2. Set a **dictation shortcut** next to the toggle — default double-press of a Control key. Two-tap, talk, two-tap: a rhythm your wrists will thank you for.
3. Click into your text field and fire the shortcut. Speak. Press the shortcut again to stop.

Notes for authors:

- Mac dictation on Apple Silicon is fast and decently accurate, and the offline setting makes it the easiest fully-private option of any major platform.
- It does **not** auto-punctuate on many versions; run the punctuation tricks from Chapter 3 or the cleanup pass in Chapter 4.
- **MacOS Voice Control** (Accessibility settings) is a deeper tool that lets you say commands like "Select paragraph" — genuinely useful for editing by voice, worth exploring after a week.

## 1.3 iPhone — free dictation while walking

Dictation on iPhone runs on-device on recent models and is often excellent.

1. In any text field, tap the **microphone key** in the keyboard's bottom row. If it's missing: **Settings → General → Keyboard → Enable Dictation**.
2. Talk. Tap the mic again (or tap in the text) to stop.
3. iOS auto-punctuates in recent versions, and newer iOS can even auto-insert your typed **Text Replacements** mid-dictation.
4. Bonus move for authors: pair it with the **free Notes or Pages app**, or better, talk straight into a notes app synced to your editor.

The killer author combination is **walking + dictation**: voice drafts are one of the only forms of writing that pairs with exercise. Ten blocks around the neighborhood becomes a thousand words before you're back at your door.

## 1.4 Android — Gboard voice typing

1. Tap any text field to summon **Gboard**.
2. Tap the **microphone icon** on the toolbar.
3. Speak; tap the mic again to stop.
4. **Settings → System → Keyboards → Gboard → Voice typing → Faster on-device typing** enables offline recognition on many recent phones — check this box if you want drafts created with no data leaving the device.

Pixel phones have exceptionally good on-device dictation, including automatic punctuation. Samsung keyboards work similarly through the mic key. If your keyboard lacks a mic icon, install Gboard from the Play Store — it's free and Google's keyboard works on any Android.

## 1.5 Free cloud transcription you can also use

If you prefer *talking into audio files* (e.g., you brainstorm on a phone voice memo) rather than live dictation:

- **Windows Voice Typing** and phone dictation are live-transcription, no upload of audio files.
- For file-based notes, the fully-free path is running a **local transcription server** in Chapter 2, which converts your audio to text on your own machine. Several free apps can also front this for you.
- Avoid pasting unpublished manuscript audio into random websites promising "free transcription." Chapter 5 explains why.

## 1.6 Which tool, when?

| Situation | Best free choice |
| --- | --- |
| Quick scene at the desk (Windows) | Windows Voice Typing (Win + H) |
| Quick scene at the desk (Mac, private) | macOS dictation, on-device setting |
| Walking, commuting, lying down | Phone dictation into Notes |
| Spiral-of-ideas 20-minute brain dump | Phone voice memo → transcribe later (Chapter 2) |
| Legal or privacy-sensitive content | On-device dictation or Chapter 2 local server only |

You now have zero-cost dictation everywhere. Next chapter, for those ready, is the local-first power move: a no-API-key transcription endpoint on your own computer.
