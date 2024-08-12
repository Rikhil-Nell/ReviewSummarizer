from driver_init import SeleniumDriver
from review_scraper import ReviewScraper, parse_reviews
from review_classifier import ReviewClassifier


def main():
    url = "https://www.amazon.in/Number-Backpack-Compartment-Charging-Organizer/dp/B09VTDMRY7?pd_rd_w=giCzt&content-id=amzn1.sym.ec5c60c1-ae3d-4950-9707-1e49240719bc&pf_rd_p=ec5c60c1-ae3d-4950-9707-1e49240719bc&pf_rd_r=Y3MSH92QWBEKYCN9ATGK&pd_rd_wg=ZzwV4&pd_rd_r=8e0c7a40-a11e-4573-9b38-15ab13f59a8c&pd_rd_i=B09VTDMRY7&ref_=pd_hp_d_btf_unk_B09VTDMRY7"

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
            # Parse reviews
            positive_reviews = parse_reviews(page_sources[0])
            negative_reviews = parse_reviews(page_sources[1])

            # Combine positive and negative reviews
            reviews = ([review for review in positive_reviews] +
                       [review for review in negative_reviews])

            print("Reviews:")
            for i, review in enumerate(reviews, start=1):
                print(f"Review {i}:")
                print(f"Review: {review['review']}")
                print(f"Date: {review['date']}")
                print("-" * 40)  # Separator line

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
