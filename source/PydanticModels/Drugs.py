from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field
#UUIDStr

from source.PydanticModels.Common import Action, EntityRef, Diarization


class MedicationEvent(BaseModel):
    event_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier for this medication event. Auto-generated; do not infer from text."
    )

    drug_name: str = Field(
        ...,
        description="Name of the medication as stated or clearly implied in the conversation (e.g., 'metformin', 'ibuprofen')."
    )

    action: Action = Field(
        ...,
        description="Action taken or discussed regarding the medication (e.g., started, stopped, continued, adjusted)."
    )

    dose: float | None = Field(
        default=None,
        description="Numeric dose amount of the medication if explicitly mentioned (e.g., 500 for '500 mg'). Do not infer units."
    )

    frequency: str | None = Field(
        default=None,
        description="Frequency at which the medication is taken if stated (e.g., 'once daily', 'twice a day')."
    )

    route: str | None = Field(
        default=None,
        description="Route of administration if mentioned (e.g., 'oral', 'IV', 'subcutaneous')."
    )

    effective_date: str | None = Field(
        default=None,
        description="Date or timeframe when the medication action takes effect, if mentioned (e.g., 'starting tomorrow', 'since last week')."
    )

    reason: str | None = Field(
        default=None,
        description="Reason for starting, stopping, or changing the medication, if provided."
    )

    entity_ref: EntityRef = Field(
        ...,
        description="Reference type indicating whether the medication is explicitly mentioned, inferred from prior context, or referred to indirectly."
    )

    speaker: Diarization = Field(
        ...,
        description="Speaker identifier indicating who stated or confirmed the medication information (e.g., patient or clinician speaker label)."
    )

    confidence: float = Field(
        ...,
        ge=0,
        le=10,
        description="Extractor confidence score (0–10) reflecting how clearly this medication event is supported by the transcript."
    )

    evidence: str = Field(
        ...,
        description="Exact quoted text or a faithful paraphrase from the transcript that supports this medication event."
    )

    doctor_remarks: str | None = Field(
        default=None,
        description="Additional clinician comments or clarifications related to the medication, if provided."
    )

class MedicationExtraction(BaseModel):
    events: List[MedicationEvent] = Field(
        default_factory=list,
        description="List of medication events extracted from the input conversation or transcript segment."
    )

