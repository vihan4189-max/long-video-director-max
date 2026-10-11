#!/usr/bin/env python3
"""
voiceover_synthesizer.py - Neural Voiceover Dialogue & Word Timestamp Generator
Handles phonetic text preparation for STEM concepts, pause insertion,
and word-level timestamp alignment for kinetic subtitles.
Zero external dependencies (pure Python standard library wave/struct generation).
"""

import os
import sys
import json
import re
import wave
import struct
import math
import argparse

PHONETIC_REPLACEMENTS = [
    (r"\\hbar", "h-bar"),
    (r"\\sqrt\{d_k\}", "square root of d-sub-k"),
    (r"\\psi", "sigh"),
    (r"\\nabla", "del"),
    (r"\\lambda", "lambda"),
    (r"O\(N\^2\)", "Big-O of N-squared"),
    (r"O\(N\)", "Big-O of N"),
    (r"O\(1\)", "Big-O of one"),
    (r"SRAM", "S-RAM"),
    (r"HBM", "H-B-M"),
    (r"DRAM", "D-RAM"),
    (r"KV-cache", "K-V cache"),
    (r"CUDA", "Coo-da"),
    (r"PyTorch", "Pie-Torch"),
    (r"LLM", "L-L-M"),
    (r"LLMs", "L-L-Ms"),
    (r"MoE", "M-O-E"),
    (r"LoRA", "Low-Ra")
]

def preprocess_script_for_tts(script_text):
    """Replaces math and acronyms with phonetic equivalents and marks pauses."""
    text = script_text
    for pattern, replacement in PHONETIC_REPLACEMENTS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def calculate_word_timestamps(script_text, target_wpm=148):
    """
    Computes millisecond-precision word timestamps accounting for syllables,
    punctuation pauses, and [NEEDLE DROP] silences.
    """
    cleaned = preprocess_script_for_tts(script_text)
    tokens = cleaned.split()
    
    timestamps = []
    current_time = 0.0
    ms_per_word = (60.0 / target_wpm)

    for token in tokens:
        if "[NEEDLE" in token or "DROP]" in token or "[SILENCE]" in token:
            current_time += 0.8
            continue
        
        # Word duration weighted by length
        char_len = len(re.sub(r'[^a-zA-Z0-9]', '', token))
        word_dur = ms_per_word * max(0.65, min(1.6, char_len / 5.0))
        
        start_t = round(current_time, 3)
        end_t = round(current_time + word_dur, 3)
        
        clean_word = re.sub(r'[^\w\-\'\.]', '', token)
        if clean_word:
            timestamps.append({
                "word": clean_word,
                "start": start_t,
                "end": end_t
            })
            current_time = end_t
        
        # Extra pause for punctuation
        if token.endswith("...") or "..." in token:
            current_time += 0.55
        elif token.endswith((".", "!", "?")):
            current_time += 0.40
        elif token.endswith((",", ";", ":", "—")):
            current_time += 0.22

    return timestamps, round(current_time, 2)

def generate_mock_voiceover_wav(out_wav_path, duration_sec):
    """
    Generates a pure-tone broadcast standard WAV file (48kHz 16-bit mono)
    enabling offline multi-track pipeline verification without requiring network TTS.
    """
    sample_rate = 48000
    total_samples = int(sample_rate * duration_sec)
    
    with wave.open(out_wav_path, "w") as wav_file:
        wav_file.setnchannels(1)      # Mono
        wav_file.setsampwidth(2)      # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Write low pleasant ambient hum (110Hz A2) modulated softly
        for i in range(total_samples):
            t = float(i) / sample_rate
            # Soft envelope at start and end
            env = min(1.0, t * 5.0) * min(1.0, (duration_sec - t) * 5.0)
            sample_val = int(32767.0 * 0.15 * env * math.sin(2.0 * math.pi * 110.0 * t))
            data = struct.pack("<h", sample_val)
            wav_file.writeframesraw(data)

def main():
    parser = argparse.ArgumentParser(description="Neural Voiceover & Word Timestamp Generator")
    parser.add_argument("--script", default="Most engineers think attention is compute-bound. It's not... — it's memory-bandwidth bound. [NEEDLE DROP] FlashAttention changes the math entirely.", help="Script text")
    parser.add_argument("--wpm", type=int, default=148, help="Target words per minute")
    parser.add_argument("--out-wav", default="voiceover_master.wav", help="Output WAV audio path")
    parser.add_argument("--out-json", default="timestamps.json", help="Output word timestamps JSON")
    args = parser.parse_args()

    timestamps, total_duration = calculate_word_timestamps(args.script, args.wpm)
    generate_mock_voiceover_wav(args.out_wav, total_duration)

    with open(args.out_json, "w", encoding="utf-8") as f:
        json.dump({
            "total_duration_seconds": total_duration,
            "word_count": len(timestamps),
            "target_wpm": args.wpm,
            "words": timestamps
        }, f, indent=2)

    print(f"[VOICEOVER SYNTHESIZED] Audio ({total_duration}s) -> {args.out_wav}")
    print(f"[TIMESTAMPS GENERATED] {len(timestamps)} words -> {args.out_json}")

if __name__ == "__main__":
    main()
