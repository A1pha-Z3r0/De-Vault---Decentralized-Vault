from typing import Optional, Annotated, Union, Literal, List
from enum import Enum
from uuid import uuid4

from pydantic import BaseModel, Field, model_validator
from source.PydanticModels.Common import EntityRef, Diarization  # assuming common.py


class LifestyleDomain(str, Enum):
    sleep = "sleep"
    diet = "diet"
    alcohol = "alcohol"
    tobacco = "tobacco"
    exercise = "exercise"


class SleepPayload(BaseModel):
    domain: Literal["sleep"]
    duration_hours: Optional[float] = Field(default=None, ge=0, le=24)
    quality: Optional[Literal["poor", "fair", "good"]] = None
    timeframe: Optional[str] = None


class DietPayload(BaseModel):
    domain: Literal["diet"]
    pattern: Optional[Literal["balanced", "high_carb", "high_protein", "low_appetite", "unknown"]] = None
    notes: Optional[str] = None


class ExercisePayload(BaseModel):
    domain: Literal["exercise"]
    sessions_per_week: Optional[float] = Field(default=None, ge=0)
    duration_minutes: Optional[float] = Field(default=None, ge=0)
    intensity: Optional[Literal["light", "moderate", "vigorous"]] = None
    activity_type: Optional[str] = None


class AlcoholPayload(BaseModel):
    domain: Literal["alcohol"]
    use_status: Optional[Literal["uses", "denies", "stopped"]] = None
    drinks_per_week: Optional[float] = Field(default=None, ge=0)
    drinks_per_day: Optional[float] = Field(default=None, ge=0)
    binge: Optional[bool] = None
    last_use: Optional[str] = None


class TobaccoPayload(BaseModel):
    domain: Literal["tobacco"]
    product: Optional[Literal[
        "cigarettes", "vape", "cigar", "pipe", "chew", "nicotine_pouch", "patch_gum", "unknown"
    ]] = None
    use_status: Optional[Literal["uses", "denies", "stopped"]] = None
    cigarettes_per_day: Optional[float] = Field(default=None, ge=0)
    packs_per_day: Optional[float] = Field(default=None, ge=0)
    years_used: Optional[float] = Field(default=None, ge=0)
    quit_timeframe: Optional[str] = None


LifestyleDetails = Annotated[
    Union[SleepPayload, DietPayload, AlcoholPayload, TobaccoPayload, ExercisePayload],
    Field(discriminator="domain"),
]


class LifestyleEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid4()))
    domain: LifestyleDomain = Field(..., description="Lifestyle domain for this event (must match details.domain).")

    entity_ref: EntityRef = Field(..., description="How the entity was referenced (explicit, previous, etc.).")

    status: Optional[Literal["current", "past", "never"]] = Field(
        default=None,
        description="Temporal status if stated; otherwise null."
    )

    speaker: Diarization = Field(..., description="Speaker label who stated the info.")
    confidence: float = Field(ge=0, le=10, description="Extractor confidence 0–10.")
    evidence: str = Field(..., description="Quoted text or faithful paraphrase supporting the event.")

    details: LifestyleDetails

    @model_validator(mode="after")
    def _domain_consistency(self):
        # details.domain is a string Literal; self.domain is an Enum
        if self.details.domain != self.domain.value:
            raise ValueError("domain must match details.domain")
        return self


class LifestyleExtraction(BaseModel):
    events: List[LifestyleEvent] = Field(default_factory=list)
