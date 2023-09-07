from seleniumbase import BaseCase


class IssuePage(BaseCase):
    summary = "//h1[@id='summary-val']"
    project = "//a[@id='project-name-val']"
    issue = "//span[@id='type-val']"

    def get_summary(self):
        return self.get_text(self.summary)

    def get_project_name(self):
        return self.get_text(self.project)

    def get_issue_type(self):
        return self.get_text(self.issue)