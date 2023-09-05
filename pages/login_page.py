import csv
from seleniumbase import BaseCase


class LoginPage(BaseCase):
    username_field = "//input[@id='login-form-username']"
    password_field = "//input[@id='login-form-password']"
    login_btn = "//input[@id='login']"
    username_on_profile = "//dd[@id='up-d-username']"
    error_message_on_login = "//p[contains(text(),'Sorry, your username and password are incorrect - ')]"
    captcha_div = "//div[@id='captcha']"

    def navigate(self, url):
        self.get(url)

    def set_password(self):
        self.set_text(self.password_field, "asd")

    def successful_login(self):
        with open("../successful_login.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                username = row['username']
                password = row['pass']
                self.set_text(self.username_field, username)
                self.set_text(self.password_field, password)
        self.click(self.login_btn)

    def set_username(self):
        with open("../successful_login.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                username = row['username']
                self.set_text(self.username_field, username)

    def set_invalid_username(self):
        self.set_text(self.username_field, "asd123")

    def set_invalid_password(self):
        self.set_text(self.password_field, "asd123")

    def click_login_btn(self):
        self.click(self.login_btn)

    def get_username(self):
        return self.get_text(self.username_on_profile)

    def captcha_is_displayed(self):
        return self.is_element_present(self.captcha_div)

    def get_login_error_msg(self):
        return self.get_text(self.error_message_on_login)