from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_daad():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # ✅ Use Service object for new Selenium versions
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.daad.de/en/study-and-research-in-germany/scholarships-database/")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    scholarships = []
    cards = soup.select('.scholarship-item__body')[:5]

    for item in cards:
        title_tag = item.find('h3')
        link_tag = item.find('a', href=True)

        if title_tag and link_tag:
            scholarships.append({
                "title": title_tag.text.strip(),
                "deadline": "Varies",
                "amount": "Varies",
                "country": "Germany",
                "link": "https://www.daad.de" + link_tag['href'],
                "source": "DAAD"
            })

    return scholarships

if __name__ == "__main__":
    results = scrape_daad()
    for r in results:
        print(r)

