drug_examples = """
TASK:
Medication Extraction ONLY

You are extracting ONLY MedicationEvent objects.

Definition of a MedicationEvent:
- A medication being started, stopped, continued, adjusted, prescribed, or used.
- This includes discussions of dose, frequency, route, or timing.
- Indirect references (e.g., "it", "the same meds") are allowed ONLY if a medication context is present.

DO NOT extract:
- Allergies (these belong to AllergyEvent).
- Side effects unless the task explicitly includes them.
- Symptoms not framed as medication management.
- Diagnoses, family history, lifestyle, administrative details, or small talk.
- Statements without medication relevance.

Critical constraints:
- If a medication name OR a medication action is not present, DO NOT create an event.
- NEVER create placeholder or filler events.
- NEVER create events with all null fields.
- If no medication events are present in the provided text, return:
  { "events": [] }

Field rules:
- drug_name: null ONLY if the medication is referred to indirectly (e.g., "the same meds").
- action: must be one of the allowed enum values. If unclear, set to null.
- confidence: reflect how clearly the medication event is supported (0–10). Do not use 0 as a placeholder.


Example 1: Single Clear medication

Transcript:
Doctor: Let’s start you on metformin 500 mg once daily.
Patient: Okay.

Output JSON object:

{{
  "events": [
    {{
      "drug_name": "metformin",
      "action": "started",
      "dose": 500,
      "frequency": "once daily",
      "route": null,
      "effective_date": null,
      "reason": null,
      "entity_ref": "explicit",
      "speaker": "doctor",
      "confidence": 9,
      "evidence": "Let’s start you on metformin 500 mg once daily.",
      "doctor_remarks": null
    }}
  ]
}}

Example 2: Multiple Medications

Transcript:
Patient: I’ve been taking ibuprofen as needed.
Doctor: Continue that, but stop aspirin.

Output JSON object:

{{
  "events": [
    {{
      "drug_name": "ibuprofen",
      "action": "continued",
      "dose": null,
      "frequency": "as needed",
      "route": null,
      "effective_date": null,
      "reason": null,
      "entity_ref": "explicit",
      "speaker": "patient",
      "confidence": 8,
      "evidence": "I’ve been taking ibuprofen as needed.",
      "doctor_remarks": null
    }},
    {{
      "drug_name": "aspirin",
      "action": "stopped",
      "dose": null,
      "frequency": null,
      "route": null,
      "effective_date": null,
      "reason": null,
      "entity_ref": "explicit",
      "speaker": "doctor",
      "confidence": 9,
      "evidence": "Stop aspirin.",
      "doctor_remarks": null
    }}
  ]
}}

Example 3: No Medications
Patient: I’m totally allergic to Cephalosporins, like Ceftriaxone .
Doctor: That’s common, with don't worry we will look at alternatives.
Output JSON object:

{{
  "events": []
}}

Example 4: No Medications

Transcript:
Patient: I’ve been feeling tired lately.
Doctor: That’s common with stress.

Output JSON object:

{{
  "events": []
}}
"""


