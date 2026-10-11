#!/usr/bin/env python3
"""
hermes_agent.py - Nous Hermes Local Tool Calling Execution Harness
Parses <tool_call> tags from Hermes completions and executes Video Director tools locally.
Zero external dependencies.
"""

import os
import sys
import json
import re

TOOLS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
sys.path.insert(0, TOOLS_DIR)

from symphony_client import SymphonyClient
from hyperframes_renderer import render_html_card, render_svg_card

def execute_hermes_tool_call(tool_name, arguments):
    """Dispatches a Hermes tool call to local Python video tools."""
    print(f"[HERMES DISPATCH] Executing: {tool_name}({arguments})")
    
    if tool_name == "video_director_interrogate":
        topic = arguments.get("topic", "STEM Topic")
        return {
            "status": "success",
            "hook_recommendation": f"Why standard implementations of {topic} fail under load...",
            "visual_balance": "45% Symphony vertical B-roll + 55% Hyperframes motion cards",
            "duration": "58-second high-velocity Short/Reel"
        }
    elif tool_name == "symphony_generate_shot":
        client = SymphonyClient()
        scene = arguments.get("scene_description", "Lab scene")
        focal = arguments.get("focal_length", "35mm")
        prompt = client.build_picture_prompt(scene, focal)
        return client.generate_shot(prompt, dry_run=True)
    elif tool_name == "hyperframes_render_card":
        tmpl = arguments.get("template_id", "TMPL-11")
        content = arguments.get("content", "E = mc^2")
        out_path = os.path.join(os.getcwd(), f"hermes_render_{tmpl}.html")
        render_html_card(tmpl, "Hermes Render", "Physics // Formula", content, out_path)
        return {"status": "success", "file": out_path}
    else:
        return {"status": "error", "message": f"Unknown tool: {tool_name}"}

def parse_and_run_hermes_output(model_output_text):
    """Extracts <tool_call> blocks from model output and runs them."""
    matches = re.findall(r"<tool_call>\s*(.*?)\s*</tool_call>", model_output_text, re.DOTALL)
    results = []
    for m in matches:
        try:
            call_obj = json.loads(m)
            name = call_obj.get("name")
            args = call_obj.get("arguments", {})
            res = execute_hermes_tool_call(name, args)
            results.append({"tool": name, "result": res})
        except Exception as e:
            results.append({"error": str(e)})
    return results

def main():
    sample_hermes_output = """
I will now generate the introductory hook for the FlashAttention video.
<tool_call>
{"name": "video_director_interrogate", "arguments": {"topic": "FlashAttention GPU Tiling"}}
</tool_call>
"""
    print("[HERMES ADAPTER] Running mock parsing test...")
    res = parse_and_run_hermes_output(sample_hermes_output)
    print(json.dumps(res, indent=2))
    print("[HERMES ADAPTER] Ready for local inference engine connection.")

if __name__ == "__main__":
    main()
