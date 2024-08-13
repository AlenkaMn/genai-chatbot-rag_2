import os
import shutil

from langchain_community.document_loaders import BSHTMLLoader, CSVLoader, JSONLoader, TextLoader
from langchain_community.document_loaders.word_document import UnstructuredWordDocumentLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders.powerpoint import UnstructuredPowerPointLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores import Chroma, FAISS
from langchain_core.documents import Document

from embedding import get_embedding_function
from splitters import text_splitters


CHROMA_PATH = "chroma"
DATA_PATH = "data"


def main():
    clear_database()
    documents = load_documents()
    chunks = split_documents(documents)
    #print(chunks)
    add_to_chroma(chunks)
    # add_to_faiss(chunks)


def load_documents():
    documents = []
    for file in os.listdir(DATA_PATH):
        extension = file.split('.')[-1]
        if extension == 'txt':
            documents += TextLoader(os.path.join(DATA_PATH, file)).load()
        if extension == 'csv':
            documents += CSVLoader(os.path.join(DATA_PATH, file)).load()
        if extension == 'html':
            documents += BSHTMLLoader(os.path.join(DATA_PATH, file), open_encoding='utf-8').load()
        if extension == 'json':
            continue
            documents += JSONLoader(os.path.join(DATA_PATH, file), jq_schema='.quiz').load()
        if extension == 'pdf':
            documents += PyPDFLoader(os.path.join(DATA_PATH, file)).load()
        if extension == 'xlsx':
            documents += UnstructuredExcelLoader(os.path.join(DATA_PATH, file)).load()
        if extension == 'docx':
            documents += UnstructuredWordDocumentLoader(os.path.join(DATA_PATH, file)).load()
        if extension == 'pptx':
            documents += UnstructuredPowerPointLoader(os.path.join(DATA_PATH, file)).load()

    return documents


def split_documents(documents: list[Document]):
    text_splitter = text_splitters[0]
    #print(text_splitter.split_documents(documents))
    return text_splitter.split_documents(documents)


def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    chunks_with_ids = calculate_chunk_ids(chunks)

    new_chunk_ids = [chunk.metadata["id"] for chunk in chunks_with_ids]
    db.add_documents(chunks_with_ids, ids=new_chunk_ids)
    db.persist()
    print("✅ Chroma was updated")


def add_to_faiss(chunks: list[Document]):
    chunks_with_ids = calculate_chunk_ids(chunks)
    db2 = FAISS.from_documents(chunks_with_ids, get_embedding_function())
    db2.save_local("faiss_index")


def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}"
        if page:
            current_page_id += f":{page}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        chunk.metadata["id"] = chunk_id

    return chunks


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)


if __name__ == "__main__":
    main()
