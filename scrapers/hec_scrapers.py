import requests
from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_hec():
    url = "https://www.hec.gov.pk/english/scholarshipsgrants/Pages/default.aspx"
    response = requests.get(url, verify=False)  # Skip SSL ch
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select(".linkGroup li a")[:5]

    results = []
    for link in links:
        results.append({
            "title": link.text.strip(),
            "deadline": "N/A",
            "amount": "N/A",
            "country": "Pakistan",
            "link": "https://www.hec.gov.pk" + link.get("href"),
            "source": "HEC"
        })
    return results

