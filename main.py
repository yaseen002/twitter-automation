from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TWITTER_EMAIL = "username"
TWITTER_PASSWORD = "password"
TWITTER_LINK = "https://twitter.com/"


def tweet_bot():
    driver = webdriver.Chrome()
    driver.get(TWITTER_LINK)
    time.sleep(5)

    # Click the "Sign In" button
    sign_in = driver.find_element(By.XPATH, '//a[contains(text(), "Log in")]')
    sign_in.click()
    time.sleep(5)

    # Enter the username
    username = driver.find_element(By.NAME, 'session[username_or_email]')
    username.send_keys(TWITTER_EMAIL)

    # Click the "Next" button
    next_button = driver.find_element(By.XPATH, '//div[contains(text(), "Next")]')
    next_button.click()
    time.sleep(5)

    # Enter the password
    password = driver.find_element(By.NAME, 'session[password]')
    password.send_keys(TWITTER_PASSWORD)
    time.sleep(5)

    # Click the "Log in" button
    sign_in_credential = driver.find_element(By.XPATH, '//div[contains(text(), "Log in")]')
    sign_in_credential.click()
    time.sleep(5)

    # Making a post
    post = driver.find_element(By.XPATH, '//div[@aria-label="Tweet text"]')
    post.send_keys("Hello Guys testing my bot to get post")
    time.sleep(2)

    # Click the "Tweet" button
    post_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
    post_button.click()

    # Keep the browser active until user input
    input("Press Enter to exit")

    # Close the browser
    driver.quit()

tweet_bot()
