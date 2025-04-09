import re

def read_and_analyze_file(file_path):
    """Read the file, analyze its content and output results."""
    
    # Open and read the content of the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Analyze the entire content
    analyze_content(content)


def analyze_content(content):
    """Perform analysis on the entire content"""

    # Extended list of keywords for analysis
    keywords = [
        "AI", "Python", "Machine Learning", "Quantum", "Data", "Data Science", 
        "Data Analysis", "Data Engineering", "Big Data", "Statistical Analysis", 
        "Data Mining", "Data Modeling", "Predictive Analytics", "Data Wrangling", 
        "Data Visualization", "Exploratory Data Analysis", "Business Intelligence", 
        "Insights", "Trend Analysis", "Correlation", "Regression Analysis", 
        "Supervised Learning", "Unsupervised Learning", "Neural Networks", 
        "Deep Learning", "Reinforcement Learning", "Natural Language Processing", 
        "Feature Engineering", "Model Training", "AI Model", "Classification", 
        "Clustering", "Data Algorithms", "Statistical Inference", "ETL", 
        "Extract, Transform, Load", "Data Pipelines", "Data Architecture", 
        "Distributed Systems", "Data Warehousing", "Cloud Data", "SQL", "NoSQL", 
        "Apache Hadoop", "Apache Spark", "Kafka", "Data Lakes", "Batch Processing", 
        "Real-Time Data Processing", "AI Optimization", "Automation", "Robotics", 
        "Pattern Recognition", "AI Systems", "AI Models", "AI Integration", 
        "Cloud AI", "Scalable AI Systems", "Model Optimization", "Convolutional Neural Networks", 
        "Recurrent Neural Networks", "Transfer Learning", "Model Fine-Tuning", 
        "TensorFlow", "PyTorch", "Keras", "Excel", "Artificial Neural Networks", "SQL", "Bash", "Linux"
    ]
    
    # Convert content to lowercase for case-insensitive search
    content_lower = content.lower()

    # Initialize a dictionary to store keyword counts
    keyword_counts = {keyword.lower(): 0 for keyword in keywords}

    # Count keyword occurrences across the entire content
    for keyword in keywords:
        keyword_counts[keyword.lower()] = content_lower.count(keyword.lower())

    # Display the results of the keyword count
    print("\nKeyword Analysis Results:")
    for keyword, count in keyword_counts.items():
        if count > 0:  # Only display keywords that appear at least once
            print(f"'{keyword}': {count} occurrence(s)")

    # Additional analysis: word count in the entire document
    word_count = len(content.split())  # Use split() without arguments to handle multiple spaces and newlines
    print(f"\nTotal word count in the document: {word_count} words.")


# Run the script
if __name__ == "__main__":
    file_path = "job_details.txt"  # Path to the job details text file
    read_and_analyze_file(file_path)
