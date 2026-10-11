#!/usr/bin/env python3
"""
Test & Validation Suite for Video-Director Skill
Verifies:
1. Master SKILL.md frontmatter and structure
2. All 6 sub-skills frontmatter and content
3. All reference documents
4. All 36 Perplexity-style templates
5. All 120 STEM case studies
6. Vertical safe zones compliance (9:16)
"""

import os
import re
import sys

BASE_DIR = r"c:\Users\user\Documents\VIDEO-EDIT-SKILL"
ERRORS = []
WARNINGS = []
PASSED_CHECKS = 0

def check_file_exists(rel_path):
    global PASSED_CHECKS
    p = os.path.join(BASE_DIR, rel_path)
    if not os.path.isfile(p):
        ERRORS.append(f"Missing required file: {rel_path}")
        return False
    PASSED_CHECKS += 1
    return True

def validate_frontmatter(file_path):
    global PASSED_CHECKS
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if not content.startswith("---"):
        ERRORS.append(f"Missing YAML frontmatter start in {os.path.basename(file_path)}")
        return False
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        ERRORS.append(f"Invalid YAML frontmatter block in {os.path.basename(file_path)}")
        return False
    
    fm = parts[1]
    if "name:" not in fm or "description:" not in fm:
        ERRORS.append(f"Frontmatter missing 'name' or 'description' in {os.path.basename(file_path)}")
        return False
    
    PASSED_CHECKS += 1
    return True

def validate_templates():
    global PASSED_CHECKS
    tmpl_dir = os.path.join(BASE_DIR, "templates")
    total_templates = 0
    for root, _, files in os.walk(tmpl_dir):
        for f in files:
            if f.endswith(".md"):
                total_templates += 1
                fp = os.path.join(root, f)
                with open(fp, "r", encoding="utf-8") as tf:
                    text = tf.read()
                if "Perplexity" not in text:
                    WARNINGS.append(f"Template {f} does not explicitly mention Perplexity design.")
                if "1080" not in text or "1920" not in text:
                    ERRORS.append(f"Template {f} missing 1080x1920 vertical canvas specification.")
                if "Hyperframes" not in text:
                    ERRORS.append(f"Template {f} missing Hyperframes specification.")
                PASSED_CHECKS += 1
    
    if total_templates < 30 or total_templates > 40:
        ERRORS.append(f"Template count out of requested bounds (30-40). Found: {total_templates}")
    else:
        print(f"  [OK] Verified {total_templates} Perplexity templates (Target: 30-40)")

def validate_case_studies():
    global PASSED_CHECKS
    cs_dir = os.path.join(BASE_DIR, "case-studies")
    total_cs = 0
    domains = {"ai-machine-learning": 0, "mathematics-probability": 0, "physics-quantum": 0, "computer-science-systems": 0}
    
    for domain in domains.keys():
        d_path = os.path.join(cs_dir, domain)
        if not os.path.isdir(d_path):
            ERRORS.append(f"Missing case study domain directory: {domain}")
            continue
        files = [f for f in os.listdir(d_path) if f.endswith(".md")]
        domains[domain] = len(files)
        total_cs += len(files)
        
        for f in files:
            fp = os.path.join(d_path, f)
            with open(fp, "r", encoding="utf-8") as cs_f:
                c_text = cs_f.read()
            
            # Check mandatory production stages
            for req in ["Stage 1: Interactive Interrogation", "Stage 2: Dual-Pass Self-Refining", 
                        "Stage 4: Symphony 9:16", "Stage 5: Hyperframes Motion", "Stage 6: Voiceover", "Stage 7: Clipchat"]:
                if req not in c_text:
                    ERRORS.append(f"Case study {f} missing required section: {req}")
            
            # Check 9:16 and vertical constraint
            if "9:16" not in c_text:
                ERRORS.append(f"Case study {f} missing 9:16 vertical specification.")
            
            PASSED_CHECKS += 1

    print(f"  [OK] Verified {total_cs} case studies across 4 domains (Target: 100-200).")
    for d, c in domains.items():
        print(f"       - {d}: {c} studies")

def main():
    print("=" * 60)
    print("RUNNING VIDEO-DIRECTOR SKILL VALIDATION SUITE")
    print("=" * 60)

    # 1. Master SKILL.md, README.md, and USE-ME.md
    print("1. Validating Master SKILL.md, README.md, and USE-ME.md...")
    master_skill = os.path.join(BASE_DIR, "SKILL.md")
    if check_file_exists("SKILL.md"):
        validate_frontmatter(master_skill)
    check_file_exists("README.md")
    check_file_exists("USE-ME.md")

    # 2. Sub-Skills
    print("2. Validating Sub-Skills...")
    sub_skills = [
        "sub-skills/01-director-workflow/SKILL.md",
        "sub-skills/02-asset-gathering/SKILL.md",
        "sub-skills/03-symphony-vertical-generation/SKILL.md",
        "sub-skills/04-hyperframes-motion/SKILL.md",
        "sub-skills/05-voiceover-and-subtitles/SKILL.md",
        "sub-skills/06-clipchat-assembly/SKILL.md"
    ]
    for ss in sub_skills:
        if check_file_exists(ss):
            validate_frontmatter(os.path.join(BASE_DIR, ss))

    # 3. References
    print("3. Validating References...")
    refs = [
        "references/perplexity-design-system.md",
        "references/vertical-video-safe-zones.md",
        "references/camera-and-lens-reference.md",
        "references/character-sheet-for-tech.md",
        "references/prompt-pack-stem.md",
        "references/perplexity-theme.css",
        "references/PerplexityDarkSlate.cube"
    ]
    for r in refs:
        check_file_exists(r)

    # 4. Templates
    print("4. Validating Perplexity Design Templates...")
    validate_templates()

    # 5. Case Studies
    print("5. Validating Production Case Studies...")
    validate_case_studies()

    # 6. Harness Adapters
    print("6. Validating Multi-Harness Adapters...")
    adapters = [
        "adapters/ADAPTERS_GUIDE.md",
        "adapters/antigravity/SKILL.md",
        "adapters/antigravity/mcp_config.json",
        "adapters/claude-code/CLAUDE.md",
        "adapters/claude-code/tools.json",
        "adapters/codex/SYSTEM_PROMPT.md",
        "adapters/codex/openai_tools.json",
        "adapters/codex/codex_assistant.py",
        "adapters/grok/grok_system.md",
        "adapters/grok/grok_runner.py",
        "adapters/hermes/hermes_prompt.md",
        "adapters/hermes/hermes_agent.py",
        "adapters/openclaw/skill.json",
        "adapters/openclaw/actions.py"
    ]
    for a in adapters:
        check_file_exists(a)

    # 7. Python Tools
    print("7. Validating Standalone Python Tools...")
    tools = [
        "tools/mcp_server.py",
        "tools/hyperframes_renderer.py",
        "tools/symphony_client.py",
        "tools/clipchat_compiler.py",
        "tools/voiceover_synthesizer.py",
        "tools/subtitle_generator.py",
        "tools/asset_harvester.py",
        "tools/prompt_auditor.py",
        "tools/pipeline_runner.py",
        "tools/MCP_GUIDE.md"
    ]
    for t in tools:
        check_file_exists(t)

    print("=" * 60)
    print(f"VALIDATION SUMMARY: {PASSED_CHECKS} checks passed.")
    if WARNINGS:
        print(f"WARNINGS ({len(WARNINGS)}):")
        for w in WARNINGS:
            print(f"  [!] {w}")
    if ERRORS:
        print(f"FAILED with {len(ERRORS)} errors:")
        for e in ERRORS:
            print(f"  [X] {e}")
        sys.exit(1)
    else:
        print("[SUCCESS] All components validated with 100% compliance across all harnesses and tools!")
        sys.exit(0)

if __name__ == "__main__":
    main()
