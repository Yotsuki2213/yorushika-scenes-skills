# Human Treatment and Line References

Use this reference after inspecting the source and before compiling any route. The branch is determined by the source, independently of scene orientation and style route.

## Decide the branch

`human_subject_present=true` means one or more people carry the scene's compositional or narrative focus: consider scale, isolation, visible action, gaze and placement together. Do not count distant incidental passers-by alone as a primary subject. Existing drawn people and body fragments can be subjects too.

Record:
- `human_subject_present`: true / false
- `human_treatment`: add-white-protagonist / cover-existing-heads / user-override
- existing primary subjects' positions, body actions, body anchors and visible head regions
- for addition: resolved location, depth plane, scale basis, action, back-facing torso, over-shoulder head turn, weight-bearing support and contact/occlusion
- selected style reference(s), with their role separate from the source edit target

### Resolve a new figure's place and scale

For `add-white-protagonist`, complete this spatial pass before choosing the final gesture or route:

1. Read the oriented image for foreground, middle ground and background planes; mark the horizon, vanishing point or converging lines, visible support surfaces, major eye path and quiet areas.
2. Choose a location that belongs to the real scene. Prefer a road, roof edge, shore, step, wall, railing, bench, shadow boundary or other visible plane that can explain the figure's feet, pelvis, hand or forearm. Record the position relative to the frame and the object or edge that carries the figure.
3. Assign the figure to a depth plane and use nearby doors, windows, trees, roof courses, paving, railings, boats or other visible references to establish its relative size. Let perspective, occlusion and atmospheric distance set the scale continuously; a far-away figure may remain a small part of the image when that best preserves the scene's spatial reading.
4. Place the figure on the source eye path or in a quiet area only when that placement creates a believable emotional pause without taking over the source focal anchor. Keep the original architecture, road, water, roofline, vegetation and horizon as the dominant evidence.
5. Choose the action after the location and scale are settled. Walking, standing, sitting, leaning or looking toward water/space must follow the selected support and vanishing direction. The default back-facing torso with a natural over-shoulder look back is used only when the visible neck, shoulders, pelvis, feet and support remain physically coherent.
6. Record `location`, `depth`, `scale_basis`, `action`, `support_contact`, `occlusion` and `eye_path` in `figure_plan`. The record is internal production data and does not add user-facing parameters.

### No human subject: add-white-protagonist

Add one anonymous young man or young woman protagonist with uneven pure-white contours and loose hatching. It must be a readable person with an intentional action, not merely a gesture mark. Use the resolved `figure_plan`: the figure's location and size follow the source perspective, depth plane, nearby scale references and emotional weight, while the source's principal objects and relationships remain dominant.

Compose a single believable moment: the new figure's torso is turned away from the camera, while the head turns naturally back toward the camera over one shoulder. Use shoulder line, neck attachment and head placement to communicate the turn even though the head is fully scribbled over. Allow a small coordinated upper-torso turn, not a backward-mounted face, a 180-degree neck twist or front-facing chest on a back-facing pelvis. This is one figure in one still, not a before/after sequence or duplicate silhouette.

Ground that gesture in the resolved support: walking away along a road while glancing back, sitting with weight on an existing step and looking back over a shoulder, or pausing by a railing with the torso facing away and the head turned back. Match the figure's size to the visible support and depth; a distant person can be small in the overall frame while remaining readable through a clear silhouette, action direction and head scribble. Choose a stable support and plausible joint arrangement before stylizing: a walking step has a weight-bearing foot, sitting has a supported pelvis, and leaning has a believable hand/forearm contact. Respect gravity, balance, perspective, limb connections and foreground occlusion. If little ground is visible, use an existing seat/support or a plausible partially framed figure at a supported edge. Place a figure in naturally contrasting space, or allow a bounded scene-side tonal adjustment when needed for white-line visibility.

Let the figure be slightly abstract and sketchily scrawled: irregular pressure, wobbling broken contours, sparse overlapping construction lines and uneven hatching, with transparent body gaps revealing the scene. Simplify clothing and fine anatomy while keeping the torso, limbs, support and turn readable. Use pure-white ink, pencil or chalk-like strokes, not a polished cartoon or a solid filled body.

Cover the entire visible new head, including crown, hair mass, face, ears and back of head, with dense irregular white hatching and horizontal scribbles. No original or newly drawn head detail may read through. Keep the cover visibly made of strokes rather than a clean outline, empty face oval, smooth white disk or rectangular censor patch; any tiny inter-stroke gaps must not expose head features.

### Existing human subject(s): cover-existing-heads

Keep each primary subject's body, clothing, pose, relative size, position and contact intact. The back-facing/looking-back default is for newly added figures; do not rotate or re-pose an existing photographic or drawn subject to enforce it. Mark visible heads as editable exceptions to preservation locks, including in `strict`. Apply dense, irregular white hand-drawn hatching with overlapping, predominantly horizontal scribble strokes across the head.

Cover the entire visible head region, including crown, hair, face, ears and back of head, until none of those original details reads through; a face-only patch or sparse outline around a still-visible head is insufficient. Keep dense coverage visibly hand-scrawled with irregular white stroke ends, not a smooth fill. Let stroke ends extend slightly beyond the head contour when composition calls for it, but protect neck/body landmarks and adjacent important objects. Keep the overall head scale and facing gesture legible.

Apply this to visible heads of a group of co-primary subjects, including back-facing ones. For a partially visible head, cover only its visible region and respect existing occlusion. If the head is completely outside the frame or fully hidden, record coverage as not applicable and preserve the body fragment/occluder. Do not invent a head or another person.

In explicit `redraw`, the unlocked scene may be re-authored but these body anchors and human-branch decisions still apply unless the user specifically authorizes their redesign.

## Supporting references

The user-selected reference is bundled beside this guide:

- [线稿小人抠图联系表.png](../assets/line-figures/线稿小人抠图联系表.png): transparent contact sheet of five isolated white line figures. Use it to guide rough contour rhythm, sparse body hatching, dense horizontal head scribbles, youthful proportions and simple barefoot line feet. It is a style reference only; do not copy its arrangement or treat its figures as extra people.
- [Source record](../assets/line-figures/SOURCES.md).

When drawing is required, inspect the contact sheet with `view_image` and use it as the line-style reference. Extract only contour wobble, hatching rhythm, transparent body gaps, head scribble density, youthful proportions and simple barefoot line feet; do not reproduce its layout, background or extra figure.

Pass the user's scene as the edit target and selected images as explicitly labeled supporting line-style references using the supported ImageGen attachment mechanism. A path written in prompt text alone is not an image attachment. Do not import the reference backgrounds, masking fields, exact pose, props or recognizable character design. If bundled references are unavailable, state that and apply the written grammar without claiming to have attached them.
