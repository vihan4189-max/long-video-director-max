---
name: "03-symphony-vertical-generation"
description: "Mastery guide for Symphony AI image and video asset generation. Enforces strict vertical (9:16) composition, single-movement camera physics, the PICTURE-916 prompting formula, and artifact prevention for scientific and STEM B-roll."
---

# Sub-Skill: Symphony Vertical (9:16) Asset Generation

> [!CAUTION]
> **CRITICAL ARCHITECTURAL CONSTRAINT: Symphony generates ONLY vertical (9:16 / 1080x1920) assets.**
> Do not request horizontal (16:9) framing, panoramic pans, or ultrawide aspect ratios from Symphony. Every visual must be conceptualized, framed, and rendered in vertical orientation.

Symphony is your primary generation engine for cinematic, photorealistic, and physical B-roll. It is used for real-world scientific equipment, semiconductor cleanrooms, quantum dilution refrigerators, optical laser benches, astrophysics phenomena, and dramatic metaphorical visual hooks.

---

## 1. The Symphony Prompting Architecture (PICTURE-916 Formula)

Every prompt passed to Symphony must follow the 7-block PICTURE-916 formula. Do not write freeform poetic prose; diffusion models require concrete, physical camera and lighting instructions.

```
[P] PHOTOGRAPHIC STYLE: 
    35mm anamorphic cine-lens, ARRI Alexa 65 sensor, photochemical film emulation, fine high-latitude grain, 9:16 vertical composition.
[I] IMAGERY & SCENE: 
    A state-of-the-art silicon wafer fabrication cleanroom. A robotic vacuum arm with an orange anodized end-effector lifts a 300mm patterned silicon wafer.
[C] CAMERA & COMPOSITION: 
    Vertical portrait angle, camera positioned at chest height looking down at 15 degrees. Subject centered vertically with 25% upper headroom for overlay cards. 35mm prime lens, f/2.8 aperture.
[T] TIMING & LIGHTING: 
    Cold laboratory lighting (5600K) from recessed ceiling LED panels, accented by hard electric cyan rim light along the edge of the robotic arm. Deep crisp shadows.
[U] USE OF ATMOSPHERE: 
    Pristine filtered cleanroom air, subtle optical lens flare off the mirror finish of the silicon disc.
[R] RENDER STYLE: 
    Hyper-realistic, tactile industrial textures, brushed stainless steel, copper cabling, absolute physical realism, zero cartoon/3D render gloss.
[E] EXTRA MOTION / PERFORMANCE: 
    Camera executes a single smooth push forward along the Z-axis over 4 seconds. The robotic arm raises the wafer smoothly by 10 centimeters without shaking.
```

---

## 2. The Five Golden Rules of Vertical Symphony Generation

### Rule 1: Never Ask Symphony for Text, Math, or UI
AI video models hallucinate symbols, generating gibberish letters and melted numbers.
- **Wrong**: `A blackboard with the Schrödinger equation written on it.` (Produces illegible scrawl).
- **Right (Symphony)**: `A theoretical physicist in a tweed jacket holding chalk, viewed from behind, standing before a towering dark slate blackboard covered in white chalk dust. 35mm lens, atmospheric dust motes.`
- **Right (Hyperframes)**: Overlay the actual, crisp LaTeX Schrödinger equation on top of the Symphony clip in the Clipchat assembly stage.

### Rule 2: One Camera Movement Per Generation
Compounding movements (e.g. pan left while zooming in while rotating) destroy diffusion stability and cause severe rubbery morphing.
Choose **one** movement:
- `slow dolly push in along central axis` (for tension and focus)
- `steady lateral tracking shot past foreground cables` (for parallax depth)
- `slow vertical pedestal down along the towering server rack` (for vertical scale)
- `locked-off macro shot with micro depth-of-field drift` (for precision hardware)

### Rule 3: The 3-Second Rule (Generate Longer Than Needed)
Video diffusion models suffer from "start-frame shock" and "end-frame drift" (where limbs or edges warp in the first and last 10–15 frames).
- If your timeline beat requires a **2.5-second clip**, generate a **5.0-second clip**.
- In Clipchat, trim the first 0.5s and the last 1.0s, using only the rock-solid middle 2.5s. This habit single-handedly eliminates 90% of visible AI artifacts.

### Rule 4: Compose for the Golden Vertical Safe Zones
Keep the hero subject inside the **Hero Action Zone** (`Y: 450px – 1450px`).
- Leave the top 250px clear of critical detail so Hyperframes topic badges or search bars can sit cleanly.
- Leave the bottom 350px clear of essential action so subtitles and mobile app UI don't block the visual.

### Rule 5: Maintain Visual Continuity (The Seed & Lighting Anchor)
When producing multiple Symphony clips for the same video:
- Reuse the exact same `[P]` (Photographic Style) and `[T]` (Timing & Lighting) blocks across every prompt in that scene.
- Keep the color temperature (e.g. `5600K slate cool with 480nm cyan accent`) identical so the shots cut together seamlessly without jarring color shifts.

---

## 3. Symphony Shot Catalog for STEM Explainer Videos

| Shot Archetype | Recommended Focal Length | Camera Move | Target Use Case |
|---|---|---|---|
| **The Quantum / Optics Bench** | 100mm Macro f/2.8 | Locked-off or micro-drift | Quantum computing, laser optics, photonics |
| **The Server Cluster / Supercomputer** | 24mm Wide Cine | Vertical pedestal down | AI training, GPU clusters, distributed systems |
| **The Silicon Micro-Architecture** | 65mm Close-Up | Slow push forward | Chip design, Blackwell, photolithography |
| **The Deep Ocean / Spacetime Metaphor** | 35mm Anamorphic | Steady lateral track | Relativity, gravitational waves, fluid dynamics |
| **The Academic Archive / Library** | 50mm Prime f/2.0 | Slow dolly push | Historical math proofs, Turing/Shannon papers |

---

## 4. Symphony Acceptance Checklist

Before approving any generated clip for the Clipchat timeline:
- [ ] Aspect ratio is strictly 9:16 vertical (1080 x 1920)
- [ ] No deformed hands, extra fingers, or rubbery shifting geometry
- [ ] No hallucinated text or garbled pseudo-writing on screens or walls
- [ ] Only one steady camera movement occurred
- [ ] Hero subject is framed within safe zones (upper two-thirds)
- [ ] Minimum 1.0s of clean footage available to trim on both head and tail
- [ ] Lighting color temperature matches adjacent shots in the director's plan
