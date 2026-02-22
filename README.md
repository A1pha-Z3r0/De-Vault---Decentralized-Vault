# De Vault - Decentralized Vault for your medical Data

**This repo consists of my team's attempt to tackle a hackathon's problem statement:** Patient-reported data (symptoms, side effects, quality of life) 
is frequently collected but underutilized. This data is often unstructured and difficult to analyze, limiting its value for improving care or 
research outcomes.

You could ask did we win? Nahh, even better, we forgot to register :(

## Solution:

Patient-reported data is underutilized largely because it's unstructured, and the best way to structure data is to control how it's collected in the first place. 
So we start by audio-recording a patient's clinical visit with their doctor. We then transcribe it and pass it through a HIPAA module, which de-identifies the transcript by stripping out PHI 
(Protected Health Information) while also retaining the original version. From there, we structure the data into a JSON format that transforms these unstructured transcripts into discrete events—things like MedicationEvent,
SideEffectsEvent, and so on. Essentially, events that both the patient and healthcare providers would actually care about.

Here's the key: we don't store any of this data up to this point. Instead, we stream these data points directly to the patient and store them only on their chosen device. They could opt to store it with us if they want,
but the whole purpose of keeping it on their device is about putting patients first—their privacy first.

How many of us actually know where our last clinical visit data is stored? Or better yet, did anyone even bother to ask?
We want to change that by bringing it to your phone in an easy-to-read, digestible format—not raw transcripts or overwhelming forms, but simple ways you can manage your health data. Only you choose where to store it and who to share it with. 
**De Vault, the decentralized vault**, does exactly this for you.
Now, the proposed uses of this data:

* **Rare disease identification:** We could have a crawler that periodically screens for rare diseases and alerts the healthcare professional or the patient to take a secondary look.
* **Clinical studies:** Since data isn't stored centrally, each patient in the network receives a notification about a study—its purpose and which specific data points researchers want access to.
* **Digital twins:** On a crazier note, as science moves toward digital twins, this data format could be incredibly valuable—linking a patient's own lifestyle to their medications and other medical "agents" in a much deeper way.
* **Adverse drug reaction monitoring:** We could get firsthand inferences during Phase IV market monitoring, tracking adverse reactions to drugs in real time.


## Implementation:

**TL;DR**

This project turns patient–doctor conversations into structured, patient-owned health data.

Clinical visits are audio-recorded locally, transcribed using Whisper, anonymized with Presidio (POC), and converted into schema-validated JSON events (e.g., medications, symptoms, diagnoses, side effects, lifestyle factors). Event extraction is enforced using Pydantic schemas to reduce hallucination and ensure consistency.

All processing runs locally using Ollama-hosted LLMs. No data is stored by default—structured outputs are streamed directly to the patient’s device, putting privacy and control first.












