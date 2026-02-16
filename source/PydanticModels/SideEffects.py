from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field

from source.PydanticModels.Common import Status, TimeRef, EntityRef, Diarization


class SideEffectEvent(BaseModel):
    event_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier for this side effect event. Auto-generated; do not infer from text."
    )

    effect: str = Field(
        ...,
        description="Reported or observed side effect or adverse reaction (e.g., 'nausea', 'rash', 'fatigue') as stated in the conversation."
    )

    status: Status = Field(
        ...,
        description="Temporal status of the side effect (e.g., current, past, resolved), based on how it is described."
    )

    time_ref: TimeRef = Field(
        ...,
        description="Time reference indicating when the side effect occurred relative to treatment or conversation (e.g., onset, ongoing, resolved)."
    )

    entity_ref: EntityRef = Field(
        ...,
        description="Reference type indicating whether the side effect is explicitly mentioned, inferred from prior context, or referred to indirectly."
    )

    speaker: Diarization = Field(
        ...,
        description="Speaker identifier indicating who reported or confirmed the side effect (e.g., patient or clinician speaker label)."
    )

    confidence: float = Field(
        ...,
        ge=0,
        le=10,
        description="Extractor confidence score (0–10) reflecting how clearly this side effect is supported by the transcript."
    )

    evidence: str = Field(
        ...,
        description="Exact quoted text or a faithful paraphrase from the transcript that supports the side effect information."
    )

    doctor_remarks: str | None = Field(
        default=None,
        description="Additional clinician comments or contextual notes related to the side effect, if provided."
    )


class SideEffectExtraction(BaseModel):
    events: List[SideEffectEvent] = Field(
        default_factory=list,
        description="List of side effect events extracted from the input conversation or transcript segment."
    )
