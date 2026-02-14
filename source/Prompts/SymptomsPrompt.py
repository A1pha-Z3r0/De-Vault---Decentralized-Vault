symptoms_examples = """
TASK:
Symptom Extraction ONLY

You are extracting ONLY SymptomEvent objects.

Definition of a SymptomEvent:
- Any patient-reported or clinician-confirmed symptom/complaint (physical or psychological).
- Examples: chest pain, shortness of breath, headache, nausea, fatigue, dizziness.

Important rule (high recall):
- If a symptom is mentioned, extract it as a SymptomEvent.
- Do NOT try to decide whether it is a medication side effect. Attribution is handled separately by the SideEffects extractor.

DO NOT extract:
- Diagnoses (e.g., “You have asthma”) → DiagnosisEvent
- Allergies (e.g., “allergic to penicillin”) → AllergyEvent
- Medication actions/changes (start/stop/continue/change dose) → MedicationEvent
- Lifestyle behaviors (sleep, alcohol, tobacco, exercise)
- Administrative details or small talk

Critical constraints:
- Create a SymptomEvent ONLY if a symptom description is present.
- NEVER create placeholder or filler events.
- If no symptoms are present, return:
  { "events": [] }

Field rules (must match enum values exactly):
- status: one of {present, absent, resolved, denied, suspected, unknown}
  - present: symptom currently happening
  - resolved: symptom occurred before but is gone now
  - denied: patient explicitly denies the symptom
  - suspected: clinician suggests possible symptom without confirmation
  - unknown: unclear
- severity: one of {mild, moderate, severe, unknown, null} OR None if not specified.
  - If severity not stated, use null (or None if you prefer missing).
- entity_ref: use {explicit, previous, currently, same, that, other, unknown}
  - explicit when directly stated; previous if referencing past context (“like last time”); that/same for indirect references.
- speaker: one of {patient, healthcare_professional, unknown}
- onset: use exact transcript wording (e.g., “three days ago”); do not normalize.
- duration: use exact transcript wording (e.g., “for two weeks”, “intermittent”); do not normalize.
- evidence: MUST quote the supporting line(s).
- confidence: 0–10 based on clarity; do not use 0 as a placeholder.
- doctor_remarks: include only if clinician explicitly comments on the symptom.

Example 1: Current symptom + duration + severity

Transcript:
Patient: I’ve had chest pain for three days. It’s pretty severe.
Doctor: Okay.

Output JSON object:

{{
"events": [
{{
"symptom": "chest pain",
"entity_ref": "explicit",
"status": "present",
"severity": "severe",
"onset": "three days ago",
"duration": "for three days",
"speaker": "patient",
"confidence": 9,
"evidence": "I’ve had chest pain for three days. It’s pretty severe.",
"doctor_remarks": "Okay."
}}
]
}}

Example 2: Resolved symptom

Transcript:
Patient: I had a fever last week, but it’s gone now.
Doctor: Good.

Output JSON object:

{{
"events": [
{{
"symptom": "fever",
"entity_ref": "explicit",
"status": "resolved",
"severity": "unknown",
"onset": "last week",
"duration": null,
"speaker": "patient",
"confidence": 8,
"evidence": "I had a fever last week, but it’s gone now.",
"doctor_remarks": "Good."
}}
]
}}

Example 3: Denied symptom

Transcript:
Doctor: Any shortness of breath?
Patient: No, none.

Output JSON object:

{{
"events": [
{{
"symptom": "shortness of breath",
"entity_ref": "explicit",
"status": "denied",
"severity": null,
"onset": null,
"duration": null,
"speaker": "patient",
"confidence": 8,
"evidence": "No, none.",
"doctor_remarks": null
}}
]
}}

Example 4: Symptom mentioned alongside medication (STILL extract as Symptom)

Transcript:
Patient: I started metformin last month. I’ve been feeling nauseous recently.
Doctor: Okay.

Output JSON object:

{{
"events": [
{{
"symptom": "nausea",
"entity_ref": "explicit",
"status": "present",
"severity": "unknown",
"onset": "recently",
"duration": null,
"speaker": "patient",
"confidence": 7,
"evidence": "I’ve been feeling nauseous recently.",
"doctor_remarks": "Okay."
}}
]
}}

Example 5: No symptoms present

Transcript:
Doctor: Let’s review your medications.
Patient: Sure.

Output JSON object:

{{
"events": []
}}

"""