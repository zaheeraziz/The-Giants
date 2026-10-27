"""Helpers for authoring seed data in the v1 model (docs/data-model.md).

Seed files call these helpers; write_all() emits one JSON file per collection into data/.
IDs in the seed are readable slugs. They are still treated as permanent: never rename one,
add a redirect instead (see "Merging duplicates" in the data model).
"""
import json, os

COLLECTIONS = ["persons", "names", "life_events", "relations", "works", "work_contributors", "work_relations",
               "places", "person_places", "institutions", "person_institutions", "events", "person_events", "sources"]
D = {k: [] for k in COLLECTIONS}
_persons = {}

def _l(x):
    return list(x) if isinstance(x, (list, tuple)) else ([x] if x else [])

# ---------- sources ----------
def source(id, title, url=None, type="web", note=None):
    D["sources"].append({k: v for k, v in dict(id=id, type=type, title=title, url=url, note=note).items() if v is not None})
    return id

# ---------- dates ----------
def date(hy=None, hm=None, hd=None, gy=None, gm=None, gd=None, approx=False, precision=None, text=None):
    if precision is None:
        precision = "day" if (gd or hd) else "month" if (gm or hm) else "year"
    sort = None
    if gy:
        sort = gy + ((gm - 1) / 12 if gm else 0) + ((gd - 1) / 365 if gd else 0)
    elif hy:  # rough Hijri -> CE for sorting only
        sort = round(hy * 0.97 + 622, 1)
    d = {"hijri": {k: v for k, v in dict(y=hy, m=hm, d=hd).items() if v}, "gregorian": {k: v for k, v in dict(y=gy, m=gm, d=gd).items() if v},
         "precision": precision, "approx": approx, "sort": round(sort, 3) if sort else None}
    if text: d["text"] = {"en": text}
    return d

# ---------- places ----------
def place(id, en, ar=None, type="town", parent=None, region=None):
    D["places"].append({k: v for k, v in dict(id=id, name={"en": en, **({"ar": ar} if ar else {})}, type=type, parent_id=parent, region=region).items() if v is not None})

# ---------- persons ----------
def person(id, en, ar=None, *, status="full", kind="scholar", summary=None, legacy=None, tags=None, honorific=True,
           note=None, cites=(), names=(), title=None):
    """Create or upgrade a person. `names`: list of (type, lang, value_or_translit)."""
    if id in _persons:  # upgrade a stub to a full record
        p = _persons[id]
        if status == "full" and p["status"] == "stub":
            D["persons"].remove(p); del _persons[id]
            D["names"][:] = [n for n in D["names"] if n["person_id"] != id]
            D["life_events"][:] = [e for e in D["life_events"] if e["person_id"] != id]
        else:
            return id
    p = {k: v for k, v in dict(id=id, slug=id, kind=kind, status=status,
         summary={"en": summary} if summary else None, legacy={"en": legacy} if legacy else None,
         tags=_l(tags) or None, note={"en": note} if note else None, citations=_l(cites) or None).items() if v is not None}
    if honorific is False: p["honorific"] = False
    D["persons"].append(p); _persons[id] = p
    D["names"].append({"person_id": id, "type": "shuhra", "lang": "en", "translit": en, "primary": True})
    if ar: D["names"].append({"person_id": id, "type": "shuhra", "lang": "ar", "value": ar, "primary": True})
    if title: D["names"].append({"person_id": id, "type": "title", "lang": "en", "translit": title})
    for t, lang, v in names:
        D["names"].append({"person_id": id, "type": t, "lang": lang, **({"translit": v} if lang == "en" else {"value": v})})
    return id

def stub(id, en, ar=None, born=None, died=None, desc=None, honorific=True, cites=()):
    """A second-level person: name, dates and a one-line descriptor only."""
    if id in _persons: return id
    person(id, en, ar, status="stub", summary=desc, honorific=honorific, cites=cites)
    if born: life(id, "birth", born, conf="reported")
    if died: life(id, "death", died, conf="reported")
    return id

def life(pid, type, d, place=None, conf="reported", cites=(), note=None):
    D["life_events"].append({k: v for k, v in dict(person_id=pid, type=type, date=d, place_id=place, preferred=True,
                             confidence=conf, citations=_l(cites) or None, note={"en": note} if note else None).items() if v is not None})

def lived(pid, place, role, note=None, conf="reported", cites=()):
    D["person_places"].append({k: v for k, v in dict(person_id=pid, place_id=place, role=role, note={"en": note} if note else None,
                               confidence=conf, citations=_l(cites) or None).items() if v is not None})

# ---------- relations ----------
_rel_n = [0]
def rel(type, frm, to, subjects=None, note=None, place=None, conf="reported", cites=(), rank=None, years=None):
    sym = type in ("companion_of", "fellow_student", "corresponded_with", "family", "co_founder")
    for r in D["relations"]:  # one link per pair and type; peer links count both ways
        if r["type"] == type and ((r["from"], r["to"]) == (frm, to) or (sym and (r["from"], r["to"]) == (to, frm))):
            return
    _rel_n[0] += 1
    D["relations"].append({k: v for k, v in dict(id=f"rel-{_rel_n[0]:04d}", type=type, **{"from": frm}, to=to,
                           subjects=_l(subjects) or None, note={"en": note} if note else None, place_id=place,
                           period={"text": years} if years else None, confidence=conf, citations=_l(cites) or None, rank=rank).items() if v is not None})

# ---------- works ----------
def work(id, translit, original=None, *, by, role="author", meaning=None, genres=(), langs=(), desc=None, rank=None,
         status="extant", composed=None, publication=None, conf="reported", cites=()):
    if not any(w["id"] == id for w in D["works"]):
        D["works"].append({k: v for k, v in dict(id=id, title={k2: v2 for k2, v2 in dict(translit=translit, original=original, meaning=meaning).items() if v2},
                           genres=_l(genres) or None, languages=_l(langs) or None, description={"en": desc} if desc else None, rank=rank,
                           status=status, composed=composed, publication=publication, confidence=conf, citations=_l(cites) or None).items() if v is not None})
    for pid in _l(by):
        D["work_contributors"].append({"work_id": id, "person_id": pid, "role": role})
    return id

def work_rel(frm, type, to):
    D["work_relations"].append({"from": frm, "type": type, "to": to})

# ---------- institutions & events ----------
def institution(id, en, ar=None, type="madrasa", place=None, founded=None, cites=()):
    D["institutions"].append({k: v for k, v in dict(id=id, name={"en": en, **({"ar": ar} if ar else {})}, type=type, place_id=place,
                              founded=founded, citations=_l(cites) or None).items() if v is not None})

def member(pid, inst, role, note=None, conf="reported", cites=()):
    D["person_institutions"].append({k: v for k, v in dict(person_id=pid, institution_id=inst, role=role, note={"en": note} if note else None,
                                     confidence=conf, citations=_l(cites) or None).items() if v is not None})

def event(id, en, d=None, place=None, cites=()):
    D["events"].append({k: v for k, v in dict(id=id, name={"en": en}, date=d, place_id=place, citations=_l(cites) or None).items() if v is not None})

def took_part(pid, ev, role="participant", note=None, cites=()):
    D["person_events"].append({k: v for k, v in dict(person_id=pid, event_id=ev, role=role, note={"en": note} if note else None,
                               citations=_l(cites) or None).items() if v is not None})

# ---------- output ----------
def write_all(outdir, start):
    os.makedirs(outdir, exist_ok=True)
    for k in COLLECTIONS:
        with open(os.path.join(outdir, k + ".json"), "w", encoding="utf-8") as f:
            json.dump(D[k], f, ensure_ascii=False, indent=1)
    with open(os.path.join(outdir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump({"start": start, "model": "v1"}, f, indent=1)
    return {k: len(v) for k, v in D.items()}
