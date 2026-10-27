# The Giants

A visual explorer of Muslim scholars and their networks. Each page puts one scholar in the centre:

- **Top:** teachers, with an arrow up to them
- **Bottom:** students and disciples
- **Right:** major works (first five shown, the rest under "more"); click a book for its details
- **Left:** companions and friends (first five shown, the rest under "more")
- **Centre:** name, with birth and death dates in AH and CE; click it for the full record: names, places, burial, institutions, events, and sources with a confidence level for each fact

Every name is clickable and moves that scholar to the centre. Scholars are shown with the honorific "Sheikh".

## Demo: Sheikh Qāsim Nānautavī

The seed dataset is built around Sheikh Qāsim Nānautavī (1248–1297 AH / 1832–1880 CE), co-founder of Darul Uloom Deoband, one level deep:

| | Count | Each has a full page |
|---|---|---|
| Teachers | 7 | yes |
| Students (and his son) | 10 | yes |
| Companions and friends | 12 | yes |
| His works | 24 | detail panel per book |

Everyone those 30 people link to (their own teachers, students and peers) appears as a smaller record with name, dates and a one-line description. In total: 99 people, 194 relations, 95 works, 85 sources.

## Run it

Open `index.html` through any static server (it loads `data/bundle.js`), or deploy with GitHub Pages: Settings → Pages → deploy from `main`, root.

```bash
python3 -m http.server   # then open http://localhost:8000
```

## Data

The data follows the model in [`docs/data-model.md`](docs/data-model.md). Each collection is one JSON file in `data/`:

`persons`, `names`, `life_events`, `relations`, `works`, `work_contributors`, `work_relations`, `places`, `person_places`, `institutions`, `person_institutions`, `events`, `person_events`, `sources`

To change data:

```bash
python3 scripts/seed/build_seed.py   # regenerate data/*.json from the seed scripts
node scripts/build.mjs               # check every reference and write data/bundle.js
```

The seed scripts in `scripts/seed/` (`base.py`, `teachers.py`, `students.py`, `companions.py`, `works.py`) are the readable source. `build.mjs` fails if any ID points at something that doesn't exist.

## How reliable is it

Every fact carries a confidence level and its sources:

- **attested**: stated in a primary or major source (e.g. Nuzhat al-Khawāṭir, Darul Uloom Deoband's official site, academic articles)
- **reported**: secondary sources such as Wikipedia
- **disputed**: sources disagree (both views noted)
- **uncertain**: thin evidence, or marked "Not yet checked against a source" where a date comes from general knowledge

Known open questions, to check against *Sawāniḥ Qāsmī* (Gīlānī) and *Sawāneḥ ʿUlamāʾ-e Deoband*:

- Whether Ḥāfiẓ Muḥammad Aḥmad studied under his father (shown as family for now)
- No named khalīfa of Nānautavī himself was found
- Darul Uloom's founding: 15 Muḥarram 1283 is attested; the Gregorian date is given as 30 or 31 May 1866
- Who counts as founder: early records name Ḥājī ʿĀbid; later accounts name Nānautavī
- Gangohī as co-founder in 1866 and Sir Sayyid as a fellow student are both disputed
- Which chapters of the Bukhārī notes are Nānautavī's
- Most Arabic/Urdu-script names are standard spellings, not quoted from sources
