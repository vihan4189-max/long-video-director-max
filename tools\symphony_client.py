#!/usr/bin/env python3
"""
symphony_client.py - Symphony Vertical (9:16) Asset Generation Client & Validator
Enforces strictly vertical (1080x1920) aspect ratio, the PICTURE-916 formula,
and validates prompts against AI diffusion failure modes (anti-drift, negative steering).
Zero external dependencies.
"""

import os
import sys
import json
import re
import argparse

PICTURE_BLOCKS = ["STYLE", "IMAGERY", "CAMERA", "TIMING", "ATMOSPHERE", "RENDER", "EXTRA"]

BANNED_SYMPHONY_TERMS = [
    (r"\b(render|show|write|display)\s+(code|equation|formula|math|text|subtitles|numbers)\b",
     "Symphony AI video models hallucinate text/math. Delegate all typography, formulas, and code to Hyperframes."),
    (r"\b(16:9|horizontal|widescreen|landscape|panoramic)\b",
     "CRITICAL CONSTRAINT VIOLATION: Symphony generates ONLY vertical (9:16) assets. Do not request horizontal ratios."),
    (r"\bnot\s+smiling\b", "Negative steering: use 'flat neutral expression, jaw set' instead of 'not smiling'."),
    (r"\bno\s+modern\b", "Negative steering: state positive period material details instead of 'no modern'."),
    (r"\bdo\s+not\s+shake\b", "Negative steering: use 'locked-off camera on solid tripod' instead of 'do not shake'.")
]

class SymphonyClient:
    def __init__(self, api_key=None, endpoint=None):
        self.api_key = api_key or os.getenv("SYMPHONY_API_KEY", "")
        self.endpoint = endpoint or os.getenv("SYMPHONY_ENDPOINT", "https://api.symphony.ai/v1")

    def validate_prompt(self, prompt_text):
        """Audits a prompt against Symphony constraints and PICTURE formula."""
        warnings = []
        errors = []

        # Check banned terms / violations
        for pattern, explanation in BANNED_SYMPHONY_TERMS:
            if re.search(pattern, prompt_text, re.IGNORECASE):
                if "CRITICAL" in explanation or "hallucinate" in explanation:
                    errors.append(explanation)
                else:
                    warnings.append(explanation)

        # Check for 9:16 specification
        if "9:16" not in prompt_text and "vertical" not in prompt_text.lower():
            warnings.append("Prompt does not explicitly specify '9:16 vertical composition'. Symphony may default improperly.")

        # Check camera moves
        moves = re.findall(r"(dolly|push|pull|track|pedestal|orbit|locked-off)", prompt_text, re.IGNORECASE)
        if len(moves) > 2:
            warnings.append(f"Detected {len(moves)} camera movement terms ({', '.join(moves)}). AI video generation is most stable with exactly ONE camera movement per shot.")

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }

    def build_picture_prompt(self, scene, focal="35mm", move="slow push forward", lighting="5400K cold slate with cyan rim light"):
        """Constructs a validated PICTURE-916 prompt."""
        prompt = (
            f"[P] PHOTOGRAPHIC STYLE: {focal} anamorphic cine-lens, ARRI Alexa LF look, 9:16 portrait vertical framing, photochemical grain.\n"
            f"[I] IMAGERY & SCENE: {scene}.\n"
            f"[C] CAMERA & COMPOSITION: Vertical angle, camera low at chest height, subject centered with 25% upper headroom for UI overlay, {focal} prime lens at f/2.8.\n"
            f"[T] TIMING & LIGHTING: {lighting}.\n"
            f"[U] USE OF ATMOSPHERE: Micro-filtered air, subtle optical lens flare.\n"
            f"[R] RENDER STYLE: Absolute physical material realism, tactile industrial textures, zero 3D CGI gloss.\n"
            f"[E] EXTRA MOTION: {move} over 4 seconds, single camera motion vector."
        )
        return prompt

    def generate_shot(self, prompt, dry_run=True, output_path=None):
        """Submits or simulates a Symphony generation job."""
        audit = self.validate_prompt(prompt)
        if not audit["valid"]:
            raise ValueError(f"Symphony Prompt Rejected:\n" + "\n".join(audit["errors"]))

        if dry_run:
            print(f"[SYMPHONY DRY RUN] Validated 9:16 prompt:")
            print("-" * 50)
            print(prompt)
            print("-" * 50)
            if audit["warnings"]:
                print(f"[SYMPHONY WARNINGS]:")
                for w in audit["warnings"]:
                    print(f"  (!) {w}")
            return {
                "job_id": "sym_mock_916_88329",
                "status": "ready",
                "resolution": "1080x1920 (9:16)",
                "duration_seconds": 4.0,
                "cut_rule": "Trim first 0.5s and last 0.5s in Clipchat",
                "output": output_path or "assets/symphony_shots/shot_mock_916.mp4"
            }
        else:
            # Here real API network call would execute if credentials are set
            return {"job_id": "real_sym_job_placeholder", "status": "queued"}

def main():
    parser = argparse.ArgumentParser(description="Symphony Vertical Asset Generation Client")
    parser.add_argument("--scene", default="Cleanroom robotics holding a 300mm silicon wafer", help="Scene description")
    parser.add_argument("--focal", default="35mm", help="Focal length")
    parser.add_argument("--move", default="slow push forward", help="Camera movement")
    parser.add_argument("--validate-only", action="store_true", help="Only validate input prompt")
    parser.add_argument("--prompt", default=None, help="Raw prompt to validate")
    args = parser.parse_args()

    client = SymphonyClient()

    if args.prompt:
        audit = client.validate_prompt(args.prompt)
        print(json.dumps(audit, indent=2))
        sys.exit(0 if audit["valid"] else 1)

    built_prompt = client.build_picture_prompt(args.scene, args.focal, args.move)
    result = client.generate_shot(built_prompt, dry_run=True)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
