from enum import Enum

class Status(str, Enum):
    present = "present"
    absent = "absent"
    resolved = "resolved"
    denied = "denied"
    suspected = "suspected"
    unknown = "unknown"


class TimeRef(str, Enum):
    now = "now"
    last_week = "last week"
    last_month = "last month"
    last_year = "last year"
    after_starting_medication = "after starting medication"
    recently = "recently"
    null = "null"
    unknown = "unknown"

class EntityRef(str, Enum):
    explicit = "explicit"
    previous = "previous"
    currently = "currently"
    same = "same"
    that = "that"
    other = "other"
    unknown = "unknown"

class Diarization(str,Enum):
    healthcare_professional = "healthcare_professional"
    patient = "patient"
    unknown = "unknown"

class Severity(str, Enum):
    mild = "mild"
    moderate = "moderate"
    severe = "severe"
    unknown = "unknown"
    null = "null"

class Action(str, Enum):
    going_to_start = "going_to_start"
    start = "start"
    stop = "stop"
    change = "change"
    continued = "continued"

class Chronic(str, Enum):
    acute = "acute"
    chronic = "chronic"
    unknown = "unknown"
    null = "null"

class DiagnosisConf(str, Enum):
    confirmed = "confirmed"
    suspected = "suspected"
    ruled_out = "ruled_out"
    unknown = "unknown"