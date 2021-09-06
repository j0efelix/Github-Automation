from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Development\chromedriver.exe"
USERNAME = "EMAIL"
PASSWORD = "PASSWORD"

repoInput = input("Enter your repo name: ")


class GitHubAutomation:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def githublogin(self, email, password):
        self.driver.get("https://github.com/login")
        login = self.driver.find_element_by_id("login_field")
        passwordField = self.driver.find_element_by_id("password")

        login.send_keys(email)
        passwordField.send_keys(password)
        passwordField.send_keys(Keys.ENTER)

    def createrepo(self):
        time.sleep(10)
        plus_btn = self.driver.find_element_by_class_name("dropdown-caret")
        plus_btn.click()
        time.sleep(1)
        new_repo = self.driver.find_element_by_link_text("New repository")
        new_repo.click()
        time.sleep(5)
        repo_name = self.driver.find_element_by_id("repository_name")
        repo_name.send_keys(repoInput)
        time.sleep(2)
        repo_name.send_keys(Keys.ENTER)
        time.sleep(5)


auto = GitHubAutomation(PATH)
auto.githublogin(email=USERNAME, password=PASSWORD)
auto.createrepo()
