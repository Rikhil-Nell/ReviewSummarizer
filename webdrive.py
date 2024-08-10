from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://www.amazon.in/AS-Nutrition-Creatine-Monohydrate-Building/dp/B07Q8JJLFL/ref=cm_cr_arp_d_pdt_img_top?ie=UTF8"

options = Options()
options.add_argument('--no-sandbox')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Navigate to the product page
    driver.get(URL)
    time.sleep(3)  # Wait for the page to load

    try:
        # Click on the "See all reviews" link to navigate to the reviews page
        reviews_link = driver.find_element(By.XPATH, '//a[@data-hook="see-all-reviews-link-foot"]')
        reviews_link.click()
        print("Navigated to the reviews page.")
        time.sleep(5)  # Wait for the reviews page to load

        try:
            # Click on the "Positive reviews" link to navigate to the positive reviews page
            positive_reviews_link = driver.find_element(By.XPATH, '//a[@data-reftag="cm_cr_arp_d_viewpnt_lft"]')
            positive_reviews_link.click()
            print("Navigated to the positive reviews page.")
            time.sleep(5)  # Wait for the positive reviews page to load

        except Exception as e:
            print("Positive reviews link not found or an error occurred:", e)

    except Exception as e:
        print("Reviews link not found or an error occurred:", e)

except Exception as e:
    print("An error occurred while loading the page:", e)

finally:
    # Clean up by closing the browser
    driver.quit()
