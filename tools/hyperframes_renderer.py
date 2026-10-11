#!/usr/bin/env python3
"""
hyperframes_renderer.py - Programmatic Motion Graphics Renderer for Perplexity Visuals
Compiles Hyperframes JSON templates and design tokens into standalone HTML5/SVG animations.
Zero external dependencies.
"""

import os
import sys
import json
import argparse

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1080, height=1920, initial-scale=1.0">
  <title>Hyperframes Perplexity Render: {title}</title>
  <!-- KaTeX for crisp LaTeX mathematical rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      width: 1080px;
      height: 1920px;
      background-color: {canvas_bg};
      color: #F3F3EE;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      overflow: hidden;
      position: relative;
    }}
    
    /* 9:16 Safe Zone Overlay Indicator (Optional Debug Grid) */
    .safe-zone {{
      position: absolute;
      top: 240px;
      bottom: 470px;
      left: 80px;
      right: 80px;
      pointer-events: none;
      border: 1px dashed rgba(35, 39, 47, 0.5);
    }}

    /* Perplexity Card Container */
    .pplx-card {{
      position: absolute;
      left: 80px;
      top: {card_top}px;
      width: 920px;
      background: {card_bg};
      border: 1px solid #23272F;
      border-radius: 16px;
      padding: 36px 40px;
      box-shadow: 0 12px 40px -4px rgba(0, 0, 0, 0.6), 0 4px 12px -2px rgba(0, 0, 0, 0.4);
      opacity: 0;
      transform: translateY(14px);
      animation: pplxSpringEnter 0.45s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      animation-delay: {animation_delay}ms;
    }}

    @keyframes pplxSpringEnter {{
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}

    /* Perplexity Header Pill */
    .pplx-header-pill {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(32, 184, 205, 0.12);
      border: 1px solid rgba(32, 184, 205, 0.3);
      padding: 6px 14px;
      border-radius: 9999px;
      color: {accent_color};
      font-size: 20px;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin-bottom: 24px;
    }}

    .pplx-title {{
      font-size: 40px;
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.02em;
      color: #F3F3EE;
      margin-bottom: 20px;
    }}

    .pplx-content {{
      font-size: 28px;
      line-height: 1.5;
      color: #C5C9D3;
    }}

    /* Math Formula Block */
    .pplx-formula-container {{
      background: #111418;
      border: 1px solid #23272F;
      border-radius: 12px;
      padding: 24px;
      margin: 20px 0;
      text-align: center;
      font-size: 38px;
    }}
    .pplx-formula-highlight {{
      color: {accent_color};
      border-bottom: 2px solid {accent_color};
      padding-bottom: 2px;
    }}

    /* Code Diff Container */
    .pplx-code-container {{
      background: #0D0E11;
      border: 1px solid #23272F;
      border-radius: 12px;
      padding: 24px;
      font-family: 'JetBrains Mono', 'Fira Code', monospace;
      font-size: 22px;
      line-height: 1.6;
      overflow-x: auto;
    }}
    .code-line {{ display: flex; }}
    .line-no {{ width: 45px; color: #646C7A; user-select: none; }}
    .line-add {{ background: rgba(16, 185, 129, 0.15); color: #10B981; }}
    .line-del {{ background: rgba(239, 68, 68, 0.15); color: #EF4444; }}

    /* Citation Badge */
    .pplx-citation {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      background: #1B1F26;
      border: 1px solid #23272F;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 18px;
      color: {accent_color};
      margin-left: 6px;
    }}

    /* Dynamic Subtitle Demo Bar (Safe baseline: Y = 1540px) */
    .pplx-subtitle-bar {{
      position: absolute;
      top: 1540px;
      left: 50%;
      transform: translateX(-50%);
      width: 820px;
      text-align: center;
      font-size: 42px;
      font-weight: 700;
      line-height: 1.3;
      color: #8E95A2;
    }}
    .pplx-subtitle-bar .active {{
      color: #F3F3EE;
      background: rgba(32, 184, 205, 0.22);
      border-radius: 8px;
      padding: 2px 10px;
    }}
  </style>
</head>
<body>
  <div class="safe-zone"></div>

  <div class="pplx-card">
    <div class="pplx-header-pill">
      <span>{pill_text}</span>
    </div>
    <div class="pplx-title">{title}</div>
    <div class="pplx-content">
      {body_html}
    </div>
  </div>

  <div class="pplx-subtitle-bar">
    <span>EACH TOKEN REQUIRES</span> <span class="active">READING SRAM</span> <span>BANDWIDTH</span>
  </div>

  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      if (window.renderMathInElement) {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ]
        }});
      }}
    }});
  </script>
</body>
</html>
"""

def render_html_card(tmpl_id, title, pill_text, body_html, out_path, accent_color="#20B8CD", card_top=480):
    html = HTML_TEMPLATE.format(
        title=title,
        pill_text=pill_text,
        body_html=body_html,
        canvas_bg="#111418",
        card_bg="#16191E",
        card_top=card_top,
        accent_color=accent_color,
        animation_delay=120
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[HYPERFRAMES RENDERED] HTML Card ({tmpl_id}) -> {out_path}")
    return out_path

def render_svg_card(title, pill_text, formula_or_code, out_path, accent_color="#20B8CD"):
    """Renders a standalone 1080x1920 SVG graphic matching Perplexity styling."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
  <defs>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="12" stdDeviation="20" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="1080" height="1920" fill="#111418"/>

  <!-- Perplexity Main Card Container -->
  <g filter="url(#card-shadow)">
    <rect x="80" y="480" width="920" height="620" rx="16" fill="#16191E" stroke="#23272F" stroke-width="1.5"/>
  </g>

  <!-- Header Pill Badge -->
  <rect x="120" y="525" width="280" height="38" rx="19" fill="#20B8CD" fill-opacity="0.12" stroke="#20B8CD" stroke-width="1" stroke-opacity="0.3"/>
  <text x="140" y="550" fill="{accent_color}" font-family="'Inter', sans-serif" font-size="18" font-weight="600" letter-spacing="1">{pill_text.upper()}</text>

  <!-- Title -->
  <text x="120" y="615" fill="#F3F3EE" font-family="'Inter', sans-serif" font-size="38" font-weight="700" letter-spacing="-0.5">{title}</text>

  <!-- Inner Display Container -->
  <rect x="120" y="655" width="840" height="380" rx="12" fill="#111418" stroke="#23272F" stroke-width="1"/>

  <!-- Content Representation -->
  <text x="150" y="740" fill="#20B8CD" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="600">{formula_or_code[:45]}</text>
  <text x="150" y="795" fill="#C5C9D3" font-family="'Inter', sans-serif" font-size="24">Optimized on-chip memory tiling cuts global memory IO by 5x.</text>

  <!-- Citation Pill Badge [1] -->
  <g transform="translate(150, 840)">
    <rect width="220" height="36" rx="18" fill="#1B1F26" stroke="#23272F" stroke-width="1"/>
    <text x="20" y="24" fill="#9DA3AE" font-family="'Inter', sans-serif" font-size="17">arXiv:2307.08691 <tspan fill="{accent_color}" font-weight="700">[1]</tspan></text>
  </g>

  <!-- Subtitle Bar in Safe Zone -->
  <text x="540" y="1540" text-anchor="middle" font-family="'Inter', sans-serif" font-size="42" font-weight="700" fill="#8E95A2">
    EACH TOKEN REQUIRES <tspan fill="#F3F3EE">READING SRAM</tspan> BANDWIDTH
  </text>
</svg>"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[HYPERFRAMES RENDERED] SVG Card -> {out_path}")
    return out_path

def main():
    parser = argparse.ArgumentParser(description="Render Hyperframes Perplexity motion card")
    parser.add_argument("--template", default="TMPL-11", help="Template ID")
    parser.add_argument("--title", default="FlashAttention: SRAM Tiling", help="Card Title")
    parser.add_argument("--pill", default="Deep Learning // Optimization", help="Pill category")
    parser.add_argument("--body", default="$$Attention(Q,K,V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V$$", help="Body text or LaTeX")
    parser.add_argument("--out", default="rendered_card.html", help="Output path (.html or .svg)")
    parser.add_argument("--format", choices=["html", "svg"], default="html")
    args = parser.parse_args()

    if args.format == "svg" or args.out.endswith(".svg"):
        render_svg_card(args.title, args.pill, args.body, args.out)
    else:
        render_html_card(args.template, args.title, args.pill, f"<div class='pplx-formula-container'>{args.body}</div>", args.out)

if __name__ == "__main__":
    main()
