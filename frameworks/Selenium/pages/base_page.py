from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
      self.driver = driver

    def find_element(self, locator):
      return self.driver.find_element(*locator)

    def find_elements(self, locator):
      return self.driver.find_elements(*locator)

    def presence_wait(self, locator, timeout=10):
      return WebDriverWait(self.driver, timeout).until(
        EC.presence_of_element_located(locator)
      )

    def exists_on_screen(self, locator, text=None, timeout=10):
      locator = (locator[0], locator[1].format(text))
        
    def text_exists_on_screen(self, locator, text, timeout=10):
      element = self.find_element(locator)

    def click(self, locator):
      self.presence_wait(locator, 20)
      element = self.find_element(locator)
      self.driver.execute_script("arguments[0].click();", element)

    def write(self, locator, text, timeout=10):
      self.presence_wait(locator, timeout)
      self.find_element(locator).send_keys(text)
