import unittest
import random
import string
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

class LinearDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.fake = Faker()

    def tearDown(self):
        self.driver.quit()

    def test_linear_flow_testing_03(self):
        self.driver.get("https://jignect.tech/")

# 1. Check if the web title is as expected
        self.assertIn("Software and QA Testing Company| JigNect Technologies Pvt Ltd", self.driver.title, 
                      "Expected text not found in page title")
        
# 2. Check if the 'contact us' button is displayed properly
        try:
            contact_us_button = self.driver.find_element(By.XPATH, "//nav/ul/li[8]/a")
            self.assertTrue(contact_us_button.is_displayed(), "The 'contact us button' element not displayed")
        except NoSuchElementException as e:
            self.fail(f"Contact us button not found: {e}")

# 3. Check if the 'contact us' button is clickable and redirects to the expected subpage
        contact_us_button.click()
        WebDriverWait(self.driver, 5).until(EC.title_contains("Contact Us | JigNect Technologies Pvt Ltd"))
        self.assertIn("Contact Us | JigNect Technologies Pvt Ltd", self.driver.title, 
                      "Expected text not found in page title after clicking 'Contact Us'")
        
# 4. Check if the 'contact-new-form' element is displayed properly
        contact_new_form = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form")
        self.assertTrue(contact_new_form.is_displayed(), "The element 'contact_new_form' not displayed")

# 5. Check if the 'contact us' box displays the expected text header
        contact_us_header = self.driver.find_element(By.CSS_SELECTOR, "div.contact-title h2").text
        self.assertEqual(contact_us_header, "Let's talk", "Contact Us welcome message not displayed")

# 6. Check if the 'contact us box' displays the expected 'contact message' 
        contact_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form textarea[placeholder]")
        placeholder = contact_message.get_attribute("placeholder")
        self.assertEqual(placeholder, 
                         "Do you have any specific requirements? Please let us know and we can include them in the discussion.",
                         "Expected text not present")

# 7. Check if the 'fields have an error' message is not present before the 'submit button' is clicked
        error_message_element = self.driver.find_element(By.XPATH, "//*[@id='wpcf7-f4408-p4307-o1']/form/div[3]")
        self.assertFalse(error_message_element.is_displayed(), "Unexpected field error message")

# 8. Check validation messages after clicking and leaving fields empty, then clicking the 'submit' button
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form textarea").click()
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form input[name='your-name']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form input[name='your-email']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form input[name='your-company']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form input[name='your-phone']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form input[type='submit']").click()

        expected_validation_message = 'The field is required.'

        # Validate each required field's validation message
        fields = [
            (By.CSS_SELECTOR, "#contact-new-form div:nth-child(2) span.wpcf7-not-valid-tip"),
            (By.CSS_SELECTOR, "#contact-new-form div:nth-child(3) div:nth-child(1) span.wpcf7-not-valid-tip"),
            (By.CSS_SELECTOR, "#contact-new-form div:nth-child(3) div:nth-child(2) span.wpcf7-not-valid-tip"),
            (By.CSS_SELECTOR, "#contact-new-form div:nth-child(4) div:nth-child(1) span.wpcf7-not-valid-tip"),
            (By.CSS_SELECTOR, "#contact-new-form div:nth-child(4) div:nth-child(2) span.wpcf7-not-valid-tip"),
            (By.CSS_SELECTOR, "#contact-new-form div:nth-child(5) span.wpcf7-not-valid-tip")
        ]

        for locator in fields:
            validation_message = self.driver.find_element(*locator).text
            self.assertEqual(validation_message, expected_validation_message, 
                             f"Validation message mismatch: {validation_message}")
            
# 9. Check if 'One or more fields have an error' message is present
        fields_have_an_error_message = self.driver.find_element(By.XPATH, "//*[@id='wpcf7-f4408-p4307-o1']/form/div[3]")
        self.assertTrue(fields_have_an_error_message.is_displayed(), "'Fields have an error message' did not appear")

# 10. Check if the 'contact new form' saves 'user message' properly
        user_message = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(1222))
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form textarea").send_keys(user_message)
        user_message_value = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form textarea").get_attribute("value")
        self.assertEqual(user_message_value, user_message, "Expected user input not present")

# 11. Check if the 'Full name' field saves input correctly
        full_name = self.fake.name()
        full_name_field = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form input[name='your-name']").send_keys(full_name)
        full_name_value = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form input[name='your-name']").get_attribute("value")
        self.assertEqual(full_name, full_name_value, "'Full name' value missing")

# 12. Check if the 'user message' textarea 'validation message' disappears after being clicked and left empty
        textarea_locator = (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > span")
        try:
            WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located(textarea_locator))
        except TimeoutException:
            self.fail("'Textarea' validation message still appears")

# 13. Check if the 'Full name' validation message disappears after being clicked and left empty
        self.driver.find_element(By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[1]/p/span/input').click()
        full_name_validation_locator = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[1]/p/span/span')
        try:
            WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located(full_name_validation_locator))
        except TimeoutException:
            self.fail("'Full name' validation message still appears")   

# 14. Check if the 'Company' field is interactive and saves 'user text' properly
        company_name = "".join(random.choice(string.ascii_letters) for _ in range(12))
        self.driver.find_element(By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[1]/p/span/input').send_keys(company_name)
        company_name_value = self.driver.find_element(By.CSS_SELECTOR, '#contact-new-form div:nth-child(4) div:nth-child(1) span input').get_attribute("value")
        self.assertEqual(company_name_value, company_name, "Expected user input not present in 'Company' field")





# 15. Check if the 'Work email address' is clickable and saves 'user message' properly
        work_email_address_locator = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/input')
        try:
            work_email_address_field = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(work_email_address_locator))
            work_email_address_field.click()
            self.driver.find_element(*work_email_address_locator).send_keys(self.fake.email())
        except TimeoutException:
            self.fail("'Work email address' field not interactive")

 
 
 
 
 
 
        # 16. Check if the 'Work email address' returns an invalid email format prompt correctly
        invalid_email_format_locator = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/span')
        
        def generate_invalid_email():
            random_length = random.randint(1, 20)
            return "".join(random.choice(string.ascii_letters) for _ in range(random_length))

        work_email_field = self.driver.find_element(*work_email_address_locator)
        phone_field = self.driver.find_element(By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[2]/p/span/input')

        for _ in range(11):
            invalid_email = generate_invalid_email()
            work_email_field.send_keys(invalid_email)
            phone_field.click()

            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(invalid_email_format_locator))

            error_message = self.driver.find_element(*invalid_email_format_locator).text
            self.assertIn("invalid email format", error_message.lower(), f"Email format error message not found for input: {invalid_email}")
            work_email_field.clear()

        work_email_field.clear()
        phone_field.click()

if __name__ == "__main__":
    unittest.main()