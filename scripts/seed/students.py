"""Nanautavi's students, each with one level of their own network."""
from lib import *
U = "unverified"
QN = "qasim-nanautavi"

source("wiki-mahmud", "Wikipedia — Mahmud Hasan Deobandi", "https://en.wikipedia.org/wiki/Mahmud_Hasan_Deobandi")
source("tarajm-mahmud", "Nuzhat al-Khawatir — Mahmud Hasan (tarajm.com)", "https://tarajm.com/people/93876")
source("wiki-amrohi", "Wikipedia — Ahmad Hasan Amrohi", "https://en.wikipedia.org/wiki/Ahmad_Hasan_Amrohi")
source("tarajm-amrohi", "Nuzhat al-Khawatir — Ahmad Hasan Amrohi (tarajm.com)", "https://tarajm.com/people/95768")
source("shamela-budur", "al-Budur al-Mudiyya (Shamela) — Murtaza Hasan entry", "https://shamela.ws/book/819/6980")
source("tarajm-fakhr", "Nuzhat al-Khawatir — Fakhrul Hasan Gangohi (tarajm.com)", "https://tarajm.com/people/96252")
source("tarajm-abdulali", "Nuzhat al-Khawatir — Abdul Ali Meeruti (tarajm.com)", "https://tarajm.com/people/96055")
source("tarajm-mansur", "Nuzhat al-Khawatir — Mansur Ali Muradabadi (tarajm.com)", "https://tarajm.com/people/96364")
source("tarajm-abdurrahman", "Nuzhat al-Khawatir — Abdur Rahman Amrohi (tarajm.com)", "https://tarajm.com/people/96049")
source("tarajm-ismail", "Nuzhat al-Khawatir — Ismail Kawli (tarajm.com)", "https://tarajm.com/people/95807")
source("tarajm-abdullah", "Nuzhat al-Khawatir — Abdullah Ansari Anbahtawi (tarajm.com)", "https://tarajm.com/people/96151")
source("wiki-abdulwahid", "Wikipedia — Abdul Wahid Bengali", "https://en.wikipedia.org/wiki/Abdul_Wahid_Bengali")
source("wiki-hafizahmad", "Wikipedia — Hafiz Muhammad Ahmad", "https://en.wikipedia.org/wiki/Hafiz_Muhammad_Ahmad")

# ---------- shared second-level people ----------
for sid, en, ar, b, d, desc in [
    ("anwar-shah-kashmiri", "Anwar Shāh Kashmīrī", "انور شاہ کشمیری", (1292, 1875), (1352, 1933), "Hadith master; principal of Deoband."),
    ("husain-ahmad-madani", "Ḥusayn Aḥmad Madanī", "حسین احمد مدنی", (1296, 1879), (1377, 1957), "Shaykh al-Islām; head teacher of Deoband."),
    ("ubaidullah-sindhi", "ʿUbaydullāh Sindhī", "عبید اللہ سندھی", (None, 1872), (None, 1944), "Revolutionary of the Silk Letter Movement."),
    ("kifayatullah", "Muftī Kifāyatullāh Dihlawī", "کفایت اللہ دہلوی", (None, 1875), (None, 1952), "Muftī of India; first president of Jamiat Ulema-e-Hind."),
    ("ilyas-kandhlawi", "Muḥammad Ilyās Kāndhlawī", "محمد الیاس کاندھلوی", (None, 1885), (None, 1944), "Founder of the Tablighi Jamaat."),
    ("izaz-ali-amrohi", "Iʿzāz ʿAlī Amrohī", "اعزاز علی امروہی", None, (1374, 1955), "Deoband teacher of literature and fiqh."),
    ("manazir-gilani", "Manāẓir Aḥsan Gīlānī", "مناظر احسن گیلانی", (None, 1892), (None, 1956), "Author of Sawāniḥ Qāsmī, the major life of Nānautavī."),
    ("qari-tayyib", "Qārī Muḥammad Ṭayyib", "قاری محمد طیب", (None, 1897), (None, 1983), "Nānautavī's grandson; rector of Deoband for about fifty years."),
    ("mulla-mahmud", "Mullā Maḥmūd Deobandī", "ملا محمود دیوبندی", None, (None, 1886), "First teacher of Darul Uloom Deoband, appointed by Nānautavī."),
    ("shabbir-usmani", "Shabbīr Aḥmad ʿUthmānī", "شبیر احمد عثمانی", (1305, 1887), (1369, 1949), "Exegete and hadith commentator; author of Fatḥ al-Mulhim."),
    ("aziz-rahman-usmani", "ʿAzīz al-Raḥmān ʿUthmānī", "عزیز الرحمٰن عثمانی", (None, 1859), (None, 1928), "First Grand Muftī of Darul Uloom Deoband."),
    ("habib-rahman-usmani", "Ḥabīb al-Raḥmān ʿUthmānī", "حبیب الرحمٰن عثمانی", None, None, "Rector of Deoband, 1928–29."),
    ("murtaza-chandpuri", "Murtaḍā Ḥasan Chāndpūrī", "مرتضیٰ حسن چاندپوری", (1285, 1868), None, "Deobandi debater."),
    ("sanaullah-amritsari", "Thanāʾullāh Amritsarī", "ثناء اللہ امرتسری", (None, 1868), (None, 1948), "Ahl-e Hadith scholar and debater."),
    ("fazlur-rahman-ganjmuradabadi", "Faḍl al-Raḥmān Ganj Murādābādī", "فضل رحمان گنج مرادآبادی", (1208, 1793), (1313, 1895), "Naqshbandī shaykh of Ganj Moradabad."),
    ("abdur-rahman-panipati", "ʿAbd al-Raḥmān Pānīpatī", "عبد الرحمن پانی پتی", None, None, "Hadith scholar of Panipat."),
    ("hussain-yamani", "Ḥusayn ibn Muḥsin al-Anṣārī al-Yamānī", "حسين بن محسن الأنصاري اليماني", None, None, "Yemeni hadith scholar in Bhopal."),
    ("hakim-mahmud-khan", "Ḥakīm Maḥmūd Khān Dihlawī", "حکیم محمود خان", None, None, "Delhi physician."),
    ("habibullah-qurayshi", "Ḥabībullāh Qurayshī", "حبیب اللہ قریشی", (None, 1865), (None, 1943), "Co-founder of the Hathazari madrasa."),
    ("azizur-rahman-sufi", "Ṣūfī ʿAzīz al-Raḥmān", "صوفی عزیز الرحمن", None, None, "Co-founder of the Hathazari madrasa."),
    ("shah-ahmad-hasan", "Shāh Aḥmad Ḥasan", "شاہ احمد حسن", None, None, "Chittagong scholar."),
    ("mukhtar-ansari", "Mukhtār Aḥmad Anṣārī", "مختار احمد انصاری", (None, 1880), (None, 1936), "Physician and nationalist leader in Delhi.")]:
    kw = {}
    if b: kw["born"] = date(hy=b[0], gy=b[1])
    if d: kw["died"] = date(hy=d[0], gy=d[1])
    stub(sid, en, ar, desc=desc, cites=[U], honorific=sid not in {'mukhtar-ansari'}, **kw)

# =====================================================================
# 1. Maḥmūd Ḥasan Deobandī — Shaykh al-Hind
S = person("mahmud-hasan", "Maḥmūd Ḥasan Deobandī", "محمود حسن دیوبندی", title="Shaykh al-Hind",
    summary=("Son of Ḏhū al-Fiqār ʿAlī, one of Deoband's founders. He was the madrasa's first student, and later its principal (1890–1915) "
             "and senior hadith teacher. He planned the anti-British Silk Letter scheme, was arrested in the Hijaz and held in Malta "
             "from 1917 to 1920, and on his return backed the Khilafat and non-cooperation campaigns."),
    legacy="Trained almost every leading Deobandi scholar of the next generation and tied the seminary to the freedom movement.",
    tags=["Ḥanafī", "Chishtī-Ṣābirī", "Deobandī"], cites=["wiki-mahmud", "tarajm-mahmud"],
    names=[("laqab", "en", "Asīr-e Mālṭā (prisoner of Malta)"), ("nisba", "en", "al-ʿUthmānī")])
life(S, "birth", date(hy=1268, gy=1851, approx=True), place="bareilly", conf="attested", cites=["wiki-mahmud"])
life(S, "death", date(hy=1339, hm=3, hd=18, gy=1920, gm=11, gd=30), place="delhi", conf="attested", cites=["wiki-mahmud"])
lived(S, "deoband", "taught", cites=["wiki-mahmud"]); lived(S, "malta", "lived", note="prisoner, 1917–20", cites=["wiki-mahmud"])
lived(S, "deoband", "buried", note="Qabrastān-e Qāsmī, Deoband, beside Nānautavī", conf="attested", cites=["wiki-mahmud"])
member(S, "darul-uloom-deoband", "student", note="its first student", conf="attested", cites=["wiki-mahmud"])
member(S, "darul-uloom-deoband", "head_teacher", note="principal 1890–1915", conf="attested", cites=["wiki-mahmud"])
took_part(S, "silk-letter", role="leader", cites=["wiki-mahmud"])
took_part(S, "shahjahanpur-1876", note="accompanied Nānautavī", cites=["tareen-shahjahanpur"])
rel("studied_under", S, QN, "hadith (the Six Books)", note="The Six Books of hadith; long companionship", place="meerut", years="c.1869–1872",
    conf="attested", cites=["tarajm-mahmud", "dud-ar-qn", "madarisweb-asanid"], rank=1)
rel("studied_under", S, "mahtab-ali", ["Persian", "Arabic basics"], cites=["wiki-mahmud"])
rel("studied_under", S, "mulla-mahmud", note="Dars-e Niẓāmī at Deoband", cites=["wiki-mahmud"])
rel("studied_under", S, "yaqub-nanautavi", cites=["wiki-mahmud"])
rel("khalifa_of", S, "rashid-gangohi", note="Khalīfa in taṣawwuf", cites=["wiki-mahmud"])
rel("khalifa_of", S, "imdadullah", cites=["wiki-mahmud"])
rel("ijaza_from", S, "abdul-ghani-mujaddidi", "hadith", cites=["tarajm-mahmud"])
rel("studied_under", S, "zulfiqar-ali", note="His father: Arabic literature", cites=["wiki-mahmud"])
for sid in ["anwar-shah-kashmiri", "ashraf-ali-thanwi", "husain-ahmad-madani", "ubaidullah-sindhi", "kifayatullah", "shabbir-usmani",
            "ilyas-kandhlawi", "izaz-ali-amrohi", "manazir-gilani", "qari-tayyib"]:
    rel("studied_under", sid, S, cites=["wiki-mahmud"])
rel("companion_of", S, "mukhtar-ansari", note="Host and physician in Delhi", cites=["wiki-mahmud"])
for wid, tr, orig, gen, lang, d, r in [
    ("tarjuma-shaykh-al-hind", "Tarjuma-e Shaykh al-Hind", "ترجمہ شیخ الہند", "tafsir", "ur", "Urdu translation of the Qur'an; his notes reach Sūrat al-Nisāʾ and were completed by Shabbīr Aḥmad ʿUthmānī.", 1),
    ("adilla-e-kamila", "Adilla-e Kāmila", "ادلۂ کاملہ", "polemics", "ur", "Ten questions put to Ahl-e Hadith scholars, written at Nānautavī's request.", 2),
    ("izah-al-adilla", "Īḍāḥ al-Adilla", "ایضاح الادلہ", "polemics", "ur", "Defence of Adilla-e Kāmila against a rebuttal.", 3),
    ("al-abwab-wal-tarajim", "al-Abwāb wa al-Tarājim li al-Bukhārī", "الأبواب والتراجم للبخاري", "hadith", "ar", "Study of Bukhārī's chapter headings, begun in Malta.", 4),
    ("ahsan-al-qira", "Aḥsan al-Qirā", "احسن القریٰ", "fiqh", "ur", "Defends Gangohī's ruling on Friday prayer in villages.", 5),
    ("juhd-al-muqill", "Juhd al-Muqill", "جہد المقل", "kalam", "ur", "Two volumes on the divine attributes.", 6)]:
    work(wid, tr, orig, by=S, genres=gen, langs=lang, desc=d, rank=r, cites=["wiki-mahmud"])
work("abu-dawud-edition", "Sunan Abī Dāwūd (edition with notes)", by=S, role="editor", genres="hadith", langs="ar", rank=7,
     desc="Edited and annotated for the Mujtabāʾī Press, Delhi, 1900.", cites=["wiki-mahmud"])
work_rel("izah-al-adilla", "reply_to", "adilla-e-kamila")

# 2. Aḥmad Ḥasan Amrohī
S = person("ahmad-hasan-amrohi", "Aḥmad Ḥasan Amrohī", "سید احمد حسن محدث امروہی", title="Qāsim-e Thānī (the second Qāsim)",
    summary=("Born in Amroha. He read the rational and religious sciences with Nānautavī in Meerut, then graduated from Deoband alongside "
             "Maḥmūd Ḥasan in 1873. He was the first principal of Madrasa Shahi in Moradabad (1879–85), revived the madrasa at Amroha's "
             "Jama Masjid, and debated Arya Samaj and Ahmadi speakers."),
    legacy="Called 'the second Qāsim' for how closely he carried on Nānautavī's theology and madrasa-building.",
    tags=["Ḥanafī", "Māturīdī", "Chishtī-Ṣābirī", "Deobandī"], cites=["wiki-amrohi", "tarajm-amrohi"],
    names=[("laqab", "en", "Sayyid al-ʿUlamāʾ"), ("nisba", "en", "al-Ḥusaynī al-Amrohī")])
life(S, "birth", date(gy=1850, approx=True), place="amroha", cites=["wiki-amrohi"])
life(S, "death", date(hy=1330, hm=3, gy=1912, gm=3, gd=18), place="amroha", conf="attested", cites=["wiki-amrohi", "tarajm-amrohi"], note="Died of plague.")
for pl in ["meerut", "deoband", "khurja", "moradabad", "sambhal", "kanpur"]: lived(S, pl, "taught" if pl not in ("meerut", "deoband") else "studied", cites=["tarajm-amrohi"])
lived(S, "amroha", "buried", note="Jama Masjid precinct, Amroha", conf="uncertain", cites=["tarajm-abdurrahman"])
member(S, "madrasa-shahi", "head_teacher", note="first principal, 1879–85", conf="attested", cites=["wiki-shahi", "wiki-amrohi"])
member(S, "darul-uloom-deoband", "student", note="graduated 1290 AH / 1873", conf="attested", cites=["wiki-amrohi"])
rel("studied_under", S, QN, ["rational sciences", "kalām", "the Ṣaḥīḥayn"], note="The full syllabus, rational sciences and kalām",
    place="meerut", years="c.1286–1290 AH", conf="attested", cites=["tarajm-amrohi", "dud-ar-qn"], rank=2)
rel("ijaza_from", S, "ahmad-ali-saharanpuri", "hadith", cites=["tarajm-amrohi"])
rel("ijaza_from", S, "abdul-ghani-mujaddidi", "hadith", cites=["tarajm-amrohi"])
rel("ijaza_from", S, "abdur-rahman-panipati", "hadith", cites=["tarajm-amrohi"])
rel("khalifa_of", S, "imdadullah", note="Taṣawwuf, in Mecca", cites=["tarajm-amrohi"])
rel("studied_under", "murtaza-chandpuri", S, ["logic", "philosophy"], cites=["shamela-budur"])
rel("fellow_student", S, "mahmud-hasan", note="Classmates; graduated together in 1873", conf="attested", cites=["wiki-amrohi"])
rel("fellow_student", S, "fakhrul-hasan-gangohi", note="Classmates; graduated together", cites=["wiki-amrohi"])
rel("companion_of", S, "sanaullah-amritsari", note="Fellow debater against Ahmadis, Rampur 1909", cites=["wiki-amrohi"])
rel("companion_of", S, "hafiz-muhammad-ahmad", note="Led his funeral prayer", cites=["wiki-amrohi"])
work("ifadat-e-ahmadiyya", "Ifādāt-e Aḥmadiyya", "افادات احمدیہ", by=S, genres="kalam", langs="ur", rank=1, desc="His collected expositions.", cites=["tarajm-amrohi"])
work("izalat-al-waswas", "Izālat al-Waswās", "ازالۃ الوسواس", by=S, genres="polemics", langs="ur", rank=2, desc="Rebuttal of doubts (topic not verified).", conf="uncertain", cites=["tarajm-amrohi"])
work("al-malumat-al-ilahiyya", "al-Maʿlūmāt al-Ilāhiyya", "المعلومات الالٰہیہ", by=S, genres="kalam", langs="ur", rank=3, desc="On divine knowledge.", conf="uncertain", cites=["tarajm-amrohi"])
work("amrohi-fatawa", "Fatāwā (manuscript)", by=S, genres="fiqh", langs="ur", rank=4, status="manuscript", desc="His legal rulings, held in Phalauda and Rampur libraries.", cites=["tarajm-amrohi"])

# 3. Fakhr al-Ḥasan Gangohī
S = person("fakhrul-hasan-gangohi", "Fakhr al-Ḥasan Gangohī", "فخر الحسن گنگوہی",
    summary=("A close companion of Nānautavī who travelled with him and lived in his household. He studied hadith with Gangohī and medicine "
             "in Delhi, graduated from Deoband in 1873 and spent his last years practising medicine in Kanpur. He wrote down Nānautavī's "
             "public debates with Christian and Hindu speakers."),
    legacy="The main eyewitness recorder of Nānautavī's debates, and author of a standard short commentary on Abū Dāwūd.",
    tags=["Ḥanafī", "Deobandī"], note="Not to be confused with Fakhrul Hasan Muradabadi (d. 1400 AH).", cites=["tarajm-fakhr"])
life(S, "death", date(hy=1315, gy=1897), place="kanpur", conf="attested", cites=["tarajm-fakhr"])
lived(S, "deoband", "studied", cites=["tarajm-fakhr"]); lived(S, "kanpur", "lived", note="physician", cites=["tarajm-fakhr"])
member(S, "darul-uloom-deoband", "student", note="graduated 1290 AH", cites=["wiki-amrohi"])
took_part(S, "shahjahanpur-1876", note="recorded the debates", cites=["tareen-shahjahanpur"]); took_part(S, "shahjahanpur-1877", note="recorded the debates", cites=["hira-shahjahanpur"])
rel("studied_under", S, QN, "the Ṣaḥīḥayn", note="The Ṣaḥīḥayn and long companionship at home and on travel", conf="attested", cites=["tarajm-fakhr", "dud-ar-qn", "madarisweb-asanid"], rank=3)
rel("studied_under", S, "rashid-gangohi", "hadith", cites=["tarajm-fakhr"])
rel("studied_under", S, "hakim-mahmud-khan", "medicine", cites=["tarajm-fakhr"])
rel("fellow_student", S, "mahmud-hasan", note="Classmates", cites=["wiki-amrohi"])
work("al-taliq-al-mahmud", "al-Taʿlīq al-Maḥmūd ʿalā Sunan Abī Dāwūd", "التعليق المحمود على سنن أبي داود", by=S, genres="hadith", langs="ar", rank=1,
     desc="Short marginal commentary often printed with Sunan Abī Dāwūd.", conf="attested", cites=["tarajm-fakhr"])
work("hashiya-ibn-majah-fakhr", "Ḥāshiya ʿalā Sunan Ibn Mājah", "حاشية على سنن ابن ماجه", by=S, genres="hadith", langs="ar", rank=2, desc="Brief glosses.", cites=["tarajm-fakhr"])
work("hashiya-talkhis", "Ḥāshiya ʿalā Talkhīṣ al-Miftāḥ", "حاشية على تلخيص المفتاح", by=S, genres="rhetoric", langs="ar", rank=3, desc="Glosses on a classic of Arabic rhetoric.", cites=["tarajm-fakhr"])

# 4. ʿAbd al-ʿAlī Meeruthī
S = person("abdul-ali-meeruti", "ʿAbd al-ʿAlī Meeruthī", "عبد العلی میرٹھی",
    summary=("From a village near Meerut, he studied at Deoband under Nānautavī and the Saharanpur hadith teachers. From 1312 AH he taught "
             "hadith for decades at the Ḥusayn Bakhsh madrasa in Delhi and became one of the city's leading hadith teachers."),
    legacy="Carried Nānautavī's hadith teaching into Delhi's madrasas; Muftī Kifāyatullāh was among his students.",
    tags=["Ḥanafī", "Deobandī"], cites=["tarajm-abdulali", "dud-ar-qn"])
life(S, "death", date(hy=1347, hm=5, hd=12, gy=1928, gm=10, approx=True), place="delhi", conf="attested", cites=["tarajm-abdulali"])
lived(S, "delhi", "taught", cites=["tarajm-abdulali"])
lived(S, "delhi", "buried", note="Graveyard of Shāh Walīullāh's family (Mehdiyan), Delhi", conf="attested", cites=["tarajm-abdulali"])
rel("studied_under", S, QN, "the Ṣaḥīḥayn", note="The Ṣaḥīḥayn and the general syllabus", place="deoband", conf="attested", cites=["tarajm-abdulali", "dud-ar-qn"], rank=4)
rel("studied_under", S, "ahmad-ali-saharanpuri", "hadith", cites=["tarajm-abdulali"])
rel("studied_under", S, "faiz-hasan-saharanpuri", "Arabic literature", cites=["tarajm-abdulali"])
rel("studied_under", "kifayatullah", S, "hadith", cites=["tarajm-abdulali"])

# 5. Ḥakīm Manṣūr ʿAlī Khān Murādābādī
S = person("mansur-ali-khan", "Ḥakīm Manṣūr ʿAlī Khān Murādābādī", "منصور علی خان مرادآبادی",
    summary=("A physician and scholar from Moradabad who studied with Nānautavī and lived with him for a time, and took hadith from Aḥmad ʿAlī "
             "Sahāranpūrī. He taught for many years at the medical school in Hyderabad, then retired to Mecca, where he died."),
    legacy="His Madhhab-e Manṣūr is an early source for Nānautavī's hadith studies.",
    tags=["Ḥanafī", "Deobandī"], cites=["tarajm-mansur", "madarisweb-asanid"])
life(S, "death", date(hy=1337, gy=1918), place="mecca", conf="attested", cites=["tarajm-mansur"])
lived(S, "moradabad", "born", cites=["tarajm-mansur"]); lived(S, "hyderabad", "taught", note="medical school", cites=["tarajm-mansur"])
rel("studied_under", S, QN, "the Ṣaḥīḥayn", note="The Ṣaḥīḥayn and general sciences; lived with him", conf="attested", cites=["tarajm-mansur", "dud-ar-qn"], rank=5)
rel("studied_under", S, "ahmad-ali-saharanpuri", "hadith", cites=["tarajm-mansur"])
work("madhhab-e-mansur", "Madhhab-e Manṣūr", "مذہب منصور", by=S, genres="fiqh", langs="ur", rank=1, desc="Two volumes defending the Ḥanafī school from hadith.", cites=["tarajm-mansur"])
work("mayar-al-adwiya", "Miʿyār al-Adwiya", "معيار الأدوية", by=S, genres="medicine", rank=2, desc="On pharmacology.", cites=["tarajm-mansur"])
work("al-fath-al-mubin-mansur", "al-Fatḥ al-Mubīn", "الفتح المبين", by=S, rank=3, desc="Topic not verified.", conf="uncertain", cites=["tarajm-mansur"])

# 6. Ḥāfiẓ ʿAbd al-Raḥmān Amrohī
S = person("abdur-rahman-amrohi", "Ḥāfiẓ ʿAbd al-Raḥmān Amrohī", "حافظ عبد الرحمن امروہی",
    summary=("A hadith scholar described as one of Nānautavī's last students, with whom he read Tirmidhī. He went on to study hadith under "
             "Aḥmad Ḥasan Amrohī at Moradabad, later led teaching at Amroha's madrasa, and taught hadith at Dabhel."),
    legacy="Took over Amroha's hadith chair, linking Nānautavī's teaching to the twentieth century.",
    tags=["Ḥanafī", "Chishtī", "Deobandī"], cites=["tarajm-abdurrahman"])
life(S, "death", date(hy=1367, hm=6, hd=23, gy=1948, gm=5, approx=True), place="amroha", conf="attested", cites=["tarajm-abdurrahman"])
lived(S, "bombay", "born", conf="reported", cites=["tarajm-abdurrahman"]); lived(S, "dabhel", "taught", cites=["tarajm-abdurrahman"])
lived(S, "amroha", "buried", note="Jama Masjid, Amroha, beside Aḥmad Ḥasan Amrohī", cites=["tarajm-abdurrahman"])
rel("studied_under", S, QN, "Jāmiʿ al-Tirmidhī", note="Tirmidhī; one of his last students", years="c.1296–97 AH", conf="attested", cites=["tarajm-abdurrahman"], rank=6)
rel("studied_under", S, "ahmad-hasan-amrohi", "hadith", cites=["tarajm-abdurrahman"])
rel("studied_under", S, "rashid-gangohi", "hadith", cites=["tarajm-abdurrahman"])
rel("bayah_to", S, "imdadullah", cites=["tarajm-abdurrahman"])
rel("ijaza_from", S, "hussain-yamani", "hadith", cites=["tarajm-abdurrahman"])
work("hashiya-mukhtasar-maani", "Ḥāshiya ʿalā Mukhtaṣar al-Maʿānī", by=S, genres="rhetoric", langs="ar", rank=1, desc="Glosses on a rhetoric textbook.", cites=["tarajm-abdurrahman"])
work("hawashi-mutawwal", "Ḥawāshī ʿalā al-Muṭawwal", by=S, genres="rhetoric", langs="ar", rank=2, desc="Glosses on al-Taftāzānī's Muṭawwal.", cites=["tarajm-abdurrahman"])
work("hashiya-baydawi", "Ḥāshiya ʿalā Tafsīr al-Bayḍāwī", by=S, genres="tafsir", langs="ar", rank=3, desc="Glosses on al-Bayḍāwī's commentary.", cites=["tarajm-abdurrahman"])

# 7. Ismāʿīl Kōlī
S = person("ismail-koli", "Ismāʿīl ibn ʿAbd al-Jalīl Kōlī", "اسماعیل کولی علی گڑھی",
    summary=("An Aligarh scholar who, after his early studies, read the Ṣaḥīḥ and Sunan collections with Nānautavī. Nuzhat al-Khawāṭir "
             "describes him as relying directly on the Qur'an and hadith, and he wrote against Ahmadi claims."),
    legacy="Wrote one of the early rebuttals of the claim to be 'like the Messiah'.",
    tags=["Ḥanafī"], cites=["tarajm-ismail"])
life(S, "birth", date(hy=1263, gy=1846), place="aligarh", conf="attested", cites=["tarajm-ismail"])
life(S, "death", date(hy=1311, gy=1893), place="aligarh", conf="attested", cites=["tarajm-ismail"])
rel("studied_under", S, QN, "the Ṣiḥāḥ and Sunan", note="The Ṣiḥāḥ and Sunan collections", conf="attested", cites=["tarajm-ismail"], rank=7)
rel("studied_under", S, "faiz-hasan-saharanpuri", cites=["tarajm-ismail"])
work("al-qawl-al-sarih-masih", "al-Qawl al-Ṣarīḥ fī Takdhīb Mathīl al-Masīḥ", by=S, genres="polemics", rank=1, desc="Rebuttal of the claim to be 'like the Messiah'.", cites=["tarajm-ismail"])
work("al-qawl-al-sawab-mawlid", "al-Qawl al-Ṣawāb fī al-Mawlid wa al-Qiyām", by=S, genres="fiqh", rank=2, desc="On mawlid gatherings and standing during them.", cites=["tarajm-ismail"])

# 8. ʿAbd Allāh Anṣārī Anbahṭawī
S = person("abdullah-ambehtvi", "ʿAbd Allāh Anṣārī Anbahṭawī", "عبد اللہ انصاری انبہٹوی",
    summary=("A nephew of Yaʿqūb Nānautavī and a relative of Nānautavī by marriage. He studied with both, and in 1311 AH was made religious "
             "preacher at the Aligarh college because of that connection."),
    legacy="A Deoband-linked religious presence inside Sir Sayyid's Aligarh college.",
    tags=["Ḥanafī", "Deobandī"], cites=["tarajm-abdullah"])
life(S, "death", date(hy=1344, gy=1925, approx=True), place="bombay", cites=["tarajm-abdullah"])
lived(S, "ambehta", "born", cites=["tarajm-abdullah"]); lived(S, "aligarh-college", "taught", cites=["tarajm-abdullah"])
member(S, "aligarh-college", "teacher", note="religious preacher from 1311 AH", cites=["tarajm-abdullah"])
rel("studied_under", S, QN, note="Student, and related to him by marriage", conf="attested", cites=["tarajm-abdullah"], rank=8)
rel("studied_under", S, "yaqub-nanautavi", note="His maternal uncle", cites=["tarajm-abdullah"])
rel("ijaza_from", S, "ahmad-ali-saharanpuri", cites=["tarajm-abdullah"])
rel("studied_under", S, "imdadullah", note="Read the Masnavī with him", cites=["tarajm-abdullah"])

# 9. ʿAbd al-Wāḥid Bangālī
S = person("abdul-wahid-bengali", "ʿAbd al-Wāḥid Bangālī", "عبد الواحد بنگالی", title="Munāẓir-e Islām",
    summary=("A Chittagong scholar who spent about fourteen years at Deoband studying with Qāsim and Yaʿqūb Nānautavī. Back in Bengal he "
             "helped start the Deobandi movement there and co-founded the Hathazari madrasa in 1896."),
    legacy="Brought the Deoband model to East Bengal; Hathazari is now one of the largest Qawmi madrasas.",
    tags=["Ḥanafī", "Naqshbandī-Mujaddidī", "Deobandī"], cites=["wiki-abdulwahid"],
    names=[("shuhra", "bn", "আব্দুল ওয়াহেদ বাঙ্গালী")])
life(S, "birth", date(hy=1268, gy=1851, approx=True), place="chittagong", cites=["wiki-abdulwahid"])
life(S, "death", date(gy=1905), place="chittagong", cites=["wiki-abdulwahid"])
lived(S, "deoband", "studied", note="about fourteen years", cites=["wiki-abdulwahid"])
lived(S, "chittagong", "buried", note="Munshipara, Kharandwip", cites=["wiki-abdulwahid"])
member(S, "hathazari", "co_founder", note="1896", cites=["wiki-abdulwahid"])
rel("studied_under", S, QN, "hadith", note="Hadith; Nānautavī sent him to Imdādullāh for taṣawwuf", place="deoband", years="c.1870s", conf="reported", cites=["wiki-abdulwahid"], rank=9)
rel("studied_under", S, "yaqub-nanautavi", cites=["wiki-abdulwahid"])
rel("khalifa_of", S, "fazlur-rahman-ganjmuradabadi", note="Naqshbandī", cites=["wiki-abdulwahid"])
rel("studied_under", "shah-ahmad-hasan", S, cites=["wiki-abdulwahid"])
for pid in ["habibullah-qurayshi", "azizur-rahman-sufi"]:
    member(pid, "hathazari", "co_founder", cites=["wiki-abdulwahid"])

# Family: Ḥāfiẓ Muḥammad Aḥmad (son) — shown as family, not student
S = person("hafiz-muhammad-ahmad", "Ḥāfiẓ Muḥammad Aḥmad", "حافظ محمد احمد", title="Shams al-ʿUlamāʾ",
    summary=("Nānautavī's son. He was rector (muhtamim) of Darul Uloom Deoband from 1895 to 1928, and Grand Muftī of Hyderabad State from "
             "1922 to 1925. He was about eighteen when his father died; his recorded teachers are Maḥmūd Ḥasan, Yaʿqūb Nānautavī and Gangohī."),
    legacy="Led Deoband through its expansion into a major institution for more than thirty years.",
    tags=["Ḥanafī", "Deobandī"], cites=["wiki-hafizahmad"])
life(S, "birth", date(hy=1279, gy=1862), place="nanauta", cites=["wiki-hafizahmad"])
life(S, "death", date(hy=1347, hm=5, hd=3, gy=1928, gm=10, gd=18), conf="attested", cites=["wiki-hafizahmad"], note="Died on a train near Nizamabad.")
lived(S, "hyderabad", "buried", note="Khiṭṭa-e Ṣāliḥīn, Hyderabad", cites=["wiki-hafizahmad"])
member(S, "darul-uloom-deoband", "rector", note="1895–1928", conf="attested", cites=["wiki-hafizahmad"])
rel("family", QN, S, note="His son", conf="attested", cites=["wiki-hafizahmad"], rank=20)
rel("studied_under", S, "mahmud-hasan", cites=["wiki-hafizahmad"]); rel("studied_under", S, "yaqub-nanautavi", cites=["wiki-hafizahmad"])
rel("studied_under", S, "rashid-gangohi", cites=["wiki-hafizahmad"]); rel("bayah_to", S, "imdadullah", cites=["wiki-hafizahmad"])
rel("family", S, "qari-tayyib", note="His son", cites=["wiki-hafizahmad"])
for sid in ["anwar-shah-kashmiri", "shabbir-usmani", "husain-ahmad-madani"]:
    rel("studied_under", sid, S, cites=["wiki-hafizahmad"])
