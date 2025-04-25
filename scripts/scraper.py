import requests
from bs4 import BeautifulSoup
import json
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}
BASE_URL = "https://www.finn.no"

# Set your fixed search URL here
SEARCH_URL = "https://www.finn.no/job/fulltime/search.html?q=python"

def get_job_links(search_url):
    """Extract job ad links from a FINN.no job search results page"""
    response = requests.get(search_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/job/fulltime/ad.html?" in href:
            full_url = href if href.startswith("http") else BASE_URL + href
            if full_url not in links:
                links.append(full_url)
    
    return links


def extract_job_info(url):
    """Fetch job listing details from a job ad URL"""
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    
    job_info = {"URL": url}
    script_tag = soup.find("script", {"type": "application/json"})

    if script_tag:
        try:
            json_data = json.loads(script_tag.string.strip())
            targeting = json_data.get("config", {}).get("adServer", {}).get("gam", {}).get("targeting", [])
            targeting_dict = {item["key"]: item["value"] for item in targeting if "key" in item}

            job_info.update({
                "Job Title": targeting_dict.get("job_title", ["Unknown"])[0],
                "Company": targeting_dict.get("company_name", ["Unknown"])[0],
                "Industry": targeting_dict.get("industry", ["Unknown"]),
                "Sector": targeting_dict.get("job_sector", ["Unknown"])[0],
                "Occupation": targeting_dict.get("occupation", ["Unknown"]),
                "Location": targeting_dict.get("municipality", ["Unknown"])[0],
                "Working Language": targeting_dict.get("working_language", ["Unknown"])[0],
                "Job Duration": targeting_dict.get("job_duration", ["Unknown"])[0],
                "Job Positions": targeting_dict.get("job_positions", ["Unknown"])[0],
            })
        except json.JSONDecodeError:
            pass

    # Fallback: Extract title and description from HTML
    if not job_info.get("Job Title"):
        title_tag = soup.find("h1", class_="t3")
        job_info["Job Title"] = title_tag.text.strip() if title_tag else "Unknown"

    description_tag = soup.find("div", class_="import-decoration") or \
                      soup.find("section", {"data-testid": "ad-description"})

    job_info["Description"] = description_tag.get_text(separator="\n", strip=True) if description_tag else "No description available"

    return job_info


def read_last_scraped_url(filename="last_scraped.txt"):
    """Read the last scraped job ad URL from a file"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def write_last_scraped_url(url, filename="last_scraped.txt"):
    """Write the last scraped job ad URL to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(url)


def scrape_jobs_from_search_page(search_url, output_file="job_data.jsonl"):
    last_scraped_url = read_last_scraped_url()
    job_links = get_job_links(search_url)
    print(f"Found {len(job_links)} job links.")

    with open(output_file, "a", encoding="utf-8") as f:
        for i, link in enumerate(job_links, 1):
            print(f"[{i}/{len(job_links)}] Scraping: {link}")
            
            # Stop scraping when we reach the last scraped URL
            if last_scraped_url and link == last_scraped_url:
                print("Reached the last scraped job, stopping.")
                return
            
            job_info = extract_job_info(link)
            if job_info:
                f.write(json.dumps(job_info, ensure_ascii=False) + "\n")
                write_last_scraped_url(link)  # Update the last scraped URL
            
            time.sleep(1)  # Be polite: avoid overloading the server

    print(f"Done! Data saved to {output_file}")


if __name__ == "__main__":
    scrape_jobs_from_search_page(SEARCH_URL)
