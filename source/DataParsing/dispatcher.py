from source.PydanticModels.Allergy import AllergyExtraction
from source.Prompts.AllergyPrompt import allergy_examples

from source.Prompts.DrugPrompt import drug_examples
from source.PydanticModels.Drugs import MedicationExtraction


def getallergy():
    return allergy_examples, AllergyExtraction

def getdiagnosis():
    pass

def getmedications():
    return drug_examples, MedicationExtraction

def getlifestyle():
    pass

def getsideeffects():
    pass

def getsymptoms():
    pass