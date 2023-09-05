import csv
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I am logged in with valid credentials')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://jira-auto.codecool.metastage.net/secure/Dashboard.jspa")
    username_field = context.driver.find_element(By.XPATH, "//input[@id='login-form-username']")
    password_field = context.driver.find_element(By.XPATH, "//input[@id='login-form-password']")
    with open("successful_login.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row['username']
            password = row['pass']
            username_field.send_keys(username)
            password_field.send_keys(password)
    context.driver.find_element(By.XPATH, "//input[@id='login']").click()
    time.sleep(1)


@when(u'I navigate to the given "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@then(u'The key on the right side of the page matches "{expected_key}"')
def step_impl(context, expected_key):
    key = context.driver.find_element(By.XPATH,
                                      "//dd[normalize-space() = 'MTP' or normalize-space() = 'COALA' or normalize-space() = 'TOUCAN' or normalize-space() = 'JETI']")
    proj_key = key.text
    assert proj_key == expected_key
    context.driver.close()

