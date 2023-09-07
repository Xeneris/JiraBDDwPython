import time

from pages.create_issue_page import CreateIssuePage
from pages.issue_page import IssuePage
from pages.login_page import LoginPage
from pages.navbar import Navbar


class CreateIssueTest(LoginPage, Navbar, CreateIssuePage, IssuePage):

    def setUp(self):
        super().setUp()
        self.maximize_window()
        self.navigate("https://jira-auto.codecool.metastage.net/secure/Dashboard.jspa")

    def test_create_issue_in_coala_project(self):
        # Login
        self.successful_login()
        # Click the create button on the navbar
        self.click_on_create_btn()
        # Check if the project name needs to be changed
        self.validate_project_name("COALA project (COALA)")
        # Check if the issue type needs to be changed
        self.validate_issue_type("Story")
        # Set the summary
        self.set_summary("This is a test for coala")
        # Submit the issue
        self.click_submit_issue_btn()
        # Click the popup that takes us to our created issue
        self.click_popup()
        # Check if the summary on the page matches the one we gave
        self.assertEquals(self.get_summary(), "This is a test for coala")
        # Check if the project matches
        self.assertEquals(self.get_project_name(), "COALA project")
        # Check if the issue type is correct
        self.assertEquals(self.get_issue_type(), "Story")

    def test_create_issue_in_jeti_project(self):
        # Login
        self.successful_login()
        # Click the create button on the navbar
        self.click_on_create_btn()
        # Check if the project name needs to be changed
        self.validate_project_name("JETI project (JETI)")
        # Check if the issue type needs to be changed
        self.validate_issue_type("Bug")
        # Set the summary
        self.set_summary("This is a test for jeti")
        # Submit the issue
        self.click_submit_issue_btn()
        # Click the popup that takes us to our created issue
        self.click_popup()
        # Check if the summary on the page matches the one we gave
        self.assertEquals(self.get_summary(), "This is a test for jeti")
        # Check if the project matches
        self.assertEquals(self.get_project_name(), "JETI project")
        # Check if the issue type is correct
        self.assertEquals(self.get_issue_type(), "Bug")

    def test_create_issue_in_toucan_project(self):
        # Login
        self.successful_login()
        # Click the create button on the navbar
        self.click_on_create_btn()
        # Check if the project name needs to be changed
        self.validate_project_name("TOUCAN project (TOUCAN)")
        time.sleep(2)
        # Check if the issue type needs to be changed
        self.validate_issue_type("Story")
        # Set the summary
        self.set_summary("This is a test in toucan")
        # Submit the issue
        self.click_submit_issue_btn()
        # Click the popup that takes us to our created issue
        self.click_popup()
        # Check if the summary is correct
        self.assertEquals(self.get_summary(), "This is a test in toucan")
        # Check if the project is correct
        self.assertEquals(self.get_project_name(), "TOUCAN project")
        # Check if the issue type is correct
        self.assertEquals(self.get_issue_type(), "Story")

    def tearDown(self):
        super().tearDown()