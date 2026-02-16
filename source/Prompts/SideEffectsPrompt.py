side_effect_examples ="""
TASK:
SideEffects Extraction ONLY (HIGH PRECISION)

You are extracting ONLY SideEffectEvent objects.

Definition of a SideEffectEvent:
- A symptom/adverse effect that is explicitly attributed to a medication or treatment in the transcript.
- The causal link must be stated clearly (do NOT infer causality).

Required explicit attribution cues:
- “X causes/makes me …”
- “After starting X, I had …”
- “Since I began X, I’ve been …”
- “That’s a side effect of X”
- “This medication is giving me …”
- “Because of the pill/meds, I feel …”

DO NOT extract:
- General symptoms without explicit attribution → SymptomEvent
- Allergies (“allergic to penicillin”) → AllergyEvent
- Medication changes/plans (start/stop/continue/change dose) → MedicationEvent
- Diagnoses, lifestyle, admin info, small talk

Critical constraints:
- Create a SideEffectEvent ONLY if explicit medication/treatment attribution is present in the same chunk.
- NEVER infer causality.
- NEVER create placeholder or filler events.
- If no explicitly attributed side effects are present, return:
  { "events": [] }

Field rules (must match enum values exactly):
- status: one of {present, absent, resolved, denied, suspected, unknown}
  - present: currently experiencing
  - resolved: happened before but is gone now
  - denied: explicitly denies side effects
- time_ref: one of {now, last week, last month, last year, after starting medication, recently, null, unknown}
  - Use "after starting medication" when timing is described relative to starting meds.
  - Otherwise choose the closest bucket from the transcript (recently/last week/last month/last year). If not stated, use unknown.
- entity_ref: one of {explicit, previous, currently, same, that, other, unknown}
- speaker: one of {patient, healthcare_professional, unknown}
- effect: the side effect text as stated (e.g., “nausea”, “diarrhea”, “rash”).
- evidence: MUST quote the attribution statement.
- confidence: 0–10 based on clarity; do not use 0 as placeholder.
- doctor_remarks: include only if explicitly stated by clinician.

Example 1: Explicit “after starting” link

Transcript:
Patient: After I started metformin, I’ve been nauseous and getting diarrhea.
Doctor: That can happen.

Output JSON object:

{{
"events": [
{{
"effect": "nausea and diarrhea",
"status": "present",
"time_ref": "after starting medication",
"entity_ref": "explicit",
"speaker": "patient",
"confidence": 9,
"evidence": "After I started metformin, I’ve been nauseous and getting diarrhea.",
"doctor_remarks": "That can happen."
}}
]
}}

Example 2: Explicit “med makes me” cue (time not specific)

Transcript:
Patient: This new blood pressure pill makes me dizzy sometimes.
Doctor: Okay, we can adjust it.

Output JSON object:

{{
"events": [
{{
"effect": "dizziness",
"status": "present",
"time_ref": "unknown",
"entity_ref": "explicit",
"speaker": "patient",
"confidence": 8,
"evidence": "This new blood pressure pill makes me dizzy sometimes.",
"doctor_remarks": "Okay, we can adjust it."
}}
]
}}

Example 3: Resolved side effect + time bucket

Transcript:
Patient: Last month, when I started the antibiotic, I got a rash, but it went away.
Doctor: Good.

Output JSON object:

{{
"events": [
{{
"effect": "rash",
"status": "resolved",
"time_ref": "last month",
"entity_ref": "explicit",
"speaker": "patient",
"confidence": 8,
"evidence": "Last month, when I started the antibiotic, I got a rash, but it went away.",
"doctor_remarks": "Good."
}}
]
}}

Example 4: General symptom only (NO attribution) → empty

Transcript:
Patient: I’ve been nauseous recently.
Doctor: Okay.

Output JSON object:

{{
"events": []
}}

Example 5: Allergy mention (NOT a side effect) → empty

Transcript:
Patient: I’m allergic to penicillin — I break out in hives.
Doctor: Noted.

Output JSON object:

{{
"events": []
}}

Example 6: Denied side effects (explicit denial)

Transcript:
Doctor: Any side effects from the medication?
Patient: No, none.

Output JSON object:

{{
"events": [
{{
"effect": "side effects",
"status": "denied",
"time_ref": "now",
"entity_ref": "explicit",
"speaker": "patient",
"confidence": 7,
"evidence": "No, none.",
"doctor_remarks": null
}}
]
}}
"""