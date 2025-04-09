# job_scraper
# 🏢 Job Scraper

A Python-based web scraper that extracts job details from job listing websites. For now only test version is working correctly. This tool fetches job titles, descriptions, companies, locations, and other relevant information from a given job URL. In the future I want this programm to scrap job listing websites and write everything to a database. 

Recentry added write to file feature and pyhton script to read and analyse data from that file. Next step saving all it in a database with link to job description.

---

## 📌 Features
- **Extracts Job Details** – Job title, company, location, sector, industry, and more  
- **Supports JSON Parsing** – Fetches structured job data if available  
- **Handles Missing Data** – Falls back to HTML scraping if JSON is unavailable  
- **User-Friendly** – Just provide a job listing URL and get detailed results  
- **Expandable** – Easily add support for new job websites  

---

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/job_scraper.git
cd job_scraper
```

### **2️⃣ Set Up a Virtual Environment (Optional)**
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Required Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🚀 Usage

### **Run the Script**
```sh
python test_scraper.py - test version working correctly
python scripts/scraper.py - version under development, not really useufl right now
```

### **Provide a Job Listing URL**
When prompted, enter the URL of a job posting:
```sh
Enter the job listing URL: https://example.com/job-listing
```

### **Example Output**
```
Extracted Job Details:
Job Title: Software Engineer
Company: TechCorp Inc.
Industry: IT & Software
Sector: Development
Occupation: Software Development
Location: Oslo, Norway
Working Language: English
Job Duration: Permanent
Job Positions: 1
Description: Looking for a skilled software engineer with experience in Python and web scraping.
```

---

## 📝 Configuration

### **Modify CSS Selectors**
If the website structure changes, update `job_scraper.py` and adjust:
- `soup.find(...)` for extracting titles, descriptions, etc.
- JSON extraction logic (if needed)

---

## 🐄 Project Structure
```
job_scraper/
|-- test_scraper.py             # working protopype, only scraps one listing at a time when given url
│-- scripts/
│   ├── scraper.py              # Main scraping script
│-- venv/                        # Virtual environment (ignored in .gitignore)
│-- data/                        # Folder for storing scraped job data (if needed)
│-- requirements.txt              # Python dependencies
│-- README.md                     # Project documentation
│-- .gitignore                     # Ignore virtual env & data files
```

---

## ❌ Adding a `.gitignore`
To avoid committing unnecessary files, use the following `.gitignore`:
```
# Ignore virtual environments
venv/
*.pyc
__pycache__/

# Ignore data and text files
data/
*.csv
*.json
*.txt
```

Add `.gitignore` to Git:
```sh
git add .gitignore
git commit -m "Added .gitignore"
```

---

## 📌 Future Improvements
- 🚀 Save scraped job data to a **CSV or JSON file**  
- 🚀 Add support for **multiple job boards**  
- 🚀 Implement a **GUI** for easy interaction  
- 🚀 Use **AI-based job description analysis**  


## 💡 Contributing
Feel free to open issues or submit pull requests to improve this project!


