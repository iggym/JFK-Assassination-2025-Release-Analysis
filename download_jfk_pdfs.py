import requests
from bs4 import BeautifulSoup
import os

def download_pdfs(url, download_folder="jfk_pdfs"):
    """
    Extracts PDF URLs from a webpage and downloads the files.

    Args:
        url (str): The URL of the webpage.
        download_folder (str): The folder to save the PDFs to.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, "html.parser")

        pdf_links = []
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if href.endswith(".pdf"):
                full_url = requests.compat.urljoin(url, href)  # Ensure full URL
                pdf_links.append(full_url)

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        for pdf_url in pdf_links:
            try:
                pdf_response = requests.get(pdf_url, stream=True)
                pdf_response.raise_for_status()

                filename = os.path.join(download_folder, pdf_url.split("/")[-1])

                with open(filename, "wb") as f:
                    for chunk in pdf_response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                print(f"Downloaded: {filename}")

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {pdf_url}: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    target_url = "https://www.archives.gov/research/jfk/release-2025"
    download_pdfs(target_url)