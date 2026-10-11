#!/usr/bin/env python3
"""
make_lut.py - Generate valid Adobe .cube 3D LUTs for Perplexity-grade video color grading.
Zero dependencies. Pure Python 3.

Presets included:
  - perplexity-dark-slate (Default: deep matte slate blacks, subtle cyan specular highlights)
  - perplexity-light-parchment (Warm academic ivory for paper reviews)
  - quantum-lab (Cold 5200K lab tint with electric cyan rim separation)
  - silicon-cleanroom (High-contrast cleanroom lighting with controlled amber/cyan tones)
  - theoretical-blackboard (High-contrast matte slate for chalkboard & mathematical proofs)

Usage:
  python scripts/make_lut.py --preset perplexity-dark-slate --out references/PerplexityDarkSlate.cube
"""

import argparse
import sys

REC709 = (0.2126, 0.7152, 0.0722)

PRESETS = {
    "identity": {},
    "perplexity-dark-slate": dict(
        contrast=1.14,
        saturation=0.88,
        temp=-0.04,
        lift=(0.015, 0.018, 0.022),
        shadow_tint=(-0.01, 0.00, 0.03),
        highlight_tint=(0.02, 0.04, 0.05),
        gain=(0.98, 1.00, 1.02)
    ),
    "perplexity-light-parchment": dict(
        contrast=1.06,
        saturation=0.82,
        temp=0.06,
        lift=(0.025, 0.024, 0.020),
        shadow_tint=(0.02, 0.01, -0.01),
        highlight_tint=(0.04, 0.03, -0.02)
    ),
    "quantum-lab": dict(
        contrast=1.18,
        saturation=0.80,
        temp=-0.08,
        lift=(0.010, 0.014, 0.024),
        shadow_tint=(-0.02, 0.01, 0.06),
        highlight_tint=(0.01, 0.05, 0.07)
    ),
    "silicon-cleanroom": dict(
        contrast=1.20,
        saturation=0.92,
        temp=0.03,
        lift=(0.012, 0.012, 0.014),
        shadow_tint=(0.01, 0.00, 0.02),
        highlight_tint=(0.05, 0.03, -0.02)
    ),
    "theoretical-blackboard": dict(
        contrast=1.24,
        saturation=0.72,
        temp=-0.02,
        lift=(0.008, 0.010, 0.014),
        shadow_tint=(-0.01, 0.00, 0.02),
        highlight_tint=(0.02, 0.02, 0.02)
    )
}

def clamp(x, lo=0.0, hi=1.0):
    return lo if x < lo else hi if x > hi else x

def build_transform(a):
    lift, gamma, gain = a.lift, a.gamma, a.gain
    sh, hl = a.shadow_tint, a.highlight_tint
    temp, tint = a.temp, a.tint
    contrast, pivot, sat = a.contrast, a.pivot, a.saturation

    def transform(r, g, b):
        c = [r, g, b]

        # White balance (temp: amber/blue, tint: green/magenta)
        c[0] += temp * 0.5
        c[2] -= temp * 0.5
        c[1] += tint * 0.5
        c = [clamp(v) for v in c]

        # Contrast around pivot
        c = [clamp(pivot + (v - pivot) * contrast) for v in c]

        # Lift / Gamma / Gain
        for i in range(3):
            # Lift
            c[i] = c[i] * (1.0 - lift[i]) + lift[i]
            # Gain
            c[i] = c[i] * gain[i]
            # Gamma
            if c[i] > 0.0 and gamma[i] != 1.0:
                c[i] = c[i] ** (1.0 / gamma[i])
            c[i] = clamp(c[i])

        # Luminance for split toning
        lum = REC709[0] * c[0] + REC709[1] * c[1] + REC709[2] * c[2]

        # Shadow tint (falls off as lum -> 1)
        sh_weight = (1.0 - lum) ** 2
        for i in range(3):
            c[i] = clamp(c[i] + sh[i] * sh_weight)

        # Highlight tint (falls off as lum -> 0)
        hl_weight = lum ** 2
        for i in range(3):
            c[i] = clamp(c[i] + hl[i] * hl_weight)

        # Saturation
        lum = REC709[0] * c[0] + REC709[1] * c[1] + REC709[2] * c[2]
        c = [clamp(lum + (v - lum) * sat) for v in c]

        return c

    return transform

def parse_args():
    p = argparse.ArgumentParser(description="Generate .cube 3D LUT for Perplexity video color grading.")
    p.add_argument("--preset", choices=list(PRESETS.keys()), default="perplexity-dark-slate",
                   help="Starting preset (default: perplexity-dark-slate)")
    p.add_argument("--size", type=int, default=33,
                   help="LUT cube dimension N (default 33 -> 35,937 points)")
    p.add_argument("--out", required=True, help="Output .cube file path")
    p.add_argument("--title", default="", help="TITLE line in .cube header")
    p.add_argument("--identity", action="store_true", help="Generate identity LUT (no-op)")
    return p.parse_args()

def main():
    args = parse_args()
    title = args.title or args.preset or "Perplexity LUT"

    # Assemble parameters from preset
    params = argparse.Namespace(
        contrast=1.0, pivot=0.435, saturation=1.0, temp=0.0, tint=0.0,
        lift=(0.0, 0.0, 0.0), gamma=(1.0, 1.0, 1.0), gain=(1.0, 1.0, 1.0),
        shadow_tint=(0.0, 0.0, 0.0), highlight_tint=(0.0, 0.0, 0.0)
    )

    if not args.identity:
        preset_vals = PRESETS.get(args.preset, {})
        for k, v in preset_vals.items():
            setattr(params, k, v)

    tf = build_transform(params)
    n = args.size

    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(f'TITLE "{title}"\n')
        f.write("LUT_3D_SIZE {}\n".format(n))
        f.write("DOMAIN_MIN 0.0 0.0 0.0\n")
        f.write("DOMAIN_MAX 1.0 1.0 1.0\n\n")

        # In Adobe .cube, RED changes fastest, GREEN middle, BLUE slowest
        denom = float(n - 1)
        for b_idx in range(n):
            b_in = b_idx / denom
            for g_idx in range(n):
                g_in = g_idx / denom
                for r_idx in range(n):
                    r_in = r_idx / denom
                    r_out, g_out, b_out = tf(r_in, g_in, b_in)
                    f.write(f"{r_out:.6f} {g_out:.6f} {b_out:.6f}\n")

    print(f"Successfully generated 3D LUT ({n}x{n}x{n}) -> {args.out}")

if __name__ == "__main__":
    main()
