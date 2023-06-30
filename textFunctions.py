from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import SeleniumURLLoader
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import requests
import langchain


# Multiple PDFs


def get_pdfs_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        text += get_pdf_text(pdf)
    return text


# Single PDF
def get_pdf_text(pdf):
    text = ""
    print('pdf = ', pdf.type)
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


def get_url_text(url):
    test_urls = "https://www.wsj.com/articles/ukraine-says-frontlines-around-embattled-city-of-bakhmut-are-stabilizing-ed7dc7d"
    # loader = UnstructuredURLLoader(urls=urls)
    # data = loader.load()
    # print(data)
    response = requests.get(test_urls)
    content = response.text

    # Step 2: Extract the relevant text from the webpage
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()

    # Step 3: Use the langchain library to generate the summary
    # summary = langchain.summarize(text)

    # Step 4: Print or use the generated summary
    print('here is summary = ', text)
    return '13'
