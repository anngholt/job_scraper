import requests
from bs4 import BeautifulSoup
import json

def extract_job_info(url):
    """Fetch job listing details from the given URL"""
    
    # Fetch the web page
    headers = {"User-Agent": "Mozilla/5.0"}  
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Try to find JSON data within a script tag
    job_info = {}
    script_tag = soup.find("script", {"type": "application/json"})  
    
    if script_tag:
        try:
            json_data = json.loads(script_tag.string.strip())  # Parse JSON
            config = json_data.get("config", {})
            targeting = config.get("adServer", {}).get("gam", {}).get("targeting", [])
            
            # Convert targeting list into a dictionary
            targeting_dict = {item["key"]: item["value"] for item in targeting if "key" in item}
            
            # Extract relevant job details
            job_info = {
                "Job Title": targeting_dict.get("job_title", ["Unknown"])[0],
                "Company": targeting_dict.get("company_name", ["Unknown"])[0],
                "Industry": targeting_dict.get("industry", ["Unknown"]),
                "Sector": targeting_dict.get("job_sector", ["Unknown"])[0],
                "Occupation": targeting_dict.get("occupation", ["Unknown"]),
                "Location": targeting_dict.get("municipality", ["Unknown"])[0],
                "Working Language": targeting_dict.get("working_language", ["Unknown"])[0],
                "Job Duration": targeting_dict.get("job_duration", ["Unknown"])[0],
                "Job Positions": targeting_dict.get("job_positions", ["Unknown"])[0],
            }
        except json.JSONDecodeError:
            print("Failed to parse JSON data.")
    
    # Try extracting job title and description from HTML (fallback method)
    if not job_info.get("Job Title"):
        title_tag = soup.find("h1")
        job_info["Job Title"] = title_tag.text.strip() if title_tag else "Unknown"

    description_tag = soup.find("div", class_="job-description")  # Adjust based on the site
    job_info["Description"] = description_tag.text.strip() if description_tag else "No description available"
    
    # Print extracted job details
    print("\nExtracted Job Details:")
    for key, value in job_info.items():
        print(f"{key}: {value}")

# Run the script
if __name__ == "__main__":
    job_url = input("Enter the job listing URL: ")
    extract_job_info(job_url)
