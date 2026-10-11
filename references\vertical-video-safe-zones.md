# Vertical Video (9:16) Safe Zone Specification

This reference defines the strict spatial layout and safe visual zones for **1080 x 1920 (9:16 aspect ratio)** vertical videos across YouTube Shorts, TikTok, and Instagram Reels. 

Any text, equation, card, or vital visual subject placed outside these safe boundaries will be clipped, obscured by platform UI icons (like/comment buttons, caption overlays, account handles), or cut off on various mobile screen aspect ratios (19.5:9, 20:9, 16:9).

---

## 1. Master Canvas Grid (1080 x 1920 px)

```
0px ------------------------------------------------------------- 1080px
    |                      TOP DEAD ZONE                        |  Y: 0 - 220px
    |   [Platform status bar, search icon, sound pills, tabs]   |
220px |---------------------------------------------------------|
    |                                                           |
    |                   TOP SAFE ZONE (HEADROOM)                |  Y: 220 - 450px
    |          [Perplexity Search Bar / Video Hook Card]        |
    |                                                           |
450px |---------------------------------------------------------|
    |                                             |             |
    |                                             |             |
    |              PRIMARY ACTION ZONE            |  RIGHT      |
    |                                             |  UI ZONE    |  Y: 450 - 1450px
    |   - Symphony visual subjects                |             |
    |   - Hyperframes interactive cards           |  Like,      |  X: 920 - 1080px
    |   - LaTeX equations & diagrams              |  Comment,   |  (Dead for
    |   - Code diff comparisons                   |  Share,     |   vital UI/text)
    |   - Benchmark charts                        |  Audio disc |
    |                                             |             |
    |                                             |             |
1450px|---------------------------------------------------------|
    |                                                           |
    |               SUBTITLE & CAPTION ZONE                     |  Y: 1450 - 1640px
    |      [Dynamic word-highlight captions (Max 3-5 words)]     |
    |                                                           |
1640px|---------------------------------------------------------|
    |                    BOTTOM DEAD ZONE                       |  Y: 1640 - 1920px
    |      [Creator handle, caption text, audio title, CTA]     |
1920px-----------------------------------------------------------
```

---

## 2. Precise Coordinate Boundaries

| Zone | X Range (Horizontal) | Y Range (Vertical) | Safe For | Prohibited Content |
|---|---|---|---|---|
| **Top Dead Zone** | `0px – 1080px` | `0px – 220px` | Background atmosphere, ambient gradients | Titles, hooks, search bars, key text |
| **Top Header Zone** | `70px – 1010px` | `220px – 450px` | Perplexity search bar, Hook cards, topic badges | Body paragraphs, complex diagrams |
| **Hero Focus Zone** | `70px – 900px` | `450px – 1450px` | **All core content**: Symphony subjects, LaTeX math, code blocks, diagrams | None (Optimal golden rectangle) |
| **Right UI Gutter** | `910px – 1080px` | `550px – 1550px` | Symphony background imagery only | Equations, code lines, buttons, citations |
| **Subtitle Safe Zone**| `120px – 880px` | `1480px – 1620px` | Dynamic active-word subtitles | Static charts, code snippets |
| **Bottom Dead Zone**| `0px – 1080px` | `1640px – 1920px` | Clean background gradient fade | Any text, diagrams, labels, citations |

---

## 3. Composition Rules for Symphony (9:16 Vertical)

Symphony creates strictly vertical media. Adhere to these three spatial rules:

1. **Upper-Third Headroom**:
   Center the focal point of the shot at `Y = 700px` to `Y = 950px`. Never position the primary object in the lower 400px of the frame.
2. **Vertical Leading Lines**:
   Compose with vertical depth—tall server racks, towering chalkboards, vertical microscope tubes, upward fiber-optic strands. Horizontal lines get cropped and lose perspective.
3. **Left-Biased Framing for Dual-Layer Overlays**:
   When planning to overlay a Hyperframes card or LaTeX formula on the right side of the video, instruct Symphony to frame the background physical subject on the left (`X: 100px – 500px`) and leave negative space on the right.

---

## 4. Subtitle Placement Rules

1. **Max Width**: `800px` centered at `X = 540px` (Margins: `140px` on left and right).
2. **Baseline Y-Coordinate**: Fixed at `Y = 1540px`.
3. **Line Wrap Limit**: Never exceed 2 lines simultaneously; prefer single-line 3-4 word bursts.
4. **Padding & Backdrop**: When background Symphony footage has high contrast or motion, render a subtle dark slate pill backdrop (`rgba(17, 20, 24, 0.75)` with `12px` border-radius and `backdrop-filter: blur(8px)`).
