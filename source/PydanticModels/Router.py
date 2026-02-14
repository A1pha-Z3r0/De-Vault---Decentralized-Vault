from enum import Enum
from typing import List, Dict

from pydantic import BaseModel, Field

class Domain(str, Enum):
    Allergy = "Allergy"
    Diagnosis = "Diagnosis"
    Medication = "Medications"
    Lifestyle = "Lifestyle"
    SideEffect = "SideEffects"
    Symptom = "Symptoms"
    Nothing = "None"

class RouterExtraction(BaseModel):
    domain : List[Domain] = Field(
                            default_factory=list,
                            description= "List of all Domains extracted from the input conversation or transcript segment.")

    confidence: Dict[Domain, float] = Field(
        ...,
        description="Per-event confidence scores (0–10) indicating certainty of each detected event."
    )

    notes: str | None = Field(
        default=None,
        description="Optional short note explaining ambiguity or indirect references."
    )


