import json
from concurrent.futures import ThreadPoolExecutor
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
from crawl4ai import WebCrawler
import pandas as pd


def process_link(link):
    crawler = WebCrawler()
    # Warm up the crawler (load necessary models)
    crawler.warmup()

    try:
        result = crawler.run(url=link)
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system",
                 "Extract pricing information along with the catalogue which has comparison in a structured dictionary format along with comparisons if there are any."),
                ("user", "{context}"),
                ("ai", "only return in python dictionary format, don't return a markdown.")
            ]
        )
        chain = prompt | ChatOpenAI(model_name="gpt-4o")
        output = chain.invoke({"context": result.markdown})
        name = link.split("//")[1].split("/")[0].strip(".com")
        with open(f"/Users/vanshpundir/roundcircle/pricing_extractor/json/{name}.json", "w") as f:
            f.write(str(output.content))
    except Exception as e:
        print(f"{e} occurred for link {link}")


# Load data and filter links
df = pd.read_csv("/Users/vanshpundir/roundcircle/pricing_extractor/RFQ - Tools-Questionnaire_RFQ.csv")
list_of_links = list(df["Resource "].dropna())

df = pd.read_csv("RFQ - Tools-Questionnaire_RFQ.csv")
df2 = df["Resource "].dropna()
price_list = list(df2)
list1 = []
for i in price_list:
    list11 = i.split("\n")
    for k in list11:
        if "https://" in k:
            list1.append(k)

links = [i for i in list1]

# Use ThreadPoolExecutor to process links in parallel
with ThreadPoolExecutor() as executor:
    executor.map(process_link, links)
