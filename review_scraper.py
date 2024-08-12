from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def parse_reviews(page_source):
    if page_source:
        soup = BeautifulSoup(page_source, 'html.parser')
        reviews = soup.find_all('span', {'data-hook': 'review-body'})
        dates = soup.find_all('span', {'data-hook': 'review-date'})

        review_data = []
        for review, date in zip(reviews, dates):
            review_data.append({
                'review': review.get_text(strip=True),
                'date': date.get_text(strip=True)
            })

        return review_data

    print("Page sources parsed.")
    return None


class ReviewScraper:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_reviews(self, url):
        try:
            self.driver.get(url)

            # Wait for the "See all reviews" link to be present
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//a[@data-hook="see-all-reviews-link-foot"]'))
            )

            try:
                # Click on the "See all reviews" link to navigate to the reviews page
                reviews_link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@data-hook="see-all-reviews-link-foot"]'))
                )
                reviews_link.click()
                print("Navigated to the reviews page.")

                # Wait for the positive reviews link to be present
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//a[@data-reftag="cm_cr_arp_d_viewpnt_lft"]'))
                )
                page_sources = []
                # Click on the "Positive reviews" link
                positive_reviews_link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@data-reftag="cm_cr_arp_d_viewpnt_lft"]'))
                )
                positive_reviews_link.click()
                time.sleep(2)  # Short sleep to ensure the page has loaded
                page_sources.append(self.driver.page_source)

                # Wait for the critical reviews link to be present
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//a[@data-reftag="cm_cr_arp_d_viewpnt_rgt"]'))
                )

                # Click on the "Critical reviews" link
                critical_reviews_link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@data-reftag="cm_cr_arp_d_viewpnt_rgt"]'))
                )
                critical_reviews_link.click()
                time.sleep(2)  # Short sleep to ensure the page has loaded
                page_sources.append(self.driver.page_source)

                print("Obtained Page Sources.")
                return page_sources

            except Exception as e:
                print("Filtered reviews not found or an error occurred:", e)
                return None

        except Exception as e:
            print("Reviews not found or an error occurred:", e)
            return None
