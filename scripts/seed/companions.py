"""Nanautavi's companions and friends, each with one level of their own network."""
from lib import *
U = "unverified"
QN = "qasim-nanautavi"

for sid, title, url in [
    ("wiki-gangohi", "Wikipedia — Rashid Ahmad Gangohi", "https://en.wikipedia.org/wiki/Rashid_Ahmad_Gangohi"),
    ("ilmgate-gangohi", "ilmgate — Academic education and spiritual training of Rasheed Ahmad Gangohi", "https://www.ilmgate.org/the-academic-education-and-spiritual-training-of-hadrat-rasheed-ahmad-gangohi/"),
    ("wiki-yaqub", "Wikipedia — Yaqub Nanautawi", "https://en.wikipedia.org/wiki/Yaqub_Nanautawi"),
    ("dud-yaqub", "Darul Uloom Deoband — Muhammad Yaqub Nanautawi (co-founders list)", "https://dud.edu.in/index.php/en/co-founders-list?id=26"),
    ("wiki-abid", "Wikipedia — Sayyid Muhammad Abid", "https://en.wikipedia.org/wiki/Sayyid_Muhammad_Abid"),
    ("dud-rectors", "Darul Uloom Deoband — former rectors", "https://dud.edu.in/index.php/en/former-rectors"),
    ("wiki-founding", "Wikipedia — Foundation of Darul Uloom Deoband", "https://en.wikipedia.org/wiki/Foundation_of_Darul_Uloom_Deoband"),
    ("wiki-zulfiqar", "Wikipedia — Zulfiqar Ali Deobandi", "https://en.wikipedia.org/wiki/Zulfiqar_Ali_Deobandi"),
    ("dud-zulfiqar", "Darul Uloom Deoband — Zulfiqar Ali (co-founders list)", "https://dud.edu.in/index.php/en/co-founders-list?id=27"),
    ("wiki-fazlurrahman", "Wikipedia — Fazlur Rahman Usmani", "https://en.wikipedia.org/wiki/Fazlur_Rahman_Usmani"),
    ("wiki-sirsyed", "Wikipedia — Syed Ahmad Khan", "https://en.wikipedia.org/wiki/Syed_Ahmad_Khan"),
    ("tareen-2024", "SherAli Tareen, 'Theological foundations of Muslim modernism and traditionalism in South Asia', Modern Asian Studies 58(2), 2024",
     "https://www.cambridge.org/core/journals/modern-asian-studies/article/theological-foundations-of-muslim-modernism-and-traditionalism-in-south-asia/CF73849C02B3C3C5B8C4142B48BC21C8"),
    ("wiki-mazhar", "Wikipedia — Mazhar Nanautawi", "https://en.wikipedia.org/wiki/Mazhar_Nanautawi"),
    ("deoband-mazhar", "deoband.org — Scholar of deep learning: Shaykh Mazhar Nanautwi", "https://deoband.org/2009/11/biographical-notes/scholar-of-deep-learning-shaykh-mazhar-nanautwi/"),
    ("ilmgate-mazhar", "ilmgate — A short biography of Mawlana Muhammad Mazhar Nanautwi", "https://www.ilmgate.org/a-short-biography-of-mawlana-muhammad-mazhar-nanautwi/"),
    ("wiki-shamli", "Wikipedia — Battle of Shamli", "https://en.wikipedia.org/wiki/Battle_of_Shamli"),
    ("wiki-munir", "Wikipedia — Muhammad Munir Nanautavi", "https://en.wikipedia.org/wiki/Muhammad_Munir_Nanautavi"),
    ("wiki-rafiuddin", "Wikipedia — Rafiuddin Deobandi", "https://en.wikipedia.org/wiki/Rafiuddin_Deobandi"),
    ("wiki-fazlehaq", "Wikipedia — Fazl-e-Haque Deobandi", "https://en.wikipedia.org/wiki/Fazl-e-Haque_Deobandi"),
    ("basair-ahsan", "Basair — on Tahdhir al-Nas and Muhammad Ahsan Nanautavi", "https://www.basair.net/?p=5368"),
    ("loc-qn", "Library of Congress — Introducing Imam Muhammad Qasim al-Nanautwi (PDF)", "https://tile.loc.gov/storage-services/service/gdc/gdcovop/2014311081/2014311081.pdf")]:
    source(sid, title, url)

# ---------- shared second-level people ----------
for sid, en, ar, b, d, desc in [
    ("yahya-kandhlawi", "Muḥammad Yaḥyā Kāndhlawī", "محمد یحییٰ کاندھلوی", None, (None, 1915), "Recorded Gangohī's hadith lectures."),
    ("ashiq-ilahi", "ʿĀshiq Ilāhī Mīrathī", "عاشق الٰہی میرٹھی", None, None, "Gangohī's biographer (Tadhkirat al-Rashīd)."),
    ("abdur-rahim-raipuri", "ʿAbd al-Raḥīm Rāipūrī", "عبد الرحیم رائپوری", None, None, "Khalīfa of Gangohī; Raipur khanqah."),
    ("mumtaz-ali", "Sayyid Mumtāz ʿAlī", "سید ممتاز علی", (None, 1860), (None, 1935), "Publisher and social reformer."),
    ("karim-bakhsh-rampuri", "Karīm Bakhsh Rāmpūrī", "کریم بخش رامپوری", None, None, "Sufi shaykh."),
    ("hali", "Alṭāf Ḥusayn Ḥālī", "الطاف حسین حالی", (None, 1837), (None, 1914), "Poet; biographer of Sir Sayyid."),
    ("mohsin-ul-mulk", "Nawwāb Muḥsin al-Mulk", "محسن الملک", (None, 1837), (None, 1907), "Sir Sayyid's successor at Aligarh."),
    ("chiragh-ali", "Chirāgh ʿAlī", "چراغ علی", (None, 1844), (None, 1895), "Modernist writer."),
    ("saadat-ali-saharanpuri", "Saʿādat ʿAlī Sahāranpūrī", "سعادت علی سہارنپوری", None, None, "Founder of the Saharanpur madrasa (Maẓāhir ʿUlūm)."),
    ("hafiz-yusuf-thanawi", "Ḥāfiẓ Muḥammad Yūsuf", "حافظ محمد یوسف", None, None, "Son of Ḥāfiẓ Ḍāmin; asked Imdādullāh to write Ḍiyāʾ al-Qulūb."),
    ("nihal-ahmad", "Nihāl Aḥmad Deobandī", "نہال احمد دیوبندی", None, None, "Among the early founders of Darul Uloom."),
    ("ghulam-ali-dehlawi", "Shāh Ghulām ʿAlī Dihlawī", "شاہ غلام علی دہلوی", (None, 1743), (None, 1824), "Naqshbandī-Mujaddidī shaykh of Delhi.")]:
    kw = {}
    if b: kw["born"] = date(hy=b[0], gy=b[1])
    if d: kw["died"] = date(hy=d[0], gy=d[1])
    stub(sid, en, ar, desc=desc, cites=[U], honorific=sid not in {'hali', 'mohsin-ul-mulk', 'chiragh-ali'}, **kw)

# =====================================================================
# 1. Rashīd Aḥmad Gangohī
C = person("rashid-gangohi", "Rashīd Aḥmad Gangohī", "رشید احمد گنگوہی", title="Quṭb al-Irshād",
    summary=("A Ḥanafī jurist and hadith teacher from Gangoh who studied in Delhi under Mamlūk ʿAlī and Shāh ʿAbd al-Ghanī, then became a Sufi "
             "deputy of Ḥājī Imdādullāh. He taught the six hadith collections at Gangoh for decades and issued the rulings that set much of "
             "the Deobandi legal method. After 1857 he was held for six months on suspicion of rebellion, then released."),
    legacy="With Nānautavī, one of the two pillars of Deoband: Nānautavī shaped its institution, Gangohī its method.",
    tags=["Ḥanafī", "Māturīdī", "Chishtī-Ṣābirī", "Deobandī"], cites=["wiki-gangohi", "deoband-org-gangohi", "ilmgate-gangohi"],
    names=[("kunya", "en", "Abū Masʿūd"), ("nasab", "en", "Rashīd Aḥmad ibn Hidāyat Aḥmad"), ("laqab", "en", "Faqīh al-Nafs"), ("nisba", "en", "al-Anṣārī al-Gangohī")])
life(C, "birth", date(hy=1244, hm=11, hd=6, gy=1826, gm=6, gd=12), place="gangoh", conf="attested", cites=["wiki-gangohi"])
life(C, "death", date(hy=1323, hm=6, hd=8, gy=1905, gm=8, gd=11), place="gangoh", conf="attested", cites=["wiki-gangohi"])
lived(C, "delhi", "studied", cites=["wiki-gangohi"]); lived(C, "gangoh", "taught", cites=["wiki-gangohi"])
lived(C, "gangoh", "buried", note="Beside his khanqah in Gangoh", cites=["wiki-gangohi"])
member(C, "darul-uloom-deoband", "co_founder", note="Listed by Darul Uloom; patron (sarparast) after 1880. Disputed for 1866 itself.", conf="disputed", cites=["dud-cofounders", "wiki-gangohi"])
took_part(C, "shamli-1857", note="served as qāḍī", cites=["wiki-shamli"])
rel("fellow_student", QN, C, note="Classmates under Mamlūk ʿAlī; fellow disciples of Imdādullāh; fought together at Shāmlī; Hajj together in 1877",
    place="delhi", years="from c.1845", conf="attested", cites=["ilmgate-gangohi", "wiki-gangohi", "deoband-org-gangohi"], rank=1)
for tid, subj in [("mamluk-ali", ["rational sciences"]), ("abdul-ghani-mujaddidi", ["hadith", "tafsīr"]), ("sadruddin-azurda", ["rational sciences"])]:
    rel("studied_under", C, tid, subj, cites=["wiki-gangohi"])
rel("bayah_to", C, "imdadullah", note="Chishtī-Ṣābirī; khalīfa", conf="attested", cites=["wiki-gangohi"])
for sid in ["khalil-ahmad", "abdur-rahim-raipuri", "husain-ahmad-madani", "yahya-kandhlawi", "ashiq-ilahi"]:
    rel("studied_under", sid, C, cites=["wiki-gangohi"])
rel("ijaza_from", "mazhar-nanautavi", C, note="Ijāza in taṣawwuf", cites=["deoband-mazhar"])
for wid, tr, orig, gen, lang, d, r in [
    ("fatawa-rashidiyya", "Fatāwā-e Rashīdiyya", "فتاویٰ رشیدیہ", "fiqh", "ur", "His collected legal rulings.", 1),
    ("lami-al-darari", "Lāmiʿ al-Darārī ʿalā Jāmiʿ al-Bukhārī", "لامع الدراری", "hadith", "ar", "His Bukhārī lectures, recorded by Yaḥyā Kāndhlawī and edited by Zakariyyā Kāndhlawī.", 2),
    ("al-kawkab-al-durri", "al-Kawkab al-Durrī", "الکوکب الدری", "hadith", "ar", "His Tirmidhī lectures, compiled the same way.", 3),
    ("imdad-al-suluk", "Imdād al-Sulūk", "امداد السلوک", "taṣawwuf", "fa", "Treatise on the Sufi path.", 4),
    ("hidayat-al-shia-gangohi", "Hidāyat al-Shīʿa", "ہدایۃ الشیعہ", "polemics", "ur", "Response to Shīʿī positions.", 5),
    ("zubdat-al-manasik", "Zubdat al-Manāsik", "زبدۃ المناسک", "fiqh", "ur", "On the rites of Hajj.", 6),
    ("sabil-al-rashad", "Sabīl al-Rashād", "سبیل الرشاد", "fiqh", "ur", "A short treatise.", 7),
    ("tasfiyat-al-qulub", "Taṣfiyat al-Qulūb", "تصفیۃ القلوب", "taṣawwuf", "ur", "On purifying the heart.", 8)]:
    work(wid, tr, orig, by=C, genres=gen, langs=lang, desc=d, rank=r, cites=["wiki-gangohi"])

# 2. Muḥammad Yaʿqūb Nānautavī
C = person("yaqub-nanautavi", "Muḥammad Yaʿqūb Nānautavī", "محمد یعقوب نانوتوی",
    summary=("Son of Mamlūk ʿAlī. He studied in Delhi under his father and Shāh ʿAbd al-Ghanī, taught in government colleges and served as a "
             "schools inspector, then left that career. In 1866 he became the first head teacher of Darul Uloom Deoband and taught hadith "
             "there for about nineteen years."),
    legacy="First principal of Deoband (1866–1883), teacher of Maḥmūd Ḥasan and Ashraf ʿAlī Thānawī, and Nānautavī's first biographer.",
    tags=["Ḥanafī", "Chishtī-Ṣābirī", "Deobandī"], cites=["wiki-yaqub", "dud-yaqub"], names=[("laqab", "en", "Gumnām (pen name)")])
life(C, "birth", date(hy=1249, hm=2, hd=13, gy=1833, gm=7), place="nanauta", conf="attested", cites=["wiki-yaqub"])
life(C, "death", date(hy=1302, hm=3, hd=3, gy=1884), place="nanauta", conf="attested", cites=["wiki-yaqub", "dud-yaqub"], note="Died of cholera.")
lived(C, "deoband", "taught", cites=["dud-yaqub"]); lived(C, "nanauta", "buried", note="Garden north of the Saharanpur road, Nanauta", cites=["dud-yaqub"])
member(C, "darul-uloom-deoband", "head_teacher", note="first head teacher, 1866–1883", conf="attested", cites=["dud-yaqub"])
member(C, "darul-uloom-deoband", "co_founder", conf="attested", cites=["dud-cofounders"])
took_part(C, "shamli-1857", note="listed among the commanders", cites=["wiki-shamli"])
rel("companion_of", QN, C, note="Lifelong friend; Hajj together in 1860 and 1877; co-founder of Deoband; wrote Nānautavī's first biography",
    conf="attested", cites=["dud-yaqub", "wiki-yaqub"], rank=2)
rel("studied_under", C, "mamluk-ali", note="His father", cites=["wiki-yaqub"]); rel("studied_under", C, "abdul-ghani-mujaddidi", "hadith", cites=["wiki-yaqub"])
rel("studied_under", C, "ahmad-ali-saharanpuri", "hadith", cites=["wiki-ahmadali"]); rel("khalifa_of", C, "imdadullah", cites=["wiki-yaqub"])
rel("family", C, "mamluk-ali", note="Son", cites=["wiki-yaqub"])
for sid in ["ashraf-ali-thanwi", "khalil-ahmad", "aziz-rahman-usmani", "mumtaz-ali", "habib-rahman-usmani"]:
    rel("studied_under", sid, C, cites=["wiki-yaqub"])
rel("companion_of", C, "rashid-gangohi", note="Fellow disciple of Imdādullāh", cites=["wiki-yaqub"])
work("sawanih-qasimi-yaqub", "Sawāniḥ-e Qāsimī (Sawāneḥ ʿUmrī)", "سوانح قاسمی", by=C, genres="biography", langs="ur", rank=1,
     desc="The earliest short life of Nānautavī, written by his friend; printed at the Mujtabāʾī Press, Delhi, 1894.", conf="attested", cites=["wiki-yaqub"])
work("maktubat-yaqubi", "Maktūbāt-e Yaʿqūbī", "مکتوبات یعقوبی", by=C, genres="letters", langs="ur", rank=2, desc="Sixty-four letters on Sufi practice and legal questions.", cites=["wiki-yaqub"])
work("bayaz-yaqubi", "Bayāḍ-e Yaʿqūbī", "بیاض یعقوبی", by=C, genres="other", langs=["ur", "fa"], rank=3, desc="Notebook of Hajj diaries, hadith chains, poems and devotions.", cites=["wiki-yaqub"])

# 3. Ḥājī Sayyid Muḥammad ʿĀbid
C = person("sayyid-abid", "Ḥājī Sayyid Muḥammad ʿĀbid", "حاجی سید محمد عابد دیوبندی",
    summary=("A Sayyid of Deoband who left his studies in Delhi when his father died and became a Sufi master, authorised by Imdādullāh. In "
             "1866 he raised the first funds for the madrasa at the Chhatta Masjid and served three terms as its rector. He also had the "
             "Jama Masjid of Deoband built."),
    legacy="Named founder and first proposer of Deoband in the madrasa's own documents of 1889–90.",
    tags=["Ḥanafī", "Chishtī-Ṣābirī", "Deobandī"], cites=["wiki-abid", "dud-rectors", "wiki-founding"], names=[("ism", "en", "ʿĀbid Ḥusayn")])
life(C, "birth", date(hy=1250, gy=1834, approx=True), place="deoband", conf="attested", cites=["wiki-abid"])
life(C, "death", date(hy=1331, hm=12, hd=27, gy=1912), place="deoband", conf="reported", cites=["wiki-abid"], note="The Hijri date converts to late 1913; sources give 1912.")
member(C, "darul-uloom-deoband", "co_founder", note="raised the first funds in 1866", conf="attested", cites=["wiki-founding"])
member(C, "darul-uloom-deoband", "rector", note="1866–67, 1869–71, 1890–92", conf="attested", cites=["dud-rectors"])
took_part(C, "deoband-founding", role="founder", cites=["wiki-founding"])
rel("co_founder", QN, C, note="Co-founder of Deoband; wrote to Nānautavī asking for a teacher; fellow disciple of Imdādullāh",
    conf="attested", cites=["wiki-founding", "dud-rectors"], rank=3)
rel("bayah_to", C, "imdadullah", note="Ijāza in taṣawwuf", cites=["wiki-abid"]); rel("bayah_to", C, "karim-bakhsh-rampuri", cites=["wiki-abid"])
rel("bayah_to", "aziz-rahman-usmani", C, cites=["wiki-abid"])
rel("companion_of", C, "rafi-uddin-deobandi", note="Alternated with him as rector", cites=["dud-rectors"])

# 4. Ḏhū al-Fiqār ʿAlī Deobandī
C = person("zulfiqar-ali", "Ḏhū al-Fiqār ʿAlī Deobandī", "ذوالفقار علی دیوبندی",
    summary=("A Delhi College graduate who taught at Bareilly College and became an inspector of schools, later an honorary magistrate in "
             "Deoband. He wrote Urdu commentaries on classical Arabic poetry and an Arabic account of the Deoband madrasa, and sat on its "
             "council from 1866 to 1903."),
    legacy="Father of Shaykh al-Hind Maḥmūd Ḥasan, Deoband's first student.",
    tags=["Ḥanafī", "Deobandī"], cites=["wiki-zulfiqar", "dud-zulfiqar"])
life(C, "birth", date(hy=1237, gy=1822, approx=True), place="deoband", cites=["wiki-zulfiqar"])
life(C, "death", date(hy=1322, gy=1904), place="deoband", conf="attested", cites=["wiki-zulfiqar"])
lived(C, "bareilly", "taught", cites=["wiki-zulfiqar"])
lived(C, "deoband", "buried", note="Qabrastān-e Qāsmī, east of Nānautavī's grave", conf="attested", cites=["dud-zulfiqar"])
member(C, "darul-uloom-deoband", "co_founder", note="council member 1866–1903", conf="attested", cites=["wiki-zulfiqar"])
rel("companion_of", QN, C, note="A close friend; co-founder of Deoband; father of his chief student; buried beside him", conf="attested", cites=["dud-zulfiqar"], rank=4)
rel("studied_under", C, "mamluk-ali", note="Delhi College", cites=["wiki-zulfiqar"]); rel("studied_under", C, "sadruddin-azurda", cites=["wiki-zulfiqar"])
rel("studied_under", C, "mahtab-ali", note="His elder brother", cites=["wiki-zulfiqar"])
rel("family", C, "mahtab-ali", note="Younger brother", cites=["wiki-zulfiqar"]); rel("family", C, "mahmud-hasan", note="Father", cites=["wiki-zulfiqar"])
for wid, tr, orig, gen, lang, d, r in [
    ("al-hadiyya-al-saniyya", "al-Hadiyya al-Saniyya fī Dhikr al-Madrasa al-Islāmiyya al-Dīwbandiyya", "الہدیۃ السنیۃ", "history", "ar", "1307 AH account of the Deoband madrasa and its elders.", 1),
    ("tashil-al-dirasa", "Tashīl al-Dirāsa", "تسہیل الدراسہ", "commentary", "ur", "On the Dīwān al-Ḥamāsa.", 2),
    ("tashil-al-bayan", "Tashīl al-Bayān", "تسہیل البیان", "commentary", "ur", "On the Dīwān of al-Mutanabbī.", 3),
    ("taliqat-muallaqat", "al-Taʿlīqāt ʿalā al-Sabʿ al-Muʿallaqāt", "التعلیقات علی السبع المعلقات", "commentary", "ur", "On the seven Muʿallaqāt odes.", 4),
    ("itr-al-warda", "ʿIṭr al-Warda", "عطر الوردہ", "commentary", "ur", "On the Qaṣīdat al-Burda.", 5),
    ("al-irshad-zulfiqar", "al-Irshād", "الارشاد", "commentary", "ur", "On the Bānat Suʿād ode.", 6),
    ("tadhkirat-al-balagha", "Tadhkirat al-Balāgha", "تذکرۃ البلاغہ", "rhetoric", "ur", "Rhetoric handbook with Urdu examples.", 7),
    ("tashil-al-hisab", "Tashīl al-Ḥisāb", "تسہیل الحساب", "mathematics", "ur", "Arithmetic textbook, printed at Bareilly in 1852.", 8)]:
    work(wid, tr, orig, by=C, genres=gen, langs=lang, desc=d, rank=r, cites=["wiki-zulfiqar"])

# 5. Faḍl al-Raḥmān ʿUthmānī
C = person("fazlur-rahman-usmani", "Faḍl al-Raḥmān ʿUthmānī", "فضل الرحمٰن عثمانی دیوبندی",
    summary=("A Delhi College graduate under Mamlūk ʿAlī who worked as a deputy inspector of schools in several districts. He wrote poetry "
             "and chronograms in Persian and Urdu, including a Persian poem on the 1883 plague in Deoband, and sat on the Deoband council "
             "for life."),
    legacy="Head of the ʿUthmānī family of Deoband; father of ʿAzīz al-Raḥmān, Ḥabīb al-Raḥmān and Shabbīr Aḥmad ʿUthmānī.",
    tags=["Ḥanafī", "Deobandī"], cites=["wiki-fazlurrahman"])
life(C, "birth", date(gy=1831, approx=True), place="deoband", cites=["wiki-fazlurrahman"])
life(C, "death", date(hy=1325, gy=1907, gm=6, gd=15), conf="attested", cites=["wiki-fazlurrahman"])
member(C, "darul-uloom-deoband", "co_founder", note="council member for life", conf="attested", cites=["wiki-fazlurrahman"])
rel("co_founder", QN, C, note="Co-founder of Deoband; both studied under Mamlūk ʿAlī", conf="attested", cites=["wiki-fazlurrahman", "dud-cofounders"], rank=5)
rel("studied_under", C, "mamluk-ali", note="Delhi College", cites=["wiki-fazlurrahman"])
for k in ["aziz-rahman-usmani", "habib-rahman-usmani", "shabbir-usmani"]:
    rel("family", C, k, note="Father", cites=["wiki-fazlurrahman"])
work("qissa-gham-diban", "Qiṣṣa-e Gham-e Dībān", "قصۂ غم دیبان", by=C, genres="poetry", langs="fa", rank=1, desc="1301 AH poem on the plague in Deoband; a historical source.", cites=["wiki-fazlurrahman"])

# 6. Muḥammad Maẓhar Nānautavī
C = person("mazhar-nanautavi", "Muḥammad Maẓhar Nānautavī", "محمد مظہر نانوتوی",
    summary=("A Delhi-trained scholar who studied under Mamlūk ʿAlī and Shāh Muḥammad Isḥāq and worked as a teacher and copy-editor. A bullet "
             "wound at Shāmlī in 1857 left his leg paralysed. From 1867 he was head teacher of the Saharanpur madrasa later named Maẓāhir "
             "ʿUlūm, and taught there for nineteen years."),
    legacy="Founding head teacher of Maẓāhir ʿUlūm, Saharanpur; teacher of Khalīl Aḥmad Sahāranpūrī.",
    tags=["Ḥanafī", "Chishtī-Ṣābirī", "Deobandī"], cites=["wiki-mazhar", "deoband-mazhar", "ilmgate-mazhar"])
life(C, "birth", date(hy=1238, gy=1821, approx=True), place="nanauta", cites=["wiki-mazhar"])
life(C, "death", date(hy=1302, hm=12, hd=24, gy=1885, gm=10, gd=3), place="saharanpur", conf="attested", cites=["wiki-mazhar"])
lived(C, "deoband", "buried", note="Qabrastān-e Qāsmī, beside Ḏhū al-Fiqār ʿAlī", cites=["deoband-mazhar"])
member(C, "mazahir-uloom", "head_teacher", note="from 1867", conf="attested", cites=["wiki-mazhar"])
took_part(C, "shamli-1857", note="wounded; his leg was paralysed", cites=["deoband-mazhar"])
rel("companion_of", QN, C, note="Close friend; fought beside him at Shāmlī; Hajj together in 1860 and 1877; taught him some early books",
    conf="attested", cites=["deoband-mazhar"], rank=6)
for tid, subj in [("mamluk-ali", None), ("shah-ishaq", "Ṣaḥīḥ al-Bukhārī"), ("abdul-ghani-mujaddidi", "Muwaṭṭaʾ"), ("sadruddin-azurda", None), ("ahmad-ali-saharanpuri", "hadith")]:
    rel("studied_under", C, tid, subj, cites=["wiki-mazhar"])
rel("studied_under", "khalil-ahmad", C, note="His most prominent student", cites=["wiki-mazhar"])
rel("studied_under", "mahmud-hasan", C, note="Received his ijāza", cites=["deoband-mazhar"])
rel("family", C, "ahsan-nanautavi", note="Brother", cites=["wiki-mazhar"]); rel("family", C, "munir-nanautavi", note="Brother", cites=["wiki-mazhar"])
rel("companion_of", C, "saadat-ali-saharanpuri", note="Founder of the Saharanpur madrasa", cites=["wiki-mazhar"])
work("ghayat-al-awtar", "Ghāyat al-Awṭār (completion)", "غایۃ الاوطار", by=C, genres="fiqh", langs="ur", rank=1, desc="Helped complete the Urdu translation of al-Durr al-Mukhtār.", cites=["wiki-mazhar"])

# 7. Muḥammad Munīr Nānautavī
C = person("munir-nanautavi", "Muḥammad Munīr Nānautavī", "محمد منیر نانوتوی",
    summary=("The youngest of the Nānautavī brothers, with Maẓhar and Aḥsan. He studied in Delhi and taught at Bareilly College from 1861 "
             "while running the family's Matbaʿ-e Ṣiddīqī press. He served briefly as rector of Darul Uloom Deoband, and once sold his own "
             "land to replace stolen madrasa funds."),
    legacy="Rector of Deoband in the early 1890s and Urdu translator of al-Ghazālī.",
    tags=["Ḥanafī", "Naqshbandī", "Deobandī"], cites=["wiki-munir"])
life(C, "birth", date(hy=1247, gy=1831), place="nanauta", conf="attested", cites=["wiki-munir"])
member(C, "darul-uloom-deoband", "rector", note="about 1892–94; sources differ", cites=["wiki-munir", "dud-rectors"])
took_part(C, "shamli-1857", note="commanded the left flank; told by Imdādullāh never to leave Nānautavī's side", cites=["wiki-munir"])
rel("companion_of", QN, C, note="Guarded him at Shāmlī on Imdādullāh's order; urged him to attend the Shahjahanpur fair", conf="attested", cites=["wiki-munir", "loc-qn"], rank=7)
for tid in ["mamluk-ali", "sadruddin-azurda", "abdul-ghani-mujaddidi"]:
    rel("studied_under", C, tid, cites=["wiki-munir"])
rel("family", C, "ahsan-nanautavi", note="Brother; partner in the press", cites=["wiki-munir"])
work("siraj-al-salikin", "Sirāj al-Sālikīn", "سراج السالکین", by=C, role="translator", genres="taṣawwuf", langs="ur", rank=1,
     desc="Urdu translation of al-Ghazālī's Minhāj al-ʿĀbidīn (1281 AH / 1864).", cites=["wiki-munir"])
work("fawaid-e-gharibah", "Fawāʾid-e Gharība", "فوائد غریبہ", by=C, genres="taṣawwuf", langs="ur", rank=2, desc="Treatise on Sufism.", cites=["wiki-munir"])

# 8. Ḥāfiẓ Muḥammad Ḍāmin Shahīd
C = person("hafiz-zamin", "Ḥāfiẓ Muḥammad Ḍāmin Shahīd", "حافظ محمد ضامن شہید",
    summary=("A ḥāfiẓ and Sufi of Thana Bhawan in Imdādullāh's circle who joined the 1857 rising there. He was killed at Shāmlī, and accounts "
             "say the rebels' position collapsed after his death."),
    legacy="Remembered in Deobandi tradition as the martyr of Shāmlī.",
    tags=["Ḥanafī", "Chishtī-Ṣābirī"], cites=["wiki-shamli", "deoband-imdad"])
life(C, "death", date(hy=1273, gy=1857), place="shamli", conf="attested", cites=["wiki-shamli"], note="Killed in battle; exact date unverified.")
lived(C, "thana-bhawan", "lived", cites=["wiki-shamli"])
took_part(C, "shamli-1857", role="participant", note="killed in the battle", cites=["wiki-shamli"])
rel("companion_of", QN, C, note="Fought beside him under Imdādullāh at Shāmlī, 1857", conf="attested", cites=["wiki-shamli", "deoband-imdad"], rank=8)
rel("bayah_to", C, "nur-muhammad-jhanjhanawi", conf="uncertain", cites=[U])
rel("companion_of", C, "imdadullah", note="Leader of the Thana Bhawan circle", cites=["deoband-imdad"])
rel("family", C, "hafiz-yusuf-thanawi", note="Father", cites=["deoband-imdad"])

# 9. Rafīʿ al-Dīn Deobandī
C = person("rafi-uddin-deobandi", "Rafīʿ al-Dīn Deobandī", "رفیع الدین دیوبندی",
    summary=("A Naqshbandī-Mujaddidī deputy of Shāh ʿAbd al-Ghanī who had no formal madrasa degree. He was rector of Deoband for about nineteen "
             "years over two terms, and its first building, the Nau Darah, was finished under him. He migrated to the Hijaz in 1888 and died "
             "in Medina."),
    legacy="Rector during Deoband's formative building phase.",
    tags=["Ḥanafī", "Naqshbandī-Mujaddidī", "Deobandī"], cites=["wiki-rafiuddin", "dud-rectors"])
life(C, "birth", date(hy=1252, hm=9, hd=19, gy=1836, gm=12, gd=28), place="deoband", conf="attested", cites=["wiki-rafiuddin"])
life(C, "death", date(hy=1308, hm=6, hd=12, gy=1891, gm=1, gd=22), place="medina", conf="attested", cites=["wiki-rafiuddin"])
lived(C, "medina", "buried", note="Jannat al-Baqīʿ, Medina", conf="attested", cites=["wiki-rafiuddin"])
member(C, "darul-uloom-deoband", "rector", note="1867–69 and 1871/72–1888", conf="attested", cites=["dud-rectors"])
member(C, "darul-uloom-deoband", "co_founder", conf="attested", cites=["dud-cofounders"])
rel("co_founder", QN, C, note="Co-founder; Nānautavī laid the Nau Darah foundation stone during his rectorship (1875)", conf="attested", cites=["wiki-rafiuddin"], rank=9)
rel("khalifa_of", C, "abdul-ghani-mujaddidi", note="Naqshbandī-Mujaddidī", conf="attested", cites=["wiki-rafiuddin"])
rel("bayah_to", "aziz-rahman-usmani", C, cites=["wiki-rafiuddin"]); rel("bayah_to", "murtaza-chandpuri", C, cites=["wiki-rafiuddin"])

# 10. Sayyid Faḍl-i Ḥaqq Deobandī
C = person("fazl-e-haq-deobandi", "Sayyid Faḍl-i Ḥaqq Deobandī", "سید فضل حق دیوبندی",
    summary=("A disciple of Nānautavī and one of Deoband's early founders. The first public appeal for donations, in Muḥarram 1283, was "
             "issued under his supervision, and he sat on the council until 1311 AH, serving briefly as rector. He wrote a biography of "
             "Nānautavī that was never published but is quoted by Gīlānī."),
    tags=["Ḥanafī", "Deobandī"], cites=["wiki-fazlehaq"])
life(C, "death", date(hy=1315, gy=1898), cites=["wiki-fazlehaq"], note="Died at Jhalawar, Rajputana.")
member(C, "darul-uloom-deoband", "co_founder", note="supervised the first appeal for funds", conf="attested", cites=["wiki-fazlehaq"])
member(C, "darul-uloom-deoband", "rector", note="1310–1311 AH", cites=["wiki-fazlehaq"])
rel("co_founder", QN, C, note="Early founder of Deoband; disciple and biographer of Nānautavī", conf="reported", cites=["wiki-fazlehaq"], rank=10)

# 11. Muḥammad Aḥsan Nānautavī (upgrades the stub)
C = person("ahsan-nanautavi", "Muḥammad Aḥsan Nānautavī", "محمد احسن نانوتوی",
    summary=("Elder brother of Maẓhar and Munīr. He ran the family's Matbaʿ-e Ṣiddīqī press in Bareilly, translated al-Ghazālī's Iḥyāʾ and "
             "annotated works of Shāh Walīullāh. His question prompted Nānautavī's Taḥdhīr al-Nās, which he titled and printed in Bareilly."),
    tags=["Ḥanafī"], cites=["basair-ahsan", "ilmgate-mazhar"])
life(C, "birth", date(gy=1825, approx=True), cites=["basair-ahsan"]); life(C, "death", date(gy=1895), cites=["basair-ahsan"])
lived(C, "bareilly", "lived", note="ran the press", cites=["basair-ahsan"])
lived(C, "deoband", "buried", note="Qabrastān-e Qāsmī, beside Ḏhū al-Fiqār ʿAlī", cites=["dud-zulfiqar"])
rel("companion_of", QN, C, note="Asked the question behind Taḥdhīr al-Nās and published it; wrote a biography of Nānautavī", conf="reported", cites=["basair-ahsan", "loc-qn"], rank=11)
rel("studied_under", C, "mamluk-ali", cites=["wiki-mamluk"]); rel("studied_under", C, "ahmad-ali-saharanpuri", cites=["wiki-ahmadali"])

# 12. Sir Sayyid Aḥmad Khān (no "Sheikh": known as a reformer)
C = person("sir-syed", "Sir Sayyid Aḥmad Khān", "سر سید احمد خان", honorific=False,
    summary=("A Delhi-born reformer and East India Company judicial officer who wrote on archaeology, the causes of the 1857 revolt and a "
             "modernist commentary on the Qur'an. He founded the Muhammadan Anglo-Oriental College at Aligarh in 1875 and the journal "
             "Tahdhīb al-Akhlāq, reading scripture in the light of 'the law of nature'."),
    legacy="Founder of the Aligarh movement, the modernist counterpart to Deoband.",
    tags=["modernist", "Aligarh"], cites=["wiki-sirsyed", "tareen-2024"])
life(C, "birth", date(gy=1817, gm=10, gd=17), place="delhi", conf="attested", cites=["wiki-sirsyed"])
life(C, "death", date(gy=1898, gm=3, gd=27), place="aligarh-college", conf="attested", cites=["wiki-sirsyed"])
lived(C, "aligarh-college", "buried", note="Beside the Sir Syed Masjid, Aligarh Muslim University", conf="attested", cites=["wiki-sirsyed"])
member(C, "aligarh-college", "founder", note="1875", conf="attested", cites=["wiki-sirsyed"])
rel("debated", C, QN, note="Exchanged views in 1874 on reason and revelation; Nānautavī replied in Taṣfiyat al-ʿAqāʾid. Wrote a warm obituary of him in 1880.",
    years="1874", conf="attested", cites=["tareen-2024", "wiki-sirsyed"], rank=12)
rel("studied_under", C, "mamluk-ali", note="Disputed", conf="disputed", cites=["wiki-mamluk"])
rel("studied_under", C, "ghulam-ali-dehlawi", note="Early education", cites=["wiki-sirsyed"])
for sid in ["hali", "mohsin-ul-mulk", "chiragh-ali", "shibli-nomani", "nazir-ahmad"]:
    rel("companion_of", C, sid, note="Aligarh circle", cites=["wiki-sirsyed"])
for wid, tr, orig, gen, d, r in [
    ("athar-al-sanadid", "Āthār al-Ṣanādīd", "آثار الصنادید", "history", "Survey of Delhi's monuments (1847).", 1),
    ("asbab-e-baghawat", "Asbāb-e Baghāwat-e Hind", "اسباب بغاوت ہند", "history", "On the causes of the 1857 revolt (1859).", 2),
    ("tafsir-sir-syed", "Tafsīr al-Qurʾān", "تفسیر القرآن", "tafsir", "Modernist commentary on the Qur'an (from 1877).", 3),
    ("khutubat-e-ahmadiyya", "al-Khuṭubāt al-Aḥmadiyya", "خطبات احمدیہ", "sira", "Reply to William Muir's life of the Prophet (1870).", 4),
    ("tahzib-al-akhlaq", "Tahdhīb al-Akhlāq", "تہذیب الاخلاق", "journal", "Reformist Urdu journal (from 1870).", 5),
    ("tabyin-al-kalam", "Tabyīn al-Kalām", "تبیین الکلام", "interfaith", "A Muslim commentary on the Bible (1862–65).", 6)]:
    work(wid, tr, orig, by=C, genres=gen, langs="ur", desc=d, rank=r, cites=["wiki-sirsyed"])

# Delhi College alumni who also founded Deoband
member("nihal-ahmad", "darul-uloom-deoband", "co_founder", cites=["wiki-founding"])
member("mulla-mahmud", "darul-uloom-deoband", "teacher", note="first teacher, appointed by Nānautavī", conf="attested", cites=["wiki-founding"])
