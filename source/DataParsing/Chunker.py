from chonkie import SentenceChunker

def parser(text):
    # Basic initialization with default parameters
    chunker = SentenceChunker(
        tokenizer="character",  # Default tokenizer (or use "gpt2", etc.)
        chunk_size=2048,  # Maximum tokens per chunk
        chunk_overlap=0,  # Overlap between chunks
        min_sentences_per_chunk=1  # Minimum sentences in each chunk
    )
    for index,chunk in enumerate(chunker(text)):
        print(f"{index}: \n\n")
        print(chunk.text)
        print(chunk.token_count)

    return None



