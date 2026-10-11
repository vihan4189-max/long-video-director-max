#!/usr/bin/env python3
"""
prompt_auditor.py - AI Video Director Prompt Quality Auditor
Scans Symphony prompts, Hyperframes specs, voiceover scripts, and Clipchat timelines
for professional-grade compliance violations. Catches the top-20 amateur mistakes
before they burn generation credits or produce unusable footage.
Zero external dependencies.
"""

import os
import sys
import json
import re
import argparse


class AuditResult:
    def __init__(self):
        self.errors = []     # Hard failures (will produce garbage)
        self.warnings = []   # Soft issues (will look amateur)
        self.passes = []     # Confirmed good practices

    def error(self, rule_id, msg):
        self.errors.append(f"[{rule_id}] {msg}")

    def warn(self, rule_id, msg):
        self.warnings.append(f"[{rule_id}] {msg}")

    def ok(self, rule_id, msg):
        self.passes.append(f"[{rule_id}] {msg}")

    def summary(self):
        total = len(self.errors) + len(self.warnings) + len(self.passes)
        lines = [f"\n{'='*60}", f"PROMPT AUDIT REPORT: {total} checks"]
        lines.append(f"  PASSED:   {len(self.passes)}")
        lines.append(f"  WARNINGS: {len(self.warnings)}")
        lines.append(f"  ERRORS:   {len(self.errors)}")
        lines.append('='*60)
        if self.errors:
            lines.append("\n--- ERRORS (will produce garbage) ---")
            for e in self.errors:
                lines.append(f"  [X] {e}")
        if self.warnings:
            lines.append("\n--- WARNINGS (will look amateur) ---")
            for w in self.warnings:
                lines.append(f"  [!] {w}")
        if self.passes:
            lines.append("\n--- PASSED ---")
            for p in self.passes[:8]:
                lines.append(f"  [OK] {p}")
            if len(self.passes) > 8:
                lines.append(f"  ... and {len(self.passes)-8} more checks passed.")
        return "\n".join(lines)


def audit_symphony_prompt(text, result):
    """Audits a Symphony (video/image generation) prompt."""
    # RULE S01: Must specify vertical 9:16
    if re.search(r'9:16|vertical|portrait|1080.*1920', text, re.I):
        result.ok('S01', 'Vertical 9:16 aspect ratio specified')
    else:
        result.error('S01', 'Missing vertical 9:16 specification. Symphony generates ONLY vertical.')

    # RULE S02: Must not request text/math/code rendering
    if re.search(r'\b(write|render|show|display|print)\s+(text|equation|formula|code|math|number|subtitle)', text, re.I):
        result.error('S02', 'Symphony cannot render legible text/math/code. Route to Hyperframes.')
    else:
        result.ok('S02', 'No text-rendering requests detected')

    # RULE S03: Must not request 16:9 / horizontal
    if re.search(r'16:9|horizontal|widescreen|landscape|panoramic', text, re.I):
        result.error('S03', 'Horizontal aspect ratio requested. Symphony is STRICTLY vertical 9:16.')
    else:
        result.ok('S03', 'No horizontal aspect ratio violations')

    # RULE S04: Should specify camera position physically
    if re.search(r'camera.*(low|high|chest|shoulder|overhead|eye.?level)', text, re.I):
        result.ok('S04', 'Camera position specified in physical terms')
    else:
        result.warn('S04', 'No physical camera position stated. Model defaults to flat frontal view.')

    # RULE S05: Should have exactly one camera movement
    moves = re.findall(r'(push|pull|dolly|track|pedestal|orbit|lateral|pan|tilt|zoom|locked)', text, re.I)
    if len(moves) == 0:
        result.warn('S05', 'No camera movement specified. Consider adding one for cinematic depth.')
    elif len(moves) == 1:
        result.ok('S05', f'Single camera movement detected: {moves[0]}')
    elif len(moves) >= 3:
        result.error('S05', f'Multiple camera movements detected ({len(moves)}): {", ".join(moves)}. Use exactly ONE per clip.')
    else:
        result.warn('S05', f'{len(moves)} movement terms detected ({moves}). Prefer exactly one.')

    # RULE S06: Should not use negative steering
    negatives = re.findall(r'\b(not\s+\w+ing|do\s+not|don\'t|no\s+\w+ing|without\s+\w+ing)', text, re.I)
    if negatives:
        result.warn('S06', f'Negative steering detected: {", ".join(negatives[:3])}. Diffusion models handle prohibitions badly. Rephrase positively.')
    else:
        result.ok('S06', 'No negative steering phrases detected')

    # RULE S07: Should specify lighting temperature
    if re.search(r'\d{4}K|cold|warm|daylight|tungsten|cyan.*light|rim.*light', text, re.I):
        result.ok('S07', 'Lighting specification found')
    else:
        result.warn('S07', 'No explicit lighting specification. Model will default to flat generic lighting.')

    # RULE S08: Should have the PICTURE format markers
    picture_blocks = re.findall(r'\[([PICTURE])\]', text)
    if len(picture_blocks) >= 4:
        result.ok('S08', f'PICTURE-916 formula markers detected ({len(picture_blocks)}/7 blocks)')
    else:
        result.warn('S08', 'Missing PICTURE-916 formula structure. Use [P], [I], [C], [T], [U], [R], [E] blocks.')


def audit_hyperframes_spec(text, result):
    """Audits a Hyperframes motion graphics specification."""
    # RULE H01: Must reference Perplexity design tokens
    if re.search(r'#111418|#16191E|#20B8CD|#23272F', text, re.I):
        result.ok('H01', 'Perplexity color tokens detected')
    else:
        result.warn('H01', 'No Perplexity color tokens found. Use #111418 (canvas), #16191E (card), #20B8CD (accent).')

    # RULE H02: Must use correct animation curve
    if re.search(r'cubic-bezier\(0\.16.*1.*0\.3.*1\)', text, re.I):
        result.ok('H02', 'Perplexity spring easing curve detected')
    else:
        result.warn('H02', 'Missing cubic-bezier(0.16, 1, 0.3, 1) spring physics curve.')

    # RULE H03: Canvas must be 1080x1920
    if '1080' in text and '1920' in text:
        result.ok('H03', 'Canvas dimensions 1080x1920 confirmed')
    else:
        result.warn('H03', 'Canvas dimensions not explicitly 1080x1920.')

    # RULE H04: Safe zone bounds
    if re.search(r'240|1450|1540', text):
        result.ok('H04', 'Safe zone coordinates referenced')
    else:
        result.warn('H04', 'No safe zone coordinates found. Top: Y>=240, Bottom: Y<=1450, Subtitles: Y=1540.')


def audit_voiceover_script(text, result):
    """Audits a voiceover script for professional quality."""
    words = text.split()
    wc = len(words)

    # RULE V01: Word count vs 60s target
    if 120 <= wc <= 180:
        result.ok('V01', f'Word count ({wc}) is within optimal 60s range (120-180)')
    elif wc < 120:
        result.warn('V01', f'Word count ({wc}) is low for a 60s video. Target 140-160 words.')
    elif wc > 200:
        result.warn('V01', f'Word count ({wc}) is high. May feel rushed at 150+ WPM.')

    # RULE V02: Has pause markers
    if re.search(r'\.\.\.|—|\[PAUSE|\[SILENCE|\[NEEDLE', text):
        result.ok('V02', 'Pause/silence markers found for natural pacing')
    else:
        result.warn('V02', 'No pause markers (..., em-dash, [NEEDLE DROP]). Script may sound monotonous.')

    # RULE V03: YouTube/TikTok hype banned
    if re.search(r'WHAT\'S UP|HEY GUYS|SMASH.*LIKE|SUBSCRIBE|INSANE|MIND.?BLOWN|CRAZY', text, re.I):
        result.error('V03', 'Generic YouTuber hype language detected. Use calm, intellectual delivery.')
    else:
        result.ok('V03', 'No amateur hype language detected')

    # RULE V04: Math symbols should be phonetically spelled
    if re.search(r'\\(sqrt|frac|hbar|nabla|psi|lambda)', text):
        result.warn('V04', 'Raw LaTeX symbols in voiceover script. Spell out phonetically (e.g. \\sqrt -> "square root of").')
    else:
        result.ok('V04', 'No raw LaTeX in voiceover script')


def audit_timeline_json(data, result):
    """Audits a Clipchat timeline JSON for professional editing standards."""
    tracks = data.get('tracks', {})

    # RULE T01: Resolution check
    res = data.get('resolution', {})
    if res.get('width') == 1080 and res.get('height') == 1920:
        result.ok('T01', 'Resolution is 1080x1920 (9:16)')
    else:
        result.error('T01', f'Resolution is not 1080x1920. Got: {res}')

    # RULE T02: Has voiceover track
    if 'a1_voiceover' in tracks or 'a1_voice' in tracks:
        result.ok('T02', 'Voiceover audio track present')
    else:
        result.error('T02', 'Missing voiceover track (a1_voiceover). No-face videos require voice.')

    # RULE T03: Symphony clips should have trim
    v1 = tracks.get('v1_symphony', [])
    for i, clip in enumerate(v1):
        in_pt = clip.get('in', 0)
        if in_pt < 0.3:
            result.warn('T03', f'Symphony clip {i+1} starts at {in_pt}s. Trim first 0.5s to remove AI edge artifacts.')
        else:
            result.ok('T03', f'Symphony clip {i+1} trimmed correctly (in={in_pt}s)')

    # RULE T04: Has subtitle track
    if 'v3_subtitles' in tracks:
        result.ok('T04', 'Subtitle track (v3) present')
    else:
        result.warn('T04', 'No subtitle track (v3_subtitles). No-face videos need dynamic subtitles.')


def main():
    parser = argparse.ArgumentParser(description='Video Director Prompt Quality Auditor')
    parser.add_argument('--symphony', help='Symphony prompt text or file path')
    parser.add_argument('--hyperframes', help='Hyperframes spec text or file path')
    parser.add_argument('--voiceover', help='Voiceover script text or file path')
    parser.add_argument('--timeline', help='Clipchat timeline JSON file path')
    parser.add_argument('--all-in', help='Audit a complete project directory')
    args = parser.parse_args()

    result = AuditResult()

    def read_input(val):
        if val and os.path.isfile(val):
            with open(val, 'r', encoding='utf-8') as f:
                return f.read()
        return val or ''

    if args.symphony:
        print('[AUDITING] Symphony Prompt...')
        audit_symphony_prompt(read_input(args.symphony), result)

    if args.hyperframes:
        print('[AUDITING] Hyperframes Specification...')
        audit_hyperframes_spec(read_input(args.hyperframes), result)

    if args.voiceover:
        print('[AUDITING] Voiceover Script...')
        audit_voiceover_script(read_input(args.voiceover), result)

    if args.timeline:
        print('[AUDITING] Clipchat Timeline...')
        with open(args.timeline, 'r', encoding='utf-8') as f:
            data = json.load(f)
        audit_timeline_json(data, result)

    if args.all_in and os.path.isdir(args.all_in):
        print(f'[AUDITING] Full project directory: {args.all_in}')
        for fn in os.listdir(args.all_in):
            fp = os.path.join(args.all_in, fn)
            if fn.endswith('_prompts.txt') or 'symphony' in fn.lower():
                with open(fp, 'r', encoding='utf-8') as f:
                    audit_symphony_prompt(f.read(), result)
            elif fn.endswith('.json') and 'timeline' in fn.lower():
                with open(fp, 'r', encoding='utf-8') as f:
                    audit_timeline_json(json.load(f), result)

    if not any([args.symphony, args.hyperframes, args.voiceover, args.timeline, args.all_in]):
        # Demo audit
        print('[AUDITING] Running demo audit on sample prompts...')
        audit_symphony_prompt(
            '[P] 35mm cine-lens, 9:16 vertical. [I] Cleanroom robotics. [C] Camera low at chest height. '
            '[T] 5400K cold slate with cyan rim light. [E] Slow push forward over 4 seconds.',
            result
        )
        audit_voiceover_script(
            'Most engineers think attention is compute-bound. It\'s not... — it\'s memory-bandwidth bound. '
            '[NEEDLE DROP] FlashAttention changes the math entirely. Instead of materializing the full attention matrix, '
            'it tiles the computation into ultra-fast on-chip SRAM blocks.',
            result
        )

    print(result.summary())
    sys.exit(1 if result.errors else 0)


if __name__ == '__main__':
    main()
