import spacy
import re

from source.SpeechToText import transcribe_speech
from test_data import test

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

class Nlp():
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.txt = []

    def read_txt(self):
        txt = transcribe_speech()[0] #tuple shape(2)
        for sentences in txt:
            self.txt.append(sentences.text)

        string = " ".join(self.txt)

        return string


    def anonymize(self, st):
        # Set up the engine, loads the NLP module (spaCy model by default)
        # and other PII recognizers
        analyzer = AnalyzerEngine()

        # Call analyzer to get results
        results = analyzer.analyze(text=st,
                                   #entities=["PHONE_NUMBER"],
                                   language='en')
        print(results)

        # Analyzer results are passed to the AnonymizerEngine for anonymization
        anonymizer = AnonymizerEngine()

        anonymized_text = anonymizer.anonymize(text=st, analyzer_results=results)

        #print(anonymized_text)

        return anonymized_text

    def remove_address(self):

        pass

    def remove_phonenumber(self, st):
        PHONE_REGEX = r"\b(\+\d{1,3}[\s\-]?)?(\(?\d{2,4}\)?[\s\-]?){2,4}\d{2,4}\b"

        for match in re.finditer(PHONE_REGEX, st):
            print(match.group(), match.start(), match.end())

        return None

    def remove_dates(self):

        pass

    def remove_ages(self):

        pass


    def remove_names(self, st):
        #print(f"Before NLP: {string}")
        doc = self.nlp(st)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                print(ent.text, ent.label_)
                print(f"Position: {ent.start_char, ent.end_char}")


def hipaa_pipeline():
    nlp = Nlp()
    list_string = nlp.read_txt()

    list_string = test

    #print(f"###################"
    #      f"BEFORE:"
    #      f"{list_string}"
    #      f"###################")

    text = nlp.anonymize(list_string)
    #nlp.remove_phonenumber(list_string)
    #nlp.remove_names(list_string)

    return text


