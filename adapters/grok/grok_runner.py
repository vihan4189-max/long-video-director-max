#!/usr/bin/env python3
"""
grok_runner.py - xAI Grok Function Calling Execution Harness for Video-Director
Bridges Grok's native function-calling JSON responses to the local tool engine.
Zero external dependencies.
"""

import os
import sys
import json

TOOLS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
sys.path.insert(0, TOOLS_DIR)

from symphony_client import SymphonyClient
from hyperframes_renderer import render_html_card, render_svg_card

GROK_TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "video_director_interrogate",
            "description": "Analyzes a STEM topic and returns the Rule of Three Clarifications.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "Scientific or technical topic"}
                },
                "required": ["topic"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "symphony_generate_shot",
            "description": "Generates a validated Symphony strictly vertical (9:16) B-roll prompt.",
            "parameters": {
                "type": "object",
                "properties": {
                    "scene_description": {"type": "string"},
                    "focal_length": {"type": "string", "default": "35mm"},
                    "camera_movement": {"type": "string", "default": "slow push forward"}
                },
                "required": ["scene_description"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "hyperframes_render_card",
            "description": "Renders a Perplexity motion graphic card (LaTeX, code diff, UI).",
            "parameters": {
                "type": "object",
                "properties": {
                    "template_id": {"type": "string"},
                    "title": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["template_id", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "clipchat_assemble_timeline",
            "description": "Compiles multi-track video timeline into FFmpeg script and EDL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_title": {"type": "string"},
                    "voiceover_file": {"type": "string"}
                },
                "required": ["project_title", "voiceover_file"]
            }
        }
    }
]


def execute_grok_function_call(name, arguments):
    """Dispatches a Grok function call to the local Video-Director tool chain."""
    if name == "video_director_interrogate":
        topic = arguments.get("topic", "STEM Topic")
        return {
            "status": "success",
            "rule_of_three": [
                {"question": "Hook Angle", "recommendation": f"Counter-intuitive bottleneck in {topic}"},
                {"question": "Visual Balance", "recommendation": "45% Symphony 9:16 B-roll + 55% Hyperframes"},
                {"question": "Duration", "recommendation": "58s High-Velocity Short (148 words)"}
            ]
        }
    elif name == "symphony_generate_shot":
        client = SymphonyClient()
        scene = arguments.get("scene_description", "Lab hardware")
        focal = arguments.get("focal_length", "35mm")
        move = arguments.get("camera_movement", "slow push forward")
        prompt = client.build_picture_prompt(scene, focal, move)
        return client.generate_shot(prompt, dry_run=True)
    elif name == "hyperframes_render_card":
        tmpl = arguments.get("template_id", "TMPL-11")
        title = arguments.get("title", "Grok Render")
        content = arguments.get("content", "")
        out_path = os.path.join(os.getcwd(), f"grok_render_{tmpl}.svg")
        render_svg_card(title, "Physics // Derivation", content, out_path)
        return {"status": "success", "file": out_path}
    elif name == "clipchat_assemble_timeline":
        return {
            "status": "success",
            "project": arguments.get("project_title", "Project"),
            "resolution": "1080x1920 (9:16) @ 60fps",
            "note": "FFmpeg command would be compiled from timeline JSON"
        }
    else:
        return {"status": "error", "message": f"Unknown function: {name}"}


def process_grok_response(response_json):
    """Processes a Grok API response containing tool_calls and executes them."""
    tool_calls = response_json.get("choices", [{}])[0].get("message", {}).get("tool_calls", [])
    results = []
    for tc in tool_calls:
        fn = tc.get("function", {})
        name = fn.get("name", "")
        try:
            args = json.loads(fn.get("arguments", "{}"))
        except Exception:
            args = {}
        result = execute_grok_function_call(name, args)
        results.append({"tool_call_id": tc.get("id", ""), "name": name, "result": result})
    return results


def main():
    # Demo: simulate a Grok function call
    print("[GROK ADAPTER] Testing function call dispatch...")
    result = execute_grok_function_call("video_director_interrogate", {"topic": "Quantum Entanglement & Bell Inequality"})
    print(json.dumps(result, indent=2))

    result2 = execute_grok_function_call("symphony_generate_shot", {"scene_description": "Optical photon entanglement apparatus on lab bench"})
    print(json.dumps(result2, indent=2))

    print("\n[GROK ADAPTER] Tools schema for xAI API registration:")
    print(json.dumps(GROK_TOOLS_SCHEMA[:1], indent=2)[:200] + "...")
    print(f"\n[GROK ADAPTER] Total registered tools: {len(GROK_TOOLS_SCHEMA)}")


if __name__ == "__main__":
    main()
