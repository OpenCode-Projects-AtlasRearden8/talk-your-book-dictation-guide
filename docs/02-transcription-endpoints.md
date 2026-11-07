# Chapter 2 — OpenAI-Compatible & Local Transcription Endpoints

This chapter is optional but powerful: instead of live device dictation, you record voice memos, then a **local transcription server** on your own machine converts them to text. Two big wins for authors:

- **Privacy by architecture.** Your voice audio never leaves your computer.
- **Freedom of form.** Talk while driving, washing dishes, at the gym. The transcript waits for you.

This is the Ollama-friendly: no API keys anywhere approach.

## 2.1 What "OpenAI-compatible" means (in one paragraph)

Many tools expose a **/v1/audio/transcriptions** endpoint that speaks the same request/response format as OpenAI's hosted transcription endpoint. The benefit: one client tool can switch between a cloud provider and your homelab simply by changing two settings — the **base URL** and nothing else. You get cloud-quality ergonomics with local-first freedom, and you never need to create an account just to try something.

## 2.2 What Ollama does here — and what it doesn't

An honest map, because this confuses everyone:

- **Ollama** is a beloved local app for running chat models (Llama, Mistral, Qwen, etc.). If you edit drafts with a local model, Ollama pairs perfectly with this workflow — and we'll use it in Chapter 4.
- **As of writing, Ollama does not host audio transcription.** Its endpoint set does not include /v1/audio/transcriptions, and uploading voice audio to a local chat model the ordinary way is not the intended path.
- The practical pattern used in this guide is therefore: **a dedicated transcription server for audio + Ollama for prose cleanup.** Both stay local; both are keyless; they chain like scissors before a broom.

## 2.3 Two free keyless transcription servers

Pick whichever fits your comfort level. Both work fully offline after setup.

### Option A: whisper.cpp native server (lightest footprint)

Runs the battle-tested Whisper models in C++ on CPU or GPU. No Python environment required.

1. **Download a whisper.cpp model**, e.g. `ggml-base.bin` or `ggml-small.bin` (base is quicker; small trades speed for accuracy).
2. **Dump the source.** Finger-typing build instructions moves faster than one paragraph can: clone the whisper.cpp repository and follow its README's build steps (`cmake -B build && cmake --build build` on most machines).
3. **Start the server:** run its bundled HTTP server (called with a `--server` switch and pointing at your model file). It now listens on localhost for transcription requests in the OpenAI-compatible shape.
4. **Point a client at it** (Chapter 2.4). Base URL: `http://localhost:PORT/v1`.

Good when: you want minimal moving parts, offline after setup, and don't mind typing one terminal command.

### Option B: a Python local server (friendliest UI)

Several open-source projects package Whisper with an OpenAI-compatible HTTP layer, frequently named "Speaches", "faster-whisper-server", or similar. They expose **/v1/audio/transcriptions** directly and are started with one or two commands. You install them with Python's usual tooling; then the endpoint promotes your phone-recorded audio into prose with zero API registration.

Good when: you want the exact OpenAI-compatible shape (so any generic client works), and you're comfortable with `python -m` style commands or a small UI.

Either option works. Speed, memory size, and language options vary slightly; the *workflow identical*.

## 2.4 Pointing a client tool at your local endpoint

The OpenAI-compatible promise means any "talk to a transcription endpoint" tool works by setting:

- **Base URL:** `http://localhost:8080/v1` (or the port your server printed)
- **API key:** anything it requires to satisfy the client — most keyless local servers accept any non-empty string because nothing is actually keyed. Never store a real secret for a local server.

Two author-friendly client styles:

1. **Clipboard-first:** a menubar/indicator app that listens for a hotkey, records, transcribes to your local server, and pastes text into whatever's focused — then Chapter 3's punctuation tricks polish it.
2. **File-first:** you record .m4a or .wav files on your phone, transfer them (USB, cloud folder, or the same Wi-Fi share tools), then send each file to `POST /v1/audio/transcriptions` with the file in the request body and the model name in the normal parameter. The server returns plain text you paste into your draft folder.

File-first is the most forgiving workflow for long-form book work, because it decouples *talking* from *typing*, which lets you record on days you're at the gym but write on days you're at the desk.

## 2.5 Word-cost, memory cost, and model choice

| Whisper size | Rough RAM needed | Best for |
| --- | --- | --- |
| tiny / base | ~1 GB | Fast drafts, long brain dumps, older laptops |
| small | ~2 GB | The sweet spot for most book work |
| medium | ~5 GB | Noisy environments (Cafe, gym audio) |
| large (fleet variants) | 10 GB+ | Accuracy maximalists; often overkill |

Start with **base** or **small**. Don't optimize transcription on day one; upgrade only if you keep hearing the model mishear you on words that matter (medical terms, FFXIV raid names, chess jargon).

## 2.6 The Ollama-friendly pipeline, end to end

Here's the local chain in one glance:

```
Phone / recorder → audio file
      ↓
Local transcription server (whisper.cpp or Python Whisper server)
      ↓  raw spoken text deposited in your draft folder
Ollama (local chat model)  → the sculpting pass, Chapter 4
      ↓
Readable prose → your manuscript
```

No API keys are generated, stored, or rotated anywhere in this chain. If your network sits at home and both servers run on one machine, not a single byte of audio or manuscript ever touches the public internet.

Chapter 4 picks up exactly where the transcript lands and polishes into prose — but first, Chapter 3: making the *raw* dictation cleaner, because punctuation hygiene in your voice saves real editing time later.

## 2.7 Troubleshooting quick-hits

- **Server "connection refused"?** Check the port and that the process is still running. Beginners almost always have a port typo or a server that exited from a missing model file.
- **Audio "unsupported format"?** Convert with a free tool to WAV or use the server's documented accepted formats; some prefer 16 kHz mono WAV. Your server's own docs will list accepted inputs on their project page.
- **Garbled long files?** Many local servers cap audio length per request. Split a long recording at a natural body paragraph with the free audio tool of your choice — splits at silence boundaries are usually automatic.
- **USB versus Bluetooth microphone:** Bluetooth compression shows up in accuracy. In a pinch, the free path around it is a wired or on-device mic.
