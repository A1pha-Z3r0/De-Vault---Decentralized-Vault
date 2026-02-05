from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from source.PydanticModels.Drugs import MedicationExtraction

template = """You are an AI- agent tasked in extracting structured clinical data from a conversation.

Think of this task as filling out a form:
- Each medication mentioned corresponds to one form entry.
- If no medications are mentioned, the form remains empty.

Important constraints:
- Only use information that appears in the transcript.
- Every field must be supported by the transcript or set to null.
- Do not invent, normalize, or correct medical information.
- The final output must match the schema exactly.

Structure rules:
- The output is ONE JSON object.
- That object contains an "events" field.
- "events" is a list of medication event objects.

Example 1: Single Clear medication

Transcript:
Doctor: Let’s start you on metformin 500 mg once daily.
Patient: Okay.

Output JSON object:

{{
  "events": [
    {{
      "drug_name": "metformin",
      "action": "started",
      "dose": 500,
      "frequency": "once daily",
      "route": null,
      "effective_date": null,
      "reason": null,
      "entity_ref": "explicit",
      "speaker": "doctor",
      "confidence": 9,
      "evidence": "Let’s start you on metformin 500 mg once daily.",
      "doctor_remarks": null
    }}
  ]
}}

Example 2: Multiple Medications

Transcript:
Patient: I’ve been taking ibuprofen as needed.
Doctor: Continue that, but stop aspirin.

Output JSON object:

{{
  "events": [
    {{
      "drug_name": "ibuprofen",
      "action": "continued",
      "dose": null,
      "frequency": "as needed",
      "route": null,
      "effective_date": null,
      "reason": null,
      "entity_ref": "explicit",
      "speaker": "patient",
      "confidence": 8,
      "evidence": "I’ve been taking ibuprofen as needed.",
      "doctor_remarks": null
    }},
    {{
      "drug_name": "aspirin",
      "action": "stopped",
      "dose": null,
      "frequency": null,
      "route": null,
      "effective_date": null,
      "reason": null,
      "entity_ref": "explicit",
      "speaker": "doctor",
      "confidence": 9,
      "evidence": "Stop aspirin.",
      "doctor_remarks": null
    }}
  ]
}}

Example 3: No Medications

Transcript:
Patient: I’ve been feeling tired lately.
Doctor: That’s common with stress.

Output JSON object:

{{
  "events": []
}}


Transcript:
{context}

Schema to follow:
{format_instructions}

Output the completed JSON object and nothing else.
"""


def prompt_creator():
    parser = PydanticOutputParser(pydantic_object = MedicationExtraction)

    prompt_template = PromptTemplate(
        input_variables=["context"],
        template=template,
        partial_variables = {"format_instructions" : parser.get_format_instructions()}
    )

    return prompt_template, parser



