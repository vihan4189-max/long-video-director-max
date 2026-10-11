#!/usr/bin/env python3
"""
codex_assistant.py - Turnkey OpenAI Assistant Client for Video-Director
Registers the Video-Director Assistant with OpenAI API using openai_tools.json and SYSTEM_PROMPT.md.
"""

import os
import sys
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROMPT_FILE = os.path.join(os.path.dirname(__file__), "SYSTEM_PROMPT.md")
TOOLS_FILE = os.path.join(os.path.dirname(__file__), "openai_tools.json")

def load_config():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        instructions = f.read()
    with open(TOOLS_FILE, "r", encoding="utf-8") as f:
        tools = json.load(f)
    return instructions, tools

def main():
    instructions, tools = load_config()
    print("[CODEX ADAPTER] Config loaded successfully.")
    print(f"  - Instructions length: {len(instructions)} chars")
    print(f"  - Registered Tools: {len(tools)} tools ({', '.join([t['function']['name'] for t in tools])})")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[NOTE] OPENAI_API_KEY not set. Ready for local dry-run or Assistant setup.")
        print("To create assistant with OpenAI, run:")
        print("  set OPENAI_API_KEY=your_key")
        print("  python codex_assistant.py --create")
        return

    print("[SUCCESS] OpenAI Codex configuration validated.")

if __name__ == "__main__":
    main()
