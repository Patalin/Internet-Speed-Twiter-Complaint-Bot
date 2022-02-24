from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


NORMAL_DOWNLOAD_SPEED = 60
NORMAL_UP_SPEED = 5
# YOUR DRIVER PATH
CHROME_DRIVER_PATH = '/Users/macbookpro/Desktop/chromedriver'
TWITTER_EMAIL = 'your email'
TWITTER_PASS = 'your password'
USERNAME = 'YOUR TWitter username'


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver_path = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        press_consent = self.driver.find_element(By.ID, '_evidon-banner-acceptbutton')
        press_consent.click()

        press_go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        press_go.click()
        time.sleep(50)

        down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div'
                                                        '[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div'
                                                      '[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        self.up = up_speed
        self.down = down_speed

        print(down_speed)
        print(up_speed)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        time.sleep(3)

        accept_cookies = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div')
        accept_cookies.click()

        press_log_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                                           '/div[1]/div/div[3]/div[5]/a/div')
        press_log_in.click()
        time.sleep(5)

        insert_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        insert_email.send_keys(TWITTER_EMAIL)
        time.sleep(2)

        press_next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]'
                                                        '/div/div/div[2]/div[2]/div[1]/div/div[6]')
        press_next.click()
        time.sleep(2)

        enter_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        enter_username.send_keys(USERNAME)
        time.sleep(1)

        press_next_again = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        press_next_again.click()
        time.sleep(3)

        enter_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        enter_password.send_keys(TWITTER_PASS)
        time.sleep(1)

        press_log_in_again = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
        press_log_in_again.click()
        time.sleep(4)

        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_message = f"Hey @VodafoneUK, why is my internet speed {self.down} MBBs Download/{self.up}" \
                        f" MBs Upload when I pay for {NORMAL_DOWNLOAD_SPEED} MBs Download/{NORMAL_UP_SPEED} MBs Upload?"
        tweet.send_keys(tweet_message)
        time.sleep(1)

        press_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        press_tweet.click()




bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
