---
name: "04-hyperframes-motion"
description: "Mastery guide for Hyperframes motion graphics engine. Builds Perplexity-grade UI simulations, kinetic typography, animated LaTeX mathematical derivations, syntax-highlighted code diffs, citation cards, and vector DAG architectures using spring physics."
---

# Sub-Skill: Hyperframes Motion Graphics & Perplexity UI Engine

Hyperframes is your programmatic, code-driven motion graphics studio. While Symphony handles photorealistic organic B-roll, Hyperframes handles all information design, mathematical rigor, UI interactions, and typographic clarity.

Hyperframes output must be indistinguishable from native screen interactions on **Perplexity ([www.perplexity.ai](https://www.perplexity.ai))**.

---

## 1. Core Principles of Perplexity Motion Design

### 1. Spring Physics Easing
Never use linear interpolation (`linear`) or generic ease-in-out for cards or UI elements.
- **Perplexity Spring Curve**: `cubic-bezier(0.16, 1, 0.3, 1)`
- Cards enter rapidly, decelerating smoothly into place as if resting on a mechanical dampener.
- Translation: `translateY(12px) -> translateY(0px)` combined with `opacity: 0 -> 1` over `320ms`.

### 2. Information Density with Restraint
Amateur motion graphics crowd the screen with spinning 3D cubes and flying confetti. Perplexity motion is calm, focused, and academic:
- Deep dark slate cards (`#16191E`) with razor-sharp 1px borders (`#23272F`).
- Electric cyan (`#20B8CD`) used exclusively to draw the eye to the key mathematical variable, code change, or citation index.
- Clean typography hierarchy: `Inter` for UI, `Iowan Old Style` for editorial thesis quotes, `JetBrains Mono` for code and citations.

---

## 3. The 5 Core Hyperframes Component Archetypes

### Archetype 1: The Perplexity Query & Pro Search Simulator (`TMPL-01` to `TMPL-04`)
Simulates the interactive search and synthesis engine:
1. **The Search Bar Input**:
   - Background `#1B1F26`, 24px border radius, search icon on left.
   - Text types out at realistic human keystroke cadence (`35ms – 60ms` per character).
   - Pulsating blinking cyan cursor (`#20B8CD`).
2. **Pro Search Step-by-Step Breakdown**:
   - Staggered pill checklist:
     - `● Searching 14 arXiv papers...`
     - `● Parsing FlashAttention CUDA source code...`
     - `● Deriving memory bandwidth equation...`
   - Active step has a glowing cyan pulse animation; completed steps turn slate gray with an emerald checkmark.

### Archetype 2: The Citation Pill Matrix (`TMPL-05`, `TMPL-06`)
- Floating horizontal list of citation pills:
  - Favicon + Domain (`arxiv.org`, `nature.com`) + `[1]` in bold cyan.
  - On entrance, pills slide in from right to left with a 60ms staggered delay.
  - When the voiceover references a source, that pill scales up by 1.05x with an ambient cyan border glow.

### Archetype 3: The Stepwise LaTeX Mathematical Derivation (`TMPL-11` to `TMPL-15`)
Complex equations must never be dumped onto the screen all at once.
- Rendered using KaTeX in clean white math type.
- Step 1 renders initial formula (e.g. \(Attention(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V\)).
- Step 2: The denominator \(\sqrt{d_k}\) highlights in electric cyan with an explanatory callout pill: `"Scale factor to prevent vanishing gradients"`.
- Step 3: Equation morphs smoothly into its memory-efficient tiled equivalent.

### Archetype 4: The Syntax-Highlighted Code Diff Card (`TMPL-23`, `TMPL-24`)
- Minimalist dark terminal card (`#16191E`).
- Header shows filename: `flash_attn.cu` with tab indicator.
- Line numbers in muted gray (`#646C7A`).
- Deleted/inefficient code highlighted in subtle dark crimson (`rgba(239, 68, 68, 0.15)`).
- Optimized kernel code highlighted in subtle dark emerald (`rgba(16, 185, 129, 0.15)`).
- Focus camera zooms into the specific 3 lines that solve the bottleneck.

### Archetype 5: The Vector Architecture DAG & Dataflow (`TMPL-21`, `TMPL-22`)
- Clean rectangular nodes representing layers, tensors, or distributed servers.
- Connecting lines with animated dashes or glowing cyan pulses traveling along the directional vector to demonstrate data movement or message passing.

---

## 4. Hyperframes Layout & Motion Specification Format

When writing Hyperframes specifications in director plans or code files:

```json
{
  "component": "PerplexityCardDerivation",
  "canvas": { "width": 1080, "height": 1920 },
  "safeZone": { "top": 240, "bottom": 1600, "left": 80, "right": 1000 },
  "theme": "darkSlate",
  "elements": [
    {
      "id": "citation_badge",
      "type": "pill",
      "text": "arXiv:2307.08691 [1]",
      "x": 80, "y": 280,
      "animation": { "enter": "fadeSlideUp", "delayMs": 100, "durationMs": 300, "easing": "cubic-bezier(0.16,1,0.3,1)" }
    },
    {
      "id": "latex_formula",
      "type": "latex",
      "content": "S = \\frac{c^3 k_B A}{4 G \\hbar}",
      "x": 80, "y": 520,
      "fontSize": 48,
      "highlightVariable": { "symbol": "A", "color": "#20B8CD", "pulse": true }
    }
  ]
}
```

---

## 5. Hyperframes Quality Checklist

- [ ] All typography uses Perplexity fonts (`Inter`, `Iowan Old Style`, `JetBrains Mono`)
- [ ] No elements cross into top (0–220px) or bottom (1640–1920px) dead zones
- [ ] All animations use the Perplexity spring curve `cubic-bezier(0.16, 1, 0.3, 1)`
- [ ] Mathematical equations are validated LaTeX syntax
- [ ] Code snippets have all non-essential lines removed for instant mobile readability
- [ ] Total visual hold time per card allows an average human to read all text 1.5 times
