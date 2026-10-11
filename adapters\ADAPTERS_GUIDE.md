# Video Director: Multi-Harness Adapter Guide

This guide explains how to install and use the Video-Director skill across 6 different AI coding harnesses.

---

## Supported Harnesses

| Harness | Adapter Directory | Integration Method | Primary Config File |
|---|---|---|---|
| **Antigravity** | `adapters/antigravity/` | MCP Server (stdio JSON-RPC) + Direct Python tools | `SKILL.md` + `mcp_config.json` |
| **Claude Code** | `adapters/claude-code/` | MCP Server (stdio JSON-RPC) | `CLAUDE.md` + `tools.json` |
| **Codex (OpenAI)** | `adapters/codex/` | OpenAI Function Calling API | `openai_tools.json` + `SYSTEM_PROMPT.md` |
| **Hermes (Nous)** | `adapters/hermes/` | `<tool_call>` XML tag parsing | `hermes_prompt.md` + `hermes_agent.py` |
| **OpenClaw** | `adapters/openclaw/` | Action space plugin | `skill.json` + `actions.py` |
| **Grok (xAI)** | `adapters/grok/` | xAI Function Calling API | `grok_system.md` + `grok_runner.py` |

---

## Quick Start per Harness

### Antigravity
```bash
# Option 1: Register MCP server
agy mcp add video-director python c:/Users/user/Documents/VIDEO-EDIT-SKILL/tools/mcp_server.py

# Option 2: Copy skill to workspace
cp -r VIDEO-EDIT-SKILL/ your-project/.gemini/skills/video-director/
```

### Claude Code
```bash
claude mcp add video-director python c:/Users/user/Documents/VIDEO-EDIT-SKILL/tools/mcp_server.py
```

### Codex (OpenAI Assistants)
```bash
python adapters/codex/codex_assistant.py --create
```
Requires `OPENAI_API_KEY` environment variable.

### Hermes (Local Inference)
```bash
# Include hermes_prompt.md as system prompt in your inference engine
# Run the tool dispatcher:
python adapters/hermes/hermes_agent.py
```

### OpenClaw
```bash
# Register as a skill plugin:
python adapters/openclaw/actions.py interrogate '{"topic": "FlashAttention"}'
```

### Grok (xAI)
```bash
# Test locally:
python adapters/grok/grok_runner.py
# Register tools via xAI API using grok_system.md as system prompt
```

---

## Universal MCP Server (Works with ALL Harnesses)

The MCP server at `tools/mcp_server.py` implements the standard Model Context Protocol (JSON-RPC 2.0 over stdio) and works with any harness that supports MCP:

```bash
python tools/mcp_server.py
```

It exposes 8 tools:
1. `video_director_interrogate` - Rule of Three Questions
2. `video_director_plan` - Dual-pass director timeline
3. `symphony_generate_shot` - 9:16 vertical B-roll prompt
4. `hyperframes_render_card` - Motion graphics card
5. `voiceover_synthesize` - Neural voice + timestamps
6. `subtitle_generate` - Dynamic .ass subtitles
7. `clipchat_assemble_timeline` - Multi-track FFmpeg compile
8. `asset_gather_paper` - arXiv metadata & citation badge

---

## Standalone Python Tools (No Harness Required)

Every tool works as a standalone CLI script with zero external dependencies:

| Tool | CLI Command | Output |
|---|---|---|
| Symphony Prompt Validator | `python tools/symphony_client.py --scene "quantum lab bench"` | Validated PICTURE-916 prompt JSON |
| Hyperframes HTML/SVG Renderer | `python tools/hyperframes_renderer.py --title "FlashAttention" --format svg --out card.svg` | Standalone 1080x1920 SVG/HTML |
| Voiceover + Timestamps | `python tools/voiceover_synthesizer.py --script "Your script..." --out-wav voice.wav --out-json ts.json` | 48kHz WAV + word timestamps |
| Dynamic Subtitles | `python tools/subtitle_generator.py --timestamps ts.json --out-ass subs.ass --out-srt subs.srt` | .ass with cyan glow + .srt |
| Clipchat FFmpeg + EDL | `python tools/clipchat_compiler.py --timeline timeline.json --out-script render.bat --out-edl cut.edl --out-html preview.html` | Batch script + CMX EDL + HTML visualizer |
| arXiv Metadata | `python tools/asset_harvester.py --arxiv 2307.08691` | Paper metadata JSON |
| 3D LUT Generator | `python scripts/make_lut.py --preset perplexity-dark-slate --out grade.cube` | Adobe .cube 33x33x33 LUT |
| Interactive Director | `python scripts/interactive_director.py --topic "Raft Consensus" --domain computer-science-systems` | Full project directory with plan, prompts, and EDL |
| Skill Validator | `python scripts/validate_skill.py` | 173-point compliance test |
