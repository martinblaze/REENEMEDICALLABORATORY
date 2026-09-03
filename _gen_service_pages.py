# -*- coding: utf-8 -*-
"""Generates the seven service landing pages.
Content sources: Reene's own published service copy + established general
medical facts. No invented prices, equipment models, turnaround times or
staff numbers — pricing renders as an explicit placeholder.
"""
import io, json

BASE = 'https://reenemedicaldiagnostics.com'
PRICE_PLACEHOLDER = 'Call for current pricing'   # <-- swap when real prices arrive

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')

PAGES = [
{
 'slug': 'pregnancy-ultrasound-onitsha',
 'title': 'Pregnancy Ultrasound in Onitsha | 2D, 3D &amp; 4D Scans',
 'desc': 'Obstetric ultrasound in Awada, Obosi, Onitsha — dating, anomaly, growth, 3D and 4D scans by certified sonographers at Reene Medical Diagnostics. Book or call today.',
 'eyebrow': 'Ultrasound',
 'h1a': 'Pregnancy ultrasound', 'h1b': 'in <span class="italic">Onitsha.</span>',
 'img': 'ULTRASOUND.png', 'pos': '55% 45%',
 'lede': 'Obstetric and gynaecological scanning at our Awada centre — including 3D and 4D imaging and Doppler studies, performed by certified sonographers.',
 'duration': 'Typically 20–30 min',
 'radiation': 'None — sound waves',
 'body': [
  ('h2', 'What a pregnancy ultrasound does'),
  ('p', 'Ultrasound builds a live image of your baby using high-frequency sound waves. Because it uses no ionising radiation, it is the standard imaging method used in pregnancy care worldwide, and can be repeated when there is a clinical reason to do so.'),
  ('p', 'A scan can confirm a pregnancy and its location, estimate how far along you are, check the number of babies, follow growth and position, assess the placenta and amniotic fluid, and look at blood flow through Doppler study.'),
  ('h2', 'Scans available at Reene'),
  ('ul-cols', ['Obstetric ultrasound (all trimesters)', 'Gynaecological ultrasound',
               '3D pregnancy scans', '4D pregnancy scans',
               'Doppler blood-flow studies', 'Pelvic ultrasound',
               'Abdominal ultrasound', 'Breast, thyroid and neck ultrasound']),
  ('h3', '2D, 3D and 4D — the difference'),
  ('p', '<strong>2D</strong> is the standard greyscale cross-section used for clinical assessment and measurement. <strong>3D</strong> combines those slices into a still surface image. <strong>4D</strong> is 3D imaging in motion, so you see movement in real time. 3D and 4D are usually added to a clinical scan rather than replacing it.'),
  ('h2', 'How to prepare'),
  ('p', 'Preparation depends on the stage of pregnancy and the type of scan. Early scans are often clearer with a comfortably full bladder, while later scans usually need no preparation at all. Wear something that lets you expose your abdomen easily.'),
  ('p', 'Tell us which scan you have been asked to have when you book, and we will confirm exactly what you need to do beforehand. Bring any referral or request form from your doctor, along with previous scan reports if you have them.'),
  ('h2', 'What happens during the scan'),
  ('ul', ['You lie on your back on the couch and your abdomen is exposed.',
          'A water-based gel is applied — it improves contact and can feel cold.',
          'The sonographer moves a handheld probe over the area, watching the screen.',
          'Measurements are taken as the scan proceeds. It is painless, though light pressure may be used.',
          'Your report is prepared afterwards; we confirm the timeline when you book.']),
 ],
 'faqs': [
  ('Is ultrasound safe during pregnancy?',
   'Yes. Ultrasound uses high-frequency sound waves rather than ionising radiation, which is why it is used routinely in pregnancy care worldwide. Scans should still be carried out for a clinical reason by a trained operator — discuss the timing and number of scans with your doctor or midwife.'),
  ('When should I have my scans?',
   'Timing is decided by your doctor or midwife based on your care plan. Broadly, an early scan confirms the pregnancy and dates it, a mid-pregnancy scan reviews development in detail, and later scans follow growth and position. Bring your referral so we perform exactly the scan you have been asked to have.'),
  ('Do I need a full bladder?',
   'Often for early pregnancy scans, rarely for later ones. Tell us which scan you are booked for and we will give you the specific instruction beforehand.'),
  ('Can you tell me the baby&rsquo;s sex?',
   'Sex can often be seen from the middle of pregnancy onward, but it depends on the baby&rsquo;s position and is never guaranteed. It is not the clinical purpose of the scan — please ask the sonographer at the time.'),
  ('Do I need a referral from my doctor?',
   'Bring a referral or request form if you have one, since it tells us precisely which scan to perform. If you do not have one, call us and we will advise.'),
 ],
 'related': ['blood-test-laboratory-services-onitsha', 'health-screening-packages', 'digital-x-ray-services-onitsha'],
},
{
 'slug': 'blood-test-laboratory-services-onitsha',
 'title': 'Blood Tests &amp; Laboratory Services in Onitsha | Reene Medical',
 'desc': 'Clinical laboratory testing in Awada, Obosi, Onitsha — full blood count, liver and kidney function, lipids, thyroid, hormones, urinalysis and screening. Book or call.',
 'eyebrow': 'Laboratory',
 'h1a': 'Blood tests &amp; lab', 'h1b': 'work in <span class="italic">Onitsha.</span>',
 'img': 'LAB.png', 'pos': '70% 45%',
 'lede': 'A fully equipped clinical laboratory running routine and specialised investigations under strict quality control — the discipline our founder built his career in.',
 'duration': 'Sample taken in minutes',
 'radiation': 'None',
 'body': [
  ('h2', 'Testing we run'),
  ('p', 'Our laboratory covers the routine investigations most patients are referred for, along with specialised assays:'),
  ('ul-cols', ['Complete Blood Count (CBC)', 'Blood chemistry &amp; metabolic panel',
               'Liver function tests (LFT)', 'Kidney function tests (RFT)',
               'Lipid profile', 'Blood sugar tests',
               'Thyroid function tests', 'Hormone tests',
               'Urinalysis', 'HIV, hepatitis &amp; STI screening',
               'Tumour markers', 'Electrolyte studies']),
  ('callout', 'Clinical chemistry is the specialty of our founder, <a href="dr-augustine-ihim.html">Dr. Augustine Chinedu Ihim</a> — a Reader in Clinical Chemistry at Nnamdi Azikiwe University with a PhD in Chemical Pathology and more than 100 published papers.'),
  ('h2', 'What some common tests show'),
  ('h3', 'Complete Blood Count'),
  ('p', 'A CBC measures red cells, white cells and platelets. It is one of the broadest first-line tests available and is used to investigate anaemia, infection, clotting problems and general health.'),
  ('h3', 'Liver and kidney function'),
  ('p', 'These panels measure enzymes, proteins and waste products that indicate how well the liver and kidneys are working. They are commonly requested before starting certain medicines, and to monitor known conditions.'),
  ('h3', 'Lipid profile and blood sugar'),
  ('p', 'Lipid profile measures cholesterol and related fats; blood sugar tests measure glucose. Together they inform cardiovascular and diabetes risk, and both are standard parts of a general health check.'),
  ('h2', 'How to prepare'),
  ('p', 'Some tests require fasting — commonly lipid profile and fasting glucose — which usually means no food for a set period beforehand, though water is normally allowed. Others need no preparation at all.'),
  ('p', 'Because requirements differ by test, tell us what you have been referred for when you book and we will confirm whether you need to fast and for how long. Bring your referral form and a list of any medicines you take.'),
  ('h2', 'Giving your sample'),
  ('ul', ['Most tests need a small blood sample taken from a vein in your arm.',
          'The draw itself takes only a few minutes.',
          'Urine or other samples are collected in a private area where required.',
          'Samples are processed under our quality-control procedures.',
          'We confirm when your report will be ready before you leave.']),
 ],
 'faqs': [
  ('Do I need to fast before a blood test?',
   'It depends on the test. Fasting is commonly required for lipid profile and fasting blood sugar, and not required for many others. Tell us which test you are booked for and we will confirm exactly what to do.'),
  ('Do I need a doctor&rsquo;s referral?',
   'Many routine tests can be arranged directly with us. If your doctor has given you a referral or request form, bring it — it specifies exactly which investigations to run.'),
  ('How long do results take?',
   'Turnaround depends on the test — routine investigations are generally faster than specialised assays. We confirm the expected timeline for your specific test when you book or check in.'),
  ('Does taking blood hurt?',
   'You will usually feel a brief sharp scratch as the needle goes in, and the draw itself is over in a couple of minutes. Tell the scientist if you have fainted during blood tests before so they can take extra care.'),
 ],
 'related': ['health-screening-packages', 'ecg-heart-health-testing', 'pregnancy-ultrasound-onitsha'],
},
{
 'slug': 'ct-scan-imaging-anambra',
 'title': 'CT Scan in Onitsha, Anambra | Reene Medical Diagnostics',
 'desc': 'CT scan imaging in Awada, Obosi, Onitsha LGA — brain, chest, abdomen, pelvis and spine, with contrast and non-contrast studies. Book a CT scan or call for details.',
 'eyebrow': 'Imaging',
 'h1a': 'CT scan imaging', 'h1b': 'in <span class="italic">Anambra.</span>',
 'img': 'CTSCAN.png', 'pos': '60% 50%',
 'lede': 'Cross-sectional imaging that shows bone, soft tissue and blood vessels in detail — used to investigate injury, infection, tumours and structural problems.',
 'duration': 'Typically 10–20 min',
 'radiation': 'Low-dose X-ray',
 'body': [
  ('h2', 'What a CT scan shows'),
  ('p', 'Computed tomography takes X-ray images from many angles and reconstructs them into detailed cross-sections. Because it separates tissues far more clearly than a plain X-ray, it is used where fine structural detail matters — internal injury, bleeding, blood clots, infection, tumours and other structural abnormalities.'),
  ('h2', 'Studies available'),
  ('ul-cols', ['Brain &amp; head CT', 'Chest CT', 'Abdominal &amp; pelvic CT',
               'Spine CT', 'CT angiography', 'CT-guided procedures',
               'Contrast studies', 'Non-contrast studies']),
  ('h3', 'Contrast studies'),
  ('p', 'Some scans use a contrast agent to make blood vessels and certain tissues stand out. It may be given by injection or as a drink depending on the study. Tell us in advance if you have ever reacted to contrast, have kidney problems, or are taking medication for diabetes, as this affects how the scan is planned.'),
  ('h2', 'How to prepare'),
  ('p', 'Preparation depends on the region being scanned and whether contrast is used — some studies require you not to eat for a period beforehand, others need no preparation. We confirm the specifics when you book.'),
  ('p', 'Wear comfortable clothing without metal fastenings where possible, and leave jewellery at home. <strong>Tell us if you are pregnant or think you might be</strong>, so the request can be reviewed before going ahead.'),
  ('h2', 'During the scan'),
  ('ul', ['You lie on a motorised couch that moves slowly through a ring-shaped scanner.',
          'The scanner is open at both ends — it does not enclose you like an MRI tunnel.',
          'You may be asked to hold your breath briefly so the images stay sharp.',
          'The scan itself is painless; if contrast is injected you may feel a warm flush.',
          'Images are reviewed and reported after the scan.']),
 ],
 'faqs': [
  ('Is a CT scan safe?',
   'CT uses ionising radiation, so scans are performed when the clinical benefit justifies it — which is why a referral matters. Doses are kept as low as reasonably achievable. Tell the radiographer if you are pregnant or think you might be.'),
  ('What is the difference between a CT scan and an MRI?',
   'CT uses X-rays and is fast and excellent for bone, acute bleeding and chest or abdominal detail. MRI uses a magnetic field with no ionising radiation and gives superior soft-tissue contrast, making it preferred for brain, spinal cord and joint detail. Your doctor chooses based on what needs to be seen.'),
  ('Will I need contrast?',
   'Only some studies require it. If contrast is planned, tell us beforehand about any previous reaction, kidney problems or diabetes medication.'),
  ('How long does a CT scan take?',
   'The scan itself is usually brief — often a matter of minutes — though your total visit is longer once preparation, positioning and any contrast are included.'),
 ],
 'related': ['mri-scan-services-onitsha', 'digital-x-ray-services-onitsha', 'blood-test-laboratory-services-onitsha'],
},
{
 'slug': 'mri-scan-services-onitsha',
 'title': 'MRI Scan in Onitsha | Reene Medical Diagnostics, Anambra',
 'desc': 'MRI scanning in Awada, Obosi, Onitsha — brain, spine, musculoskeletal, abdominal and pelvic imaging with no ionising radiation. Book an MRI scan or call for details.',
 'eyebrow': 'Imaging',
 'h1a': 'MRI scanning', 'h1b': 'in <span class="italic">Onitsha.</span>',
 'img': 'MRI.png', 'pos': '58% 50%',
 'lede': 'Detailed imaging of soft tissue, nerves and joints using a magnetic field and radio waves — no ionising radiation involved.',
 'duration': 'Typically 30–45 min',
 'radiation': 'None — magnetic field',
 'body': [
  ('h2', 'What MRI is used for'),
  ('p', 'Magnetic resonance imaging uses a strong magnetic field and radio waves rather than X-rays. It produces exceptional soft-tissue contrast, which is why it is the preferred test for the brain and spinal cord, ligaments and cartilage, and many abdominal and pelvic questions.'),
  ('h2', 'Studies available'),
  ('ul-cols', ['Brain &amp; neurological MRI', 'Spinal MRI', 'Musculoskeletal MRI',
               'Abdominal MRI', 'Pelvic MRI', 'Cardiac MRI', 'MR angiography']),
  ('h2', 'Safety screening comes first'),
  ('p', 'Because the scanner uses a powerful magnet, we screen everyone before entry. <strong>You must tell us if you have any metal or electronic implant</strong> — including a pacemaker or defibrillator, cochlear implant, aneurysm clip, neurostimulator, metal fragments in the eye, or surgical implants.'),
  ('p', 'Some implants are MRI-safe and some are not, so bring any implant card or documentation you have. All metal objects — jewellery, watches, hairpins, cards — must be left outside the scan room.'),
  ('h2', 'How to prepare'),
  ('p', 'Most MRI scans need little preparation, though some abdominal studies require you not to eat beforehand. We confirm what applies to your scan when you book. Wear clothing without metal fastenings if you can.'),
  ('h2', 'During the scan'),
  ('ul', ['You lie on a couch that slides into the scanner tunnel.',
          'The scanner is loud — knocking and buzzing are normal, and ear protection is provided.',
          'Staying still is essential, as movement blurs the images.',
          'You are in contact with the radiographer throughout and can speak to them.',
          'Tell us in advance if you find enclosed spaces difficult so we can plan for it.']),
 ],
 'faqs': [
  ('Is an MRI scan safe?',
   'MRI uses no ionising radiation and is considered very safe when the correct safety screening is done. The critical step is telling staff about any metal or electronic implant before you enter the scan room.'),
  ('Can I have an MRI with metal implants?',
   'It depends on the implant. Some are MRI-conditional or MRI-safe, others rule out scanning. Bring your implant card or documentation and tell us in advance so we can check before your appointment.'),
  ('What if I am claustrophobic?',
   'Tell us when you book. Knowing in advance lets us plan the appointment, explain what to expect and take steps to make the scan more comfortable.'),
  ('How long does an MRI take?',
   'Longer than a CT — commonly around half an hour or more depending on the region and the number of sequences. You will be told what to expect before starting.'),
  ('MRI or CT — which do I need?',
   'That is your referring doctor&rsquo;s decision. MRI is generally chosen for soft tissue, nerve and joint detail; CT is faster and often preferred for bone, acute injury and chest or abdominal assessment.'),
 ],
 'related': ['ct-scan-imaging-anambra', 'digital-x-ray-services-onitsha', 'pregnancy-ultrasound-onitsha'],
},
{
 'slug': 'digital-x-ray-services-onitsha',
 'title': 'Digital X-Ray in Onitsha | Chest &amp; Skeletal Radiography',
 'desc': 'Digital X-ray imaging in Awada, Obosi, Onitsha — chest, abdominal, skeletal, spine and extremity radiography with lower dose and faster results. Book or call.',
 'eyebrow': 'Imaging',
 'h1a': 'Digital X-ray', 'h1b': 'in <span class="italic">Onitsha.</span>',
 'img': 'XRAY.png', 'pos': '55% 45%',
 'lede': 'Digital radiography producing clear images quickly, at a lower radiation dose than older film-based systems.',
 'duration': 'Typically 5–15 min',
 'radiation': 'Low-dose X-ray',
 'body': [
  ('h2', 'What X-ray is best at'),
  ('p', 'X-ray remains the fastest and most accessible way to look at bone and the chest. It is the usual first test for suspected fractures and joint problems, and for assessing the lungs and heart outline.'),
  ('p', 'Digital detectors replace film, so images appear within moments, can be adjusted without repeating the exposure, and are stored electronically for comparison later. In general, digital systems achieve this at a lower dose than the film systems they replaced.'),
  ('h2', 'Examinations available'),
  ('ul-cols', ['Chest X-ray (PA &amp; lateral)', 'Abdominal X-ray', 'Skeletal X-ray',
               'Spine X-ray', 'Extremity X-ray', 'Skull X-ray', 'Pelvic X-ray']),
  ('h2', 'How to prepare'),
  ('p', 'Most X-rays need no preparation at all. You may be asked to change into a gown and to remove jewellery, glasses or anything metal from the area being imaged, since metal blocks X-rays and obscures the picture.'),
  ('p', '<strong>Tell the radiographer if you are pregnant or think you might be</strong> before the examination begins, so the request can be reviewed.'),
  ('h2', 'During the examination'),
  ('ul', ['You are positioned against or on the detector, depending on the body part.',
          'You hold still — and for chest images, hold your breath for a moment.',
          'The exposure itself lasts a fraction of a second and you feel nothing.',
          'More than one view is often taken, for example front and side.',
          'The radiographer checks image quality before you leave.']),
 ],
 'faqs': [
  ('Is X-ray radiation dangerous?',
   'An X-ray uses a small dose of ionising radiation. Examinations are performed when clinically justified and the dose is kept as low as reasonably achievable. Tell the radiographer if you are or might be pregnant.'),
  ('How long does an X-ray take?',
   'The exposure is a fraction of a second. Most visits are brief once positioning and any additional views are included.'),
  ('Do I need to prepare?',
   'Usually not. You may need to remove metal items or change into a gown for the area being examined.'),
  ('Do I need a referral?',
   'Bring a referral or request form if you have one, as it specifies which views to take. If you do not have one, call us and we will advise.'),
 ],
 'related': ['ct-scan-imaging-anambra', 'mri-scan-services-onitsha', 'blood-test-laboratory-services-onitsha'],
},
{
 'slug': 'ecg-heart-health-testing',
 'title': 'ECG &amp; Heart Health Testing in Onitsha | Reene Medical',
 'desc': 'ECG testing in Awada, Obosi, Onitsha — resting ECG, exercise stress testing and 24-hour Holter monitoring for rhythm and cardiac assessment. Book or call.',
 'eyebrow': 'Cardiac',
 'h1a': 'ECG &amp; heart', 'h1b': 'health <span class="italic">testing.</span>',
 'img': 'ECG.png', 'pos': '50% 45%',
 'lede': 'Recording the heart&rsquo;s electrical activity to assess rhythm and detect cardiac problems — quick, painless and non-invasive.',
 'duration': 'Resting ECG: 5–10 min',
 'radiation': 'None',
 'body': [
  ('h2', 'What an ECG records'),
  ('p', 'An electrocardiogram records the electrical signals that make your heart beat. From that trace, a clinician can assess rate and rhythm and look for patterns that suggest arrhythmia, coronary artery disease, previous or current heart attack, enlargement of the heart muscle and other cardiac conditions.'),
  ('h2', 'Tests available'),
  ('ul', ['<strong>Resting ECG</strong> — the standard recording, taken while you lie still.',
          '<strong>Exercise stress test</strong> — recorded while the heart works harder, to reveal changes that only appear under exertion.',
          '<strong>24-hour Holter monitoring</strong> — a portable recorder worn through a normal day, useful when symptoms come and go.',
          '<strong>Heart rate &amp; rhythm analysis</strong> — interpretation of the recorded trace.']),
  ('h3', 'Why Holter monitoring is sometimes needed'),
  ('p', 'A resting ECG captures a short window. If your symptoms — palpitations, dizziness, irregular beats — are intermittent, they may simply not occur during those minutes. Wearing a monitor across a full day greatly improves the chance of catching the event.'),
  ('h2', 'How to prepare'),
  ('p', 'A resting ECG needs almost no preparation. Avoid applying oils or lotion to your chest that day, as electrodes need clean skin to make good contact. Wear a top that is easy to remove or open.'),
  ('p', 'For an exercise stress test, wear clothing and shoes you can walk comfortably in, and ask us when you book whether to adjust the timing of any medication or meals.'),
  ('h2', 'During the test'),
  ('ul', ['Small adhesive electrodes are placed on your chest, arms and legs.',
          'Some chest hair may need trimming so the electrodes stick properly.',
          'You lie still and breathe normally while the trace is recorded.',
          'Nothing passes into your body — the machine only listens. It is painless.',
          'Electrodes are removed afterwards and you can carry on as normal.']),
 ],
 'faqs': [
  ('Does an ECG hurt?',
   'No. Electrodes only detect signals your heart already produces — nothing is passed into your body. You may feel slight tugging when the adhesive pads are removed.'),
  ('How long does an ECG take?',
   'A resting ECG generally takes only a few minutes once the electrodes are placed. Stress testing takes longer, and Holter monitoring runs for around 24 hours while you go about your day.'),
  ('What can an ECG detect?',
   'It can show abnormal rhythms, evidence of a previous or ongoing heart attack, signs of reduced blood supply to the heart muscle, and changes suggesting the heart is enlarged. Results are interpreted alongside your symptoms and history.'),
  ('Do I need to prepare?',
   'Very little. Avoid oils or lotion on your chest that day and wear something easy to open at the front.'),
 ],
 'related': ['health-screening-packages', 'blood-test-laboratory-services-onitsha', 'ct-scan-imaging-anambra'],
},
{
 'slug': 'health-screening-packages',
 'title': 'Health Screening &amp; Check-Up Packages | Reene Medical Onitsha',
 'desc': 'Preventive health screening in Awada, Obosi, Onitsha — laboratory, imaging and cardiac checks combined into a package built around you. Call for options and pricing.',
 'eyebrow': 'Preventive',
 'h1a': 'Health screening', 'h1b': '&amp; <span class="italic">check-ups.</span>',
 'img': 'facility.png', 'pos': '50% 42%',
 'lede': 'Preventive checks that combine laboratory, imaging and cardiac testing — assembled around your age, history and what your doctor wants reviewed.',
 'duration': 'Varies by package',
 'radiation': 'Depends on tests included',
 'body': [
  ('h2', 'Why screening matters'),
  ('p', 'Many of the conditions that cause the most harm — raised blood pressure, diabetes, kidney and liver disease, abnormal cholesterol — develop quietly. People often feel entirely well while measurable changes are already underway. Periodic testing is how those changes get found early, while there is still room to act.'),
  ('h2', 'What a package can include'),
  ('p', 'Screening at Reene draws on the full range of services under our roof, combined to suit the person being screened:'),
  ('ul-cols', ['Complete Blood Count', 'Blood sugar testing',
               'Lipid profile', 'Liver function tests',
               'Kidney function tests', 'Thyroid function tests',
               'Hormone tests', 'Urinalysis',
               'Ultrasound scanning', 'Digital X-ray',
               'ECG &amp; cardiac assessment', 'Infection screening']),
  ('callout', 'Packages are put together around your age, symptoms, family history and any tests your doctor has specifically asked for — so the right combination differs from person to person. <strong>Call us on <a href="tel:+2348122190051">0812 219 0051</a> and we will talk through what makes sense for you, including current pricing.</strong>'),
  ('h2', 'Screening for organisations'),
  ('p', 'We also arrange screening for groups of staff. If you are organising testing for a workplace, tell us the number of people involved and what you would like covered, and we will put together arrangements and pricing for the group.'),
  ('h2', 'How to arrange a screening'),
  ('ul', ['Call or message us and describe what you would like checked.',
          'We suggest a combination of tests, and confirm current pricing.',
          'We tell you what preparation is needed — some tests require fasting.',
          'You attend, and the tests are carried out in a single visit where possible.',
          'We confirm when your results will be ready before you leave.']),
 ],
 'faqs': [
  ('How often should I have a health check?',
   'That depends on your age, family history, existing conditions and risk factors — there is no single interval that fits everyone. Your doctor can advise what is appropriate for you, and we can carry out the tests recommended.'),
  ('What is included in a screening package?',
   'Packages are assembled from our laboratory, imaging and cardiac services and tailored to the individual. Call us and we will recommend a combination and confirm what it costs.'),
  ('Do I need to fast beforehand?',
   'Often yes, because packages commonly include lipid profile and blood sugar, which are usually fasting tests. We will tell you exactly what to do when you book.'),
  ('Can you screen a group of staff?',
   'Yes. Tell us how many people are involved and what you would like covered, and we will arrange it and confirm pricing for the group.'),
 ],
 'related': ['blood-test-laboratory-services-onitsha', 'ecg-heart-health-testing', 'pregnancy-ultrasound-onitsha'],
},
]

BY_SLUG = {p['slug']: p for p in PAGES}
SHORT = {
 'pregnancy-ultrasound-onitsha': ('Pregnancy Ultrasound', 'Obstetric, 3D and 4D scanning'),
 'blood-test-laboratory-services-onitsha': ('Blood Tests &amp; Lab', 'Routine and specialised testing'),
 'ct-scan-imaging-anambra': ('CT Scan', 'Cross-sectional imaging'),
 'mri-scan-services-onitsha': ('MRI Scan', 'Soft-tissue detail, no radiation'),
 'digital-x-ray-services-onitsha': ('Digital X-Ray', 'Chest and skeletal radiography'),
 'ecg-heart-health-testing': ('ECG', 'Rhythm and cardiac assessment'),
 'health-screening-packages': ('Health Screening', 'Preventive check-up packages'),
}


def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == 'h2':      out.append('<h2>%s</h2>' % val)
        elif kind == 'h3':    out.append('<h3>%s</h3>' % val)
        elif kind == 'p':     out.append('<p>%s</p>' % val)
        elif kind == 'callout': out.append('<div class="callout"><p>%s</p></div>' % val)
        elif kind == 'ul':    out.append('<ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in val))
        elif kind == 'ul-cols': out.append('<ul class="cols">%s</ul>' % ''.join('<li>%s</li>' % i for i in val))
    return '\n        '.join(out)


def strip_tags(s):
    import re
    return re.sub(r'<[^>]+>', '', s).replace('&rsquo;', '’').replace('&amp;', '&').replace('&nbsp;', ' ')


TPL = io.open('_service_template.html', encoding='utf-8').read()

for p in PAGES:
    faq_html = '\n        '.join(
        '<details class="faq-item"><summary>%s</summary><div class="faq-a">%s</div></details>' % (q, a)
        for q, a in p['faqs'])

    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q),
         "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in p['faqs']]}

    svc_schema = {
        "@context": "https://schema.org", "@type": "MedicalTest",
        "name": strip_tags(p['h1a'] + ' ' + p['h1b']).strip(' .'),
        "description": strip_tags(p['lede']),
        "url": '%s/%s' % (BASE, p['slug']),
        "provider": {"@id": BASE + "/#clinic"},
        "availableAtOrFrom": {"@id": BASE + "/#clinic"},
    }
    crumb_schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": BASE + "/services"},
        {"@type": "ListItem", "position": 3, "name": strip_tags(p['title'].split('|')[0]).strip(),
         "item": '%s/%s' % (BASE, p['slug'])}]}

    related_html = '\n        '.join(
        '<a href="%s.html"><b>%s</b><span>%s</span></a>' % (s, SHORT[s][0], SHORT[s][1])
        for s in p['related'])

    html = (TPL
        .replace('{{TITLE}}', p['title'])
        .replace('{{DESC}}', p['desc'])
        .replace('{{SLUG}}', p['slug'])
        .replace('{{IMG}}', p['img'])
        .replace('{{POS}}', p['pos'])
        .replace('{{EYEBROW}}', p['eyebrow'])
        .replace('{{H1A}}', p['h1a'])
        .replace('{{H1B}}', p['h1b'])
        .replace('{{CRUMB_NAME}}', strip_tags(p['title'].split('|')[0]).strip())
        .replace('{{LEDE}}', p['lede'])
        .replace('{{DURATION}}', p['duration'])
        .replace('{{RADIATION}}', p['radiation'])
        .replace('{{PRICE}}', PRICE_PLACEHOLDER)
        .replace('{{BODY}}', render_body(p['body']))
        .replace('{{FAQS}}', faq_html)
        .replace('{{RELATED}}', related_html)
        .replace('{{SCHEMA_SERVICE}}', json.dumps(svc_schema, indent=2, ensure_ascii=False))
        .replace('{{SCHEMA_FAQ}}', json.dumps(faq_schema, indent=2, ensure_ascii=False))
        .replace('{{SCHEMA_CRUMB}}', json.dumps(crumb_schema, indent=2, ensure_ascii=False)))

    fn = p['slug'] + '.html'
    io.open(fn, 'w', encoding='utf-8', newline='').write(html)
    words = len(strip_tags(render_body(p['body']) + faq_html).split())
    print('%-42s %4d words  %d FAQs' % (fn, words, len(p['faqs'])))
