from langchain_ollama import OllamaLLM
from source.DataParsing.prompt import prompt_creator


def llm_inference(text):
    prompt, parser = prompt_creator()

    #f_prompt = prompt.format(context = text)

    model = OllamaLLM(model="mistral:latest")

    chain = prompt | model | parser

    print(prompt.format(context=text))
    print("\n\n\n\n\n")

    result = chain.invoke(input = {"context": text})

    print(result)
    print(type(result))

    return None