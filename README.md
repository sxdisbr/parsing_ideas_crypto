# Cryptocurrency Sentiment Analysis

## Project Overview
This project aims to provide insights into the current sentiment surrounding various cryptocurrencies by analyzing headlines and summaries from TradingView's ideas page. Utilizing Selenium for web scraping and the NLTK library for sentiment analysis, this tool categorizes sentiment into "Positive", "Neutral", or "Negative" based on the content of each article.

## Features
- **Web Scraping:** Automated collection of headlines and summaries from TradingView using Selenium.
- **Sentiment Analysis:** Evaluation of the sentiment of each article using NLTK's VADER SentimentIntensityAnalyzer.
- **Data Visualization:** Visualization of sentiment distribution across scraped articles using seaborn and matplotlib.

## Installation
To set up this project locally, follow these steps:
1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required Python packages: `pip install -r requirements.txt`
4. Update the `webdriver_path` in the script to point to your WebDriver executable.

## Usage
To run the sentiment analysis, execute the script from the command line:
```bash
python sentiment_analysis_crypto.py
```

## Disclaimer

### Risk Involvement in Cryptocurrency
This tool provides sentiment analysis based on publicly available data and should not be construed as financial advice. The world of cryptocurrency trading is highly volatile and speculative, and it involves significant risks. It is possible to lose all of your investment. As with any financial decision, you should perform your due diligence and consider seeking advice from a financial professional before making any investment.

The creator of this tool bear no responsibility for any losses incurred as a result of using this tool. Users should use the information provided by the tool at their own risk.

## Contributing
Contributions to this project are welcome. Please open an issue or submit a pull request with your suggested changes.

## License
This project is licensed under the MIT License.