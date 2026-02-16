from source.Prompts.SideEffectsPrompt import side_effect_examples
from source.Prompts.SymptomsPrompt import symptoms_examples
from source.PydanticModels.Allergy import AllergyExtraction
from source.Prompts.AllergyPrompt import allergy_examples

from source.Prompts.DrugPrompt import drug_examples
from source.PydanticModels.Diagnosis import DiagnosisExtraction
from source.Prompts.DiagnosisPrompt import diagnosis_examples
from source.PydanticModels.Drugs import MedicationExtraction
from source.PydanticModels.Lifestyle import LifestyleExtraction
from source.Prompts.Lifestyle import lifestyle_examples
from source.PydanticModels.SideEffects import SideEffectExtraction
from source.PydanticModels.Symptoms import SymptomExtraction


def getallergy():
    return allergy_examples, AllergyExtraction

def getdiagnosis():
    return diagnosis_examples, DiagnosisExtraction

def getmedications():
    return drug_examples, MedicationExtraction

def getlifestyle():
    return lifestyle_examples, LifestyleExtraction

def getsideeffects():
    return side_effect_examples,SideEffectExtraction

def getsymptoms():
    return symptoms_examples, SymptomExtraction