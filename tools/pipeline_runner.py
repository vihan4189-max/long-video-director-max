#!/usr/bin/env python3
"""
pipeline_runner.py - End-to-End Video Director Pipeline Orchestrator
Runs the complete 7-stage production pipeline from topic to final render script.
Orchestrates: Symphony Client -> Hyperframes Renderer -> Voiceover Synthesizer ->
Subtitle Generator -> Clipchat Compiler -> Prompt Auditor
Zero external dependencies.
"""

import os
import sys
import json
import argparse
import shutil

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
sys.path.insert(0, TOOLS_DIR)

from symphony_client import SymphonyClient
from hyperframes_renderer import render_html_card, render_svg_card
from voiceover_synthesizer import calculate_word_timestamps, generate_mock_voiceover_wav
from subtitle_generator import compile_dynamic_ass, compile_srt
from clipchat_compiler import compile_ffmpeg_command, generate_cmx_edl, generate_html_timeline_visualizer
from prompt_auditor import AuditResult, audit_symphony_prompt, audit_voiceover_script


def run_pipeline(topic, domain='ai-machine-learning', duration_target=58, output_dir=None):
    slug = topic.lower().replace(' ', '_')[:30]
    if not output_dir:
        output_dir = os.path.join(BASE_DIR, 'projects', slug)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'assets', 'symphony_shots'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'assets', 'hyperframes_renders'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'audio'), exist_ok=True)

    print(f'\n{"="*60}')
    print(f'VIDEO DIRECTOR PIPELINE: {topic}')
    print(f'{"="*60}')

    # -- STAGE 1: Interrogation --
    print('\n-- STAGE 1: INTERROGATION --')
    interrogation = {
        'topic': topic,
        'domain': domain,
        'hook_angle': f'Counter-intuitive bottleneck in {topic}',
        'visual_balance': '45% Symphony 9:16 B-roll + 55% Hyperframes Motion Cards',
        'duration': f'{duration_target} seconds',
    }
    with open(os.path.join(output_dir, 'interrogation.json'), 'w') as f:
        json.dump(interrogation, f, indent=2)
    print(f'  -> Interrogation saved')

    # -- STAGE 2: Director Plan --
    print('\n-- STAGE 2: DIRECTOR PLAN --')
    beats = [
        {'timecode': '0:00-0:05', 'beat': 'Hook', 'tool': 'Symphony+Hyperframes', 'template': 'TMPL-01'},
        {'timecode': '0:05-0:18', 'beat': 'Bottleneck', 'tool': 'Hyperframes', 'template': 'TMPL-24'},
        {'timecode': '0:18-0:32', 'beat': 'Math Mechanism', 'tool': 'Hyperframes', 'template': 'TMPL-11'},
        {'timecode': '0:32-0:42', 'beat': 'Code Reality', 'tool': 'Hyperframes', 'template': 'TMPL-23'},
        {'timecode': '0:42-0:50', 'beat': 'Revelation', 'tool': 'Symphony+Hyperframes', 'template': 'TMPL-26'},
        {'timecode': '0:50-0:58', 'beat': 'Outro', 'tool': 'Hyperframes', 'template': 'TMPL-10'},
    ]
    plan = {'topic': topic, 'duration': duration_target, 'beats': beats}
    with open(os.path.join(output_dir, 'director_plan.json'), 'w') as f:
        json.dump(plan, f, indent=2)
    print(f'  -> Director plan saved ({len(beats)} beats)')

    # -- STAGE 3: Symphony Prompts --
    print('\n-- STAGE 3: SYMPHONY VERTICAL (9:16) GENERATION --')
    client = SymphonyClient()
    symphony_scenes = [
        ('Hook establishing shot', '35mm', 'slow push forward'),
        ('Benchmark reveal macro', '100mm', 'locked-off'),
    ]
    for i, (scene, focal, move) in enumerate(symphony_scenes):
        prompt = client.build_picture_prompt(scene, focal, move)
        prompt_path = os.path.join(output_dir, 'assets', 'symphony_shots', f'shot_{i+1}_prompt.txt')
        with open(prompt_path, 'w') as f:
            f.write(prompt)
        # Audit each prompt
        audit = AuditResult()
        audit_symphony_prompt(prompt, audit)
        print(f'  -> Shot {i+1}: {scene} ({len(audit.errors)} errors, {len(audit.warnings)} warnings)')

    # -- STAGE 4: Hyperframes Motion Graphics --
    print('\n-- STAGE 4: HYPERFRAMES MOTION GRAPHICS --')
    cards = [
        ('TMPL-01', 'Query Input', 'Deep Learning // Search', f'How does {topic} actually work?'),
        ('TMPL-11', 'Formula', 'Mathematics // Derivation', 'Attention(Q,K,V) = softmax(QK^T/sqrt(d_k))V'),
        ('TMPL-23', 'Code Diff', 'Systems // Optimization', 'for i in range(N): # O(N^2) -> O(N)'),
        ('TMPL-26', 'Benchmark', 'Evaluation // Metrics', '5.2x throughput improvement'),
    ]
    for tmpl_id, title, pill, content in cards:
        out_svg = os.path.join(output_dir, 'assets', 'hyperframes_renders', f'{tmpl_id}.svg')
        render_svg_card(title, pill, content, out_svg)
    print(f'  -> Rendered {len(cards)} motion graphics cards')

    # -- STAGE 5: Voiceover + Timestamps --
    print('\n-- STAGE 5: VOICEOVER & TIMESTAMPS --')
    script = (
        f'Most engineers think {topic} works the way tutorials explain it. '
        f'It does not... — the real bottleneck is completely different. '
        f'Under standard execution, performance collapses due to memory bandwidth limitations. '
        f'Here is the exact mathematical derivation that changes everything. '
        f'[NEEDLE DROP] The result? A five-x throughput gain with zero accuracy loss. '
        f'This is why {topic} powers modern computing. Follow for deeper breakdowns.'
    )
    timestamps, total_dur = calculate_word_timestamps(script, target_wpm=148)
    wav_path = os.path.join(output_dir, 'audio', 'voiceover_master.wav')
    ts_path = os.path.join(output_dir, 'audio', 'timestamps.json')
    generate_mock_voiceover_wav(wav_path, total_dur)
    with open(ts_path, 'w') as f:
        json.dump({'total_duration_seconds': total_dur, 'words': timestamps}, f, indent=2)
    print(f'  -> Voiceover: {total_dur}s, {len(timestamps)} words')

    # Audit voiceover
    audit_vo = AuditResult()
    audit_voiceover_script(script, audit_vo)
    print(f'  -> Voiceover audit: {len(audit_vo.errors)} errors, {len(audit_vo.warnings)} warnings')

    # -- STAGE 6: Subtitles --
    print('\n-- STAGE 6: DYNAMIC SUBTITLES --')
    ass_content = compile_dynamic_ass(timestamps, chunk_size=3)
    ass_path = os.path.join(output_dir, 'audio', 'subtitles.ass')
    with open(ass_path, 'w') as f:
        f.write(ass_content)
    srt_content = compile_srt(timestamps, chunk_size=4)
    srt_path = os.path.join(output_dir, 'audio', 'subtitles.srt')
    with open(srt_path, 'w') as f:
        f.write(srt_content)
    print(f'  -> .ass (cyan active-word) and .srt subtitles generated')

    # -- STAGE 7: Clipchat Timeline Assembly --
    print('\n-- STAGE 7: CLIPCHAT TIMELINE ASSEMBLY --')
    timeline = {
        'project': f'{topic}_Master',
        'resolution': {'width': 1080, 'height': 1920},
        'fps': 60,
        'color_grade_lut': 'references/PerplexityDarkSlate.cube',
        'tracks': {
            'v3_subtitles': {'baseline_y': 1540, 'font': 'Inter Bold', 'active_color': '#20B8CD'},
            'v2_hyperframes': [
                {'template': 'TMPL-01', 'in': 0.0, 'duration': 5.0},
                {'template': 'TMPL-24', 'in': 5.0, 'duration': 13.0},
                {'template': 'TMPL-11', 'in': 18.0, 'duration': 14.0},
                {'template': 'TMPL-23', 'in': 32.0, 'duration': 10.0},
                {'template': 'TMPL-26', 'in': 42.0, 'duration': 8.0},
                {'template': 'TMPL-10', 'in': 50.0, 'duration': 8.0},
            ],
            'v1_symphony': [
                {'shot': 'assets/symphony_shots/shot_1.mp4', 'in': 0.5, 'out': 4.5, 'timeline_start': 0.0},
                {'shot': 'assets/symphony_shots/shot_2.mp4', 'in': 0.5, 'out': 4.0, 'timeline_start': 42.0},
            ],
            'a1_voiceover': {'file': 'audio/voiceover_master.wav', 'gain_db': 0.0, 'needle_drop_at': 38.0},
            'a3_music': {'file': 'audio/ambient_score.wav', 'gain_db': -24.0, 'ducking_reduction_db': 10.0},
        }
    }
    timeline_path = os.path.join(output_dir, 'clipchat_timeline.json')
    with open(timeline_path, 'w') as f:
        json.dump(timeline, f, indent=2)

    ffmpeg_cmd = compile_ffmpeg_command(timeline)
    bat_path = os.path.join(output_dir, 'render.bat')
    with open(bat_path, 'w') as f:
        f.write('@echo off\nREM Video Director Auto-Generated Render Script\n' + ffmpeg_cmd + '\n')

    edl_text = generate_cmx_edl(timeline)
    edl_path = os.path.join(output_dir, 'timeline.edl')
    with open(edl_path, 'w') as f:
        f.write(edl_text)

    html_path = os.path.join(output_dir, 'timeline_preview.html')
    generate_html_timeline_visualizer(timeline, html_path)

    print(f'  -> Timeline JSON, FFmpeg script, CMX EDL, and HTML preview generated')

    # -- SUMMARY --
    print(f'\n{"="*60}')
    print(f'PIPELINE COMPLETE: {topic}')
    print(f'Output: {output_dir}')
    files = [f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))]
    for d in ['assets/symphony_shots', 'assets/hyperframes_renders', 'audio']:
        dp = os.path.join(output_dir, d)
        if os.path.isdir(dp):
            files += [os.path.join(d, f) for f in os.listdir(dp) if os.path.isfile(os.path.join(dp, f))]
    print(f'Total files generated: {len(files)}')
    print(f'{"="*60}')
    return output_dir


def main():
    parser = argparse.ArgumentParser(description='End-to-End Video Director Pipeline')
    parser.add_argument('--topic', default='FlashAttention-2 SRAM Tiling', help='Video topic')
    parser.add_argument('--domain', default='ai-machine-learning', help='Domain niche')
    parser.add_argument('--duration', type=int, default=58, help='Target duration in seconds')
    parser.add_argument('--out', default=None, help='Output directory')
    args = parser.parse_args()

    run_pipeline(args.topic, args.domain, args.duration, args.out)


if __name__ == '__main__':
    main()
