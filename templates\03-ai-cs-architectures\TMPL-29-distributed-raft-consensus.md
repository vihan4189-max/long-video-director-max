# Template TMPL-29-distributed-raft-consensus: Distributed Raft Consensus & Leader Election

**Category**: `03-ai-cs-architectures`  
**Domain**: `Distributed Systems`  
**Component Archetype**: `Raft Consensus`  
**Design Standards**: Perplexity ([www.perplexity.ai](https://www.perplexity.ai)) Dark Slate & Cyan Specification

---

## 1. Overview & Purpose
Cluster of 5 server nodes with heartbeat pings, election timeouts, and synchronized log commits.

Designed strictly for **1080 x 1920 (9:16 vertical)** video formats. Optimized for programmatic rendering in **Hyperframes** and seamless multi-track overlay in **Clipchat**.

---

## 2. Perplexity Design Tokens & Spatial Geometry

```css
:root {
  --canvas-width: 1080px;
  --canvas-height: 1920px;
  --card-bg: #111418;
  --card-border: 1px solid #23272F;
  --card-radius: 16px;
  --accent-color: #10B981;
  --text-primary: #F3F3EE;
  --text-secondary: #9DA3AE;
  --text-muted: #646C7A;
  --easing-spring: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Canvas Safe Zones
- **Top Bound**: `Y >= 240px` (clearing mobile search / platform indicators)
- **Bottom Bound**: `Y <= 1450px` (clearing dynamic subtitles and engagement buttons)
- **Left Margin**: `80px`
- **Right Margin**: `80px` (usable width: `920px`)

---

## 3. Hyperframes Motion & Layout Specification

```json
{
  "templateId": "TMPL-29-distributed-raft-consensus",
  "version": "2.0",
  "canvas": { "width": 1080, "height": 1920 },
  "theme": {
    "background": "#111418",
    "border": "#23272F",
    "accent": "#10B981",
    "text": "#F3F3EE"
  },
  "animation": {
    "enter": "slideFadeUp",
    "durationMs": 320,
    "easing": "cubic-bezier(0.16, 1, 0.3, 1)",
    "initialOffset": { "y": 14 },
    "opacity": [0, 1]
  },
  "elements": [
    {
      "id": "container_card",
      "type": "card",
      "x": 80,
      "y": 480,
      "width": 920,
      "height": 580,
      "borderRadius": 16,
      "backgroundColor": "#111418",
      "borderColor": "#23272F",
      "boxShadow": "0 8px 32px rgba(0,0,0,0.5)"
    },
    {
      "id": "header_pill",
      "type": "pill",
      "x": 120,
      "y": 520,
      "text": "DISTRIBUTED SYSTEMS // RAFT CONSENSUS",
      "fontSize": 20,
      "color": "#10B981",
      "backgroundColor": "rgba(32, 184, 205, 0.12)"
    },
    {
      "id": "primary_content",
      "type": "content_block",
      "x": 120,
      "y": 580,
      "width": 840,
      "lineHeight": 1.4
    }
  ]
}
```

---

## 4. Director's Execution Logic & Integration

1. **When to Trigger This Template**:
   - Use during Stage 6 (Hyperframes Motion) when the script requires clear visual evidence for raft consensus.
2. **Pacing Rules**:
   - Minimum visual hold: `2.4 seconds` (allows viewer to absorb layout).
   - Maximum visual hold without secondary state transition: `4.5 seconds`.
3. **Clipchat Multi-Track Placement**:
   - Place on **Track V2** (Motion Graphics).
   - Sync the initial card entrance with a `J-cut` audio lead (voiceover begins 6 frames before card appears).
   - Pair with subtle SFX: `ui_card_slide.wav` (-24 dB) on Track A2.

---

## 5. Quality Checklist & Verification

- [ ] All coordinates adhere to 9:16 safe bounds (`Y: 240px - 1450px`, `X: 80px - 1000px`)
- [ ] Motion curve uses `cubic-bezier(0.16, 1, 0.3, 1)`
- [ ] Text typography strictly uses `Inter`, `Iowan Old Style`, or `JetBrains Mono`
- [ ] No saturated neon TikTok colors; strictly Perplexity muted palette with cyan `#10B981` accents
