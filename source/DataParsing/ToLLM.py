from langchain_ollama import OllamaLLM
from source.DataParsing.promptMaker import prompt_creator

class LLMInference:
    def __init__(self):
        self.model = OllamaLLM(model = "gemma3:4b")
        self.prompt = None
        self.parser = None
        self.chain = None

    def create_chain(self, py_object):

        self.prompt, self.parser = prompt_creator(pydantic_object=py_object)
        self.chain = self.prompt | self.model | self.parser

        return None

    def invoke(self, text, sys_prompt, examples):

        print("###" * 10)
        print("THE FINAL PROMPT GOING IN............ ")
        print(self.prompt.format(sys_prompt = sys_prompt, examples = examples, context = text))
        print("###" * 10)

        print("###" * 10)
        print("LLM INFERENCE INCOMING............ ")
        print("###" * 10)

        #print(self.prompt.format(sys_prompt = sys_prompt, context = text, examples = examples))
        #print("\n\n\n\n\n")

        results = self.chain.invoke(input = {"sys_prompt" : sys_prompt,
                                             "examples" : examples,
                                             "context": text,
                                             })

        print(results)
        print(type(results))

        return results