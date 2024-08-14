
# Review Summarizer

## **Under Development**

**Note:** This project is currently under active development. The instructions for installation and usage will be provided once the project reaches a more stable state.

## **Project Overview**

The **Review Summarizer** is a web scraping and sentiment analysis tool designed to collect, analyze, and visualize product reviews from Amazon. The project aims to provide users with detailed insights into customer feedback through sentiment classification and review summarization.

## **Project Goals**

1. **Web Scraping**: Extract product reviews from Amazon using web scraping techniques. Initially implemented with **Selenium** for navigation and **BeautifulSoup** for parsing, this allows the collection of valuable review data for analysis.

2. **Data Storage**: Transitioned from in-memory data structures to a robust **PostgreSQL** database. This setup facilitates efficient data management, allowing for the handling of larger datasets and temporary storage of reviews for processing.

3. **Text Classification**: Employed **zero-shot classification** with the **Hugging Face Transformers** library to classify review sentiments. The classification system provides nuanced sentiment insights ranging from “positive” to “somewhat negative,” offering a comprehensive understanding of user sentiments.

4. **Charting**: Planned implementation of charting functionalities to visualize sentiment trends over time. By plotting review sentiment on a monthly basis, users will be able to track changes in public perception and identify patterns in customer feedback.

5. **LLM Summarization**: Integration of **Hugging Face’s transformers pipelines** to generate concise summaries of product reviews. This feature will enable users to quickly grasp the essence of customer feedback through insightful and comprehensive overviews.

6. **Flask Web Application**: Development of a **Flask** web application to present the results. The web interface will allow users to input a product link, view detailed sentiment analysis, and see visualizations of review data, making the information accessible and engaging.

7. **Caching**: Future integration of caching mechanisms using **Redis** to improve performance. By storing results of scraping, classification, and summarization processes, this will reduce processing times for repeat requests, minimize computational overhead, and provide a smoother user experience.

## **Current Status**

As of now, the project has successfully implemented the core functionalities of web scraping and text classification. The transition to using a PostgreSQL database for data storage has been completed, enhancing data management capabilities. The next steps include developing charting functionalities, integrating LLM summarization, and building the Flask web application.

## **Learning Experience**

This project has been a significant learning journey. Starting with tools that were less suited for the task, I discovered the advantages of using **Scrapy** for scraping and **PostgreSQL** for data storage. Each phase of development has deepened my understanding of web scraping, data management, and machine learning techniques.

## **Future Work**

- **Charting**: Implementing visualization of sentiment trends over time.
- **LLM Summarization**: Integrating summarization capabilities to provide concise overviews of reviews.
- **Flask Web App**: Developing the user interface to showcase analysis results.
- **Caching**: Enhancing performance with Redis caching to improve user experience.
