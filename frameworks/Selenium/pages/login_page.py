from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageLocators:
  textLogin = (By.XPATH, "//h5[text()='Login']")
  usernameField = (By.XPATH, "//input[@name='username']")
  passwordField= (By.XPATH, "//input[@name='password']")

class LoginPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def verify_login_page(self):
    self.exists_on_screen(LoginPageLocators.textLogin)

  def enter_credentials(self, username, password):
    self.write(LoginPageLocators.usernameField, username)
    self.write(LoginPageLocators.passwordField, password)

  def click_login(self):
    pass

  def verify_dashboard_access(self):
    pass
