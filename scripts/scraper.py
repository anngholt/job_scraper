import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of FINN.no job search page
BASE_URL = "https://www.finn.no/job/fulltime/search.html?q=python"
#BASE_URL = "https://www.finn.no/job/fulltime/search.html"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Fetch page content
response = requests.get(BASE_URL, headers=HEADERS)
if response.status_code != 200:
    print("Failed to retrieve data")
    exit()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# List to store job data
job_list = []

# Find all job listings
for job in soup.find_all("a", class_="sf-search-ad-link s-text! hover:no-underline"):
    title = job.text.strip()
    job_url = job["href"]

    # Optionally, if you want to scrape additional data (company, location)
    # You can inspect the HTML and update the classes for company and location
    company = "Unknown"  # You can add this if it's available in the HTML
    location = "Unknown"  # You can add this if it's available in the HTML

    job_list.append({"Title": title, "Company": company, "Location": location, "URL": job_url})

# Convert to DataFrame
df = pd.DataFrame(job_list)

# Save to CSV
df.to_csv("../data/finn_jobs.csv", index=False)
print(f"✅ Scraped {len(df)} jobs and saved to finn_jobs.csv")
