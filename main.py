from source.SpeechToText.RecAudio import RecordAudio
from source.HIPAA.HipaaPipeline import hipaa_pipeline
from source.DataParsing.ToLLM import LLMInference
from source.Prompts.SystemPrompt import sys_prompt_router, sys_prompt_extract, examples_router
from source.DataParsing.Chunker import chunker
from source.DataParsing.dispatcher import *
from source.PydanticModels.Router import RouterExtraction

def main():
    RA = RecordAudio()
    #RA.record_audio()

    text = hipaa_pipeline()

    chunks = chunker(text.text)

    llm = LLMInference()

    dispatcher = {
        "Allergy" : getallergy,
        "Diagnosis" : getdiagnosis,
        "Medications" : getmedications,
        "Lifestyle" : getlifestyle,
        "SideEffects" : getsideeffects,
        "Symptoms" : getsymptoms
    }

    for index,chunk in enumerate(chunks):
        print("####" * 10)
        print(index)
        print("###" * 10)
        print(chunk.text)

        # TODO: Batching of chunks
        llm.create_chain(RouterExtraction)
        routes = llm.invoke(text = chunk.text, sys_prompt= sys_prompt_router, examples = examples_router)

        for domain in routes.domain:

            print("###" * 10)
            print("GOING THROUGH DOMAINS... ")
            print(domain)
            print("###" * 10)

            if domain is None:
                continue

            dispatch = dispatcher.get(domain)

            domain_prompt, domain_extraction = dispatch()

            llm.create_chain(domain_extraction)

            results = llm.invoke(text=chunk.text, sys_prompt=sys_prompt_extract, examples=domain_prompt)

            print(type(results))


    return



if __name__ == '__main__':
    main()