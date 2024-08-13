from langchain_text_splitters import RecursiveCharacterTextSplitter

'''
      - chunk_size=1000, chunk_overlap=250
      - chunk_size=500, chunk_overlap=50
      - chunk_size=300, chunk_overlap=0
'''
text_splitters = [
    RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    ),
    RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=250,
        length_function=len,
        is_separator_regex=False,
    ),
    RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    ),
    RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=0,
        length_function=len,
        is_separator_regex=False,
    )
]

