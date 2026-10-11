#!/usr/bin/env python3
"""
actions.py - OpenClaw Action Space Handlers for Video-Director
Binds OpenClaw action requests to the Video Director tool engine.
Zero external dependencies.
"""

import os
import sys
import json

TOOLS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
sys.path.insert(0, TOOLS_DIR)

from symphony_client import SymphonyClient
from hyperframes_renderer import render_html_card, render_svg_card
from clipchat_compiler import compile_ffmpeg_command

def interrogate_action(params):
    topic = params.get("topic", "STEM Topic")
    return {
        "status": "success",
        "action": "interrogate",
        "hook_angle": f"The counter-intuitive bottleneck in {topic} (Recommended)",
        "visual_balance": "45% Symphony 9:16 B-roll + 55% Hyperframes Motion Cards",
        "duration": "58-second high-velocity Short/Reel"
    }

def generate_symphony_shot_action(params):
    client = SymphonyClient()
    scene = params.get("scene", "Cleanroom robotics")
    focal = params.get("focal", "35mm")
    prompt = client.build_picture_prompt(scene, focal)
    return client.generate_shot(prompt, dry_run=True)

def render_motion_card_action(params):
    tmpl_id = params.get("template_id", "TMPL-11")
    content = params.get("content", "\\nabla \\times B = \\mu_0 J")
    out_file = os.path.join(os.getcwd(), f"openclaw_{tmpl_id}.svg")
    render_svg_card("OpenClaw Render", "Physics // Field", content, out_file)
    return {"status": "success", "file": out_file}

def compile_timeline_action(params):
    timeline_path = params.get("timeline_json")
    if not os.path.isfile(timeline_path):
        return {"status": "error", "message": f"Timeline file not found: {timeline_path}"}
    with open(timeline_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    cmd = compile_ffmpeg_command(data)
    return {"status": "success", "ffmpeg_command": cmd}

ACTION_MAP = {
    "interrogate": interrogate_action,
    "generate_symphony_shot": generate_symphony_shot_action,
    "render_motion_card": render_motion_card_action,
    "compile_timeline": compile_timeline_action
}

def main():
    if len(sys.argv) < 2:
        print("[OPENCLAW] Available actions:", list(ACTION_MAP.keys()))
        sys.exit(0)

    raw_params = sys.argv[2] if len(sys.argv) > 2 else "{}"
    try:
        params = json.loads(raw_params)
    except Exception:
        try:
            import ast
            params = ast.literal_eval(raw_params)
        except Exception:
            params = {"topic": raw_params}
    handler = ACTION_MAP.get(action_name)
    if not handler:
        print(json.dumps({"status": "error", "message": f"Unknown action: {action_name}"}))
        sys.exit(1)

    result = handler(params)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
