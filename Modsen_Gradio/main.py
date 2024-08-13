import gradio as gr
import os
import shutil
from langchain_community.vectorstores import Chroma, FAISS
from langchain_core.prompts import ChatPromptTemplate

from langchain_community.llms.ollama import Ollama

from embedding import get_embedding_function

CHROMA_PATH = "chroma"
DATA_PATH = "data"

PROMPT_TEMPLATE = """
Ответь на вопрос, основываясь исключительно на предоставленном контексте:

{context}

---

Ответь на данный вопрос основываясь на контексте: {question}

---

Ответ не должен включать вступительные слова, такие как "Исходя из контекста", так же ответ должен быть полным.
Если ответа по данному контексту нет, то ответ должен быть "Не обладаю такой информацией. Пожалуйста, уточните запрос!"
"""


def process_input(files, question):
    if files:
        for file in files:
            shutil.copy(file, os.path.join(DATA_PATH, file.split("\\")[-1]))

    os.system("prepare_data.py")
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    # db = FAISS.load_local("faiss_index", get_embedding_function())
    results = db.similarity_search_with_score(question, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=question)

    #model = Ollama(model="phi3")
    model = Ollama(model="llama3")
    # model = Ollama(model="openhermes")
    response_text = model.invoke(prompt)

    #sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}"

    return formatted_response


iface = gr.Interface(fn=process_input,
                     inputs=[
                         gr.Files(file_types=["pdf", "txt", "pptx", "csv", "html", "xlsx", "docx"],
                                  label="Load file to RAG"),
                         gr.Textbox(label="Question")],
                     outputs="text",
                     title="Document Query with Ollama",
                     description="Enter files and a question to query the documents.")
iface.launch()
