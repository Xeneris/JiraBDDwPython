from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.navbar import Navbar


class LogoutTests(LoginPage, Navbar, LogoutPage):

    def setUp(self):
        super().setUp()
        self.maximize_window()
        self.navigate("https://jira-auto.codecool.metastage.net/secure/Dashboard.jspa")

    def test_successful_logout(self):
        self.successful_login()
        self.click_avatar()
        self.click_logout_opt()
        self.assertEquals(self.log_out_msg_is_displayed(), True)

    def tearDown(self):
        super().tearDown()
