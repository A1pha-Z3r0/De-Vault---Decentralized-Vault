from chonkie import SentenceChunker

def chunker(text):
    # Basic initialization with default parameters
    sentence_splitter = SentenceChunker(
        tokenizer="character",  # Default tokenizer (or use "gpt2", etc.)
        chunk_size=2048,  # Maximum tokens per chunk
        chunk_overlap=0,  # Overlap between chunks
        min_sentences_per_chunk=1  # Minimum sentences in each chunk
    )

    chunks = sentence_splitter.chunk(text)

    return chunks



