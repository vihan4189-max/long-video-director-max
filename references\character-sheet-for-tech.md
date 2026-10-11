# Character Consistency & Model Sheets for STEM Creators

Inspired by `01 SKILLS/character-sheet`, this reference adapts the geometric anti-drift methodology for scientific and technical video productions.

Whether featuring historical scientific titans (Alan Turing, Albert Einstein, Claude Shannon, Ada Lovelace, Richard Feynman) or maintaining a consistent synthetic host/researcher across dozens of videos, you must lock **facial geometry**, not vague impressions.

---

## 1. Why Adjectives Fail in AI Video Generation

Prompts like `young brilliant male researcher in lab coat, focused expression, cinematic 2026 look` describe a category, not an individual. The diffusion model samples a completely different face on every generation.

The only fix is to replace descriptive adjectives with **immutable geometric measurements** and anchor them with a **Multi-View Character Reference Sheet**.

---

## 2. The 10-Point Facial Geometry Protocol

For any recurring figure (historical or original), compile this exact measurement ledger:

1. **Forehead**: Height, width, slope (flat, receding, curved).
2. **Eyebrows**: Thickness, arch height, separation distance, set height relative to orbit.
3. **Eyes**: Deep-set vs prominent, eyelid heaviness, inter-pupillary distance.
4. **Craniofacial Shape**: Maximum width (cheekbones vs temples), jaw angle taper, chin projection.
5. **Jawline & Mandible**: Square, rounded, or recessed; presence/absence of submental fat.
6. **Nose**: Bridge slope, dorsal hump presence, tip width, columella angle.
7. **Ears**: Pinna height, earlobe attachment (free vs attached), lateral projection.
8. **Mouth & Lips**: Philtrum depth, vermilion border thickness, oral commissure width relative to pupils.
9. **Hairline & Texture**: Norwood scale, hair density, cowlicks, parting side.
10. **The Anchor Feature**: The single, non-negotiable facial signature that human eyes latch onto (e.g. Shannon's sharp angular jaw, Feynman's expressive arched brows, Einstein's distinctive wild hair volume and moustache).

---

## 3. The Technical Character Sheet Prompt Layout

Generate one master reference image before generating any scene footage:

```
Character reference sheet, single 9:16 vertical image, flat neutral mid-grey (#808080) studio background.

LAYOUT:
- Large frontal head-and-shoulders portrait filling top half (focal identity anchor).
- Row of four smaller profile/quarter angles: front, 45-degree left, 90-degree left profile, 45-degree right.
- Full-body standing stance filling lower third.

GEOMETRY SPECIFICATION:
[Insert the 10-point ledger here]

THE ANCHOR FEATURE:
[Stated explicitly twice with physical bounds]

ANTI-DRIFT NEGATIVE ENFORCEMENT:
No symmetrical instagram-model jawline, no salon blow-dry hair, no sculpted cheekbones, no modern gym physique, no airbrushed poreless skin, no 3D cartoon CGI.

LIGHTING & OPTICS:
Flat neutral 5000K daylight, deep f/8 aperture (everything in pin-sharp focus), zero cinematic shadows or color cast.
```

---

## 4. Re-Attaching the Character Sheet in Symphony

When generating a scene with your recurring character:
1. Attach the approved master character sheet to Symphony's reference slot.
2. In the text prompt, describe **only the wardrobe, the laboratory environment, and the camera movement**.
3. Never use a film still in the reference slot—only the neutral grey character sheet.

---

## 5. Repairing Drifted Footage in Clipchat

If an otherwise perfect 4-second Symphony clip experiences facial morphing in the final 1.5 seconds:
- **Do not regenerate the entire shot.**
- In Clipchat, execute an editorial cut at second 2.5, transitioning to a **Hyperframes technical card (`TMPL-11` or `TMPL-24`)** or a **macro hardware B-roll** while the character's voiceover continues uninterrupted over Track A1.
- This maintains 100% production momentum with zero budget waste.
