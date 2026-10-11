---
name: "06-clipchat-assembly"
description: "Mastery guide for Clipchat timeline video editing, multi-track sequencing, and final render assembly. Enforces artifact trimming (first/last 0.5s), J-cut audio leading, dynamic audio ducking, LUT color grading, and mathematical pacing."
---

# Sub-Skill: Clipchat Timeline Multi-Track Assembly

Generated assets are not a video—they are raw ingredients. Clipchat is where raw Symphony video clips, Hyperframes motion graphics renders, voiceover stems, sound effects, and music are assembled into a coherent, publication-grade film.

This sub-skill provides the professional editorial workflows, multi-track timeline organization, and cut mechanics required to eliminate the "AI feel" and produce a broadcast-grade master.

---

## 1. The Multi-Track Timeline Architecture (1080 x 1920 @ 60fps)

Clipchat timelines must be organized with strict layer discipline:

```
[V3] DYNAMIC SUBTITLES & WATERMARK (Y: 1540px, safe overlay)
[V2] HYPERFRAMES MOTION GRAPHICS (Cards, LaTeX formulas, code diffs, citations)
[V1] SYMPHONY B-ROLL & REAL-WORLD ASSETS (Cleanroom, servers, optics, PR demos)
---------------------------------------------------------------------------------
[A1] VOICEOVER STEM (Dialogue, -14 LUFS, center mono)
[A2] SFX & FOLEY (Keystrokes, paper rustle, sub-bass drops, whooshes)
[A3] AMBIENT MUSIC SCORE (Modular synth drone, ducked to -24 dB under voice)
```

---

## 2. The Four Editorial Laws of AI Video Cutting

### Law 1: Always Trim the Head and Tail of Symphony Generations
AI video diffusion models exhibit maximum drift, rubbery morphing, and stuttering during the first 12–15 frames and the final 15–20 frames.
- **Protocol**: Never use the full duration of a generated clip.
- Trim at least **0.4s – 0.6s off the start**, and **0.5s – 1.0s off the end**.
- The remaining middle section is stable, coherent, and artifact-free.

### Law 2: The J-Cut (Audio Leads the Visual Turn)
Never execute a hard simultaneous audio-visual cut where both the speaker's new topic and the new visual change on the exact same frame. This feels robotic and abrupt.
- **The J-Cut Rule**: Let the voiceover start speaking the next sentence **4 to 8 frames (0.15s – 0.25s) BEFORE** the visual cuts from Shot A to Shot B.
- This primes the viewer's auditory cortex, making the visual transition feel natural and motivated.

### Law 3: Cut on the Turn, Not on the Metronome
Amateur editors align cuts strictly to musical beats (every 2.0s or 3.0s). The brain quickly anticipates this mechanical pattern, causing viewer fatigue.
- Cut when an argument pivots, when an equation reveals its resolution, or when an error triggers.
- Vary clip duration intentionally:
  - Hook / Problem: Fast momentum (`1.2s – 2.0s` per shot)
  - Mathematical / Code Intuition: Extended hold (`3.5s – 5.5s` while motion graphics highlight lines)
  - Climax / Realization: Deep hold (`4.0s – 6.0s` with slow scale-up)

### Law 4: Audio Ducking Discipline
- When voiceover is active, Duck Track A3 (Music) down to `-24 dB`.
- When voiceover takes a breath pause or needle-drop occurs, raise music up to `-14 dB` with a smooth 150ms exponential crossfade.

---

## 3. Unifying the Aesthetic: Perplexity Dark Slate Color Grade

Symphony clips generated from different seeds can have slight color temperature mismatches. In Clipchat, apply an **Adjustment Layer** across the entire V1 track:

```
[Clipchat Grade Parameters]
- Temperature: -4 (Slight cool slate tint, 5200K)
- Saturation: 0.88 (Subtle academic desaturation, removing oversaturated yellow skin tones)
- Lift (Shadows): +0.02 (Lifted deep blacks to Perplexity dark ink #111418)
- Highlight Tint: Subtle Cyan (#20B8CD, +2% in specular highlights)
- Contrast: 1.12 (Crisp separation on hardware and glass)
```

---

## 4. Clipchat Project Specification File (`timeline_edit.json`)

When communicating with Clipchat via API or agent instruction, format the edit EDL (Edit Decision List):

```json
{
  "project": {
    "title": "FlashAttention_Explained",
    "resolution": { "width": 1080, "height": 1920 },
    "fps": 60,
    "durationSeconds": 58.4
  },
  "tracks": {
    "video": [
      {
        "id": "v1_broll",
        "clips": [
          { "src": "assets/symphony_shots/shot_01_wafer.mp4", "in": 0.5, "out": 3.8, "start": 0.0 },
          { "src": "assets/symphony_shots/shot_02_server.mp4", "in": 0.6, "out": 4.2, "start": 3.3 }
        ]
      },
      {
        "id": "v2_motion",
        "clips": [
          { "src": "assets/hyperframes/tmpl01_search_bar.webm", "start": 0.2, "duration": 3.2, "blend": "normal" },
          { "src": "assets/hyperframes/tmpl24_memory_hierarchy.webm", "start": 3.4, "duration": 5.0, "blend": "normal" }
        ]
      }
    ],
    "audio": [
      { "id": "a1_voice", "src": "audio/voiceover_master.wav", "gain": 0.0, "start": 0.0 },
      { "id": "a2_music", "src": "audio/dark_ambient_pulse.wav", "gain": -24.0, "ducking": { "threshold": -30, "reduction": 10 } }
    ]
  }
}
```

---

## 5. Clipchat Final Acceptance Checklist

Before exporting the final master MP4:
- [ ] Every Symphony clip has its first 0.5s and last 0.5s trimmed
- [ ] No visual elements clash with dynamic subtitles or platform UI safe zones
- [ ] J-cuts are applied to at least 70% of voiceover transition points
- [ ] Global Perplexity Dark Slate LUT is applied across all video footage
- [ ] Music ducking is smooth with zero audio clicks or pops
- [ ] Output renders at exactly 1080 x 1920 @ 60fps (H.264 or ProRes 422 HQ)
