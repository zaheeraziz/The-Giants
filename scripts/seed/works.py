"""Sheikh Qāsim Nānautavī's written works."""
from lib import *
QN = "qasim-nanautavi"

for sid, title, url, typ in [
    ("ajis-hujjat", "Atif Suhail Siddiqui, 'Theological and Intellectual Roots in Deobandi Thought: Ḥujjat al-Islām', AJIS 37 (2020)", "https://mail.ajis.org/index.php/ajiss/article/view/703", "article"),
    ("azhaar-sadaqat", "Wali Ul Haq & Rashid Ahmad, critical review of Sadaqat-i-Islam, Al-Azhaar 6:1 (2020)", "https://al-azhaar.org/index.php/alazhar/article/download/42/13/15", "article"),
    ("rekhta-hujjat", "Rekhta — Hujjat-ul-Islam (Mukammal)", "https://www.rekhta.org/ebooks/detail/hujjat-ul-islam-mukammal-mohammad-qasim-nanotvi-ebooks", "web"),
    ("ilmgate-zajr", "ilmgate — Reprimanding men for denying the athar of Ibn Abbas", "https://www.ilmgate.org/reprimanding-men-for-denying-the-athar-of-ibn-%E2%80%98abbas/", "web"),
    ("wiki-husam", "Wikipedia — Husamul Haramain", "https://en.wikipedia.org/wiki/Husamul_Haramain", "web"),
    ("rekhta-dilpazir", "Rekhta — Taqreer-e-Dilpazeer (1928)", "https://www.rekhta.org/ebooks/detail/taqreer-e-dil-pazeer-molvi-mohammad-qasim-ebooks", "web"),
    ("rekhta-qibla", "Rekhta — Qibla Numa (1907)", "https://www.rekhta.org/ebooks/detail/qibla-numa-molvi-mohammad-qasim-ebooks", "web"),
    ("rekhta-intisar", "Rekhta — Intesar-ul-Islam (1878)", "https://www.rekhta.org/ebooks/detail/intesar-ul-islam-molvi-mohammad-qasim-ebooks", "web"),
    ("rekhta-mubahasa", "Rekhta — Mubahasa Shahjahanpur (1891)", "https://www.rekhta.org/ebooks/detail/mubahasa-shahjahanpur-molvi-mohammad-qasim-ebooks-1", "web"),
    ("rekhta-guftgu", "Rekhta — Guftagu-e-Mazhabi: Waqia-e-Mela Khuda Shanasi (1876)", "https://www.rekhta.org/ebooks/detail/guftagua-e-mazhabi-waqia-e-mela-khuda-shanasi-unknown-author-ebooks/", "web"),
    ("rekhta-tasfiya", "Rekhta — Tasfiyat ul-Aqaid (1902)", "https://www.rekhta.org/ebooks/detail/tasfiyat-ul-aqaid-molvi-mohammad-qasim-ebooks", "web"),
    ("chughtai-tasfiya", "Chughtai Library — Tasfiyat al-Aqaid record", "https://chughtailibrary.com/digital_library/repository_detail.php?id=43643", "web"),
    ("rekhta-hadiyya", "Rekhta — Hadiyat-us-Shia (1867)", "https://www.rekhta.org/ebooks/detail/hadiyat-us-shia-maulwi-mohammad-qasim-ebooks", "web"),
    ("ilmgate-hayat", "ilmgate — On the life of the Prophet in his grave", "https://ilmgate.org/on-the-life-of-the-prophet-in-his-grave", "web"),
    ("rekhta-qasimululoom", "Rekhta — Qasimul Uloom vol. 1 (1875)", "https://www.rekhta.org/ebooks/detail/qasimul-uloom-volume-001-maulvi-qasim-ebooks", "web"),
    ("archive-ajwiba", "Archive.org — Ajuba Arbaeen", "https://archive.org/details/AjubaArbaeen", "web"),
    ("rekhta-dalil", "Rekhta — al-Daleel al-Muhkam", "https://www.rekhta.org/ebooks/detail/daleel-al-muhkam-ala-adam-qira-at-al-fatiha-mohammad-qasim-nanotvi-ebooks", "web"),
    ("rekhta-tawthiq", "Rekhta — Tauseeq-ul-Kalam", "https://www.rekhta.org/ebooks/detail/tauseeq-ul-kalam-fi-insat-e-khalaf-al-imam-mohammad-qasim-nanotvi-ebooks", "web"),
    ("rekhta-masabih", "Rekhta — Masabeehul-Taraweeh", "https://www.rekhta.org/ebooks/detail/masabeehul-taraweeh-mohammad-qasim-nanotvi-ebooks", "web"),
    ("rekhta-qasaid", "Rekhta — Qasaid-e-Qasmi (2021)", "https://www.rekhta.org/ebooks/detail/qasaid-e-qasmi-mohammad-qasim-nanotvi-ebooks-2", "web"),
    ("rekhta-jamal", "Rekhta — Jamal-e-Qasmi", "https://www.rekhta.org/ebooks/detail/jamal-e-qasmi-aaftab-e-ziya-ebooks", "web"),
    ("rekhta-fuyuz", "Rekhta — Fuyooz-e-Qasmiya", "https://www.rekhta.org/ebooks/detail/fuyooz-e-qasmiya-molvi-mohammad-qasim-ebooks", "web")]:
    source(sid, title, url, type=typ)

W = [
 # id, translit, original, meaning, genres, langs, description, composed, status/publication, conf, cites
 ("hujjat-al-islam", "Ḥujjat al-Islām", "حجۃ الاسلام", "The Proof of Islam", ["kalam"], ["ur"],
  "A reasoned case for Islam: why people were created, proofs that God exists and is one, prophethood, and a refutation of the Trinity. It grew out of the arguments he prepared for the Shahjahanpur religious fairs, and modern scholars read it as a new kind of kalām built on logical propositions.",
  date(hy=1294, gy=1877, approx=True), "Maktaba Majlis Qasim-ul-Ma'arif, Deoband, 1967; ed. Ishtiyaq Ahmad, Deoband, 2013", "attested", ["ajis-hujjat", "rekhta-hujjat", "azhaar-sadaqat"]),
 ("tahdhir-al-nas", "Taḥdhīr al-Nās", "تحذیر الناس من انکار اثر ابن عباس", "Warning the People against Denying the Report of Ibn ʿAbbās", ["aqida"], ["ur"],
  "Answers a question about Ibn ʿAbbās's report of a prophet on each of the 'seven earths'. He argues that the Prophet's being the Seal of the Prophets is first a matter of rank, not only of coming last in time, while affirming that he is the last prophet. Later Barelvi critics made it central to their case against Deobandis; Deobandis reject their reading.",
  date(hy=1290, gy=1873), "first printed at Matbaʿ Ṣiddīqī, Bareilly (reported)", "attested", ["ilmgate-zajr", "wiki-husam", "deoband-org-qn"]),
 ("hashiya-bukhari-qn", "Ḥāshiya ʿalā Ṣaḥīḥ al-Bukhārī (final portions)", "حاشیہ صحیح البخاری", "Marginal notes on Ṣaḥīḥ al-Bukhārī", ["hadith"], ["ar"],
  "At Aḥmad ʿAlī Sahāranpūrī's request he wrote the notes on the last portions of Bukhārī for Aḥmad ʿAlī's edition, which became the standard South Asian madrasa text. Exactly which chapters are his is disputed.",
  date(gy=1852, approx=True), "printed within Aḥmad ʿAlī's edition (Aḥmadī Press, Delhi)", "attested", ["wiki-qn", "ilmgate-ahmadali", "deoband-bukhari"]),
 ("taqrir-e-dilpazir", "Taqrīr-e Dilpazīr", "تقریر دلپذیر", "The Pleasing Discourse", ["kalam"], ["ur"],
  "A dense philosophical case for the truth of Islam, written as an invitation to it: the existence of a Maker and the divine attributes of knowledge, will, power and speech. Later printed under the title Ṣadāqat-e Islām.",
  None, "Matbaʿ Qāsmī, Deoband, 1928; Darul Uloom Deoband, 2013", "attested", ["azhaar-sadaqat", "rekhta-dilpazir"]),
 ("qibla-numa", "Qibla Numā", "قبلہ نما", "The Qibla-Pointer", ["interfaith"], ["ur"],
  "Answers Dayanand Saraswati's charge that Muslims worship a stone when they face the Kaaba, arguing that facing a direction of prayer is not worship of an object.",
  date(gy=1878, approx=True), "Matbaʿ Mujtabāʾī, Delhi, 1907; Darul Uloom Deoband, 2013", "attested", ["rekhta-qibla", "azhaar-sadaqat", "deoband-org-qn"]),
 ("intisar-al-islam", "Intiṣār al-Islām", "انتصار الاسلام", "The Vindication of Islam", ["interfaith"], ["ur"],
  "Rebuts objections to Islam raised by Dayanand Saraswati, founder of the Arya Samaj, in the exchanges of the late 1870s.",
  date(gy=1878), "printed 1878, 48 pp", "attested", ["rekhta-intisar", "azhaar-sadaqat"]),
 ("mubahasa-shahjahanpur", "Mubāḥatha-e Shāhjahānpūr", "مباحثہ شاہجہاں پور", "The Shahjahanpur Debate", ["interfaith"], ["ur"],
  "Record of his speeches and exchanges with Christian missionaries and Arya Samaj speakers at the second Shahjahanpur fair in 1877, compiled by his student Fakhr al-Ḥasan Gangohī.",
  date(gy=1877, gm=3), "ed. Fakhr al-Ḥasan, Matbaʿ Mujtabāʾī, Delhi, 1891", "attested", ["rekhta-mubahasa", "tareen-shahjahanpur"]),
 ("guftgu-e-mazhabi", "Guftgū-e Madhhabī", "گفتگوئے مذہبی: واقعۂ میلہ خدا شناسی", "Religious Conversation: the God-Recognition Fair", ["interfaith"], ["ur"],
  "A contemporary report of the first Shahjahanpur fair in 1876, preserving his arguments on God, prophethood and scripture before Christian and Hindu audiences.",
  date(hy=1293, gy=1876), "Matbaʿ Ḍiyāʾī, Meerut, 1876", "attested", ["rekhta-guftgu", "ajis-hujjat"]),
 ("tasfiyat-al-aqaid", "Taṣfiyat al-ʿAqāʾid", "تصفیۃ العقائد", "Purification of Beliefs", ["aqida"], ["ur"],
  "His reply to Sir Sayyid Aḥmad Khān's principles for reading the Qur'an by reason and nature. It accepts reason while refusing to let it override revelation, and prints Sir Sayyid's letter alongside the reply.",
  date(gy=1874, approx=True), "Matbaʿ Mujtabāʾī, Delhi, 1902", "attested", ["chughtai-tasfiya", "rekhta-tasfiya", "tareen-2024"]),
 ("hadiyyat-al-shia", "Hadiyyat al-Shīʿa", "ہدیۃ الشیعہ", "A Gift to the Shia", ["polemics"], ["ur"],
  "A long Sunni answer to Shīʿī claims about the Companions and the imamate, written at Gangohī's request; one of his largest books.",
  date(gy=1867), "Matbaʿ Fayḍī, Delhi, 1867", "attested", ["rekhta-hadiyya", "tarajm-qn"]),
 ("aab-e-hayat", "Āb-e Ḥayāt", "آب حیات", "The Water of Life", ["aqida"], ["ur"],
  "Argues that the prophets, the Prophet Muḥammad above all, are truly alive in their graves; still the standard reference for the Deobandi position. Not to be confused with Muḥammad Ḥusayn Āzād's history of Urdu poetry of the same name.",
  None, None, "attested", ["ilmgate-hayat", "azhaar-sadaqat"]),
 ("qasim-al-ulum", "Qāsim al-ʿUlūm (letters)", "قاسم العلوم", "Distributor of Sciences", ["letters"], ["fa", "ur"],
  "His collected letters answering questions on theology, Sufism and law; the main source for his thought outside the treatises.",
  date(gy=1875), "vol. 1, Matbaʿ Mujtabāʾī, Delhi, 1875", "attested", ["rekhta-qasimululoom"]),
 ("munazara-e-ajiba", "Munāẓara-e ʿAjība", "مناظرہ عجیبہ", "The Remarkable Disputation", ["aqida", "letters"], ["ur"],
  "His exchange of letters with ʿAbd al-ʿAzīz Amrohī defending the argument of Taḥdhīr al-Nās; in effect his own fuller explanation of that book.",
  None, "Maktaba Qasim al-'Ulum, Karachi, 1978", "attested", ["ajis-hujjat"]),
 ("ajwiba-e-arbain", "Ajwiba-e Arbaʿīn", "اجوبہ اربعین", "Answers to Forty Questions", ["polemics"], ["ur"],
  "Answers forty questions in two parts, apparently put from the Shīʿī side.", None, None, "reported", ["archive-ajwiba"]),
 ("tuhfa-lahmiya", "al-Tuḥfa al-Laḥmiyya", "تحفۂ لحمیہ", "The Gift concerning Meat", ["interfaith"], ["ur"],
  "Defends eating meat against Hindu and Jain criticism, using rational and medical arguments, at a time of tension over cow protection.",
  None, None, "attested", ["azhaar-sadaqat", "deoband-org-qn"]),
 ("dalil-al-muhkam", "al-Dalīl al-Muḥkam", "الدلیل المحکم علی عدم قراءۃ الفاتحہ", "The Firm Proof", ["fiqh"], ["ur"],
  "Argues the Ḥanafī position that a person praying behind an imam does not recite al-Fātiḥa.", None, "Shamsul Matabe, Moradabad", "attested", ["rekhta-dalil", "deoband-org-qn"]),
 ("tawthiq-al-kalam", "Tawthīq al-Kalām fī al-Inṣāt Khalf al-Imām", "توثیق الکلام", "Strengthening the Argument for Silence behind the Imam", ["fiqh"], ["ur"],
  "A short companion tract to al-Dalīl al-Muḥkam.", None, "Khairkhwah Press, Saharanpur", "attested", ["rekhta-tawthiq"]),
 ("masabih-al-tarawih", "Maṣābīḥ al-Tarāwīḥ", "مصابیح التراویح", "Lamps of the Tarāwīḥ", ["fiqh"], ["ur"],
  "On the tarāwīḥ prayer of Ramadan.", None, "Matbaʿ Ḍiyāʾī, Meerut", "attested", ["rekhta-masabih"]),
 ("qasaid-e-qasmi", "Qaṣāʾid-e Qāsmī", "قصائد قاسمی", "Qasimi Odes", ["poetry"], ["ur"],
  "His collected odes, mostly in praise of the Prophet: the devotional, literary side of a scholar known for dense theology.",
  None, "ed. Nadim Ahmad, Hujjat al-Islam Academy, Deoband, 2021", "attested", ["rekhta-qasaid"]),
 ("jamal-e-qasmi", "Jamāl-e Qāsmī", "جمال قاسمی", "Qasimi Beauty", ["letters"], ["ur"],
  "A short collection of letters on doctrine.", date(gy=1901), "ed. Mohammad Jamaluddin, Matbaʿ Mujtabāʾī, Delhi, 1901", "attested", ["rekhta-jamal"]),
 ("fuyuz-e-qasimiya", "Fuyūḍ-e Qāsimiyya", "فیوض قاسمیہ", "Qasimi Graces", ["letters"], ["ur"],
  "A short collection of letters or teachings published in Deoband.", None, "Kutub Khana Ezaziya, Deoband", "reported", ["rekhta-fuyuz"]),
 ("lataif-e-qasmi", "Laṭāʾif-e Qāsmī", "لطائف قاسمی", "Qasimi Subtleties", ["letters"], ["ur"],
  "Listed among his works; usually described as a small collection of letters.", None, None, "reported", ["deoband-org-qn", "tarajm-qn"]),
 ("al-haqq-al-sarih", "al-Ḥaqq al-Ṣarīḥ fī Bayān al-Tarāwīḥ", "الحق الصریح", "The Clear Truth on the Tarāwīḥ", ["fiqh"], ["ur"],
  "Listed among his works as a treatise on tarāwīḥ; may be another title for Maṣābīḥ al-Tarāwīḥ.", None, None, "reported", ["deoband-org-qn", "tarajm-qn"]),
 ("barahin-e-qasimiya", "Barāhīn-e Qāsimiyya", "براہین قاسمیہ", "Qasimi Proofs", ["interfaith"], ["ur"],
  "Answers Arya Samaj objections about God's existence and attributes.", None, None, "uncertain", ["azhaar-sadaqat"]),
]
for rank, (wid, tr, orig, meaning, genres, langs, desc, composed, pub, conf, cites) in enumerate(W, start=1):
    work(wid, tr, orig, by=QN, meaning=meaning, genres=genres, langs=langs, desc=desc, rank=rank, composed=composed,
         publication=pub, conf=conf, cites=cites)

# who compiled or recorded
work("mubahasa-shahjahanpur", "", by="fakhrul-hasan-gangohi", role="compiler")
work("tahdhir-al-nas", "", by="ahsan-nanautavi", role="editor")
# how the books relate
work_rel("hashiya-bukhari-qn", "gloss_on", "sahih-bukhari")
work_rel("munazara-e-ajiba", "commentary_on", "tahdhir-al-nas")
work_rel("tawthiq-al-kalam", "commentary_on", "dalil-al-muhkam")
