import threading
import requests
from bs4 import BeautifulSoup

urls =['https://langchain-ai.github.io/langgraph/tutorials/introduction/',
'https://docs.smith.langchain.com/',
'https://python.langchain.com/docs/introduction/']

def fetch_content(urls):
    response  = requests.get(urls)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify()) # encode('utf-8')
    print(f"Fetched {len(soup.text)} characters from {urls}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished execution.")