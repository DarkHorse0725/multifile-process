from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import SeleniumURLLoader
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import requests
import langchain
import tiktoken
from langchain.embeddings import OpenAIEmbeddings


# Multiple PDFs
MAX_TOKENS = 500


def get_pdfs_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        text += get_pdf_text(pdf)
    return text


# Single PDF
def get_pdf_text(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def count_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding(OPENAI_EMBEDDING_ENCODING)
    tokens = encoding.encode(text)
    num_tokens = len(tokens)
    return num_tokens, tokens


def get_url_text(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()
    for script in soup(["script", "style"]):
        script.extract()

    cleaned_text_content = soup.get_text()
    return text


# def get_excels_text(excel_docs):
#     text = ""
#     for excel in excel_docs:
#         text += get_excel_text(excel)
#     return text


# # Single Excel
# def get_excel_text(excel):
#     text = ""
#     pdf_reader = PdfReader(pdf)
#     for page in pdf_reader.pages:
#         text += page.extract_text()
#     return text
