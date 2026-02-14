allergy_examples ="""
TASK:
Allergy Extraction ONLY

You are extracting ONLY AllergyEvent objects.

Definition of an AllergyEvent:
- A stated allergy, sensitivity, or adverse immune-type reaction to a substance (medication, food, environmental agent, latex, etc.).
- Includes mentions like “I’m allergic to X”, “X gives me hives”, “I had anaphylaxis to X”, “rash with X”.
- Also includes clinician-confirmed allergies.

DO NOT extract:
- Medication usage or medication changes (those belong to MedicationEvent).
- Side effects that are not framed as an allergy (e.g., “metformin causes nausea” is a side effect, not an allergy).
- Symptoms without an allergen (e.g., “I have a rash” with no cause).
- Lifestyle, diagnoses, family history, administrative details, or small talk.

Critical constraints:
- Create an AllergyEvent ONLY if an allergen is present (explicitly named or clearly referenced).
- NEVER create placeholder or filler events.
- NEVER create events with all null/empty fields.
- If no allergy events are present in the provided text, return:
  { "events": [] }

Field rules:
- allergen: must be the triggering substance/agent (e.g., “penicillin”, “peanuts”, “latex”).
- reaction: use the stated reaction if present (e.g., “hives”, “rash”, “throat swelling”, “anaphylaxis”).
  - If reaction is not stated, set reaction to null (preferred) OR to a schema-allowed “unknown” value if your schema forbids null.
- status: use the transcript’s meaning (e.g., current/past/never). If unclear, use schema-allowed unknown/unclear value or null if allowed.
- severity: use transcript wording (mild/moderate/severe). If unclear, set to unknown/unclear (or null if allowed).
- entity_ref: “explicit” when directly stated; use “previous/indirect” only when the allergen is referenced indirectly (e.g., “that antibiotic”).
- speaker: who stated it (patient/doctor) per your Diarization enum.
- evidence: MUST quote the supporting line(s) from the transcript.
- confidence: 0–10 based on clarity; do not use 0 as a placeholder.

Example 1: Clear allergy + reaction + severity

Transcript:
Patient: I’m allergic to penicillin. I break out in hives and my lips swell.
Doctor: That sounds serious.

Output JSON object:
{
  "events": [
    {
      "allergen": "penicillin",
      "reaction": "hives and lip swelling",
      "entity_ref": "explicit",
      "status": "current",
      "severity": "severe",
      "speaker": "patient",
      "confidence": 9,
      "evidence": "I’m allergic to penicillin. I break out in hives and my lips swell.",
      "doctor_remarks": "That sounds serious."
    }
  ]
}

Example 2: Multiple allergies (food + medication)

Transcript:
Patient: Peanuts give me a rash. Also, I had a bad reaction to sulfa drugs—got hives.
Doctor: Okay, we’ll document both.

Output JSON object:
{
  "events": [
    {
      "allergen": "peanuts",
      "reaction": "rash",
      "entity_ref": "explicit",
      "status": "current",
      "severity": "moderate",
      "speaker": "patient",
      "confidence": 8,
      "evidence": "Peanuts give me a rash.",
      "doctor_remarks": null
    },
    {
      "allergen": "sulfa drugs",
      "reaction": "hives",
      "entity_ref": "explicit",
      "status": "past",
      "severity": "moderate",
      "speaker": "patient",
      "confidence": 8,
      "evidence": "I had a bad reaction to sulfa drugs—got hives.",
      "doctor_remarks": "Okay, we’ll document both."
    }
  ]
}

Example 3: Allergy stated but reaction not provided (still extract)

Transcript:
Patient: I’m allergic to latex.
Doctor: Noted.

Output JSON object:
{
  "events": [
    {
      "allergen": "latex",
      "reaction": null,
      "entity_ref": "explicit",
      "status": "current",
      "severity": "unknown",
      "speaker": "patient",
      "confidence": 7,
      "evidence": "I’m allergic to latex.",
      "doctor_remarks": "Noted."
    }
  ]
}

Example 4: Not an allergy (side effect) -> no events

Transcript:
Patient: Metformin upsets my stomach and makes me nauseous.
Doctor: That can happen.

Output JSON object:
{
  "events": []
}
"""