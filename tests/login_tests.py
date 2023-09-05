from pages.login_page import LoginPage
from pages.navbar import Navbar
import unittest

unittest.TestLoader.sortTestMethodsUsing = None


class LoginTests(LoginPage, Navbar):
    def setUp(self):
        super().setUp()
        self.maximize_window()

        self.navigate("https://jira-auto.codecool.metastage.net/secure/Dashboard.jspa")

    def test_1_successful_login(self):
        self.successful_login()
        self.click_avatar()
        self.click_profile()
        self.assertEquals(self.get_username(), "automation48")

    def test_2_login_wit_valid_username_and_invalid_password(self):
        self.set_username()
        self.set_invalid_password()
        self.click_login_btn()
        self.assertEquals(self.get_login_error_msg(),
                          "Sorry, your username and password are incorrect - please try again.")
        self.successful_login()

    def test_3_login_with_invalid_credentials(self):
        self.set_invalid_username()
        self.set_invalid_password()
        self.click_login_btn()
        self.assertEquals(self.get_login_error_msg(),
                          "Sorry, your username and password are incorrect - please try again.")
        self.successful_login()

    def test_4_login_without_credentials(self):
        self.click_login_btn()
        self.assertEquals(self.get_login_error_msg(),
                          "Sorry, your username and password are incorrect - please try again.")
        self.successful_login()

    def test_5_login_with_valid_username_and_invalid_password(self):
        self.set_username()
        self.set_invalid_password()
        self.click_login_btn()
        self.assertEquals(self.get_login_error_msg(),
                          "Sorry, your username and password are incorrect - please try again.")
        self.successful_login()

    def test_6_captcha_popup_after_three_unsuccessful_tries(self):
        # First try
        self.set_username()
        self.set_invalid_password()
        self.click_login_btn()

        # Second try
        self.set_username()
        self.set_invalid_password()
        self.click_login_btn()

        # Third try
        self.set_username()
        self.set_invalid_password()
        self.click_login_btn()
        self.assertEquals(self.captcha_is_displayed(), True)

    def tearDown(self):
        super().tearDown()
