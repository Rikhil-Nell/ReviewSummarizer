from driver_init import SeleniumDriver
from review_scraper import ReviewScraper, parse_reviews
from review_classifier import ReviewClassifier


def main():
    url = "https://www.amazon.in/ASIAN-Wonder-Firozi-Sports-Indian/dp/B01MTQ5M7B/ref=pd_rhf_cr_s_pd_crcbs_d_sccl_1_3/258-8358292-5648055?pd_rd_w=sDGPM&content-id=amzn1.sym.bc7f710c-555f-4ed6-8aed-005a29b438d8&pf_rd_p=bc7f710c-555f-4ed6-8aed-005a29b438d8&pf_rd_r=YAZ0BWGD6MH01GMDDKS9&pd_rd_wg=G1fXq&pd_rd_r=e9c8a13d-1dd7-4f05-b05c-7ebdaf442512&pd_rd_i=B01MTQ5M7B&psc=1"
    # Creating object of the class SeleniumDriver
    selenium_driver = SeleniumDriver()
    # Setting up the webdriver
    driver = selenium_driver.get_driver()

    try:
        # Creating object of the class ReviewScraper
        review_scraper = ReviewScraper(driver)
        page_sources = review_scraper.navigate_to_reviews(url)

        # Check if we have the required page sources
        if len(page_sources) >= 2:
            positive_reviews = parse_reviews(page_sources[0])
            negative_reviews = parse_reviews(page_sources[1])

            # Combine positive and negative reviews
            reviews = ([review['review'] for review in positive_reviews] +
                       [review['review'] for review in negative_reviews])

            # Create and use the ReviewClassifier
            review_classifier = ReviewClassifier(reviews)
            review_classifier.classify_reviews()
        else:
            print("Not enough page sources available.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the driver
        selenium_driver.close_driver()


if __name__ == "__main__":
    main()
