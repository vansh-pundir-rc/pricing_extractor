# Load html
# OpenAI
#  LLMChain
# context
# return dictionar

from langchain.document_loaders import UnstructuredHTMLLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


load = UnstructuredHTMLLoader("test.html")
data = load.load()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Extract pricing information along with the catalogue which has comparison in a structure dictionary format"),
        ("user", "{context}")
    ]
)
chain = prompt | ChatOpenAI(model_name = "gpt-4o")

chain.invoke({"context": data})

