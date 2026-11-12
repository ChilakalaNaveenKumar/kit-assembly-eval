# Joint review of the correct assemblies

`scripts/joint_zooms.py` draws a close-up of every graded connection of every kit, on the correct assembly, with the compared feature circled (`review/joints/<kit>.png`).

Each assembly was reviewed twice:
- **AI review.** Independent AI reviewers inspected every part and every joint, one reviewer per kit, and listed anything that looked wrong. They checked the angle, the placement, which part sits in front, and whether the holes line up.
- **Manual review.** Naveen Kumar Chilakala then reviewed every assembly and every close-up by hand, confirming that each circled point sits on a feature a person can see on both parts (a hole, an axle, a hub, the centre of a rounded end, or an edge). Problems found were fixed before the final run.

| Kit | Connections | Fixed in review |
|---|---|---|
| bike | 10 (+3 level and angle checks) | Fork blade drawn in front of the front wheel, as on a real bike. |
| pulley | 9 (+6 line, angle checks) | Hook turned 90 degrees to the shackle: it hangs behind the strap and passes in front of the shackle's bow, so the shackle visibly hangs on it. The bracket may hang anywhere under the beam (whole plate under it), not only at its centre. |
| hand_pump | 8 | None needed. |
| desk_lamp | 6 (+1 line check) | Bulb seated inside the shade's socket. An unused pivot lug was removed from the base, so the arm has one mount point. The L bracket may stand anywhere along the base's flat top edge, not only at one spot. |
| scale | 7 | Pointer hung from the beam's pivot, tip down. Stirrup hooks drawn behind the beam-end eyes, so they hang through them. |
| wheelbarrow | 7 | None needed. |

Edge contacts (the bike's headset spacer and seat collar, the pump's cap on the body) are the loosest checks: two parts meeting along an edge rather than at a hole. Where a part could equally sit anywhere along an edge (the lamp's bracket on the base, the pulley's bracket on the beam), the check accepts any point along that edge (`tests/test_grader.py::test_brackets_may_sit_anywhere_along_their_edge_but_not_off_it`).
