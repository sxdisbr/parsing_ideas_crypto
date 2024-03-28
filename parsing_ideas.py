from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import time
import os

# Path to your WebDriver executable
driver_path = os.getenv('GECKODRIVER_PATH')

# Initialize the WebDriver
service = Service(webdriver_path)
driver = webdriver.Firefox(service=service)

driver.get('https://www.tradingview.com/ideas/')

time.sleep(15)  # Adjust this as needed for the page to load

# Find all relevant tags
description_tags = driver.find_elements(By.CSS_SELECTOR, 'p')
headlines_tags = driver.find_elements(By.CSS_SELECTOR, 'h2')

# Initialize list to store structured data
articles = []

for headline, description in zip(headlines_tags, description_tags):
    articles.append({
        'title': headline.text,
        'summary': description.text
    })

# Close the WebDriver
driver.quit()

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Add sentiment scores to each article
for article in articles:
    scores = sid.polarity_scores(article['summary'])
    article['compound'] = scores['compound']  # Focus on compound for simplicity

# Convert to DataFrame
df = pd.DataFrame(articles)

# Interpret compound score for visualization
df['sentiment_type'] = pd.cut(df['compound'], bins=[-1, -0.05, 0.05, 1], labels=['Negative', 'Neutral', 'Positive'])

# Plotting
sns.countplot(x='sentiment_type', data=df, order=['Negative', 'Neutral', 'Positive'])
plt.title('Sentiment Distribution of TradingView Ideas')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
