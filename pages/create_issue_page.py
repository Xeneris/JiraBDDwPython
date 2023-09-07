from selenium.webdriver import Keys
from seleniumbase import BaseCase


class CreateIssuePage(BaseCase):
    actual_project_name = "//input[@id='project-field']"
    project_input_field = "//input[@id='project-field']"
    actual_issue_type = "//input[@id='issuetype-field']"
    issue_type_field = "//input[@id='issuetype-field']"
    summary_input_field = "//input[@id='summary']"
    create_button = "//a[@id='create_link']"
    submit_issue_btn = "//input[@id='create-issue-submit']"
    created_issue_popup = "//a[@class='issue-created-key issue-link']"

    def get_project_name_on_create(self):
        return self.get_value(self.actual_project_name)

    def get_issue_type_on_create(self):
        return self.get_value(self.actual_issue_type)

    def click_project_input(self):
        self.click(self.project_input_field)

    def set_project_input(self, project):
        self.send_keys(self.project_input_field, project)

    def click_issue_input(self):
        self.click(self.issue_type_field)

    def set_issue_type_input(self, issue_type):
        self.send_keys(self.issue_type_field, issue_type)

    def set_summary(self, summary):
        self.send_keys(self.summary_input_field, summary)

    def click_on_create_btn(self):
        self.click(self.create_button)

    def click_submit_issue_btn(self):
        self.click(self.submit_issue_btn)

    def click_popup(self):
        self.click(self.created_issue_popup)

    def validate_project_name(self, project):
        if self.get_project_name_on_create() != project:
            self.click_project_input()
            self.set_project_input(project)
            self.send_keys(self.project_input_field, Keys.ENTER)

    def validate_issue_type(self, issue_type):
        if self.get_issue_type_on_create() != issue_type:
            self.click_issue_input()
            self.set_issue_type_input(issue_type)
            self.send_keys(self.project_input_field, Keys.ENTER)
