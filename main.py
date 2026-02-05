from source.SpeechToText.RecAudio import RecordAudio
from source.HIPAA.HipaaPipeline import hipaa_pipeline
from source.DataParsing.ToLLM import llm_inference

def main():
    RA = RecordAudio()
    #RA.record_audio()

    text = hipaa_pipeline()

    #parser(text.text)

    print(text.text)

    llm_inference(text.text)

    return



if __name__ == '__main__':
    main()