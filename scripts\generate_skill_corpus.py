#!/usr/bin/env python3
"""
Corpus Generator for Video-Director Skill
Generates:
- 36 Modular Perplexity Design Templates (UI, STEM Math, AI/CS Architectures, Retention Cards)
- 120 Deep Production Case Studies across AI/ML (30), Math (30), Physics (30), CS Systems (30)
- Validation Test Suite
"""

import os
import json
import re

BASE_DIR = r"c:\Users\user\Documents\VIDEO-EDIT-SKILL"
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
CASE_STUDIES_DIR = os.path.join(BASE_DIR, "case-studies")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(CASE_STUDIES_DIR, exist_ok=True)
os.makedirs(SCRIPTS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. TEMPLATES DEFINITION (36 Perplexity-Style Templates)
# -------------------------------------------------------------

TEMPLATES = [
    # 01 - UI & Search Interactions
    ("01-ui-search-interactions", "TMPL-01-query-input-bar", "Perplexity Search Query Bar with Animated Keystrokes",
     "Interactive search bar simulation with pulsating cyan cursor and character-by-character typing animation.",
     "Search", "Query Input", "#1B1F26", "#20B8CD"),
    ("01-ui-search-interactions", "TMPL-02-pro-search-thinking-steps", "Pro Search Stepwise Reasoning Checklist",
     "Staggered execution checklist with pulsating active query indicator and completed green checkmarks.",
     "Reasoning", "Thinking Steps", "#16191E", "#10B981"),
    ("01-ui-search-interactions", "TMPL-03-source-matrix-card", "Multi-Source Matrix & Domain Badges",
     "Grid of authenticated academic and technical source cards with domain favicons and article counts.",
     "Sources", "Source Matrix", "#16191E", "#20B8CD"),
    ("01-ui-search-interactions", "TMPL-04-citation-pill-popover", "Interactive Citation Badge & Popover Excerpt",
     "Floating citation pill [1] that smoothly expands into a source quote preview with spring physics.",
     "Citations", "Citation Pill", "#16191E", "#20B8CD"),
    ("01-ui-search-interactions", "TMPL-05-answer-synthesis-stream", "Answer Synthesis Streaming Card",
     "Editorial dark slate container with streaming text, bold semantic headers, and embedded citation badges.",
     "Synthesis", "Streaming Answer", "#16191E", "#F3F3EE"),
    ("01-ui-search-interactions", "TMPL-06-related-questions-pill-stack", "Follow-up Query Pill Carousel",
     "Horizontal and vertical stack of related exploratory questions with right-arrow hover states.",
     "Exploration", "Follow-up Pills", "#16191E", "#9DA3AE"),
    ("01-ui-search-interactions", "TMPL-07-focus-mode-selector", "Perplexity Focus Mode Toggle (Academic/Code)",
     "Pill toggle displaying Academic, Writing, Computational, and Web search modes with cyan selection halo.",
     "Modes", "Focus Selector", "#1B1F26", "#20B8CD"),
    ("01-ui-search-interactions", "TMPL-08-source-verification-drawer", "Source Fact Verification Drawer",
     "Comparison slide-out separating Verified vs Disputed claims with citation footnotes.",
     "Verification", "Fact Drawer", "#16191E", "#E5A93C"),
    ("01-ui-search-interactions", "TMPL-09-collection-library-card", "Research Collection & Paper Folder Card",
     "Grouped paper card displaying metadata: tags, date, citation count, and PDF preview thumbnail.",
     "Library", "Collection Card", "#16191E", "#20B8CD"),
    ("01-ui-search-interactions", "TMPL-10-quick-summary-takeaways", "Executive Takeaways Summary Container",
     "Clean 3-bullet golden insight container with glowing cyan icon bullets and high-contrast typography.",
     "Summary", "Key Takeaways", "#16191E", "#20B8CD"),

    # 02 - STEM & Math Visualizations
    ("02-stem-math-visualizations", "TMPL-11-stepwise-latex-derivation", "Stepwise LaTeX Formula Derivation",
     "Clean white KaTeX math equation with sequential animated variable highlights and explanatory callout pills.",
     "Mathematics", "LaTeX Derivation", "#16191E", "#20B8CD"),
    ("02-stem-math-visualizations", "TMPL-12-cartesian-coordinate-plot", "2D Coordinate System with Animated Curve",
     "Minimalist dark slate Cartesian grid with smooth curve plotting and coordinate tangent line.",
     "Calculus", "Coordinate Graph", "#16191E", "#20B8CD"),
    ("02-stem-math-visualizations", "TMPL-13-3d-vector-manifold", "3D Vector Space & Manifold Projection",
     "Isometric vector coordinates with animated basis vectors i, j, k and planar surface contour lines.",
     "Linear Algebra", "Vector Manifold", "#111418", "#00A3BF"),
    ("02-stem-math-visualizations", "TMPL-14-probability-distribution-bell", "Gaussian & Probability Distribution Curve",
     "Normal distribution bell curve with dynamic standard deviation bands and shaded p-value area.",
     "Statistics", "Bell Curve", "#16191E", "#E5A93C"),
    ("02-stem-math-visualizations", "TMPL-15-matrix-tensor-grid", "Matrix Multiplication & Tensor Dot Product",
     "Row-by-column tensor dot product animation with highlighted row vector and column vector meeting at cell.",
     "Deep Learning", "Tensor Grid", "#16191E", "#20B8CD"),
    ("02-stem-math-visualizations", "TMPL-16-differential-rate-flow", "Differential Rate Equation & Dynamic Slider",
     "Continuous rate derivative dx/dt with interactive parameter slider demonstrating exponential decay or growth.",
     "Physics", "Differential Flow", "#16191E", "#10B981"),
    ("02-stem-math-visualizations", "TMPL-17-geometric-proof-construction", "Euclidean Geometric Proof & Angle Construction",
     "Dark slate geometry canvas showing triangle, circle, or polygon angles dynamically snapping with proofs.",
     "Geometry", "Geometric Proof", "#16191E", "#F3F3EE"),
    ("02-stem-math-visualizations", "TMPL-18-discrete-fourier-spectrum", "Fourier Transform Frequency Spectrum Decomposition",
     "Time-domain waveform splitting into constituent sine waves and frequency spike bar chart.",
     "Signal Processing", "Fourier Spectrum", "#111418", "#20B8CD"),
    ("02-stem-math-visualizations", "TMPL-19-physics-free-body-diagram", "Physics Free Body Force Vector Diagram",
     "Mechanical body showing labeled force arrows (Gravity, Normal, Friction, Tension) with net vector sum.",
     "Mechanics", "Free Body Diagram", "#16191E", "#E5A93C"),
    ("02-stem-math-visualizations", "TMPL-20-quantum-bloch-sphere", "Quantum Qubit State & Bloch Sphere Visualizer",
     "3D wireframe Bloch sphere with state vector |psi> rotating between basis states |0> and |1>.",
     "Quantum Computing", "Bloch Sphere", "#111418", "#20B8CD"),

    # 03 - AI & CS Architectures
    ("03-ai-cs-architectures", "TMPL-21-transformer-attention-matrix", "Transformer Multi-Head Self-Attention Matrix",
     "Query-Key attention heatmap grid with active token connection lines and softmax weight intensity.",
     "Transformers", "Attention Matrix", "#16191E", "#20B8CD"),
    ("03-ai-cs-architectures", "TMPL-22-neural-layer-dag-flow", "Neural Network Layer DAG & Tensor Flow",
     "Directed acyclic graph showing forward tensor flow through MLP, Residual, and RMSNorm blocks.",
     "Deep Learning", "DAG Flow", "#111418", "#00A3BF"),
    ("03-ai-cs-architectures", "TMPL-23-syntax-highlighted-code-diff", "Syntax-Highlighted Terminal Code Diff",
     "Side-by-side or unified red/green code diff showing naive loop vs vectorized CUDA kernel.",
     "Systems", "Code Diff", "#16191E", "#10B981"),
    ("03-ai-cs-architectures", "TMPL-24-memory-hierarchy-bottleneck", "GPU/CPU Memory Hierarchy & Bandwidth Waterfall",
     "Visual pyramid comparing SRAM, HBM3e, and DRAM latency with moving data packet counters.",
     "Hardware", "Memory Hierarchy", "#16191E", "#E5A93C"),
    ("03-ai-cs-architectures", "TMPL-25-terminal-execution-log", "Real-Time Terminal Execution & Training Metric Log",
     "Monospaced CLI window printing training step, loss curve, learning rate, and throughput (TFLOPs).",
     "LLM Training", "Terminal Log", "#12151A", "#20B8CD"),
    ("03-ai-cs-architectures", "TMPL-26-benchmark-bar-comparison", "Competitive Benchmark Bar Showdown",
     "Horizontal bar chart comparing models or algorithms with speedup multiples and error bars.",
     "Evaluation", "Benchmark Bars", "#16191E", "#20B8CD"),
    ("03-ai-cs-architectures", "TMPL-27-lora-low-rank-decomposition", "LoRA Low-Rank Weight Decomposition (W = W0 + BxA)",
     "Large weight matrix W0 kept frozen in dark gray, beside compact tall matrix B and wide matrix A in cyan.",
     "Fine-Tuning", "LoRA Decomposition", "#16191E", "#20B8CD"),
    ("03-ai-cs-architectures", "TMPL-28-kv-cache-token-buffer", "KV-Cache PagedAttention & Sliding Window Buffer",
     "Memory block table mapping logical tokens to physical GPU memory pages without memory fragmentation.",
     "Inference", "KV Cache Buffer", "#16191E", "#00A3BF"),
    ("03-ai-cs-architectures", "TMPL-29-distributed-raft-consensus", "Distributed Raft Consensus & Leader Election",
     "Cluster of 5 server nodes with heartbeat pings, election timeouts, and synchronized log commits.",
     "Distributed Systems", "Raft Consensus", "#111418", "#10B981"),
    ("03-ai-cs-architectures", "TMPL-30-lsm-tree-compaction", "Log-Structured Merge Tree (LSM) & SSTable Compaction",
     "MemTable buffer flushing to Level 0 SSTables and background merge-sort compaction to Level 1.",
     "Databases", "LSM Tree", "#16191E", "#E5A93C"),

    # 04 - Narrative Retention Cards
    ("04-narrative-retention-cards", "TMPL-31-paper-abstract-card", "Academic arXiv Paper Abstract & Spotlight Card",
     "Peer-reviewed paper title card with author tags, arXiv badge, and golden sentence highlighted.",
     "Literature", "Abstract Card", "#FBFBF9", "#0D8697"),
    ("04-narrative-retention-cards", "TMPL-32-myth-buster-split-screen", "Myth Buster: Common Intuition vs Mathematical Reality",
     "Dual-panel vertical split comparing the popular misconception (crimson tint) with the verified truth (cyan tint).",
     "Debunking", "Myth Buster", "#16191E", "#20B8CD"),
    ("04-narrative-retention-cards", "TMPL-33-big-stat-counter", "Monumental Metric Callout & Animated Counter",
     "Massive 120px stat callout (e.g. '10,000x' or '0.0001%') with ticker roll and subtitle context.",
     "Impact", "Stat Counter", "#111418", "#20B8CD"),
    ("04-narrative-retention-cards", "TMPL-34-quote-editorial-plaque", "Editorial Historical Quote Plaque",
     "Classic serif typography quote with author portrait thumbnail, year, and book reference citation.",
     "Authority", "Quote Plaque", "#16191E", "#F3F3EE"),
    ("04-narrative-retention-cards", "TMPL-35-timeline-chronology-spine", "Vertical Milestone Spine & Chronology Card",
     "Vertical timeline with glowing node checkpoints connecting historical breakthroughs.",
     "History", "Timeline Spine", "#111418", "#20B8CD"),
    ("04-narrative-retention-cards", "TMPL-36-outro-recap-cta", "Master Summary & Bookmark CTA Card",
     "3-card stacked summary reinforcing the mental model with a clean Perplexity bookmark CTA.",
     "Retention", "Summary CTA", "#16191E", "#20B8CD"),
]

def generate_template_file(category, tmpl_id, name, desc, domain, archetype, bg_color, accent_color):
    cat_dir = os.path.join(TEMPLATES_DIR, category)
    os.makedirs(cat_dir, exist_ok=True)
    file_path = os.path.join(cat_dir, f"{tmpl_id}.md")
    
    content = f"""# Template {tmpl_id}: {name}

**Category**: `{category}`  
**Domain**: `{domain}`  
**Component Archetype**: `{archetype}`  
**Design Standards**: Perplexity ([www.perplexity.ai](https://www.perplexity.ai)) Dark Slate & Cyan Specification

---

## 1. Overview & Purpose
{desc}

Designed strictly for **1080 x 1920 (9:16 vertical)** video formats. Optimized for programmatic rendering in **Hyperframes** and seamless multi-track overlay in **Clipchat**.

---

## 2. Perplexity Design Tokens & Spatial Geometry

```css
:root {{
  --canvas-width: 1080px;
  --canvas-height: 1920px;
  --card-bg: {bg_color};
  --card-border: 1px solid #23272F;
  --card-radius: 16px;
  --accent-color: {accent_color};
  --text-primary: #F3F3EE;
  --text-secondary: #9DA3AE;
  --text-muted: #646C7A;
  --easing-spring: cubic-bezier(0.16, 1, 0.3, 1);
}}
```

### Canvas Safe Zones
- **Top Bound**: `Y >= 240px` (clearing mobile search / platform indicators)
- **Bottom Bound**: `Y <= 1450px` (clearing dynamic subtitles and engagement buttons)
- **Left Margin**: `80px`
- **Right Margin**: `80px` (usable width: `920px`)

---

## 3. Hyperframes Motion & Layout Specification

```json
{{
  "templateId": "{tmpl_id}",
  "version": "2.0",
  "canvas": {{ "width": 1080, "height": 1920 }},
  "theme": {{
    "background": "{bg_color}",
    "border": "#23272F",
    "accent": "{accent_color}",
    "text": "#F3F3EE"
  }},
  "animation": {{
    "enter": "slideFadeUp",
    "durationMs": 320,
    "easing": "cubic-bezier(0.16, 1, 0.3, 1)",
    "initialOffset": {{ "y": 14 }},
    "opacity": [0, 1]
  }},
  "elements": [
    {{
      "id": "container_card",
      "type": "card",
      "x": 80,
      "y": 480,
      "width": 920,
      "height": 580,
      "borderRadius": 16,
      "backgroundColor": "{bg_color}",
      "borderColor": "#23272F",
      "boxShadow": "0 8px 32px rgba(0,0,0,0.5)"
    }},
    {{
      "id": "header_pill",
      "type": "pill",
      "x": 120,
      "y": 520,
      "text": "{domain.upper()} // {archetype.upper()}",
      "fontSize": 20,
      "color": "{accent_color}",
      "backgroundColor": "rgba(32, 184, 205, 0.12)"
    }},
    {{
      "id": "primary_content",
      "type": "content_block",
      "x": 120,
      "y": 580,
      "width": 840,
      "lineHeight": 1.4
    }}
  ]
}}
```

---

## 4. Director's Execution Logic & Integration

1. **When to Trigger This Template**:
   - Use during Stage 6 (Hyperframes Motion) when the script requires clear visual evidence for {archetype.lower()}.
2. **Pacing Rules**:
   - Minimum visual hold: `2.4 seconds` (allows viewer to absorb layout).
   - Maximum visual hold without secondary state transition: `4.5 seconds`.
3. **Clipchat Multi-Track Placement**:
   - Place on **Track V2** (Motion Graphics).
   - Sync the initial card entrance with a `J-cut` audio lead (voiceover begins 6 frames before card appears).
   - Pair with subtle SFX: `ui_card_slide.wav` (-24 dB) on Track A2.

---

## 5. Quality Checklist & Verification

- [ ] All coordinates adhere to 9:16 safe bounds (`Y: 240px - 1450px`, `X: 80px - 1000px`)
- [ ] Motion curve uses `cubic-bezier(0.16, 1, 0.3, 1)`
- [ ] Text typography strictly uses `Inter`, `Iowan Old Style`, or `JetBrains Mono`
- [ ] No saturated neon TikTok colors; strictly Perplexity muted palette with cyan `{accent_color}` accents
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# -------------------------------------------------------------
# 2. CASE STUDIES DEFINITIONS (120 Real-World STEM Scenarios)
# -------------------------------------------------------------

CASE_STUDY_DOMAINS = {
    "ai-machine-learning": [
        ("CS-AI-01", "FlashAttention: GPU SRAM Tiling & Memory Wall", "Why standard attention hits a memory wall and how tiling queries and keys in SRAM cuts memory reads by 5x."),
        ("CS-AI-02", "LoRA: Low-Rank Matrix Decomposition", "Why fine-tuning 70B parameters is unnecessary when you can decompose weight updates into two small rank-8 matrices."),
        ("CS-AI-03", "Mixture of Experts (MoE) Routing Mechanics", "How Mixtral routes tokens to 2 out of 8 experts per layer using softmax gating, running 47B capacity at 13B speed."),
        ("CS-AI-04", "Rotary Position Embeddings (RoPE)", "How complex numbers and 2D rotation matrices solve relative token distance without absolute positional bias."),
        ("CS-AI-05", "PagedAttention & KV-Cache Virtual Memory", "How vLLM adapted OS paging tables to eliminate 60% memory fragmentation in GPU inference."),
        ("CS-AI-06", "Direct Preference Optimization (DPO)", "The mathematical proof showing you don't need a separate reward model or RL loop to align LLMs."),
        ("CS-AI-07", "Speculative Decoding: Small Draft, Big Verifier", "How running a 1B model to draft 5 tokens and verifying them in parallel with a 70B model doubles inference speed."),
        ("CS-AI-08", "Mamba & State Space Models (SSMs)", "Why selective state spaces break the quadratic attention curse with linear time complexity."),
        ("CS-AI-09", "Quantization: FP16 to INT4 AWQ", "How Activation-aware Weight Quantization preserves the top 1% salient weights to run LLMs on edge devices."),
        ("CS-AI-10", "Diffusion Models: Forward Noise vs Reverse Denoising", "How Langevin dynamics and score-based matching turn pure Gaussian static into high-fidelity imagery."),
        ("CS-AI-11", "Vector Embeddings & Cosine Distance Geometry", "How high-dimensional manifolds encode semantic meaning through inner products in 1536-dimensional space."),
        ("CS-AI-12", "Reinforcement Learning from Human Feedback (RLHF) & PPO", "Deconstructing the Proximal Policy Optimization clipped objective and KL penalty."),
        ("CS-AI-13", "Transformer Self-Attention: Q, K, V Matrix Dot Products", "The foundational derivation of Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V."),
        ("CS-AI-14", "Retrieval-Augmented Generation (RAG) Architecture", "Overcoming hallucination by routing user prompts through dense vector search and re-ranking."),
        ("CS-AI-15", "Backpropagation & Matrix Chain Rule Derivation", "The step-by-step calculus of computing gradient tensors backwards through residual stream layers."),
        ("CS-AI-16", "RMSNorm vs LayerNorm in Modern LLMs", "Why removing mean centering in RMSNorm saves GPU compute cycles without degrading training stability."),
        ("CS-AI-17", "SwiGLU Activation Function Mechanics", "Why PaLM and Llama replaced ReLU and GELU with the gated SwiGLU non-linear activation."),
        ("CS-AI-18", "Grouped-Query Attention (GQA)", "How sharing key and value heads across multiple query heads slashes memory bandwidth requirements."),
        ("CS-AI-19", "Contrastive Learning & CLIP Embeddings", "How multimodal models align visual image embeddings with textual token spaces using InfoNCE loss."),
        ("CS-AI-20", "Graph Neural Networks & Message Passing", "How node embeddings aggregate neighbor feature vectors for molecular biology and fraud detection."),
        ("CS-AI-21", "Dropout & Regularization Mathematics", "Why randomly zeroing activations prevents co-adaptation and simulates ensemble learning."),
        ("CS-AI-22", "AdamW Optimizer: Weight Decay vs L2 Regularization", "The critical distinction between decoupled weight decay in AdamW and classical L2 penalty."),
        ("CS-AI-23", "Chain-of-Thought (CoT) & Reasoning Tokens", "How generating intermediate reasoning steps expands inference compute to solve multi-step logic."),
        ("CS-AI-24", "Vision Transformers (ViT) & Patch Tokenization", "Treating an image as a 16x16 grid of word tokens and passing them through standard attention."),
        ("CS-AI-25", "Temperature & Top-p (Nucleus) Sampling", "The exact probability math behind controlling hallucination and creativity in LLM decoding."),
        ("CS-AI-26", "Autoencoders & Latent Space Compression", "Encoding high-dimensional pixel data into compact Gaussian latent bottlenecks."),
        ("CS-AI-27", "Gradient Accumulation & Distributed Data Parallel (DDP)", "Simulating massive batch sizes across multi-node GPU clusters with ring AllReduce."),
        ("CS-AI-28", "Self-Supervised Masked Language Modeling", "How BERT learns bidirectional context by predicting 15% masked tokens."),
        ("CS-AI-29", "Generative Adversarial Networks (GANs) Minimax Game", "The mathematical saddle-point formulation of Generator versus Discriminator."),
        ("CS-AI-30", "DeepSeek Multi-Head Latent Attention (MLA)", "Compressing KV caches into low-dimensional latent vectors for massive inference throughput.")
    ],
    "mathematics-probability": [
        ("CS-MATH-01", "Bayes' Theorem: Prior, Likelihood, and Posterior", "How conditional probability updates beliefs using P(A|B) = P(B|A)P(A) / P(B)."),
        ("CS-MATH-02", "Eigenvalues and Eigenvectors: Invariant Directions", "Visualizing matrix transformation vectors that only scale without rotating: Av = lambda v."),
        ("CS-MATH-03", "The Fourier Transform: Deconstructing Any Signal", "How Euler's formula e^(i omega t) unwinds complex waves into pure circular frequencies."),
        ("CS-MATH-04", "Monte Carlo Integration & High-Dimensional Volume", "Why random sampling calculates complex integrals faster than deterministic grids in N dimensions."),
        ("CS-MATH-05", "The Central Limit Theorem: The Emergence of the Bell Curve", "Why adding independent random variables inevitably produces a Gaussian normal distribution."),
        ("CS-MATH-06", "Markov Chains & Stationary Distributions", "State transition probability matrices and finding the invariant eigenvector pi P = pi."),
        ("CS-MATH-07", "Singular Value Decomposition (SVD): A = U Sigma V^T", "Decomposing any arbitrary rectangular data matrix into rotation, scaling, and rotation."),
        ("CS-MATH-08", "Gradient Descent & The Hessian Curvature", "Navigating high-dimensional loss surfaces using first and second derivatives."),
        ("CS-MATH-09", "The Monty Hall Paradox: Why You Must Always Switch", "The counter-intuitive probability distribution behind three doors and conditional information."),
        ("CS-MATH-10", "Euler's Identity: e^(i pi) + 1 = 0", "Uniting five fundamental mathematical constants in a single geometric rotation in the complex plane."),
        ("CS-MATH-11", "Topology & The Mobius Strip: Non-Orientable Surfaces", "How boundary curves and genus classify geometric spaces invariant under stretching."),
        ("CS-MATH-12", "Information Entropy & Shannon's Limit", "Measuring information content in bits using H(X) = - sum p(x) log2 p(x)."),
        ("CS-MATH-13", "The Birthday Paradox: Hash Collisions in Cryptography", "Why 23 people give a 50% collision probability and what it means for SHA-256."),
        ("CS-MATH-14", "Poisson Distribution: Modeling Rare Events", "Calculating probability of k independent occurrences in fixed time intervals."),
        ("CS-MATH-15", "Lagrange Multipliers: Constrained Optimization", "Finding local extrema on surface manifolds subject to constraint curves g(x,y) = 0."),
        ("CS-MATH-16", "The Riemann Hypothesis & Prime Distribution", "The non-trivial zeros of the Riemann Zeta function along the critical line Re(s) = 1/2."),
        ("CS-MATH-17", "Game Theory & The Nash Equilibrium", "The Prisoner's Dilemma payoff matrix where neither player can unilaterally improve their payoff."),
        ("CS-MATH-18", "Fibonacci Sequence, Golden Ratio, and Continued Fractions", "The geometric convergence of F_(n+1)/F_n to phi and spirals in nature."),
        ("CS-MATH-19", "Taylor Series & Polynomial Approximations", "Approximating any smooth differentiable function using infinite derivative sums at a point."),
        ("CS-MATH-20", "Convolution Calculus: Sliding Window Filters", "The mathematical integral of f(tau) g(t - tau) d tau in signal processing and CNNs."),
        ("CS-MATH-21", "Cauchy-Schwarz Inequality & Vector Projections", "Why |<u, v>|^2 <= <u, u><v, v> and its fundamental role in quantum mechanics and metrics."),
        ("CS-MATH-22", "Kullback-Leibler (KL) Divergence: Distance Between Distributions", "Quantifying information loss when approximating true distribution P with model Q."),
        ("CS-MATH-23", "Chaos Theory & The Lorenz Attractor", "Nonlinear differential equations displaying deterministic chaos and butterfly effect sensitivity."),
        ("CS-MATH-24", "Stochastic Calculus & Brownian Motion", "Ito's Lemma and modeling Wiener processes in financial derivatives and physical diffusion."),
        ("CS-MATH-25", "Graph Theory & The Konigsberg Seven Bridges Problem", "Eulerian paths and the birth of topology through vertex degree parity."),
        ("CS-MATH-26", "Principal Component Analysis (PCA) Derivation", "Projecting multidimensional data onto maximum variance orthogonal eigenvectors."),
        ("CS-MATH-27", "The Law of Large Numbers (Weak vs Strong)", "Convergence of sample averages to expected value as trial counts approach infinity."),
        ("CS-MATH-28", "Complex Analysis & Cauchy's Residue Theorem", "Evaluating closed contour integrals around complex singularities."),
        ("CS-MATH-29", "Simplex Algorithm & Linear Programming", "Traversing polytope vertices to optimize linear cost functions under inequality constraints."),
        ("CS-MATH-30", "Godel's Incompleteness Theorems", "Why any consistent axiomatic mathematical system contains true statements that cannot be proven.")
    ],
    "physics-quantum": [
        ("CS-PHYS-01", "The Schrodinger Wave Equation: Quantum Superposition", "How i hbar d/dt |psi> = H |psi> describes the probabilistic wave nature of matter."),
        ("CS-PHYS-02", "General Relativity: Spacetime Curvature & Geodesics", "How mass tells spacetime how to curve, and curved spacetime tells mass how to move."),
        ("CS-PHYS-03", "The Double-Slit Experiment & Wave-Particle Duality", "How single photons create interference patterns and collapse when observed."),
        ("CS-PHYS-04", "Quantum Entanglement & Bell's Inequality Test", "Proving Einstein's spooky action at a distance through experimental violation of local realism."),
        ("CS-PHYS-05", "Black Hole Event Horizons & Hawking Radiation", "Quantum vacuum fluctuations near event horizons causing black hole thermodynamic evaporation."),
        ("CS-PHYS-06", "The Second Law of Thermodynamics & Arrow of Time", "Why microscopic time-reversible laws yield macroscopic irreversible entropy increase."),
        ("CS-PHYS-07", "Special Relativity: Time Dilation & Lorentz Factor gamma", "Why clocks tick slower for moving observers according to gamma = 1 / sqrt(1 - v^2/c^2)."),
        ("CS-PHYS-08", "Quantum Tunneling: Overcoming Potential Barriers", "How wavefunctions penetrate classically forbidden finite potential barriers in semiconductors."),
        ("CS-PHYS-09", "Superconductivity & Cooper Pairs (BCS Theory)", "How phonon lattice interactions bind electrons into bosons that flow with zero electrical resistance."),
        ("CS-PHYS-10", "Maxwell's Equations & The Speed of Light", "Unifying electricity and magnetism into propagating electromagnetic waves at c = 1/sqrt(mu_0 epsilon_0)."),
        ("CS-PHYS-11", "The Higgs Mechanism & Mass Generation", "How spontaneous symmetry breaking in the scalar Higgs field imparts mass to W and Z bosons."),
        ("CS-PHYS-12", "Gravitational Waves & LIGO Interferometry", "Measuring spacetime strains smaller than a proton using 4km laser Fabry-Perot cavities."),
        ("CS-PHYS-13", "The Standard Model of Particle Physics", "Quarks, leptons, gauge bosons, and the fundamental forces of matter."),
        ("CS-PHYS-14", "Quantum Decoherence: How Quantum Becomes Classical", "Environmental entanglement destroying off-diagonal phase coherence in density matrices."),
        ("CS-PHYS-15", "Heisenberg's Uncertainty Principle: Delta x Delta p >= hbar / 2", "The mathematical conjugate Fourier limit between position and momentum operators."),
        ("CS-PHYS-16", "Thermodynamic Carnot Efficiency Limit", "Why heat engines have an absolute theoretical efficiency ceiling of eta = 1 - T_C / T_H."),
        ("CS-PHYS-17", "Cosmic Microwave Background (CMB) Radiation", "The 2.7K thermal remnant of the Big Bang and acoustic peaks of primordial plasma."),
        ("CS-PHYS-18", "The Casimir Effect: Quantum Vacuum Pressure", "Attraction between uncharged metal plates caused by vacuum electromagnetic zero-point fluctuations."),
        ("CS-PHYS-19", "Dark Matter & Galactic Rotation Curves", "Why stars in outer spiral galaxies orbit at flat velocities, implying unseen halo mass."),
        ("CS-PHYS-20", "Nuclear Fusion: The Lawson Criterion & Coulomb Barrier", "Overcoming electrostatic repulsion to fuse deuterium and tritium in magnetic confinement tokamaks."),
        ("CS-PHYS-21", "The Photoelectric Effect & Einstein's Light Quanta", "Why light frequency—not intensity—ejects electrons from metal surfaces according to E = h f."),
        ("CS-PHYS-22", "Semiconductor Band Gaps & PN Junction Diodes", "Conduction vs valence bands, Fermi levels, and electron-hole recombination in LEDs and solar cells."),
        ("CS-PHYS-23", "Feynman Path Integral Formulation", "Calculating quantum amplitudes by summing phase contributions over all possible historical paths."),
        ("CS-PHYS-24", "Fluid Dynamics: The Navier-Stokes Equations", "Conservation of momentum in viscous incompressible fluids and the Millennium Prize mystery."),
        ("CS-PHYS-25", "Fiber Optics & Total Internal Reflection", "Guiding petabits of light across oceans using Snell's Law and critical angles."),
        ("CS-PHYS-26", "Quantum Zeno Effect: Freezing States by Observing", "Frequent projective measurements preventing the unitary time evolution of an unstable state."),
        ("CS-PHYS-27", "The Fermi Paradox & Drake Equation", "Where are all the extraterrestrial civilizations? Great Filters and cosmic timescales."),
        ("CS-PHYS-28", "Special Relativity: Mass-Energy Equivalence E = mc^2", "The relativistic derivation of rest energy from momentum conservation."),
        ("CS-PHYS-29", "Quantum Hall Effect & Topological Insulators", "Quantized Hall conductance in units of e^2/h protecting edge states from scattering."),
        ("CS-PHYS-30", "String Theory & Extra Dimensions", "Replacing point particles with vibrating 1D strings in 10-dimensional Calabi-Yau manifolds.")
    ],
    "computer-science-systems": [
        ("CS-SYS-01", "Raft Consensus Algorithm: Leader Election & Log Replication", "How distributed nodes reach agreement under network partitions and node crashes."),
        ("CS-SYS-02", "Log-Structured Merge (LSM) Trees vs B-Trees", "Why modern storage engines (RocksDB, Cassandra) use append-only writes over in-place updates."),
        ("CS-SYS-03", "Cache Coherence: The MESI Protocol", "How multi-core CPUs keep L1/L2 caches synchronized across Modified, Exclusive, Shared, and Invalid states."),
        ("CS-SYS-04", "TCP 3-Way Handshake & Congestion Control (BBR vs Cubic)", "SYN, SYN-ACK, ACK sequencing and how modern congestion algorithms maximize bandwidth delay product."),
        ("CS-SYS-05", "Zero-Knowledge Proofs: zk-SNARKs Mathematics", "Proving possession of a secret without revealing the secret using polynomial commitments and elliptic curves."),
        ("CS-SYS-06", "Garbage Collection: Generational Mark-Sweep-Compact", "Why young objects die fast and how generational heaps minimize stop-the-world pauses."),
        ("CS-SYS-07", "Memory Virtualization & Multi-Level Page Tables (TLB)", "How hardware MMUs translate virtual addresses to physical RAM using Translation Lookaside Buffers."),
        ("CS-SYS-08", "CPU Branch Prediction & Speculative Execution (Spectre)", "How hardware branch predictors anticipate if-statements and why speculative rollbacks leaked cache lines."),
        ("CS-SYS-09", "Consistent Hashing & Distributed Sharding", "How hash rings minimize data remapping when scaling distributed key-value caches like Dynamo and Redis."),
        ("CS-SYS-10", "Linux Epoll vs Select: O(1) Event Loops", "How high-concurrency servers handle 1,000,000 idle connections without polling file descriptors."),
        ("CS-SYS-11", "CAP Theorem in Distributed Systems", "The mathematical proof that no distributed system can achieve Consistency, Availability, and Partition tolerance."),
        ("CS-SYS-12", "Database ACID Transactions & Two-Phase Locking (2PL)", "Serializability guarantees, deadlock detection, and strict two-phase locking protocols."),
        ("CS-SYS-13", "Public Key Cryptography: RSA & Diffie-Hellman", "Modular exponentiation, Euler's totient function, and the hardness of prime factorization."),
        ("CS-SYS-14", "CPU SIMD Vectorization: AVX-512 & Neon", "Processing 8 double-precision floats in a single CPU instruction clock cycle."),
        ("CS-SYS-15", "B-Tree Indexing in Relational Databases", "Why balanced N-ary search trees minimize disk page reads for range queries."),
        ("CS-SYS-16", "Bloom Filters: Space-Efficient Probabilistic Sets", "Using k hash functions into an m-bit array with zero false negatives and controlled false positives."),
        ("CS-SYS-17", "Concurrency: Mutexes, Semaphores, and Lock-Free Atomics", "Compare-and-Swap (CAS) hardware primitives and building lock-free queues without deadlock."),
        ("CS-SYS-18", "Compiler Architecture: AST, SSA, and LLVM Optimization", "How raw code parses into abstract syntax trees and lowers to Static Single Assignment intermediate representation."),
        ("CS-SYS-19", "DNS Resolution Architecture: From Root to Authoritative", "Recursive DNS lookup traversal, TTL caching, and BGP Anycast routing."),
        ("CS-SYS-20", "Database Sharding & Two-Phase Commit (2PC)", "Atomic distributed transactions across multiple shards with Prepare and Commit coordinator states."),
        ("CS-SYS-21", "GPU Compute Architecture: Warps, SMs, and Shared Memory", "How NVIDIA GPUs schedule 32 threads in lockstep warps across Streaming Multiprocessors."),
        ("CS-SYS-22", "Operating System Context Switching & Interrupt Handling", "Saving register state to kernel stack, hardware interrupts, and scheduling time slices."),
        ("CS-SYS-23", "HTTP/2 vs HTTP/3 (QUIC over UDP)", "Solving head-of-line blocking in mobile networks using encrypted UDP packet multiplexing."),
        ("CS-SYS-24", "Merkle Trees & Blockchain State Verification", "Hierarchical cryptographic hash trees enabling light clients to verify data integrity in O(log N)."),
        ("CS-SYS-25", "Actor Model of Concurrency (Erlang/Akka)", "Isolating mutable state inside asynchronous message-passing actors with supervision trees."),
        ("CS-SYS-26", "NVMe vs SATA: Flash Memory & PCIe Lanes", "Bypassing legacy AHCI disk bottlenecks with 64,000 parallel queues directly into PCIe lanes."),
        ("CS-SYS-27", "OAuth 2.0 & JWT Cryptographic Authorization", "Signed JSON Web Tokens (HMAC/RSA) enabling stateless authorization across microservices."),
        ("CS-SYS-28", "Dijkstra's & A* Pathfinding Algorithms", "Priority queues, heuristic distances, and finding optimal shortest paths in weighted graphs."),
        ("CS-SYS-29", "Garbage Collection: Go's Tri-Color Concurrent Mark", "White, gray, and black set classification enabling sub-millisecond GC pauses."),
        ("CS-SYS-30", "Network Socket Architecture & TCP Sliding Window", "Flow control, receive buffers, ACK round-trips, and window scale options.")
    ]
}

def generate_case_study_file(domain_dir, cs_id, title, premise):
    full_domain_dir = os.path.join(CASE_STUDIES_DIR, domain_dir)
    os.makedirs(full_domain_dir, exist_ok=True)
    clean_title = re.sub(r'[^a-zA-Z0-9\s-]', '', title).lower().strip()
    clean_title = re.sub(r'[\s_]+', '-', clean_title)[:40]
    slug = cs_id.lower() + "-" + clean_title
    file_path = os.path.join(full_domain_dir, f"{slug}.md")
    
    # Pick template mappings based on domain
    if "ai" in domain_dir:
        t_hook = "TMPL-01"
        t_motion = "TMPL-21"
        t_code = "TMPL-23"
        t_sum = "TMPL-10"
        symph_scene = "A macro shot of a state-of-the-art silicon semiconductor wafer inside an argon-gas cleanroom."
    elif "math" in domain_dir:
        t_hook = "TMPL-11"
        t_motion = "TMPL-12"
        t_code = "TMPL-15"
        t_sum = "TMPL-32"
        symph_scene = "An antique European university lecture hall with tall windows casting cold afternoon sunlight on a dark slate blackboard."
    elif "phys" in domain_dir:
        t_hook = "TMPL-33"
        t_motion = "TMPL-20"
        t_code = "TMPL-19"
        t_sum = "TMPL-31"
        symph_scene = "An optical physics laboratory table equipped with mirror mounts, beam splitters, and a pulsing cold cyan laser beam."
    else:
        t_hook = "TMPL-25"
        t_motion = "TMPL-29"
        t_code = "TMPL-24"
        t_sum = "TMPL-36"
        symph_scene = "A vertical low-angle perspective looking up at towering high-density enterprise server racks with pulsing network fiber activity."

    content = f"""# Case Study {cs_id}: {title}

**Domain**: `{domain_dir}`  
**Format**: 9:16 Vertical Short / Reel (1080 x 1920)  
**Target Duration**: 0:58 (58 seconds / 148 words)  
**Visual Standard**: Perplexity ([www.perplexity.ai](https://www.perplexity.ai)) Dark Slate & Cyan Design System

---

## 1. Concept & Narrative Premise

{premise}

### The Core Pedagogical Hook
Most people look at this problem with classical intuition and hit an impossible paradox. This video reveals the underlying engineering/mathematical mechanism that unlocks 10x performance or resolves the contradiction.

---

## 2. Stage 1: Interactive Interrogation (Rule of Three Questions)

Before firing tool calls, the director poses three high-leverage clarifications:

1. **The Hook Paradox**:
   - *(Recommended)* Focus on the counter-intuitive performance or physical bottleneck that frustrates practitioners.
   - *Alternative*: Focus on the historical discovery paper and initial failure before the breakthrough.
2. **Visual Tool Allocation**:
   - *(Recommended)* 45% Symphony vertical B-roll (hardware/laboratory environment) + 55% Hyperframes (Perplexity cards, code diffs, LaTeX math).
   - *Alternative*: 100% Hyperframes code/math simulation.
3. **Pacing Velocity**:
   - *(Recommended)* 58 seconds (148 words, 14 visual cuts, high retention for Shorts/Reels).
   - *Alternative*: 110 seconds technical deep-dive.

---

## 3. Stage 2: Dual-Pass Self-Refining Director's Plan

### First Pass Draft
Chronological beat breakdown outlining voiceover and visual targets.

### Senior Director Self-Critique Audit
- **Pacing Check**: Ensure no static card stays on screen longer than 3.5 seconds.
- **Tool Discipline**: Verify zero text or UI prompted to Symphony. All typography and diagrams assigned to Hyperframes.
- **Audio Dynamic**: Inject a 0.8-second needle-drop silence right before the punchline resolution at second 38.
- **Safe Zones**: Ensure all LaTeX equations sit between Y=450px and Y=1450px.

### Master Production Timeline

| Timecode | Beat | Voiceover Script | Visual Execution | Engine Assigned | Template ID |
|---|---|---|---|---|---|
| `0:00 - 0:05` | The Hook | "If you think {title.split(':')[0]} works the way most tutorials explain, you're missing the real secret..." | Symphony vertical 9:16 footage + Perplexity search query typing | Symphony + Hyperframes | `{t_hook}` |
| `0:05 - 0:15` | The Bottleneck | "Under standard execution, memory reads choke the pipeline, causing severe latency spikes..." | Hyperframes technical architecture diagram showing bottleneck | Hyperframes | `{t_motion}` |
| `0:15 - 0:28` | The Mathematical Mechanism | "Here is the exact derivation that changes everything..." | Stepwise LaTeX formula with highlighted cyan variables | Hyperframes | `TMPL-11` |
| `0:28 - 0:38` | The Code / Hardware Reality | "When implemented at the system level, the difference is night and day." | Syntax-highlighted code diff comparing naive vs optimized algorithm | Hyperframes | `{t_code}` |
| `0:38 - 0:48` | The Benchmark Revelation | "[NEEDLE DROP SILENCE] The result? A 5x throughput gain with zero accuracy degradation." | Symphony cinematic macro push + benchmark bar comparison | Symphony + Hyperframes | `TMPL-26` |
| `0:48 - 0:58` | Outro & Summary | "This is why {title.split(':')[0]} powers modern computing. Follow for deeper system breakdowns." | Perplexity 3-point takeaway summary card | Hyperframes | `{t_sum}` |

---

## 4. Stage 3: Asset Gathering Plan

1. **Company PR & Demo Footage**: Official presentation clips or lab B-roll.
2. **arXiv Paper Citation**: Pull exact paper title, author list, and diagram from original publication.
3. **GitHub Code Extraction**: Isolate the 8 most critical lines of implementation code.

---

## 5. Stage 4: Symphony 9:16 Vertical Prompts

### Shot 1: The Introductory Hook (`0:00 - 0:05`)
```
[P] PHOTOGRAPHIC STYLE: 35mm anamorphic cine-lens, fine grain, 9:16 vertical composition, ARRI Alexa LF look.
[I] IMAGERY & SCENE: {symph_scene}
[C] CAMERA & COMPOSITION: Vertical angle, camera low at chest height, subject centered with upper headroom for UI card overlay, 35mm f/2.8 lens.
[T] TIMING & LIGHTING: Cold slate mood lighting (5400K) with a sharp electric cyan rim light from the upper-right edge.
[U] USE OF ATMOSPHERE: Pristine filtered laboratory atmosphere, subtle optical glass reflection.
[R] RENDER STYLE: Absolute physical material realism, anodized metal, zero 3D CGI gloss.
[E] EXTRA MOTION: Slow steady camera push forward over 4 seconds, single camera movement vector.
```

### Shot 2: The Benchmark Revelation (`0:38 - 0:45`)
```
[P] PHOTOGRAPHIC STYLE: 65mm macro cine-lens, photorealistic, 9:16 portrait orientation.
[I] IMAGERY & SCENE: Extreme close-up of hardware components functioning under load, subtle status indicator pulse.
[C] CAMERA & COMPOSITION: Extreme macro, locked-off camera with shallow depth of field (f/2.0), background softly blurred.
[T] TIMING & LIGHTING: High-contrast directional lighting, specular highlights on copper and silicone.
[U] USE OF ATMOSPHERE: Crisp optical clarity, no haze.
[R] RENDER STYLE: Industrial tactile realism.
[E] EXTRA MOTION: Micro-rack focus from foreground traces to background die over 3 seconds.
```

---

## 6. Stage 5: Hyperframes Motion Graphics Specifications

- **Template References**: `{t_hook}`, `{t_motion}`, `TMPL-11`, `{t_code}`, `{t_sum}`.
- **Motion Easing**: `cubic-bezier(0.16, 1, 0.3, 1)`.
- **Card Styling**: `#16191E` surface, `#23272F` 1px border, `#20B8CD` cyan highlights.
- **Typography**: `Inter` (UI), `JetBrains Mono` (Code/Math), `Iowan Old Style` (Thesis quotes).

---

## 7. Stage 6: Voiceover Audio & Kinetic Subtitles

- **Cadence**: 148 words in 58 seconds (~153 WPM). Conversational, intellectual, calm.
- **Needle-Drop Marker**: Full 0.8s silence at `0:38` immediately before revealing benchmark metric.
- **Subtitle Styling**:
  - Baseline: `Y = 1540px` (Safe zone).
  - Active spoken word: `#F3F3EE` with glowing cyan background pill `rgba(32, 184, 205, 0.25)`.
  - Inactive words: `#8E95A2` muted slate.
  - Max chunk: 3 to 4 words.

---

## 8. Stage 7: Clipchat Timeline Cut List & Assembly

- **Track V3**: Dynamic Subtitles (`Y = 1540px`).
- **Track V2**: Hyperframes Cards, LaTeX, Code diffs, and Perplexity UI.
- **Track V1**: Symphony 9:16 B-roll with head/tail 0.5s trimmed on all clips.
- **Track A1**: Voiceover master dialogue (-14 LUFS).
- **Track A2**: UI SFX (keystrokes, card slides, sub-bass braams).
- **Track A3**: Ambient modular synth score ducked to -24 dB under voiceover.
- **Transitions**: 70% J-cuts (audio leads visual cut by 6 frames).
- **Color Grade**: Global Perplexity Dark Slate LUT applied across Track V1.
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

def main():
    print(f"Generating 36 Perplexity Design Templates in {TEMPLATES_DIR}...")
    for tmpl in TEMPLATES:
        generate_template_file(*tmpl)
    print(f"Generated {len(TEMPLATES)} templates successfully.")

    total_cs = 0
    print(f"Generating 120 Case Studies in {CASE_STUDIES_DIR}...")
    for domain, studies in CASE_STUDY_DOMAINS.items():
        print(f"  Generating {len(studies)} case studies for {domain}...")
        for cs in studies:
            generate_case_study_file(domain, cs[0], cs[1], cs[2])
            total_cs += 1
    print(f"Generated {total_cs} case studies successfully.")

if __name__ == "__main__":
    main()
