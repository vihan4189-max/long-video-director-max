# Video Director Adapter for Claude Code

This adapter enables Anthropic's **Claude Code** (and Claude Computer Use / CLI) to natively operate the Video-Director pipeline.

---

## 1. Installation into Claude Code Project

Copy this directory's `CLAUDE.md` to your project root, or include it in your `.claudecode/` configuration:

```bash
# Add Video Director MCP server to Claude Code
claude mcp add video-director python c:/Users/user/Documents/VIDEO-EDIT-SKILL/tools/mcp_server.py
```

---

## 2. Directorial Commands for Claude Code

When chatting with Claude Code, you can use these shortcuts:

- `/video-director interrogate "<topic>"`: Analyzes the script/concept and presents the Rule of Three Questions.
- `/video-director plan "<topic>"`: Runs the dual-pass self-refining director plan loop and writes `director_plan.md`.
- `/video-director symphony "<scene>"`: Generates and validates a PICTURE-916 vertical prompt for Symphony.
- `/video-director render-card <template_id>`: Renders a Perplexity motion graphics card (e.g. `TMPL-11`).
- `/video-director compile-timeline <timeline.json>`: Compiles the Clipchat multi-track edit into an FFmpeg script and EDL.

---

## 3. Strict Guidelines for Claude Code

1. **Symphony Aspect Ratio Constraint**:
   Claude Code must NEVER prompt Symphony for horizontal (16:9) video or panoramic pans. Always frame in **9:16 vertical (1080x1920)** with upper-third headroom.
2. **Tool Specialization**:
   - Claude Code must never ask Symphony to draw equations or code. Always use `tools/hyperframes_renderer.py` for mathematical formulas, code diffs, and UI cards.
3. **Pacing & Trimming**:
   - Claude Code must ensure every Symphony clip has its first 0.5s and last 0.5s trimmed in Clipchat to remove edge morphing artifacts.
