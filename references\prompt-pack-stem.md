# Prompt Pack: Production-Grade STEM Prompts

Inspired by `02 PROMPT PACK`, this catalog provides battle-tested, copy-pasteable prompts engineered for **Symphony (vertical 9:16)**, **Hyperframes**, **Neural Voiceover**, and **Clipchat**.

---

## 1. Symphony 9:16 Vertical Prompts (Copy & Paste)

### A. The Semiconductor Wafer Fab Cleanroom
```
[P] PHOTOGRAPHIC STYLE: 35mm anamorphic cine-lens, ARRI Alexa 65 sensor look, fine photochemical grain, 9:16 portrait vertical framing.
[I] IMAGERY & SCENE: State-of-the-art semiconductor fabrication cleanroom. An automated robotic vacuum gripper holds an ultra-pure 300mm silicon wafer reflecting ambient circuitry patterns.
[C] CAMERA & COMPOSITION: Vertical angle, camera low at chest height, subject centered in middle third with clean upper headroom for text overlay. 35mm prime lens at f/2.8.
[T] TIMING & LIGHTING: Industrial cleanroom LED ceiling grid (5600K) with a sharp electric cyan rim light along the edge of the robotic arm.
[U] USE OF ATMOSPHERE: Micro-filtered air, subtle optical lens flare off the mirror finish of the silicon disc.
[R] RENDER STYLE: Absolute tactile realism, brushed stainless steel, copper cooling tubes, zero cartoon/CGI gloss.
[E] EXTRA MOTION: Slow steady camera push forward over 4 seconds, single camera motion vector.
```

### B. The Quantum Optics Laser Bench
```
[P] PHOTOGRAPHIC STYLE: 100mm macro cine-lens, shallow depth of field, 9:16 vertical composition.
[I] IMAGERY & SCENE: An optical breadboard table in a quantum physics lab. An electric cyan 480nm laser beam reflects through high-reflectivity dielectric mirror mounts and a beam splitter cube.
[C] CAMERA & COMPOSITION: Extreme close-up macro, camera locked off, shallow f/2.0 aperture with creamy foreground and background bokeh.
[T] TIMING & LIGHTING: Dim ambient room lighting, specular cyan laser glow illuminating brushed aluminum optical posts.
[U] USE OF ATMOSPHERE: Faint laboratory air dust motes scattering the coherent laser path.
[R] RENDER STYLE: Photorealistic physical optics, anti-reflective optical coatings with subtle purple-green sheen.
[E] EXTRA MOTION: Micro-rack focus from the beam splitter entrance to the exit mirror over 3.5 seconds.
```

### C. The Enterprise AI Supercomputer Server Hall
```
[P] PHOTOGRAPHIC STYLE: 24mm wide cine-lens, architectural realism, 9:16 vertical orientation.
[I] IMAGERY & SCENE: Towering vertical server racks inside an AI data center. Braided blue and cyan fiber-optic cabling cascades down vertical cable managers with active status LEDs.
[C] CAMERA & COMPOSITION: Low-angle vertical perspective looking up at the 9-foot server rack, accentuating vertical height.
[T] TIMING & LIGHTING: Moody dark data hall, cool slate illumination punctuated by rhythmic pulsing LED fiber indicators.
[U] USE OF ATMOSPHERE: Cold containment aisle airflow, subtle air shimmer.
[R] RENDER STYLE: High-end industrial hardware engineering, matte black powder-coated steel.
[E] EXTRA MOTION: Slow vertical pedestal-down camera movement descending along the server rack face over 4 seconds.
```

---

## 2. Hyperframes Code Snippets (Ready to Render)

### A. Perplexity Query Bar with Typing Simulation
```json
{
  "template": "TMPL-01",
  "canvas": { "width": 1080, "height": 1920 },
  "components": [
    {
      "type": "PerplexitySearchBar",
      "x": 80,
      "y": 280,
      "width": 920,
      "height": 96,
      "borderRadius": 24,
      "backgroundColor": "#1B1F26",
      "borderColor": "#23272F",
      "text": "How does FlashAttention-2 tile SRAM memory?",
      "typingSpeedMs": 42,
      "cursorColor": "#20B8CD",
      "cursorPulse": true
    }
  ]
}
```

### B. Stepwise LaTeX Attention Formula Highlight
```json
{
  "template": "TMPL-11",
  "canvas": { "width": 1080, "height": 1920 },
  "components": [
    {
      "type": "LatexContainer",
      "x": 80,
      "y": 520,
      "width": 920,
      "formula": "\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V",
      "fontSize": 44,
      "color": "#F3F3EE",
      "highlights": [
        { "target": "\\sqrt{d_k}", "color": "#20B8CD", "label": "Variance Normalization", "enterMs": 1200 }
      ]
    }
  ]
}
```

---

## 3. Voiceover Punctuation & Phonetic Guides

Neural TTS models require phonetic pronunciation tags and strategic punctuation to sound natural:

```
[VOICEOVER SCRIPT PROMPT]
"Most engineers think attention is compute-bound.
It's not... — it's memory-bandwidth bound. [PAUSE 0.5s]
Every token requires reading the entire key-value cache from H-B-M [spell out letters: H, B, M].
That's Big-O of N-squared memory transfers.
Flash-Attention changes the math entirely. [NEEDLE DROP 0.8s SILENCE]
Instead of materializing the full N-by-N attention matrix in slow memory,
it tiles the computation into ultra-fast on-chip S-RAM..."
```

---

## 4. Clipchat Master Timeline Cut Template

```json
{
  "sequence": {
    "fps": 60,
    "width": 1080,
    "height": 1920,
    "lut": "references/PerplexityDarkSlate.cube"
  },
  "cuts": [
    {
      "timecode": "00:00:00",
      "v1_symphony": { "src": "wafer_macro.mp4", "in": 0.5, "out": 3.8 },
      "v2_hyperframes": { "src": "tmpl01_query.webm", "enter": "fadeSlideUp" },
      "a1_voice": { "line": "Most engineers think...", "j_cut_lead_frames": 6 }
    },
    {
      "timecode": "00:03:30",
      "v1_symphony": { "src": "server_pedestal.mp4", "in": 0.6, "out": 4.5 },
      "v2_hyperframes": { "src": "tmpl24_memory_wall.webm", "enter": "slideUp" }
    }
  ]
}
```
