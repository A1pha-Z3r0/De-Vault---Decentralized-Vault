from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field

from source.PydanticModels.Common import EntityRef, Status, Severity, Diarization


class SymptomEvent(BaseModel):
    event_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier for this symptom event. Auto-generated; do not infer from text."
    )

    symptom: str = Field(
        ...,
        description="Name or description of the symptom as reported or clearly implied in the conversation (e.g., 'chest pain', 'shortness of breath')."
    )

    entity_ref: EntityRef = Field(
        ...,
        description="Reference type indicating whether the symptom is explicitly mentioned, inferred from prior context, or referred to indirectly."
    )

    status: Status = Field(
        ...,
        description="Current status of the symptom (e.g., current, past, resolved), based on how it is described."
    )

    severity: Severity | None = Field(
        default=None,
        description="Severity of the symptom if stated (e.g., mild, moderate, severe); use null if not specified."
    )

    onset: str | None = Field(
        default=None,
        description="Timeframe describing when the symptom began, if mentioned (e.g., 'three days ago', 'since last night')."
    )

    duration: str | None = Field(
        default=None,
        description="Duration for which the symptom has been present, if mentioned (e.g., 'for two weeks', 'intermittent')."
    )

    speaker: Diarization = Field(
        ...,
        description="Speaker identifier indicating who reported or confirmed the symptom (e.g., patient or clinician speaker label)."
    )

    confidence: float = Field(
        ...,
        ge=0,
        le=10,
        description="Extractor confidence score (0–10) reflecting how clearly this symptom is supported by the transcript."
    )

    evidence: str = Field(
        ...,
        description="Exact quoted text or a faithful paraphrase from the transcript that supports the symptom information."
    )

    doctor_remarks: str | None = Field(
        default=None,
        description="Additional clinician comments or contextual notes related to the symptom, if provided."
    )


class SymptomExtraction(BaseModel):
    events: List[SymptomEvent] = Field(
        default_factory=list,
        description="List of symptom events extracted from the input conversation or transcript segment."
    )
