# The Giants

A visual explorer of Muslim scholars and their networks. Each page puts one scholar in the centre:

- **Top:** teachers, with an arrow up to them
- **Bottom:** students and disciples
- **Right:** major works (first five shown, the rest under "more")
- **Left:** companions and friends
- **Centre:** name (click for a short bio), with birth and death dates in AH and CE

Every name is clickable and moves that scholar to the centre, so you can walk the chain in any direction. Scholars are shown with the honorific "Sheikh".

## Run it

It's a single static file. Open `index.html` in a browser, or serve the folder with any static host (GitHub Pages works: Settings → Pages → deploy from `main`, root).

## Data

All data lives in the `<script>` block of `index.html`:

- `S` — scholars (`n` name, `ar` Arabic name, `b`/`d` birth/death AH, `bce`/`dce` CE, `bio`, `works`, `stub` for records not yet written)
- `E` — teacher links as `[student, teacher, what was taught]`, read both ways
- `P` — companionships as `[a, b, relationship]`, read both ways

See `docs/data-model.md` for the fuller model.

## Status

Seed data. Many dates, works and links come from general knowledge and need checking against classical and Urdu biographical sources (e.g. al-Dhahabī's *Siyar*, Ibn Ḥajar's *Tahdhīb*, Gīlānī's *Sawāniḥ Qāsmī*). The page opens on Sheikh Qāsim Nānautavī.
