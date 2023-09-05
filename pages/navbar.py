from seleniumbase import BaseCase


class Navbar(BaseCase):
    avatar_icon = "//a[@id='header-details-user-fullname']"
    profile_opt = "//a[@id='view_profile']"
    log_out_opt = "//a[@id='log_out']"

    def click_avatar(self):
        self.click(self.avatar_icon)

    def click_profile(self):
        self.click(self.profile_opt)

    def click_logout_opt(self):
        self.click(self.log_out_opt)