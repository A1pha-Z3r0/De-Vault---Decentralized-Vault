lifestyle_examples = """
TASK:
Lifestyle Extraction ONLY

You are extracting ONLY LifestyleEvent objects, each with a domain-specific "details" payload.

Lifestyle domains:
- sleep, diet, alcohol, tobacco, exercise

Critical constraints:
- Use ONLY information explicitly stated in the transcript.
- Do NOT guess quantities, frequencies, or patterns.
- Do NOT create placeholder/filler events.
- If no lifestyle info is present, return:
  { "events": [] }

Discriminator rule (strict):
- For every event:
  - "domain" MUST match "details.domain" exactly.
  - Example: domain="sleep" requires details.domain="sleep" and SleepPayload fields only.

What counts as Lifestyle info:
- sleep: sleep duration, sleep quality, insomnia, sleep schedule
- diet: appetite, dietary pattern, nutrition habits, notable dietary restrictions
- alcohol: drinking status, amount/frequency, binge mention, last use
- tobacco: smoking/vaping/nicotine product use status, quantity, quit timeframe
- exercise: sessions/week, intensity, duration, activity type

DO NOT extract:
- Symptoms, diagnoses, medications, allergies, side effects
- Admin/scheduling/small talk

Field rules:
- entity_ref: must be one of {explicit, previous, currently, same, that, other, unknown}
- speaker: must be one of {patient, healthcare_professional, unknown}
- status: must be one of {"current","past","never"} or null (only if explicitly stated)
  - "never" only if the transcript explicitly denies use (e.g., “I don’t drink”).
  - If unclear, use null.
- confidence: 0–10 based on clarity; do not use 0 as placeholder.
- evidence: must quote the exact supporting line.

Details rules (no guessing):
- Only populate numeric fields (hours, drinks, sessions, minutes, years) if explicitly stated.
- If a field is not stated, set it to null/omit depending on schema defaults (use null if you must include it).

Example 1: Multi-domain (sleep + alcohol)

Transcript:
Patient: I’ve been sleeping about 5 hours a night recently. I drink socially—maybe two beers on weekends.
Doctor: Okay.

Output JSON object:

{{
"events": [
{{
"domain": "sleep",
"entity_ref": "explicit",
"status": null,
"speaker": "patient",
"confidence": 8,
"evidence": "I’ve been sleeping about 5 hours a night recently.",
"details": {{
"domain": "sleep",
"duration_hours": 5,
"quality": null,
"timeframe": "recently"
}}
}},
{{
"domain": "alcohol",
"entity_ref": "explicit",
"status": "current",
"speaker": "patient",
"confidence": 8,
"evidence": "I drink socially—maybe two beers on weekends.",
"details": {{
"domain": "alcohol",
"use_status": "uses",
"drinks_per_week": null,
"drinks_per_day": null,
"binge": null,
"last_use": "on weekends"
}}
}}
]
}}

Example 2: Tobacco denial (never)

Transcript:
Doctor: Do you smoke or use any tobacco products?
Patient: No, I don’t smoke or vape.

Output JSON object:

{{
"events": [
{{
"domain": "tobacco",
"entity_ref": "explicit",
"status": "never",
"speaker": "patient",
"confidence": 9,
"evidence": "No, I don’t smoke or vape.",
"details": {{
"domain": "tobacco",
"product": "unknown",
"use_status": "denies",
"cigarettes_per_day": null,
"packs_per_day": null,
"years_used": null,
"quit_timeframe": null
}}
}}
]
}}

Example 3: Exercise routine

Transcript:
Patient: I work out about 3 times a week, usually 45 minutes, moderate intensity. Mostly jogging.
Doctor: Great.

Output JSON object:

{{
"events": [
{{
"domain": "exercise",
"entity_ref": "explicit",
"status": "current",
"speaker": "patient",
"confidence": 9,
"evidence": "I work out about 3 times a week, usually 45 minutes, moderate intensity. Mostly jogging.",
"details": {{
"domain": "exercise",
"sessions_per_week": 3,
"duration_minutes": 45,
"intensity": "moderate",
"activity_type": "jogging"
}}
}}
]
}}

Example 4: Diet pattern + notes (no guessing)

Transcript:
Patient: My appetite’s been low. I’m trying to eat more protein but it’s been tough.
Doctor: Okay.

Output JSON object:

{{
"events": [
{{
"domain": "diet",
"entity_ref": "explicit",
"status": null,
"speaker": "patient",
"confidence": 8,
"evidence": "My appetite’s been low. I’m trying to eat more protein but it’s been tough.",
"details": {{
"domain": "diet",
"pattern": "low_appetite",
"notes": "Trying to eat more protein but it’s been tough."
}}
}}
]
}}

Example 5: No lifestyle info

Transcript:
Doctor: Let’s review your medications.
Patient: Sure.

Output JSON object:

{{
"events": []
}}
"""