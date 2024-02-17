import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time
start_time = time.time_ns() / 1_000_000
def download_page(url):
    response = requests.get(url)
    return response.text


def save_pdf(omonimlar, content):
    with open(omonimlar, 'wb') as file:
        file.write(content)


def download_pdf(url):
    response = requests.get(url)
    return response.content

def save_pdf_file(pdf_url):
    pdf_content = download_pdf(pdf_url)
    omonimlar = pdf_url.split('/')[-1]
    save_pdf(omonimlar, pdf_content)


def main():
    base_url = 'https://tilshunos.com/omonims/'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [base_url + link.get('href') for link in soup.find_all('a') if link.get('href').endswith('.pdf')]

    with ThreadPoolExecutor() as executor:
        executor.map(save_pdf_file, links)

end_time = time.time_ns() / 1_000_000

print(end_time - start_time)

if __name__ == '__main__':
    main()




