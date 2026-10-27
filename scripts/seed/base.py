"""Sources, places, institutions, events and the centre record: Sheikh Qāsim Nānautavī."""
from lib import *

# ---------- sources ----------
source("unverified", "Not yet checked against a source (general knowledge)", type="note")
source("wiki-qn", "Wikipedia — Qasim Nanawtawi", "https://en.wikipedia.org/wiki/Qasim_Nanawtawi")
source("wiki-ar-qn", "Wikipedia (Arabic) — محمد قاسم النانوتوي", "https://ar.wikipedia.org/wiki/محمد_قاسم_النانوتوي")
source("deoband-org-qn", "deoband.org — The Proof of Islam, Shaykh Qasim al-Nanotwi (tr. of Nuzhat al-Khawatir)", "https://www.deoband.org/2013/03/biographical-notes/the-proof-of-islam-shaykh-qasim-al-nanotwi/")
source("tarajm-qn", "Nuzhat al-Khawatir — entry on Qasim Nanautavi (tarajm.com)", "https://tarajm.com/people/95362", note="its Gregorian years are wrong; Hijri used")
source("dud-cofounders", "Darul Uloom Deoband — co-founders list (official site)", "https://dud.edu.in/index.php/en/co-founders-list")
source("dud-ar-qn", "Darul Uloom Deoband (Arabic) — al-Imam Muhammad Qasim al-Nanautawi", "https://darululoom-deoband.com/arabicarticles/archives/3529")
source("rekhta-qn", "Rekhta — Mohammad Qasim Nanotvi profile", "https://www.rekhta.org/poets/mohammad-qasim-nanotvi/profile")
source("ummid-qn", "Ummid.com — Qasim Nanautawi, the scholar who awakened Muslims through education", "https://ummid.com/news/2022/july/31.07.2022/qasim-nanautawi-the-scholar-who-awakened-muslims-through-education.html")
source("wiki-shahi", "Wikipedia — Madrasa Shahi", "https://en.wikipedia.org/wiki/Madrasa_Shahi")
source("madarisweb-asanid", "madarisweb — Nanautavi's hadith chains (asanid)", "https://www.madarisweb.com/ar/articles/3710")
source("deoband-org-gangohi", "deoband.org — The Epitome of Shari'a and Tariqa (Gangohi)", "https://www.deoband.org/2009/04/biographical-notes/the-epitome-of-sharia-and-tariqa/")
source("wiki-siddiqi", "Wikipedia — Siddiqi family of Nanauta", "https://en.wikipedia.org/wiki/Siddiqi_family_of_Nanauta")
source("tareen-shahjahanpur", "SherAli Tareen, 'The Polemic of Shahjahanpur', Islamic Studies", "https://journals.iiu.edu.pk/index.php/islamicstudies/article/view/3530", type="article")
source("hira-shahjahanpur", "Hira Online — introduction to Mubahatha Shahjahanpur", "https://hira-online.com/تعارف-مباحثہ-شاہ-جہاں-پور/")

# ---------- places ----------
place("hind", "Hindustan", "الهند", type="region", region="Hind")
place("hijaz", "Hijaz", "الحجاز", type="region", region="Hijaz")
place("bengal", "Bengal", type="region", parent="hind", region="Hind")
for pid, en, parent in [
    ("saharanpur", "Saharanpur", "hind"), ("nanauta", "Nanauta", "saharanpur"), ("deoband", "Deoband", "saharanpur"),
    ("gangoh", "Gangoh", "saharanpur"), ("ambehta", "Ambehta", "saharanpur"), ("delhi", "Delhi", "hind"), ("meerut", "Meerut", "hind"),
    ("moradabad", "Moradabad", "hind"), ("amroha", "Amroha", "hind"), ("thana-bhawan", "Thana Bhawan", "hind"), ("shamli", "Shamli", "hind"),
    ("shahjahanpur", "Shahjahanpur", "hind"), ("chandapur", "Chandapur, near Shahjahanpur", "hind"), ("kanpur", "Kanpur", "hind"),
    ("aligarh", "Koil (Aligarh)", "hind"), ("bareilly", "Bareilly", "hind"), ("rampur", "Rampur", "hind"), ("roorkee", "Roorkee", "hind"),
    ("hyderabad", "Hyderabad (Deccan)", "hind"), ("bombay", "Bombay", "hind"), ("khurja", "Khurja", "hind"), ("sambhal", "Sambhal", "hind"),
    ("ganj-moradabad", "Ganj Moradabad", "hind"), ("lucknow", "Lucknow", "hind"), ("kairana", "Kairana", "hind"), ("jhinjhana", "Jhinjhana", "hind"),
    ("chittagong", "Chittagong", "bengal"), ("hathazari", "Hathazari", "bengal"), ("kolkata", "Kolkata", "bengal"),
    ("mecca", "Mecca", "hijaz"), ("medina", "Medina", "hijaz"), ("malta", "Malta", None), ("dabhel", "Dabhel", "hind"),
    ("aligarh-college", "Aligarh", "hind")]:
    place(pid, en, type="town", parent=parent)

# ---------- institutions ----------
institution("darul-uloom-deoband", "Darul Uloom Deoband", "دار العلوم دیوبند", place="deoband",
            founded=date(hy=1283, hm=1, hd=15, gy=1866, gm=5, gd=30), cites=["dud-cofounders", "wiki-qn"])
institution("madrasa-shahi", "Madrasa Shahi (Madrasatul Ghuraba), Moradabad", "مدرسہ شاہی مرادآباد", place="moradabad",
            founded=date(gy=1879), cites=["wiki-shahi"])
institution("mazahir-uloom", "Mazahir Uloom, Saharanpur", "مظاہر علوم سہارنپور", place="saharanpur", founded=date(hy=1283, gy=1866), cites=["unverified"])
institution("delhi-college", "Delhi College", place="delhi", type="college", founded=date(gy=1825, approx=True), cites=["unverified"])
institution("matba-ahmadi", "Matbaʿ Aḥmadī press, Delhi", type="press", place="delhi", founded=date(gy=1845), cites=["unverified"])
institution("hathazari", "Al-Jamiatul Ahlia Darul Ulum Moinul Islam, Hathazari", place="hathazari", founded=date(gy=1896), cites=["unverified"])
institution("aligarh-college", "Muhammadan Anglo-Oriental College, Aligarh", type="college", place="aligarh-college", founded=date(gy=1875), cites=["unverified"])

# ---------- events ----------
event("shamli-1857", "Battle of Shāmlī", date(hy=1273, gy=1857), place="shamli", cites=["wiki-qn"])
event("shahjahanpur-1876", "Mela Khuda Shanasi (religious fair), Shahjahanpur — first", date(hy=1293, gy=1876, gm=5, gd=8), place="chandapur", cites=["dud-cofounders", "tareen-shahjahanpur"])
event("shahjahanpur-1877", "Mela Khuda Shanasi (religious fair), Shahjahanpur — second", date(hy=1294, gy=1877, gm=3), place="chandapur", cites=["dud-cofounders", "tareen-shahjahanpur"])
event("deoband-founding", "Founding of Darul Uloom Deoband", date(hy=1283, hm=1, hd=15, gy=1866, gm=5, gd=30), place="deoband", cites=["dud-cofounders"])
event("silk-letter", "Silk Letter Movement", date(gy=1913, approx=True, text="1913–1920"), cites=["unverified"])

# ---------- the centre record ----------
QN = person("qasim-nanautavi", "Qāsim Nānautavī", "محمد قاسم النانوتوي", title="Ḥujjat al-Islām",
    summary=("Born in Nanauta near Saharanpur into the Ṣiddīqī family. He studied in Deoband, Saharanpur and then Delhi, where Mamlūk ʿAlī "
             "took him through the whole curriculum and Shāh ʿAbd al-Ghanī taught him hadith. He fought at Shāmlī in 1857, and in 1866 "
             "helped found the madrasa at Deoband that became Darul Uloom. In his last years he debated Christian missionaries and the "
             "Arya Samaj at the Shahjahanpur fairs and set up madrasas across the region."),
    legacy="Co-founder of Darul Uloom Deoband, the root of the Deobandi movement and of thousands of madrasas worldwide.",
    tags=["Ḥanafī", "Māturīdī", "Chishtī-Ṣābirī", "Deobandī"],
    note="Sha'ban–Ramadan 1248 AH falls around Dec 1832 – Feb 1833, so some sources give 1833.",
    cites=["wiki-qn", "deoband-org-qn", "dud-ar-qn"],
    names=[("ism", "ar", "محمد قاسم"), ("ism", "en", "Muḥammad Qāsim"),
           ("nasab", "en", "Muḥammad Qāsim ibn Asad ʿAlī ibn Ghulām Shāh"), ("nisba", "en", "al-Ṣiddīqī"), ("nisba", "en", "al-Nānautavī"),
           ("shuhra", "ur", "محمد قاسم نانوتوی")])
life(QN, "birth", date(hy=1248, hm=8, gy=1832, precision="month", text="Shaʿbān or Ramaḍān 1248 AH / 1832–33 CE"), place="nanauta",
     conf="attested", cites=["wiki-qn", "deoband-org-qn", "rekhta-qn"], note="Month given as Sha'ban or Ramadan.")
life(QN, "death", date(hy=1297, hm=5, hd=4, gy=1880, gm=4, gd=15), place="deoband", conf="attested", cites=["wiki-qn", "ummid-qn"],
     note="Thursday 4 Jumada al-Ula 1297, recorded by Yaqub Nanautavi; aged about 47.")
lived(QN, "nanauta", "born", cites=["wiki-qn"])
lived(QN, "deoband", "studied", note="Arabic grammar at Karamat Husain's madrasa", cites=["wiki-qn"])
lived(QN, "saharanpur", "studied", note="Persian", cites=["wiki-qn"])
lived(QN, "delhi", "studied", note="c.1844–51", conf="attested", cites=["wiki-qn"])
lived(QN, "meerut", "lived", note="worked at presses in Meerut, 1860s", cites=["deoband-org-qn"])
lived(QN, "deoband", "taught", cites=["wiki-qn"])
lived(QN, "deoband", "buried", note="Qabrastān-e Qāsmī, north of Darul Uloom Deoband", conf="attested", cites=["wiki-qn"])
member(QN, "darul-uloom-deoband", "co_founder", note="1866", conf="attested", cites=["wiki-qn", "dud-cofounders"])
member(QN, "madrasa-shahi", "founder", note="proposed and supervised its founding, 1879", conf="attested", cites=["wiki-shahi"])
member(QN, "matba-ahmadi", "editor", note="worked on Aḥmad ʿAlī's edition of Ṣaḥīḥ al-Bukhārī", conf="attested", cites=["wiki-qn"])
member(QN, "delhi-college", "student", note="enrolled, but studied mostly privately", conf="reported", cites=["wiki-qn"])
took_part(QN, "shamli-1857", note="fought alongside Imdādullāh and Gangohī", cites=["wiki-qn"])
took_part(QN, "deoband-founding", role="founder", cites=["dud-cofounders"])
took_part(QN, "shahjahanpur-1876", role="speaker", note="debated Christian and Arya Samaj speakers", cites=["dud-cofounders", "tareen-shahjahanpur"])
took_part(QN, "shahjahanpur-1877", role="speaker", cites=["dud-cofounders", "tareen-shahjahanpur"])
