from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field

from source.PydanticModels.Common import EntityRef, Status, Severity, Diarization


class AllergyEvent(BaseModel):
    event_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier for this allergy event. Auto-generated; do not infer from text."
    )

    allergen: str = Field(
        ...,
        description="Substance or agent that triggers the allergic reaction, as explicitly stated or clearly implied (e.g., 'penicillin', 'peanuts')."
    )

    reaction: str = Field(
        ...,
        description="Observed or reported allergic reaction or symptoms associated with the allergen (e.g., 'rash', 'anaphylaxis')."
    )

    entity_ref: EntityRef = Field(
        ...,
        description="Reference type indicating whether the allergy is explicitly mentioned, inferred from prior context, or referred to indirectly."
    )

    status: Status = Field(
        ...,
        description="Temporal status of the allergy (e.g., current, past, or never), based on how it is described in the conversation."
    )

    severity: Severity = Field(
        ...,
        description="Clinical severity of the allergic reaction as described (e.g., mild, moderate, severe), or unknown if unclear."
    )

    speaker: Diarization = Field(
        ...,
        description="Speaker identifier indicating who reported or confirmed the allergy (e.g., patient or clinician speaker label)."
    )

    confidence: float = Field(
        ...,
        ge=0,
        le=10,
        description="Extractor confidence score (0–10) reflecting how clearly this allergy event is supported by the transcript."
    )

    evidence: str = Field(
        ...,
        description="Exact quoted text or a faithful paraphrase from the transcript that supports the allergy information."
    )

    doctor_remarks: str | None = Field(
        default=None,
        description="Additional clinician comments or clarifications related to the allergy, if provided."
    )

class AllergyExtraction(BaseModel):
    events: List[AllergyEvent] = Field(
        default_factory=list,
        description="List of allergy events extracted from the input conversation or transcript segment."
    )

