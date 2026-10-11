# Camera, Lens, and Cinematic Motion Reference for STEM Videos

This reference provides camera positions, focal lengths, lighting styles, and physical movements tailored for **vertical (9:16) scientific, mathematical, and computational video direction**.

---

## 1. Emotion & Pedagogical Purpose to Lens & Angle Matrix

In scientific storytelling, camera angle communicates rigor, revelation, or scale:

| Pedagogical Goal | Camera Angle | Lens (Focal Length) | Camera Movement | Symphony Keyword Prompt |
|---|---|---|---|---|
| **Monumental Discovery** | Low Angle (20° tilt up) | 24mm – 35mm Cine Wide | Slow Push-In on Dolly | `low-angle perspective, towering vertical scale, slow dolly push toward subject` |
| **Microscopic / Quantum Precision** | Eye-Level Extreme Macro | 100mm Macro Cine f/2.8 | Locked-Off or Micro-Drift | `shallow depth of field, 100mm macro lens, locked-off camera, optical flare` |
| **Theoretical Abstraction** | High Angle / Overhead | 50mm Normal Lens | Slow Top-Down Descend | `overhead architectural perspective, clean geometry, smooth vertical descent` |
| **Complex System / Network Scale** | Eye-Level Wide | 28mm Anamorphic | Lateral Track past Foreground | `cinematic lateral tracking shot, rich foreground parallax, deep depth planes` |
| **Crucial Pivot / Insight Revelation** | Medium Close-Up | 85mm Portrait f/1.8 | Slow Push-In with Focus Rack | `rack focus from background to foreground, 85mm prime lens, tight tension` |

---

## 2. Vertical Composition Rules for Lenses

### The 35mm Sweet Spot for Vertical STEM Shots
In a 9:16 frame, 35mm yields natural human perspective without fish-eye edge distortion. It provides enough vertical headroom to capture a scientist at a blackboard, a silicon wafer robotic arm, or a quantum dilution refrigerator while maintaining background context.

### The Macro 100mm for Hardware & Physics
When illustrating silicon microchips, GPU die architecture, laser mirrors, or fiber optic reflections, a 100mm macro lens creates exquisite creamy bokeh (`f/2.8`), separating the subject from distractions and allowing Hyperframes text/cards to float legibly in the soft background.

---

## 3. Lighting Setups for Academic Luxury

To eliminate the "cheap 3D render" or "stock photo" look:

1. **Edge / Rim Lighting (The Key to Separation)**:
   Always prompt for a crisp rim light along the edge of glass, metal, or machinery. This separates black/slate equipment from the dark canvas.
   - *Prompt block*: `hard rim light from top-left, edge separation on dark metal surfaces, deep shadows`
2. **Volumetric Atmosphere (Visible Light Paths)**:
   In optics, lasers, or lecture halls, subtle atmospheric dust or haze renders light beams visible as physical structures.
   - *Prompt block*: `subtle atmospheric haze catching cold cyan volumetric light beams, photochemical grain`
3. **Monochromatic Restraint with Cyan Punctuation**:
   Keep 85% of the frame in cool neutral slates (`5000K – 5600K`), with warm tungsten or electric cyan (`480nm`) highlighting the precise experimental reaction.
   - *Prompt block*: `cool slate color grading, muted neutral industrial tones with sharp electric cyan laser accent`

---

## 4. Camera Movements (One Movement Per Generation)

Video diffusion models fail when tasked with complex compounding movements (e.g. pan + tilt + zoom + spin). **Commit to one single physical camera move per clip**:

- **Slow Dolly Push**: Builds forward momentum and focus. Use for introductory hooks and pivotal conclusions.
- **Lateral Slide (Trucking)**: Slides past foreground objects (laboratory glass, oscilloscope cables) to create rich parallax depth.
- **Top-Down Pedestal Down**: Moves down vertically along towering server racks or long chalkboard equations.
- **Locked-Off Macro**: Zero camera movement; only the internal physical phenomenon moves (fluids flowing, laser pulsing, electrons ionizing).

---

## 5. PICTURE-916 Prompt Formula for Symphony

Every Symphony vertical prompt must follow this 7-part structure:

```
[P] PHOTOGRAPHIC STYLE: 35mm anamorphic photochemical film, fine large-format grain, ARRI Alexa LF look, 9:16 vertical framing
[I] IMAGERY & SCENE: [Detailed physical description of laboratory, server, hardware, or nature]
[C] CAMERA & COMPOSITION: Vertical portrait orientation, camera low at chest height, subject centered in upper two-thirds, 35mm lens at f/2.8
[T] TIMING & LIGHTING: High-contrast directional lighting from high right, deep moody shadows, cold volumetric light
[U] USE OF ATMOSPHERE: Faint dust motes, subtle air haze, clean optical glass reflections
[R] RENDER FINISH: Photorealistic, physical material realism, brushed anodized aluminum, micro-scratches, no 3D cartoon CGI
[E] EXTRA MOTION: Slow steady camera push forward over 4 seconds, single camera vector
```
