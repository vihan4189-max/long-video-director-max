---
name: "01-director-workflow"
description: "Directorial interrogation, script deconstruction, and self-refining planning loop for technical videos. Interrogates the user's premise with the Rule of Three Questions, executes a senior-director self-critique pass, and outputs a beat-by-beat production timeline with tool assignments."
---

# Sub-Skill: Director Workflow & Self-Refining Planning Loop

This sub-skill controls the cognitive director phase. Before firing any generation tools or creating assets, the agent must deconstruct the scientific concept, interrogate ambiguities, execute a self-critique audit, and formulate the production plan.

---

## 1. The Script & Concept Ingestion Protocol

When presented with a paper, a topic (e.g. "Explain FlashAttention-2" or "Why the Sky is Blue"), or a rough script:

1. **Identify the Core Scientific Turn (The Insight Pivot)**:
   - What is the common misconception or intuition trap?
   - What is the mathematical or engineering mechanism that resolves it?
   - What is the ultimate consequence (e.g., 4x lower memory bandwidth, 10x throughput, proving dark matter)?

2. **Categorize the Explainer Archetype**:
   - **Archetype A: The Architecture Breakdown** (e.g. Transformer, Raft Consensus, CPU Pipeline). Emphasizes data flow, DAG diagrams, memory buffers, and code diffs.
   - **Archetype B: The Mathematical Proof/Derivation** (e.g. Bayes Theorem, Schrödinger Wave Equation, Bell's Inequality). Emphasizes stepwise LaTeX formulas, geometric coordinate graphs, and variable highlights.
   - **Archetype C: The Myth-Buster / Benchmark Showdown** (e.g. "Is Mamba Faster Than Transformers?", "The Twin Paradox"). Emphasizes comparative bar charts, citation cards, and side-by-side terminal benchmarks.

---

## 2. The Rule of Three Clarifications (Interactive Interrogation)

Never output a generic 10-question questionnaire. Present exactly **three high-leverage directorial questions**, each equipped with a recommended option so the user can immediately respond or approve:

```markdown
### 🎬 Director's Interrogation

To ensure our 9:16 vertical video delivers maximum retention and Perplexity-grade polish, please confirm three directorial choices:

1. **The Hook Angle**:
   - *(Recommended) The Paradox*: "Why your GPU is spending 80% of its time doing zero math..."
   - *The Direct Breakthrough*: "DeepMind just solved a 50-year quantum problem with 10 lines of code..."

2. **Visual Metaphor Balance**:
   - *(Recommended) Hybrid*: 40% Cinematic Symphony B-roll (hardware/optics) + 60% Hyperframes (Perplexity cards, LaTeX & code diffs).
   - *Pure Minimalist Code/Math*: 90% Hyperframes cards, UI simulations, and LaTeX derivations.

3. **Duration & Target Platform**:
   - *(Recommended) 60-Second High-Velocity Reel/Short* (~140-160 words, 14-16 visual cuts).
   - *90-120 Second Technical Deep Dive* (~220-280 words, 22-26 visual cuts).
```

---

## 3. The Self-Refining Director Plan Loop

Once the direction is set (either by user input or self-selection in autonomous `/goal` mode), the agent runs a **two-pass planning cycle**:

### Pass 1: The Initial Beat Draft
Draft the chronological beat sheet:
- Timecode (e.g. `0:00 - 0:05`, `0:05 - 0:12`, etc.)
- Voiceover line
- Visual description
- Assigned tool (`Symphony`, `Hyperframes`, or `Clipchat`)

### Pass 2: The Senior Director Self-Critique Prompt
The agent runs an internal self-critique prompt against the Pass 1 draft:

```
[INTERNAL SELF-CRITIQUE DIRECTIVE]
Audit the Pass 1 timeline against these 6 failure modes:
1. Pacing Stagnation: Is any static card or footage held for >3.5 seconds without a secondary animation or zoom?
2. Math Overload: Does any complex LaTeX equation appear without a preceding visual intuition or highlighted variables?
3. Tool Misuse: Did we ask Symphony to generate text, numbers, or UI buttons? (Flagged: must re-route to Hyperframes).
4. Safe Zone Conflict: Are any formulas or citations positioned below Y=1450px or above Y=220px?
5. Audio Monotony: Is there a planned 0.8s silence (needle-drop) right before the punchline/solution?
6. Perplexity Aesthetic Compliance: Are citations formatted with pill badges [1] referencing real papers?
```

### Pass 3: Output the Master `director_plan.md`
Format the final plan into the standard schema:

```markdown
# Master Director's Plan: [Topic Title]

## Executive Production Specs
- **Aspect Ratio**: 9:16 Vertical (1080 x 1920)
- **Duration**: 0:58 (58 seconds)
- **Target Word Count**: 148 words
- **Aesthetic**: Perplexity Dark Slate (`#111418`) + Perplexity Cyan (`#20B8CD`)

## Master Beat-by-Beat Timeline

| Timecode | Beat Name | Voiceover Script | Visual Execution | Tool Assigned | Asset Spec / Template ID |
|---|---|---|---|---|---|
| `0:00 - 0:04` | The Hook | "Most AI engineers think..." | Symphony vertical 9:16 macro silicon wafer + Hyperframes query bar | Symphony + Hyperframes | `TMPL-01` (Search Input) |
| `0:04 - 0:11` | The Problem | "Every token generated..." | Hyperframes memory bandwidth bottleneck DAG | Hyperframes | `TMPL-24` (Memory Hierarchy) |
...
```
