import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
nltk.data.path.append('/Users/anna/projects_for_cv/job_scraper/venv/nltk_data')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Download necessary NLTK resources
#nltk.download("punkt")
#nltk.download("stopwords")
#nltk.download("wordnet")

# Sample list of skills (expand this list based on your needs)
skills = ["python", "sql", "machine learning", "data analysis", "excel", "pandas", "tensorflow", "deep learning", "numpy", "javascript"]

# Initialize lemmatizer and stop words
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Function to scrape job details from a job page
def get_job_description(job_url):
    job_page = requests.get(job_url, headers={"User-Agent": "Mozilla/5.0"})
    if job_page.status_code != 200:
        return "Description not found"

    job_soup = BeautifulSoup(job_page.text, "html.parser")
    description_tag = job_soup.find("div", class_="ads__unit__content__text")
    if description_tag:
        return description_tag.text.strip()
    return "Description not found"

# Function to extract skills from job descriptions using NLP
def extract_skills(description):
    # Tokenize the description
    words = word_tokenize(description.lower())  # convert to lowercase for uniformity
    
    # Lemmatize and remove stop words
    filtered_words = [
        lemmatizer.lemmatize(word) for word in words if word not in stop_words and word.isalpha()
    ]
    
    # Count skill occurrences
    found_skills = [word for word in filtered_words if word in skills]
    return found_skills

# URL of FINN.no job search page
BASE_URL = "https://www.finn.no/job/fulltime/search.html?q=python"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Fetch the main page content
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
    

    # Fetch job description from job URL
    description = get_job_description(job_url)

    # Optional: You can add company and location if available
    company = "Unknown"
    location = "Unknown"

    job_list.append({"Title": title, "Company": company, "Location": location, "URL": job_url, "Description": description})

# Now, process the job descriptions to extract skills
job_list_with_skills = []

for job in job_list:
    title = job["Title"]
    description = job["Description"]
    
    # Extract skills from job description
    found_skills = extract_skills(description)
    
    job_list_with_skills.append({"Title": title, "Skills": found_skills})

# Convert to DataFrame
df_with_skills = pd.DataFrame(job_list_with_skills)

# Save skills data to CSV
df_with_skills.to_csv("../data/finn_jobs_with_skills.csv", index=False)
print(f"✅ Extracted skills from job descriptions and saved to finn_jobs_with_skills.csv")
