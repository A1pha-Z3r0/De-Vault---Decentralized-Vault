"""
TODO: SHOULD ADD CONFIDENCE LEVEL TOO!
SideEffectEvent{
  "event_id": //uuid,
  "effect": "rash",
  "status": "present" | "resolved" | "denied" | "suspected",
  "time_ref": "now" | "last week" | "after starting" | null,
  entity_ref: "explicit" | "previous" | "current" | "same" | "that" | "unknown"
  "speaker": "patient" | "doctor",
  "confidence" : number,
  negated :  boolean
  "evidence": "…exact quote…",
  doctor_remarks : str
  "turn_range": [34, 36]
}
AllergyEvent {
  event_id: string,
  substance: string,
  reaction: string,
  entity_ref: "explicit" | "previous" | "current" | "same" | "that" | "unknown",
  status: "present" | "resolved" | "denied" | "suspected",
  severity: "mild" | "moderate" | "severe" | null,
  speaker_id: "A" | "B" | "unknown",
  role: "doctor" | "patient" | "unknown",
  confidence: number,
  negated: boolean,
  evidence: string,
  turn_range: [number, number]
}

MedicationEvent {
  event_id: string,                          // UUID
  drug_name: string,
  entity_ref: "explicit" | "previous" | "current" | "same" | "that" | "unknown"
  action: "start" | "stop" | "change" | "continue",
  dose: string | null,
  frequency: string | null,
  route: string | null,
  effective_date: string | null,
  reason: string | null,
  speaker_id: "A" | "B" | "unknown",
  role: "doctor" | "patient" | "unknown",
  confidence: number,
  negated: boolean,
  evidence: string,
  turn_range: [number, number]
}

SymptomEvent {
  event_id: string,
  symptom: string,
  entity_ref: "explicit" | "previous" | "current" | "same" | "that" | "unknown"
  status: "present" | "resolved" | "denied" | "worsening" | "improving",
  severity: "mild" | "moderate" | "severe" | null,
  onset: string | null,
  duration: string | null,
  speaker_id: "A" | "B" | "unknown",
  role: "doctor" | "patient" | "unknown",
  confidence: number,
  negated: boolean,
  evidence: string,
  turn_range: [number, number]
}

DiagnosisEvent {
  event_id: string,
  condition: string,
  status: "confirmed" | "suspected" | "ruled_out",
  entity_ref: "explicit" | "previous" | "current" | "same" | "that" | "unknown"
  onset: string | null,
  chronicity: "acute" | "chronic" | null | "unknown",
  speaker_id: "A" | "B" | "unknown",
  role: "doctor" | "patient" | "unknown",
  confidence: number,
  negated: boolean,
  evidence: string,
  turn_range: [number, number]
}

LifestyleEvent {
  event_id: string,
  domain: "sleep" | "alcohol" | "tobacco" | "exercise" | "diet",
  entity_ref: "explicit" | "previous" | "current" | "same" | "that" | "unknown"
  description: string,
  status: "current" | "past" | "never",
  frequency_or_amount: string | null,
  speaker_id: "A" | "B" | "unknown",
  role: "doctor" | "patient" | "unknown",
  confidence: number,
  negated: boolean,
  evidence: string,
  turn_range: [number, number]
}



LabResultEvent {
  event_id: string,
  test_name: string,
  value: string,
  unit: string | null,
  entity_ref: "explicit" | "previous" | "current" | "same" | "that" | "unknown",
  entity_ref: "explicit" | "previous" | "current" | "same" | "that" | "unknown"
  interpretation: "normal" | "high" | "low" | "abnormal" | null,
  date: string | null,
  speaker_id: "A" | "B" | "unknown",
  role: "doctor" | "patient" | "unknown",
  confidence: number,
  negated: boolean,
  evidence: string,
  turn_range: [number, number]
}

PlanEvent {
  event_id: string,
  action: "order_test" | "prescribe" | "refer" | "follow_up" | "monitor",
  target: string,
  timeframe: string | null,
  speaker_id: "A" | "B" | "unknown",
  role: "doctor" | "patient" | "unknown",
  confidence: number,
  negated: boolean,
  evidence: string,
  turn_range: [number, number]
}

"""