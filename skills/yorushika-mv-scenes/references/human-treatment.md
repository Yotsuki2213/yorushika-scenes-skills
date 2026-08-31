# Human Treatment and Line References

Use this reference after inspecting the source and before compiling any route. The branch is determined by the source, independently of scene orientation and style route.

## Decide the branch

`human_subject_present=true` means one or more people carry the scene's compositional or narrative focus: consider scale, isolation, visible action, gaze and placement together. Do not count distant incidental passers-by alone as a primary subject. Existing drawn people and body fragments can be subjects too.

Record:
- `human_subject_present`: true / false
- `human_treatment`: add-white-protagonist / cover-existing-heads / user-override
- existing primary subjects' positions, body actions, body anchors and visible head regions
- for addition: proposed position, action, facing direction, scale and contact/occlusion
- selected style reference(s), with their role separate from the source edit target

### No human subject: add-white-protagonist

Add one anonymous human protagonist with uneven pure-white contours and loose hatching. It must be a readable person with an intentional action, not merely a gesture mark. Choose proportions and scale from scene perspective and emotional weight; preserve the source's principal objects and relationships.

Ground the action in visible support: walk along a road, sit on an existing step, lean against a railing, pause facing water, or respond to the source's wind or light. Respect contact, gravity, perspective and foreground occlusion. If little ground is visible, use an existing seat/support or a plausible partially framed figure at a supported edge; do not float a figure in sky/water or invent a conspicuous prop. Place a figure in naturally contrasting space, or allow a bounded scene-side tonal adjustment when needed for white-line visibility.

Body contours may be incomplete and crosshatched, with transparent gaps revealing the scene. Use white ink, pencil or chalk-like strokes. A visible new head carries dense anonymous white hatching and horizontal scribbles. Keep the person legible without turning it into a solid filled silhouette.

### Existing human subject(s): cover-existing-heads

Keep each primary subject's body, clothing, pose, relative size, position and contact intact. Mark visible heads as editable exceptions to preservation locks, including in `strict`. Apply dense, irregular white hand-drawn hatching with overlapping, predominantly horizontal scribble strokes across the head.

Cover the identity-bearing region sufficiently that the original face/head details no longer read through the treatment; a sparse outline around a still-visible face is insufficient. Let stroke ends extend slightly beyond the head contour when composition calls for it, but protect neck/body landmarks and adjacent important objects. Keep the overall head scale and facing gesture legible.

Apply this to visible heads of a group of co-primary subjects, including back-facing ones. For a partially visible head, cover only its visible region and respect existing occlusion. If the head is completely outside the frame or fully hidden, record coverage as not applicable and preserve the body fragment/occluder. Do not invent a head or another person.

In explicit `redraw`, the unlocked scene may be re-authored but these body anchors and human-branch decisions still apply unless the user specifically authorizes their redesign.

## Supporting references

The user-selected references are bundled beside this guide:

- [Reference 1](../assets/line-figures/线稿参考1.png): seated/reclining scene contact, loose white body hatching and a broad head scribble.
- [Reference 2](../assets/line-figures/线稿参考2.png): standing posture, irregular clothing contours, sparse body strokes and dense horizontal head coverage.
- [Reference 3](../assets/line-figures/线稿参考3.png): another supplied scene-grounded white-line example, closely related visually to reference 1.
- [Source record](../assets/line-figures/SOURCES.md).

When drawing is required, inspect 1–2 relevant references with `view_image` and select by action and stroke evidence. Treat the large white masking regions surrounding the figures as reference preparation marks, not desired art direction. Extract only contour wobble, hatching rhythm, transparent body gaps, head scribble density and scene contact.

Pass the user's scene as the edit target and selected images as explicitly labeled supporting line-style references using the supported ImageGen attachment mechanism. A path written in prompt text alone is not an image attachment. Do not import the reference backgrounds, masking fields, exact pose, props or recognizable character design. If bundled references are unavailable, state that and apply the written grammar without claiming to have attached them.

## Inspection

Check branch choice, readable protagonist/action, physical contact and occlusion, body-anchor preservation, sufficient visible-head coverage, pure-white strokes and their contrast. The white-only rule applies to the new drawing and head cover, not to the source body's clothing. Dense head scribbles are allowed; body hatching should retain gaps. Explicit user instructions, including no added people, take precedence and must be reflected consistently in the branch record and prompt.
