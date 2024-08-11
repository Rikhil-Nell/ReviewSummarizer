Amazon Review Scraper

This project is designed to scrape and analyze product reviews from Amazon using Python. It integrates web scraping techniques with Natural Language Processing (NLP) for sentiment analysis and text summarization, all wrapped in a Flask-based web application for a user-friendly experience.
Technologies Used
Web Scraping

    Selenium: An automation tool for controlling web browsers. It facilitates navigation through Amazon product pages and review sections, especially for dynamic content rendered via JavaScript.
    BeautifulSoup: A library for parsing HTML and XML documents. Used to extract and process review data from the scraped HTML content retrieved by Selenium.

Natural Language Processing (NLP)

    Hugging Face Transformers: A library for utilizing state-of-the-art NLP models. It's employed for sentiment analysis and text generation. Specifically, models like BERT handle sentiment analysis, while GPT-like models generate summaries of reviews.
    NLTK (Natural Language Toolkit): A library for working with text data. Provides additional text processing functionalities.

Web Development

    Flask: A lightweight web framework for Python. Creates a RESTful API, allowing users to trigger scraping and access results through HTTP requests.

Browser Automation

    Google Chrome: The web browser used for scraping. Chosen for its compatibility with Selenium and ChromeDriver.
    ChromeDriver: A separate executable that allows Selenium to control Chrome. It acts as a bridge between the Selenium WebDriver and the Chrome browser.

Features

    Scrapes both positive and negative reviews from Amazon product pages.
    Extracts review text and posting dates.
    Performs sentiment analysis, classifying reviews as positive, negative, or neutral.
    Summarizes top reviews using advanced text generation models.
    Provides a Flask-based API to initiate scraping and retrieve review data.
    Supports headless mode for running the browser without a graphical user interface (GUI), ideal for automated environments.

Prerequisites

    Python 3.7 or higher
    Google Chrome (or another supported browser)
    ChromeDriver compatible with your Chrome version
    Transformers library by Hugging Face for NLP tasks
    NLTK library for additional text processing

Installation

    Clone the Repository:

Bash

git clone https://github.com/yourusername/amazon-review-scraper.git
cd amazon-review-scraper

Use code with caution.

    Create and Activate a Virtual Environment:

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Use code with caution.

    Install Dependencies:   

Bash

pip install -r requirements.txt  


Use code with caution.

Make sure requirements.txt includes all necessary libraries:

selenium
beautifulsoup4
flask
transformers
nltk

    Download ChromeDriver:

    Download the appropriate ChromeDriver from the official site and add it to a directory in your system's PATH.

Usage

    Run the Flask Application:

Bash

python app.py

Use code with caution.

The Flask application will start and be accessible at http://localhost:5000.

    Access the API:

    Use a browser or API client to interact with the Flask application. For example:
    Bash

    http://localhost:5000/scrape-reviews?url=https://www.amazon.in/dp/B07Q8JJLFL

    Use code with caution.

    Replace the URL parameter with the Amazon product page URL you wish to scrape.

    View Results:

    The API will return a JSON object containing the extracted review texts, dates, sentiment analysis results, and summaries.

Project Structure

    app.py: The main Flask application script that serves the API.
    driver_init.py: Contains the SeleniumDriver class responsible for setting up and managing the Selenium WebDriver.
    review_scraper.py: Defines the ReviewScraper class for navigating Amazon pages and the parse_reviews function for extracting review data.
    nlp_utils.py: Contains functions for sentiment analysis and text generation using Hugging Face Transformers and NLTK.
    requirements.txt: Lists the Python packages required for the project.
    README.md: This file (you're reading it!).
    LICENSE: The project license file.

Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Ensure your code adheres to the existing style and includes necessary tests.
License

This project is licensed under the MIT License. See the LICENSE file for
