# The Giants — data model (v0)

## Core idea
Every scholar is a node. Relationships are stored once as edges and read in both directions, so adding "X studied under Y" automatically fills Y's students and X's teachers.

## Entities
**Scholar**
- id (ascii slug), name_translit, name_ar, kunya/laqab/nisba (later)
- born_ah, died_ah, born_ce, died_ce, birth_approx (bool)
- city / places of activity, region (Hijaz, Iraq, Sham, Egypt, Khurasan, Andalus, Hind, …)
- burial place (later: lat/lng for a map)
- school / madhhab, role (Companion, Successor, …)
- bio (short, own words), movement / legacy
- status: full | stub (stub = appears in chains but no full record yet)
- sources: list of citations

**Work** — title, title_ar, scholar_id, type (hadith, fiqh, usul, tafsir, creed, interfaith, letters…), language, note

**Edge: studied_under** — student_id, teacher_id, subject (what was taught), (later: place, source)

**Edge: companionship** — a_id, b_id, reason (co-founders, fellow students, correspondence, travelled together, …)

## Page layout
- Centre: "Sheikh" + name, Arabic name, birth and death dates; click for bio
- Top: teachers (arrow up)
- Bottom: students and disciples (arrow down)
- Right: major works — first five visible, rest in a drop-down
- Left: companions and friends — first five visible, rest in a drop-down

## Display rules
- Scholars are shown with the honorific "Sheikh" before the name (Arabic: الشيخ).
