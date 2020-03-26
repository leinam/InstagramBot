from selenium import webdriver
from time import sleep


class InstaBot(object):
    def __init__(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.get('https://www.instagram.com')
        sleep(2)

    def login(self, username: str, password: str):
        self.username = username
        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        password_field = self.browser.find_element_by_xpath("//input[@aria-label='Password']")

        username_field.click()
        username_field.send_keys(username)

        password_field.click()
        password_field.send_keys(password)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.submit()

        sleep(4)

        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def like_post(self):
        like_button = self.browser.find_element_by_xpath("//button[@class='wpO6b ']")
        like_button.click()


if __name__ == "__main__":
    iBOt = InstaBot()
    iBOt.login('_leina__', 'Allllle')
    iBOt.like_post()






