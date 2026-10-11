# Model Context Protocol (MCP) Server for Video Director

This MCP server equips modern AI harnesses (**Claude Code, Antigravity, OpenClaw, Cursor, Windsurf, Hermes, Codex**) with native tool calling capabilities for the complete 7-stage video production pipeline.

---

## 1. Exposed Tools

| Tool Name | Description | Key Parameters |
|---|---|---|
| `video_director_interrogate` | Analyzes script/topic and returns the **Rule of Three Clarifications** | `topic`, `script`, `target_audience` |
| `video_director_plan` | Runs the dual-pass self-refining director plan loop and produces beat-by-beat timeline | `topic`, `clarification_choices`, `duration_target` |
| `symphony_generate_shot` | Validates & generates Symphony vertical (9:16) AI video/image assets using PICTURE-916 | `scene_description`, `focal_length`, `camera_movement`, `lighting` |
| `hyperframes_render_card` | Renders Perplexity-style motion graphics, LaTeX derivations, or code diffs | `template_id`, `data`, `format` |
| `voiceover_synthesize` | Generates neural voiceover audio and millisecond word-level timestamps | `script`, `voice_persona`, `target_wpm` |
| `subtitle_generate` | Compiles syllable-synced dynamic subtitles for 9:16 safe zones (Y=1540px) | `timestamps_file`, `highlight_color`, `output_format` |
| `clipchat_assemble_timeline` | Compiles multi-track video timeline, J-cuts, audio ducking, and LUT grade | `timeline_edl_json`, `output_video_path` |
| `asset_gather_paper` | Fetches arXiv paper abstract, authors, figures, and citation pill metadata | `arxiv_id_or_url` |

---

## 2. Server Configuration

### Claude Code (`claude.json` / `settings.json`)
```json
{
  "mcpServers": {
    "video-director": {
      "command": "python",
      "args": ["c:\\Users\\user\\Documents\\VIDEO-EDIT-SKILL\\tools\\mcp_server.py"],
      "env": {
        "PYTHONPATH": "c:\\Users\\user\\Documents\\VIDEO-EDIT-SKILL"
      }
    }
  }
}
```

### Antigravity (`agy` / `settings.json`)
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

### OpenClaw (`openclaw.json`)
```json
{
  "plugins": [
    {
      "name": "video-director-mcp",
      "type": "mcp",
      "endpoint": "stdio",
      "command": "python c:/Users/user/Documents/VIDEO-EDIT-SKILL/tools/mcp_server.py"
    }
  ]
}
```
