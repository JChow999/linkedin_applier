from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

login_email = os.environ.get("LINKEDIN_EMAIL")
login_password = os.environ.get("LINKEDIN_PASS")

# Setting up selenium webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
linkedin = webdriver.Chrome(options=chrome_options)
linkedin.get("https://www.linkedin.com/")
time.sleep(0.4)

# Check if website is returning blank
body_text = linkedin.find_element(By.TAG_NAME, "body").text
if body_text.strip() == "":
    linkedin.refresh()


# Logging onto the linkedin
email_input = linkedin.find_element(By.ID, "session_key")
email_input.send_keys(login_email)
pass_input = linkedin.find_element(By.ID, "session_password")
pass_input.send_keys(login_password)
pass_input.send_keys(Keys.ENTER)
time.sleep(1)

# Goes to job section and searches for jobs
job_button = linkedin.find_elements(By.CSS_SELECTOR, "nav ul li")
job_button[2].click()
time.sleep(0.7)

job_page = "https://www.linkedin.com/jobs/search/?currentJobId=3701796499&distance=25&geoId=101788145&keywords=software%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true"
linkedin.get(job_page)
time.sleep(0.7)

job_postings = linkedin.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
for posting in job_postings:
    posting.click()
    print(posting.text)

# linkedin.quit()

