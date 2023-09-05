from seleniumbase import BaseCase


class LogoutPage(BaseCase):
    log_out_msg = "//strong[contains(text(),'You are now logged out. Any automatic login has al')]"

    def log_out_msg_is_displayed(self):
        return self.is_element_present(self.log_out_msg)