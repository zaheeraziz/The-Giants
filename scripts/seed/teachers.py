"""Nanautavi's teachers, each with one level of their own network."""
from lib import *
U = "unverified"

source("wiki-mamluk", "Wikipedia — Mamluk Ali Nanautawi", "https://en.wikipedia.org/wiki/Mamluk_Ali_Nanautawi")
source("tarajm-mamluk", "Nuzhat al-Khawatir — Mamluk Ali (tarajm.com)", "https://tarajm.com/people/94896")
source("ulum-abdulghani", "Ulum al-Hadith — Shah Abd al-Ghani al-Mujaddidi", "https://ulumalhadith.com/?p=6844")
source("darulmaarif-abdulghani", "Dar al-Ma'arif — Shah Abd al-Ghani", "https://darulmaarif.com/?p=957")
source("wiki-ahmadali", "Wikipedia — Ahmad Ali Saharanpuri", "https://en.wikipedia.org/wiki/Ahmad_Ali_Saharanpuri")
source("ilmgate-ahmadali", "ilmgate — An introduction to Mawlana Ahmad Ali of Saharanpur", "https://www.ilmgate.org/an-introduction-to-hadhrat-mawlana-ahmad-ali-the-hadith-scholar-of-saharanpur/")
source("deoband-bukhari", "deoband.org — World's first critical edition of Sahih al-Bukhari", "https://www.deoband.org/2022/01/biographical-notes/worlds-first-critical-edition-sahih-albukhari/")
source("wiki-imdad", "Wikipedia — Imdadullah Muhajir Makki", "https://en.wikipedia.org/wiki/Imdadullah_Muhajir_Makki")
source("tarajm-imdad", "Nuzhat al-Khawatir — Imdadullah (tarajm.com)", "https://tarajm.com/people/93918")
source("deoband-imdad", "deoband.org — Shaykh Imdad Allah al-Faruqi al-Thanawi", "https://www.deoband.org/2009/03/biographical-notes/shaykh-imdad-allah-al-faruqi-al-thanawi/")
source("wiki-azurda", "Wikipedia — Sadruddin Khan Azurda Dehlawi", "https://en.wikipedia.org/wiki/Sadruddin_Khan_Azurda_Dehlawi")
source("rekhta-azurda", "Rekhta — Mufti Sadruddin Aazurda profile", "https://www.rekhta.org/poets/mufti-sadruddin-aazurda/profile?lang=ur")
source("kashmirlife-azurda", "Kashmir Life — Delhi's Kashmir teacher", "https://kashmirlife.net/delhis-kashmir-teacher-vol-18-issue-12-439483/")
source("wiki-mahtab", "Wikipedia — Mahtab Ali Deobandi", "https://en.wikipedia.org/wiki/Mahtab_Ali_Deobandi")

QN = "qasim-nanautavi"

# ---------- shared second-level people ----------
stub("shah-ishaq", "Shāh Muḥammad Isḥāq Dihlawī", "شاہ محمد اسحاق دہلوی", born=date(hy=1197, gy=1783), died=date(hy=1262, gy=1846),
     desc="Grandson of Shāh Walīullāh; leading hadith teacher of Delhi, later in Mecca.", cites=[U])
stub("shah-abdul-aziz", "Shāh ʿAbd al-ʿAzīz Dihlawī", "شاہ عبد العزیز دہلوی", born=date(hy=1159, gy=1746), died=date(hy=1239, gy=1824),
     desc="Eldest son of Shāh Walīullāh; the central hadith teacher of Delhi.", cites=[U])
stub("ilahi-bakhsh-kandhlawi", "Muftī Ilāhī Bakhsh Kāndhlawī", "الٰہی بخش کاندھلوی", born=date(hy=1162, gy=1748), died=date(hy=1245, gy=1829), desc="Jurist and student of Shāh ʿAbd al-ʿAzīz.", cites=[U])
stub("rashiduddin-khan", "Rashīd al-Dīn Khān Dihlawī", "رشید الدین خان دہلوی", died=date(hy=1249, gy=1833), desc="Delhi scholar in the Walīullāhī circle.", cites=[U])
stub("muhammad-qalandar", "Muḥammad Qalandar Jalālābādī", "محمد قلندر جلال آبادی", desc="Teacher of Mamlūk ʿAlī and Imdādullāh.")
stub("abu-said-mujaddidi", "Abū Saʿīd Mujaddidī", "ابو سعید مجددی", born=date(hy=1196, gy=1782), died=date(hy=1250, gy=1835), desc="Naqshbandī-Mujaddidī shaykh; father of Shāh ʿAbd al-Ghanī.")
stub("abid-sindhi", "Muḥammad ʿĀbid Sindhī", "محمد عابد سندھی", died=date(hy=1257, gy=1841), desc="Hadith master of Medina.", cites=[U])
stub("wajihuddin-saharanpuri", "Wajīh al-Dīn Sahāranpūrī", "وجیہ الدین سہارنپوری", desc="Saharanpur scholar; taught Aḥmad ʿAlī most of Bukhārī.")
stub("nur-muhammad-jhanjhanawi", "Miyānjī Nūr Muḥammad Jhanjhānawī", "میاں جی نور محمد جھنجھانوی", died=date(hy=1259, gy=1843), desc="Chishtī-Ṣābirī shaykh of Imdādullāh.", cites=[U])
stub("shah-rafiuddin-dehlawi", "Shāh Rafīʿ al-Dīn Dihlawī", "شاہ رفیع الدین دہلوی", died=date(hy=1233, gy=1818), desc="Son of Shāh Walīullāh; jurist and Qur'an translator.", cites=[U])
stub("fazl-imam-khairabadi", "Faḍl-i Imām Khayrābādī", "فضل امام خیرآبادی", died=date(hy=1244, gy=1829), desc="Master of the rational sciences.", cites=[U])
stub("khalil-ahmad", "Khalīl Aḥmad Sahāranpūrī", "خلیل احمد سہارنپوری", born=date(hy=1269, gy=1852), died=date(hy=1346, gy=1927), desc="Hadith scholar; author of Badhl al-Majhūd; grandson of Mamlūk ʿAlī.")
stub("ashraf-ali-thanwi", "Ashraf ʿAlī Thānawī", "اشرف علی تھانوی", born=date(hy=1280, gy=1863), died=date(hy=1362, gy=1943), desc="Ḥakīm al-Ummat; prolific Deobandi author.", cites=[U])
stub("shibli-nomani", "Shiblī Nuʿmānī", "شبلی نعمانی", born=date(gy=1857), died=date(gy=1914), desc="Historian; founder of Dār al-Muṣannifīn.", cites=[U])
stub("mehr-ali-shah", "Pīr Mehr ʿAlī Shāh", "پیر مہر علی شاہ", born=date(gy=1859), died=date(gy=1937), desc="Chishtī shaykh of Golra.", cites=[U])
stub("muhammad-ali-mongeri", "Muḥammad ʿAlī Mongerī", "محمد علی مونگیری", born=date(gy=1846), died=date(gy=1927), desc="Founder of Nadwat al-ʿUlamāʾ.", cites=[U])
stub("nur-muhammad-ludhianwi", "Nūr Muḥammad Ludhiānwī", "نور محمد لدھیانوی", desc="Author of the Nūrānī Qāʿida.")
stub("nazir-ahmad", "Naẕīr Aḥmad Dihlawī", "نذیر احمد دہلوی", born=date(gy=1836), died=date(gy=1912), desc="Urdu novelist and translator.", cites=[U])
stub("zakaullah", "Ẕakāʾullāh Dihlawī", "ذکاء اللہ دہلوی", born=date(gy=1832), died=date(gy=1910), desc="Historian and educationist.", cites=[U])
stub("ahsan-nanautavi", "Muḥammad Aḥsan Nānautavī", "محمد احسن نانوتوی", born=date(gy=1825, approx=True), died=date(gy=1895), desc="Publisher and translator; elder brother of Maẓhar and Munīr.")
stub("rafi-uddin-deobandi", "Rafīʿ al-Dīn Deobandī", "رفیع الدین دیوبندی")  # upgraded in companions
stub("ghalib", "Mīrzā Ghālib", "مرزا غالب", born=date(gy=1797), died=date(gy=1869), desc="The great Urdu and Persian poet of Delhi.", honorific=False, cites=[U])
stub("fazl-e-haq-khairabadi", "Faḍl-i Ḥaqq Khayrābādī", "فضل حق خیرآبادی", born=date(gy=1797), died=date(gy=1861), desc="Logician and 1857 leader, exiled to the Andamans.", cites=[U])
stub("momin", "Momin Khān Momin", "مومن خان مومن", born=date(gy=1800), died=date(gy=1851), desc="Delhi poet.", honorific=False, cites=[U])
stub("sahbai", "Imām Bakhsh Ṣahbāʾī", "امام بخش صہبائی", died=date(gy=1857), desc="Delhi poet and teacher.", cites=[U])
stub("rahmatullah-kairanawi", "Raḥmatullāh Kayrānawī", "رحمت اللہ کیرانوی", born=date(gy=1818), died=date(hy=1308, hm=9, hd=22, gy=1891, gm=5, gd=1),
     desc="Author of Iẓhār al-Ḥaqq; debated Pfander at Agra (1854); founded Madrasa Ṣawlatiyya in Mecca.")
stub("khairuddin-dehlawi", "Khayr al-Dīn Dihlawī", "خیر الدین دہلوی", desc="Father of Abul Kalam Azad.")
stub("yusuf-ali-khan-rampur", "Nawwāb Yūsuf ʿAlī Khān of Rampur", "نواب یوسف علی خان", desc="Ruler of Rampur.", honorific=False)
stub("siddiq-hasan-khan", "Nawwāb Ṣiddīq Ḥasan Khān", "صدیق حسن خان", born=date(gy=1832), died=date(gy=1890), desc="Scholar and consort of the Begum of Bhopal.", honorific=False, cites=[U])
stub("shefta", "Nawwāb Muṣṭafā Khān Sheftā", "مصطفیٰ خان شیفتہ", desc="Poet and critic.", honorific=False)
stub("faiz-hasan-saharanpuri", "Fayḍ al-Ḥasan Sahāranpūrī", "فیض الحسن سہارنپوری", died=date(hy=1304, gy=1887), desc="Arabic litterateur.", cites=[U])
stub("nasiruddin-naqshbandi", "Nāṣir al-Dīn Naqshbandī", "ناصر الدین نقشبندی", desc="Naqshbandī shaykh of Imdādullāh.")
stub("muhammad-thanawi", "Shaykh Muḥammad Thānawī", "شیخ محمد تھانوی", desc="Scholar of Thana Bhawan in Imdādullāh's circle.")
stub("abdul-jalil-barrada", "Sayyid ʿAbd al-Jalīl Barrāda", "عبد الجليل برادة", died=date(hy=1327), desc="Medinan scholar and student of Shāh ʿAbd al-Ghanī.")
stub("masum-mujaddidi", "Muḥammad Maʿṣūm Mujaddidī", "محمد معصوم المجددي", died=date(hy=1341), desc="Mujaddidī shaykh.")
stub("ahmad-said-mujaddidi", "Aḥmad Saʿīd Mujaddidī", "احمد سعید مجددی", born=date(hy=1217, gy=1802), died=date(hy=1277, gy=1860), desc="Elder brother of Shāh ʿAbd al-Ghanī; head of the Delhi khanqah.")
stub("muhammad-anwarullah-faruqi", "Muḥammad Anwārullāh Fārūqī", "انوار اللہ فاروقی", born=date(gy=1848), died=date(gy=1918), desc="Founder of Jāmiʿa Niẓāmiyya, Hyderabad.", cites=[U])

# =====================================================================
# 1. Mamlūk ʿAlī Nānautavī
T = person("mamluk-ali", "Mamlūk ʿAlī Nānautavī", "مملوک العلی نانوتوی",
    summary=("A scholar of the Ṣiddīqī family of Nanauta who spent his career teaching in Delhi. He joined Delhi College as an Arabic "
             "lecturer in 1825 and became its head Arabic teacher in 1841, and also taught at the Dār al-Baqāʾ madrasa. He was known for "
             "an exceptional memory and for teaching both the rational and the transmitted sciences."),
    legacy="Teacher of the whole founding generation of Deoband: Nānautavī, Gangohī, Yaʿqūb and Maẓhar Nānautavī.",
    tags=["Ḥanafī", "Māturīdī", "Walīullāhī"], cites=["wiki-mamluk", "tarajm-mamluk"],
    names=[("nisba", "en", "al-Ṣiddīqī"), ("nasab", "en", "Mamlūk al-ʿAlī ibn Aḥmad ʿAlī")])
life(T, "birth", date(gy=1789), place="nanauta", cites=["wiki-mamluk"])
life(T, "death", date(hy=1267, hm=12, hd=11, gy=1851, gm=10, gd=7), place="delhi", conf="attested", cites=["wiki-mamluk", "tarajm-mamluk"], note="Died of jaundice.")
lived(T, "delhi", "taught", cites=["wiki-mamluk"])
lived(T, "delhi", "buried", note="Mehdiyan, near the graveyard of Shāh Walīullāh", cites=["wiki-mamluk"])
member(T, "delhi-college", "teacher", note="Arabic lecturer 1825; head Arabic teacher from 1841", conf="attested", cites=["wiki-mamluk"])
rel("studied_under", QN, T, ["logic", "philosophy", "kalām", "the full Dars curriculum"], note="Logic, philosophy and the full curriculum",
    place="delhi", years="c.1844–1851", conf="attested", cites=["wiki-qn", "wiki-mamluk"])
for tid, subj in [("rashiduddin-khan", "higher studies"), ("ilahi-bakhsh-kandhlawi", "middle studies"), ("muhammad-qalandar", "middle studies")]:
    rel("studied_under", T, tid, subj, cites=["tarajm-mamluk"])
rel("studied_under", T, "shah-abdul-aziz", note="One lesson (reported only)", conf="uncertain", cites=["tarajm-mamluk"])
for sid in ["khalil-ahmad", "nazir-ahmad", "zakaullah", "ahsan-nanautavi"]:
    rel("studied_under", sid, T, cites=["wiki-mamluk"])
rel("companion_of", T, "sadruddin-azurda", note="Colleague in Delhi", cites=["wiki-mamluk"])
rel("family", T, "khalil-ahmad", note="Grandfather (through his daughter)", cites=["wiki-mamluk"])

# 2. Shāh ʿAbd al-Ghanī Mujaddidī
T = person("abdul-ghani-mujaddidi", "Shāh ʿAbd al-Ghanī Mujaddidī", "شاہ عبد الغنی مجددی دہلوی",
    summary=("A Naqshbandī-Mujaddidī shaykh and hadith master, descended from Shaykh Aḥmad Sirhindī, who led his family's khanqah lineage "
             "in Delhi. He first went on Hajj in 1849, and after the siege of Delhi in 1857 he settled in Medina with his family, where he "
             "taught hadith until his death."),
    legacy="The key hadith link, through Shāh Isḥāq and Shāh ʿAbd al-ʿAzīz, between the Walīullāhī tradition and the founders of Deoband.",
    tags=["Ḥanafī", "Naqshbandī-Mujaddidī"], cites=["ulum-abdulghani", "darulmaarif-abdulghani"],
    names=[("nisba", "en", "al-Mujaddidī al-Dihlawī thumma al-Madanī")])
life(T, "birth", date(hy=1235, hm=8, gy=1820, gm=5, precision="month"), place="delhi", conf="attested", cites=["ulum-abdulghani"])
life(T, "death", date(hy=1296, hm=1, hd=6, gy=1878, gm=12, gd=31), place="medina", conf="attested", cites=["ulum-abdulghani"], note="Tuesday 6 Muharram 1296.")
lived(T, "delhi", "taught", cites=["ulum-abdulghani"]); lived(T, "medina", "taught", note="from 1857", cites=["ulum-abdulghani"])
lived(T, "medina", "buried", note="Jannat al-Baqīʿ, Medina", cites=["ulum-abdulghani"])
rel("studied_under", QN, T, "hadith", note="Hadith", place="delhi", years="c. late 1840s–1857", conf="attested", cites=["deoband-org-qn", "wiki-qn"])
rel("studied_under", T, "abu-said-mujaddidi", note="His father: the Six Books, Muwaṭṭaʾ, fiqh and the ṭarīqa", cites=["ulum-abdulghani"])
rel("studied_under", T, "shah-ishaq", "Ṣaḥīḥ al-Bukhārī", cites=["ulum-abdulghani"])
rel("ijaza_from", T, "abid-sindhi", note="Ijāza at age 15", cites=["ulum-abdulghani"])
for sid in ["abdul-jalil-barrada", "masum-mujaddidi"]:
    rel("studied_under", sid, T, "hadith", cites=["ulum-abdulghani"])
rel("family", T, "ahmad-said-mujaddidi", note="Elder brother", cites=["ulum-abdulghani"])
work("injah-al-hajah", "Injāḥ al-Ḥājah ʿalā Sunan Ibn Mājah", "إنجاح الحاجة على سنن ابن ماجه", by=T, genres="hadith", langs="ar", rank=1,
     desc="Marginal commentary on Sunan Ibn Mājah, printed in India.", cites=["ulum-abdulghani"])
work("takhrij-maktubat", "Takhrīj Aḥādīth Maktūbāt al-Imām al-Rabbānī", by=T, genres="hadith", langs="ar", rank=2,
     desc="Traces the sources of the hadith quoted in Shaykh Aḥmad Sirhindī's letters.", cites=["ulum-abdulghani"])
work("khulasat-al-jawahir", "Khulāṣat al-Jawāhir al-ʿAliyya", by=T, genres="biography", langs="ar", rank=3, desc="Life of his father, Abū Saʿīd Mujaddidī.", cites=["ulum-abdulghani"])

# 3. Aḥmad ʿAlī Sahāranpūrī
T = person("ahmad-ali-saharanpuri", "Aḥmad ʿAlī Sahāranpūrī", "احمد علی سہارنپوری", title="Muḥaddith-e Sahāranpūrī",
    summary=("A hadith scholar trained in Delhi and in Mecca, where he spent two years with Shāh Muḥammad Isḥāq. In 1845 he set up the "
             "Matbaʿ Aḥmadī press in Delhi and produced India's first annotated edition of Ṣaḥīḥ al-Bukhārī, printed 1264–1270 AH. He later "
             "taught at Maẓāhir ʿUlūm in Saharanpur, becoming its head teacher."),
    legacy="His notes on Bukhārī still surround the text in the standard South Asian edition.",
    tags=["Ḥanafī", "Naqshbandī-Mujaddidī", "Deobandī"], cites=["wiki-ahmadali", "ilmgate-ahmadali"],
    names=[("nasab", "en", "Aḥmad ʿAlī ibn Luṭf Allāh")])
life(T, "birth", date(hy=1225, gy=1810), place="saharanpur", conf="attested", cites=["wiki-ahmadali"])
life(T, "death", date(hy=1297, hm=5, hd=6, gy=1880, gm=4, gd=17), place="saharanpur", conf="attested", cites=["wiki-ahmadali"], note="Two days after Nānautavī.")
for pl in ["saharanpur", "delhi", "mecca", "meerut", "kolkata"]: lived(T, pl, "lived", cites=["wiki-ahmadali"])
member(T, "matba-ahmadi", "founder", note="1845", conf="attested", cites=["wiki-ahmadali"])
member(T, "mazahir-uloom", "teacher", note="vice-principal 1291 AH, head teacher 1294 AH", cites=["ilmgate-ahmadali"])
rel("studied_under", QN, T, "hadith", note="Hadith; worked on his Bukhārī edition at his request", place="delhi", years="c.1848–1853",
    conf="attested", cites=["wiki-qn", "wiki-ahmadali", "deoband-bukhari"])
rel("studied_under", T, "mamluk-ali", cites=["wiki-ahmadali"])
rel("studied_under", T, "ilahi-bakhsh-kandhlawi", cites=["wiki-ahmadali"])
rel("studied_under", T, "wajihuddin-saharanpuri", note="Most of Bukhārī", cites=["ilmgate-ahmadali"])
rel("ijaza_from", T, "shah-ishaq", note="The Six Books, in Mecca (1261 AH)", conf="attested", cites=["wiki-ahmadali"])
rel("ijaza_from", T, "abdul-ghani-mujaddidi", note="Naqshbandī-Mujaddidī ṭarīqa", cites=["ilmgate-ahmadali"])
for sid in ["shibli-nomani", "mehr-ali-shah", "muhammad-ali-mongeri", "nur-muhammad-ludhianwi", "ahsan-nanautavi"]:
    rel("studied_under", sid, T, "hadith", cites=["wiki-ahmadali"])
work("hawashi-bukhari-ahmadali", "Ḥawāshī Ṣaḥīḥ al-Bukhārī", "حواشی صحیح البخاری", by=T, genres="hadith", langs="ar", rank=1,
     desc="Marginal notes on Ṣaḥīḥ al-Bukhārī; the first annotated Indian edition. Nānautavī worked on the final portions.", conf="attested", cites=["deoband-bukhari"])
work("hawashi-tirmidhi", "Ḥawāshī Jāmiʿ al-Tirmidhī", by=T, genres="hadith", langs="ar", rank=2, desc="Marginal notes on Tirmidhī.", cites=["wiki-ahmadali"])
work("hawashi-mishkat", "Ḥawāshī Mishkāt al-Maṣābīḥ", by=T, genres="hadith", langs="ar", rank=3, desc="Marginal notes on the Mishkāt.", cites=["wiki-ahmadali"])
work("sahih-muslim-edition", "Ṣaḥīḥ Muslim with al-Nawawī's commentary (edition)", by=T, role="editor", genres="hadith", langs="ar", rank=4,
     desc="Reportedly the first printed edition.", cites=["ilmgate-ahmadali"])
work("sahih-bukhari", "Ṣaḥīḥ al-Bukhārī", "صحيح البخاري", by=[], genres="hadith", langs="ar", desc="The hadith collection of al-Bukhārī (d. 256 AH).")
work_rel("hawashi-bukhari-ahmadali", "gloss_on", "sahih-bukhari")

# 4. Ḥājī Imdādullāh Muhājir Makkī
T = person("imdadullah", "Ḥājī Imdādullāh Muhājir Makkī", "حاجی امداد اللہ مہاجر مکی", title="Shaykh al-ʿArab wa al-ʿAjam",
    summary=("A Chishtī-Ṣābirī master from Nanauta, born Imdād Ḥusayn, who led the Muslims of Thana Bhawan in the 1857 rising, including "
             "the fighting at Shāmlī. He then migrated to Mecca in 1276 AH and guided disciples there for four decades. He wrote mostly "
             "devotional poetry and Sufi manuals in Urdu and Persian."),
    legacy="Spiritual father of the whole Deoband founding circle.",
    tags=["Ḥanafī", "Chishtī-Ṣābirī", "Naqshbandī", "Qādirī", "Suhrawardī", "Deobandī"], cites=["wiki-imdad", "tarajm-imdad", "deoband-imdad"],
    names=[("ism", "en", "Imdād Ḥusayn (birth name)"), ("laqab", "en", "Aʿlā Ḥaḍrat"), ("nisba", "en", "al-Fārūqī al-Thānawī")])
life(T, "birth", date(hy=1233, hm=2, hd=20, gy=1817, gm=12, gd=30), place="nanauta", conf="attested", cites=["wiki-imdad", "deoband-imdad"], note="Some give 1814 or 1818.")
life(T, "death", date(hy=1317, hm=6, hd=13, gy=1899, gm=10, gd=18), place="mecca", conf="attested", cites=["wiki-imdad"])
lived(T, "thana-bhawan", "lived", cites=["wiki-imdad"]); lived(T, "mecca", "lived", note="from 1276 AH", cites=["wiki-imdad"])
lived(T, "mecca", "buried", note="Jannat al-Muʿallā, Mecca, beside Raḥmatullāh Kayrānawī", cites=["wiki-imdad"])
took_part(T, "shamli-1857", role="leader", note="amīr of the Thana Bhawan rising", cites=["wiki-imdad"])
rel("bayah_to", QN, T, "taṣawwuf", note="Spiritual guide (bayʿah); made Nānautavī his khalīfa", place="thana-bhawan", conf="attested", cites=["wiki-qn", "wiki-imdad"])
rel("bayah_to", T, "nur-muhammad-jhanjhanawi", note="Chishtī-Ṣābirī khilāfa", cites=["wiki-imdad"])
rel("bayah_to", T, "nasiruddin-naqshbandi", note="Naqshbandī", cites=["tarajm-imdad"])
rel("studied_under", T, "shah-ishaq", cites=["tarajm-imdad"])
rel("studied_under", T, "muhammad-qalandar", note="Mishkāt and Ḥiṣn Ḥaṣīn", cites=["tarajm-imdad"])
for sid in ["ashraf-ali-thanwi", "khalil-ahmad", "mehr-ali-shah", "muhammad-anwarullah-faruqi"]:
    rel("bayah_to", sid, T, cites=["wiki-imdad"])
rel("companion_of", T, "rahmatullah-kairanawi", note="Neighbour in Mecca; buried beside him", cites=["wiki-imdad"])
rel("companion_of", T, "muhammad-thanawi", note="Thana Bhawan circle", conf="uncertain", cites=[U])
for wid, tr, orig, gen, lang, d, r in [
    ("ziya-al-qulub", "Ḍiyāʾ al-Qulūb", "ضیاء القلوب", "taṣawwuf", "fa", "Sufi manual written in Mecca, 1282 AH.", 1),
    ("ghiza-e-ruh", "Ghiżā-e Rūḥ", "غذائے روح", "poetry", "ur", "Masnavi of about 1,600 verses, 1264 AH.", 2),
    ("faisla-haft-masala", "Fayṣla-e Haft Masʾala", "فیصلہ ہفت مسئلہ", "taṣawwuf", "ur", "Mediation on seven disputed devotional questions.", 3),
    ("jihad-e-akbar", "Jihād-e Akbar", "جہاد اکبر", "poetry", "ur", "Poem on the greater struggle against the self, 1268 AH.", 4),
    ("irshad-e-murshid", "Irshād-e Murshid", "ارشاد مرشد", "taṣawwuf", "ur", "Litanies of the four Sufi orders, 1293 AH.", 5),
    ("tuhfat-al-ushshaq", "Tuḥfat al-ʿUshshāq", "تحفۃ العشاق", "poetry", "ur", "Masnavi, 1281 AH.", 6),
    ("gulzar-e-marifat", "Gulzār-e Maʿrifat", "گلزار معرفت", "poetry", "ur", "Devotional poems.", 7),
    ("hashiya-masnavi", "Ḥāshiya-e Masnavī-e Rūmī", "حاشیہ مثنوی", "taṣawwuf", "fa", "Notes on Rūmī's Masnavī.", 8),
    ("kulliyat-imdadiya", "Kulliyāt-e Imdādiyya", "کلیات امدادیہ", "poetry", "ur", "His collected works.", 9)]:
    work(wid, tr, orig, by=T, genres=gen, langs=lang, desc=d, rank=r, cites=["tarajm-imdad"])

# 5. Muftī Ṣadruddīn Āzurdah
T = person("sadruddin-azurda", "Muftī Ṣadruddīn Āzurdah", "مفتی صدر الدین آزردہ",
    summary=("A Delhi jurist and poet of Kashmiri descent. The East India Company made him Ṣadr al-Ṣudūr, the highest judicial office then "
             "open to an Indian, and he taught students at his own expense. After co-signing the 1857 fatwa he was tried and lost his "
             "property and a library said to hold some 300,000 volumes, though he was later acquitted."),
    legacy="A bridge between the Walīullāhī madrasa world, Delhi's literary salons and the scholars of 1857.",
    tags=["Ḥanafī", "Walīullāhī"], cites=["wiki-azurda", "rekhta-azurda", "kashmirlife-azurda"],
    names=[("laqab", "en", "Āzurdah (pen name)"), ("nasab", "en", "Muḥammad Ṣadr al-Dīn Khān ibn Luṭfullāh")])
life(T, "birth", date(gy=1789, gm=12, gd=12), place="delhi", cites=["rekhta-azurda"], note="Wikipedia gives 1804.")
life(T, "death", date(gy=1868, gm=7, gd=16), conf="attested", cites=["rekhta-azurda"])
lived(T, "delhi", "taught", cites=["wiki-azurda"]); lived(T, "rampur", "lived", note="late years", conf="uncertain", cites=["kashmirlife-azurda"])
rel("studied_under", QN, T, note="Several texts", place="delhi", conf="attested", cites=["wiki-qn"])
rel("studied_under", T, "shah-abdul-aziz", "hadith", cites=[U]); rel("studied_under", T, "shah-rafiuddin-dehlawi", ["fiqh", "uṣūl"], cites=[U])
rel("studied_under", T, "fazl-imam-khairabadi", "rational sciences", cites=[U])
for sid in ["khairuddin-dehlawi", "yusuf-ali-khan-rampur", "siddiq-hasan-khan", "shefta", "faiz-hasan-saharanpuri"]:
    rel("studied_under", sid, T, cites=["rekhta-azurda"])
for pid, note in [("ghalib", "Friend and sparring partner"), ("fazl-e-haq-khairabadi", "Fellow student"), ("momin", "Delhi literary circle"),
                  ("sahbai", "Delhi literary circle"), ("rahmatullah-kairanawi", "Co-signed the 1857 fatwa")]:
    rel("companion_of", T, pid, note=note, cites=["wiki-azurda"])
work("azurda-diwan", "Dīwān-e Āzurdah (fragments)", "دیوان آزردہ", by=T, genres="poetry", langs=["ur", "fa"], rank=1, status="manuscript",
     desc="His collected poems, largely lost in 1857; ghazals survive in anthologies.", cites=["rekhta-azurda"])
work("azurda-musaddas", "Musaddas on the victims of 1857", by=T, genres="poetry", langs="ur", rank=2, desc="Elegy for those killed in 1857.", cites=["kashmirlife-azurda"])
work("azurda-shahr-ashob", "Shahr-āshob", "شہر آشوب", by=T, genres="poetry", langs="ur", rank=3, desc="Lament on the ruin of Delhi.", cites=["kashmirlife-azurda"])

# 6. Mahtāb ʿAlī Deobandī
T = person("mahtab-ali", "Mahtāb ʿAlī Deobandī", "مہتاب علی دیوبندی",
    summary=("A scholar of the ʿUthmānī family of Deoband who studied at Delhi College under Mamlūk ʿAlī and Āzurdah, then taught Arabic "
             "privately at Karāmat Ḥusayn's house without taking paid work. He was consulted at the founding of Darul Uloom, was its second "
             "recorded donor and sat on its first council."),
    legacy="Nānautavī's first Arabic teacher, and uncle of Shaykh al-Hind Maḥmūd Ḥasan.",
    tags=["Ḥanafī", "Deobandī"], cites=["wiki-mahtab", "ummid-qn"])
life(T, "death", date(hy=1304, gy=1887, approx=True), place="deoband", conf="disputed", cites=["wiki-mahtab"], note="Sources give 1293 or 1304 AH; 1304 preferred.")
lived(T, "deoband", "taught", cites=["wiki-mahtab"])
member(T, "darul-uloom-deoband", "co_founder", note="consulted at the founding; second donor; first council", conf="attested", cites=["wiki-mahtab", "dud-cofounders"])
rel("studied_under", QN, T, ["Arabic grammar", "syntax"], note="Arabic grammar and syntax", place="deoband", years="c.1841–43", conf="attested", cites=["wiki-qn"])
rel("studied_under", T, "mamluk-ali", note="Delhi College", cites=["wiki-mahtab"]); rel("studied_under", T, "sadruddin-azurda", cites=["wiki-mahtab"])

# 7. Muḥammad Nawāz Sahāranpūrī
T = person("nawaz-saharanpuri", "Muḥammad Nawāz Sahāranpūrī", "محمد نواز سہارنپوری",
    summary="A teacher in Saharanpur known only as an early instructor of Nānautavī, who studied with him at about age twelve. No independent biography has been found.",
    tags=["Ḥanafī"], note="Thin record. Do not confuse with Nawaz Deobandi, the modern editor of Sawāneḥ ʿUlamāʾ-e Deoband.",
    cites=["wiki-qn", "deoband-org-qn"])
lived(T, "saharanpur", "taught", cites=["wiki-qn"])
rel("studied_under", QN, T, "Persian", note="Persian (some sources say elementary Arabic)", place="saharanpur", years="c.1843", conf="reported", cites=["wiki-qn", "dud-cofounders"])
