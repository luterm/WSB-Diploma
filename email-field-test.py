from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import string
import unittest

class ContactFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("URL_OF_YOUR_FORM")  # Replace with the actual URL

    def tearDown(self):
        self.driver.quit()

    def test_company_field_interactive(self):
        characters = string.ascii_letters + string.digits
        company_name = "".join(random.choice(characters) for _ in range(12))
        company_field = self.driver.find_element(By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[1]/p/span/input')
        company_field.send_keys(company_name)
        company_field_value = company_field.get_attribute("value")
        self.assertEqual(company_field_value, company_name, "Expected user input not present in 'Company' field")

    def test_work_email_field_clickable(self):
        work_email_xpath = '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/input'
        work_email_field = self.driver.find_element(By.XPATH, work_email_xpath)
        try:
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, work_email_xpath)))
            work_email_field.click()
            self.assertTrue(work_email_field.is_displayed() and work_email_field.is_enabled(), "'Work email address' field is not clickable")
        except TimeoutException:
            self.fail("'Work email address' field not interactive")

    def test_invalid_email_format_prompt(self):
        work_email_xpath = '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/input'
        another_field_xpath = '//*[@id="contact-new-form"]/div[4]/div[2]/p/span/input'

        def generate_invalid_email():
            characters = string.ascii_letters + string.digits
            random_length = random.randint(1, 20)
            return "".join(random.choice(characters) for _ in range(random_length))

        work_email_field = self.driver.find_element(By.XPATH, work_email_xpath)

        for _ in range(11):
            invalid_email = generate_invalid_email()
            work_email_field.send_keys(invalid_email)
            self.driver.find_element(By.XPATH, another_field_xpath).click()  # Trigger validation
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".email-error-message"))
            )
            error_message = self.driver.find_element(By.CSS_SELECTOR, ".email-error-message").text
            self.assertTrue("invalid email format" in error_message.lower(), f"Error message not found for input: {invalid_email}")
            work_email_field.clear()

        work_email_field.clear()
        self.driver.find_element(By.XPATH, another_field_xpath).click()  # Ensure form ends in a known state

if __name__ == "__main__":
    unittest.main()
