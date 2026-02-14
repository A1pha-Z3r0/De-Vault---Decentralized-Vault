domain_examples = """
TASK:
Diagnosis Extraction ONLY

You are extracting ONLY DiagnosisEvent objects.

Definition of a DiagnosisEvent:
- A condition that is stated as a diagnosis, assessment, impression, or clinician conclusion.
- Includes confirmed diagnoses (“You have asthma”), suspected diagnoses (“This might be GERD”), and ruled-out diagnoses (“This is not pneumonia”).

DO NOT extract:
- Symptoms without a diagnosis (belongs to SymptomEvent).
- Medication plans (MedicationEvent).
- Allergies (AllergyEvent).
- Family history (unless explicitly framed as the patient’s diagnosis).
- Screening/labs without a diagnostic conclusion.

Critical constraints:
- Create a DiagnosisEvent ONLY if a condition name is present (explicitly named or clearly implied as a diagnosis).
- NEVER create placeholder/filler events.
- If no diagnosis events are present, return: { "events": [] }

Enum constraints (must match exactly):
- diag_confidence: one of {confirmed, suspected, ruled_out, unknown}
- entity_ref: one of {explicit, previous, currently, same, that, other, unknown}
- speaker: one of {healthcare_professional, patient, unknown}
- chronicity: one of {acute, chronic, unknown, null} (or null/None if your schema allows)
- onset: Use the exact timeframe wording from the transcript (e.g., “since childhood”, “last year”). Do not normalize or convert into structured categories. If not stated, set to null.

Field rules:
- condition: the diagnosis label (e.g., “asthma”, “hypertension”).
- evidence: quote the exact line supporting the diagnosis.
- confidence: 0–10 based on clarity; do not use 0 as a placeholder.

Example 1: Confirmed diagnosis (explicit)

Transcript:
Doctor: Based on your labs, you have type 2 diabetes.
Patient: Okay.

Output JSON object:
{
  "events": [
    {
      "condition": "type 2 diabetes",
      "diag_confidence": "confirmed",
      "entity_ref": "explicit",
      "onset": null,
      "chronicity": "chronic",
      "speaker": "healthcare_professional",
      "confidence": 9,
      "evidence": "Based on your labs, you have type 2 diabetes."
    }
  ]
}

Example 2: Suspected diagnosis + onset mentioned

Transcript:
Doctor: This sounds like GERD. You said it started about two months ago, right?
Patient: Yeah, around two months.

Output JSON object:
{
  "events": [
    {
      "condition": "GERD",
      "diag_confidence": "suspected",
      "entity_ref": "explicit",
      "onset": "about two months ago",
      "chronicity": "unknown",
      "speaker": "healthcare_professional",
      "confidence": 8,
      "evidence": "This sounds like GERD. You said it started about two months ago, right?"
    }
  ]
}

Example 3: Ruled-out diagnosis (explicit)

Transcript:
Doctor: I do not think this is pneumonia. Your lungs sound clear.
Patient: That’s good.

Output JSON object:
{
  "events": [
    {
      "condition": "pneumonia",
      "diag_confidence": "ruled_out",
      "entity_ref": "explicit",
      "onset": null,
      "chronicity": "unknown",
      "speaker": "healthcare_professional",
      "confidence": 8,
      "evidence": "I do not think this is pneumonia."
    }
  ]
}

Example 4: Patient-reported prior diagnosis (previous)

Transcript:
Patient: I was diagnosed with asthma when I was a kid.
Doctor: Got it.

Output JSON object:
{
  "events": [
    {
      "condition": "asthma",
      "diag_confidence": "confirmed",
      "entity_ref": "previous",
      "onset": "when I was a kid",
      "chronicity": "chronic",
      "speaker": "patient",
      "confidence": 8,
      "evidence": "I was diagnosed with asthma when I was a kid."
    }
  ]
}

Example 5: No diagnosis present (symptoms only)

Transcript:
Patient: I’ve been having headaches and fatigue this week.
Doctor: Let’s see what might be causing it.

Output JSON object:
{
  "events": []
}

Example 6: Indirect reference to a diagnosis (that/same)

Transcript:
Doctor: The hypertension we talked about last visit is still not controlled.
Patient: Yeah.

Output JSON object:
{
  "events": [
    {
      "condition": "hypertension",
      "diag_confidence": "confirmed",
      "entity_ref": "previous",
      "onset": null,
      "chronicity": "chronic",
      "speaker": "healthcare_professional",
      "confidence": 7,
      "evidence": "The hypertension we talked about last visit is still not controlled."
    }
  ]
}
"""
