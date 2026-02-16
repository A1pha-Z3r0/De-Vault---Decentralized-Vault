from typing import List, Annotated
from uuid import uuid4

from pydantic import BaseModel, Field

from source.PydanticModels.Common import DiagnosisConf, EntityRef, Chronic, Diarization


class DiagnosisEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid4()),
                              description="Unique identifier for this diagnosis event. "
                                          "Auto-generated; do not infer from text."
                              )

    condition: str = Field(
        ...,
        description="Name of the diagnosed condition as stated or clearly implied "
                    "in the conversation (e.g., 'type 2 diabetes', 'asthma')."
    )

    diag_confidence: DiagnosisConf = Field(
        ...,
        description="Clinician-level certainty of the diagnosis (e.g., confirmed, suspected, ruled_out), based on how definitively it is stated."
    )


    entity_ref: EntityRef = Field(
        ...,
        description="Reference type indicating whether the diagnosis is explicitly mentioned, inferred from prior context, or referred to indirectly."
    )

    onset: str | None = Field(
        default=None,
        description="Timeframe describing when the condition began or was first diagnosed, if mentioned (e.g., 'last year', 'since childhood')."
    )

    chronicity: Chronic | None = Field(
        default=None,
        description="Whether the condition is acute, chronic, recurrent, or unclear based on the conversation."
    )

    speaker: Diarization = Field(
        ...,
        description="Speaker identifier indicating who stated or confirmed the diagnosis (e.g., patient or clinician speaker label)."
    )
    confidence: float = Field(
        ...,
        ge=0,
        le=10,
        description="Extractor confidence score (0–10) reflecting how clearly this diagnosis is supported by the transcript."
    )

    evidence: str = Field(
        ...,
        description="Exact quoted text or a faithful paraphrase from the transcript that supports this diagnosis."
    )

class DiagnosisExtraction(BaseModel):
    events: List[DiagnosisEvent] = Field(
        default_factory=list,
        description="List of diagnosis events extracted from the input conversation chunk."
    )
