---
name: "video-director-antigravity"
description: "Antigravity-native adapter for the Video-Director production pipeline. Equips Antigravity with 8 specialized MCP tools for directing, generating, and assembling high-retention vertical (9:16) STEM videos under the Perplexity editorial aesthetic. Use whenever the user asks to create, direct, edit, or storyboard a technical explainer video."
---

# Antigravity Adapter: Video Director

This adapter connects Antigravity's agent loop directly to the Video-Director MCP server and Python toolchain.

## MCP Server Registration

Add to your Antigravity workspace settings or global `~/.gemini/settings.json`:

```json
{
  "mcp_servers": {
    "video_director": {
      "command": "python",
      "args": ["c:/Users/user/Documents/VIDEO-EDIT-SKILL/tools/mcp_server.py"]
    }
  }
}
```

Alternatively, register via CLI:
```bash
agy mcp add video-director python c:/Users/user/Documents/VIDEO-EDIT-SKILL/tools/mcp_server.py
```

## Available MCP Tools

Once registered, Antigravity gains these 8 native tools:

| Tool | Purpose |
|---|---|
| `video_director_interrogate` | Analyze topic, return Rule of Three Clarifications |
| `video_director_plan` | Dual-pass self-refining director timeline plan |
| `symphony_generate_shot` | Validate & build PICTURE-916 vertical prompt |
| `hyperframes_render_card` | Render Perplexity motion card (LaTeX, code, UI) |
| `voiceover_synthesize` | Direct neural voice & generate word timestamps |
| `subtitle_generate` | Compile dynamic .ass subtitles with cyan word highlight |
| `clipchat_assemble_timeline` | Compile multi-track edit + FFmpeg script |
| `asset_gather_paper` | Fetch arXiv metadata for citation badges |

## Directorial Rules for Antigravity

1. **Symphony Constraint**: Symphony creates ONLY vertical 9:16 (1080x1920). Never request horizontal ratios.
2. **Tool Specialization**: Never ask Symphony to render text, math, or code. Route all typography to Hyperframes.
3. **Trimming**: Trim first 0.5s and last 0.5s of every Symphony clip in Clipchat.
4. **Needle Drop**: Script 0.8s silence before every major mathematical or architectural revelation.
5. **Safe Zones**: All UI elements between Y:240px and Y:1450px. Subtitles at Y:1540px.

## Standalone Python Tools

Antigravity can also invoke these tools directly via `run_command`:

| Script | Command | Purpose |
|---|---|---|
| Symphony Client | `python tools/symphony_client.py --scene "..."` | Validates & generates 9:16 B-roll prompts |
| Hyperframes Renderer | `python tools/hyperframes_renderer.py --title "..." --format svg` | Renders HTML5/SVG motion cards |
| Voiceover Synthesizer | `python tools/voiceover_synthesizer.py --script "..."` | Generates WAV audio + word timestamps |
| Subtitle Generator | `python tools/subtitle_generator.py --timestamps timestamps.json` | Compiles .ass/.srt subtitles |
| Clipchat Compiler | `python tools/clipchat_compiler.py --timeline timeline.json` | Compiles FFmpeg scripts + CMX EDL |
| Asset Harvester | `python tools/asset_harvester.py --arxiv 2307.08691` | Fetches arXiv paper metadata |
| LUT Generator | `python scripts/make_lut.py --preset perplexity-dark-slate --out lut.cube` | Creates 3D color grading LUTs |
| Interactive Director | `python scripts/interactive_director.py --topic "..."` | Full 7-stage pipeline runner |

## Workflow When User Says "Create a video about X"

1. Read `SKILL.md` (master router) to understand the 7-stage pipeline.
2. Call `video_director_interrogate` with the topic.
3. Present the Rule of Three Questions to the user.
4. Call `video_director_plan` with their choices.
5. Run `asset_harvester.py` if arXiv papers are referenced.
6. Call `symphony_generate_shot` for each B-roll beat.
7. Call `hyperframes_render_card` for each motion card beat.
8. Call `voiceover_synthesize` with the finalized script.
9. Call `subtitle_generate` with the timestamps.
10. Call `clipchat_assemble_timeline` with the complete EDL.
