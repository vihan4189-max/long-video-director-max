---
name: "05-voiceover-and-subtitles"
description: "Voiceover direction, audio dynamics, and kinetic subtitle generation for no-face technical influencers. Covers vocal cadence for STEM topics, audio needle-drops, Whisper word-level timestamps, and Perplexity active-word subtitle styling."
---

# Sub-Skill: Voiceover Direction & Kinetic Subtitles

In a no-face scientific or engineering video, the voiceover is the spine of the entire production. If the voice sounds like a hyperactive TikTok teenager or a robotic monotone text-to-speech engine, the viewer will drop off in seconds.

This sub-skill provides the complete vocal direction, audio dynamics, and subtitle synchronization protocol matching the high-trust, intellectual standard of Perplexity.

---

## 1. Vocal Persona & Delivery Style (STEM Niches)

### The Ideal Persona: "The Intellectual Colleague"
- **Tone**: Authoritative, calm, curious, conversational. Like a senior DeepMind research scientist or an MIT professor explaining a breakthrough over coffee.
- **Banned Vocal Tropes**:
  - No fake YouTuber hype ("WHAT'S UP GUYS, TODAY WE'RE LOOKING AT...").
  - No dramatic movie trailer gravel voice.
  - No lifeless default robotic TTS without punctuation inflection.
- **Recommended Voice Models**:
  - Deep, clear male or female neutral Mid-Atlantic or British RP/American neutral accents with exceptional micro-inflection (e.g., ElevenLabs "Marcus - Authoritative Explainer", "George - Warm Storyteller", or "Alice - Crisp Academic").

---

## 2. Speech Velocity & Strategic Pacing

Technical information requires time for cognitive processing:

| Video Type | Target Words Per Minute (WPM) | Max Words per 60-Second Video | Target Pause Duration at Key Beats |
|---|---|---|---|
| **High-Velocity Explainer (Shorts/Reels)** | 145 – 155 WPM | 140 – 155 words | `0.4s – 0.6s` at concept shifts |
| **Deep-Dive Math/Physics Proof** | 125 – 135 WPM | 120 – 135 words per min | `0.8s – 1.2s` after formula reveal |
| **Architecture / Code Walkthrough** | 135 – 145 WPM | 135 – 145 words per min | `0.5s – 0.7s` between code lines |

### The Power of Punctuation in Script Prompts
- Use em-dashes (`—`) to force the neural TTS engine to take a micro-pause and lower pitch slightly before an explanation.
- Use ellipses (`...`) to create anticipatory tension before revealing the answer.
- Spell out mathematical symbols phonetically in the voice prompt: write `"hbar"` as `"h-bar"`, `"\sqrt{d_k}"` as `"square root of d-sub-k"`, `"O(N^2)"` as `"Big O of N squared"`.

---

## 3. The Audio Dynamics & The "Needle Drop"

A continuous background music track makes a video feel like an elevator pitch. Great video direction uses musical contrast:

### The 3-Track Audio Hierarchy
1. **Track 1: Voiceover Dialogue**: Centered, normalized to `-14 LUFS`, peak at `-1.0 dB`.
2. **Track 2: Ambient Score / Drone**:
   - Genre: Minimalist modern ambient, modular synth pulses, analog tape textures (Max Richter, Nils Frahm, Trent Reznor & Atticus Ross style).
   - Volume: `-22 dB` to `-26 dB` under voice.
3. **Track 3: UI & Cinematic SFX**:
   - Perplexity keyboard keystroke clicks (`-18 dB`).
   - Deep sub-bass drop / low braam on dramatic reveals (`-12 dB`).
   - High-frequency subtle whoosh on card slide transitions (`-24 dB`).

### The Needle Drop Rule
Build ambient musical tension for 15 to 20 seconds. Then, at the exact moment the critical equation, revelation, or paradox is voiced:
**CUT THE MUSIC COMPLETELY TO ABSOLUTE SILENCE FOR 0.8 SECONDS.**
The silence forces the audience's brain to absorb the mathematical reality. Then drop in a low, resonant sub-pulse as the solution unfolds.

---

## 4. Whisper Word-Level Timestamp Alignment

To sync Hyperframes motion graphics and dynamic subtitles with speech, generate word-level timestamp JSON:

```json
[
  { "word": "Every", "start": 0.00, "end": 0.28 },
  { "word": "transformer", "start": 0.28, "end": 0.85 },
  { "word": "scales", "start": 0.85, "end": 1.15 },
  { "word": "quadratically", "start": 1.15, "end": 1.95 },
  { "word": "with", "start": 1.95, "end": 2.10 },
  { "word": "context.", "start": 2.10, "end": 2.65 }
]
```

---

## 5. Perplexity Subtitle Styling Specification

### Layout & Placement
- **Coordinates**: Horizontally centered (`X = 540px`), Baseline at `Y = 1540px` (inside the Subtitle Safe Zone, above bottom UI elements).
- **Chunking Limit**: Maximum **3 to 4 words** displayed at any moment. Never dump two full sentences on the screen at once.

### Visual Styling
- **Font**: `Inter Bold` or `FK Grotesk Bold`, 42px to 46px.
- **Letter Spacing**: `-0.02em`.
- **Inactive Words**: `#8E95A2` (Perplexity Muted Slate, 75% opacity).
- **Active Spoken Word**:
  - Color: `#F3F3EE` (Perplexity Off-White, 100% opacity).
  - Background Highlight: Subtle cyan pill wrapper `background: rgba(32, 184, 205, 0.2); border-radius: 6px; padding: 2px 8px;` or cyan underline `#20B8CD`.
- **Banned**: No emoji icons popping up on words, no rotation/shaking text, no rainbow colors.

```
[ TRANSFORMERS ]  ===>  [ SCALED ]  ===>  [ QUADRATICALLY ]
   (Muted Slate)       (Active Cyan Glow)     (Muted Slate)
```

---

## 6. Acceptance Checklist

- [ ] Voice pacing falls within 135–155 WPM
- [ ] Mathematical symbols and Greek letters are phonetically pronounced correctly
- [ ] At least one intentional 0.6s–1.0s silence / needle-drop is scripted at the core turn
- [ ] Subtitle baseline is fixed at Y = 1540px, never drifting into platform UI zones
- [ ] Maximum 4 words per subtitle chunk
- [ ] Active-word highlighting matches Perplexity cyan (`#20B8CD`)
