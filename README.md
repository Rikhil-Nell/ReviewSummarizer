# Amazon Review Scraper

This project is designed to scrape and analyze product reviews from Amazon using Python. It integrates web scraping techniques with Natural Language Processing (NLP) for sentiment analysis and text summarization, all wrapped in a Flask-based web application for a user-friendly experience.

## Technologies Used

### Web Scraping

* **Selenium:** An automation tool for controlling web browsers. It facilitates navigation through Amazon product pages and review sections, especially for dynamic content rendered via JavaScript.
* **BeautifulSoup:** A library for parsing HTML and XML documents. Used to extract and process review data from the scraped HTML content retrieved by Selenium.

### Natural Language Processing (NLP)

* **Hugging Face Transformers:** A library for utilizing state-of-the-art NLP models. It's employed for sentiment analysis and text generation. Specifically, models like BERT handle sentiment analysis, while GPT-like models generate summaries of reviews.
* **NLTK (Natural Language Toolkit):** A library for working with text data. Provides additional text processing functionalities.

### Web Development

* **Flask:** A lightweight web framework for Python. Creates a RESTful API, allowing users to trigger scraping and access results through HTTP requests. 

### Browser Automation

* **Google Chrome:** The web browser used for scraping. Chosen for its compatibility with Selenium and ChromeDriver.
* **ChromeDriver:** A separate executable that allows Selenium to control Chrome. It acts as a bridge between the Selenium WebDriver and the Chrome browser.

## Features

* Scrapes both positive and negative reviews from Amazon product pages.
* Extracts review text and posting dates.
* Performs sentiment analysis, classifying reviews as positive, negative, or neutral.
* Summarizes top reviews using advanced text generation models.
* Provides a Flask-based API to initiate scraping and retrieve review data.
* Supports headless mode for running the browser without a graphical user interface (GUI), ideal for automated environments.

## Prerequisites

* Python 3.7 or higher
* [Google Chrome](https://www.google.com/chrome/) (or another supported browser)
* ChromeDriver compatible with your Chrome version
* **Transformers** library by Hugging Face for NLP tasks
* **NLTK** library for additional text processing

## Installation

1. **Clone the Repository:**

```sh
git clone [https://github.com/yourusername/amazon-review-scraper.git](https://github.com/yourusername/amazon-review-scraper.git)
cd amazon-review-scraper
```

2. **Create and Activate a Virtual Environment:**

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3.
