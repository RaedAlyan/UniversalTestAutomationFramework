import logging
from selenium import webdriver
from utils.logging_config import setup_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement


setup_logger()
logger = logging.getLogger(__name__)


class BaseWebPage:

    def __init__(self, driver: webdriver.Remote, timeout: int =10):
        """
        Initializes the ConfigParser with the specified configuration file.

        :param driver: WebDriver instance to interact with the browser.
        :param timeout: Timeout duration for waiting for elements (default is 10 seconds).
        """
        self.driver = driver
        self.timeout = timeout

    def open_url(self, url: str) -> None:
        """
        Opens the specified URL.

        :param url: URL to open.
        :return: None.
        :raises WebDriverException: If the browser fails to load the page.
        """
        try:
            logger.info(f'Opening URL: {url}')
            self.driver.get(url)
        except WebDriverException as e:
            logger.error(f'An error occurred while trying to open this URL:{url}. Error: {str(e)}')
            raise

    def find_element(self, locator: tuple) -> WebElement:
        """
        Find an element on the web page with visibility condition.

        :param locator: Tuple containing (By.<method>, locator string), e.g., (By.ID, "element_id").
        :return: The web element found.
        :raises TimeoutException: If the element isn't found within the timeout.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            logger.info(f'Finding element with locator: {locator} with waiting {self.timeout} sec te be visible.')
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            logger.error(f'Element not found or not visible! Locator: {locator}, Error: {str(e)}')
            raise
        except WebDriverException as e:
            logger.error(f'An error occurred while trying to find an element! Locator:{locator}. Error: {str(e)}')
            raise

    def find_elements(self, locator: tuple) -> list[WebElement]:
        """
        Find all elements on the web page with presence condition.

        :param locator: Tuple containing (By.<method>, locator string), e.g., (By.ID, "element_id").
        :return: List of web elements found.
        :raises TimeoutException: If the elements aren't found within the timeout.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            logger.info(f'Finding elements with locator: {locator} with waiting {self.timeout} sec te be presence.')
            elements = WebDriverWait(self.driver, self.timeout).until(
                ec.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException as e:
            logger.error(f'Elements not found or not presence! Locator: {locator}, Error: {str(e)}')
            raise
        except WebDriverException as e:
            logger.error(f'An error occurred while trying to find elements! Locator:{locator}. Error: {str(e)}')
            raise

    def click(self, locator: tuple) -> None:
        """
        Click on a web element with clickable condition.

        :param locator: Tuple containing (By.<method>, locator string), e.g., (By.ID, "element_id").
        :return: None.
        :raises TimeoutException: If the element isn't clickable within the timeout.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            logger.info(f'Clicking element with locator: {locator} with waiting {self.timeout} sec to be clickable.')
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException as e:
            logger.error(f'Element isn\'t found or not clickable! Locator: {locator}, Error: {str(e)}')
            raise
        except WebDriverException as e:
            logger.error(f'An error occurred while trying to click an element! Locator:{locator}. Error: {str(e)}')
            raise

    def send_keys(self, locator: tuple, keys: str) -> None:
        """
        Send keystrokes to a web element with visible condition.

        :param locator: Tuple containing (By.<method>, locator string), e.g., (By.ID, "element_id").
        :param keys: The string of keys to send.
        :return: None.
        :raises TimeoutException: If the element isn't visible within the timeout.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            logger.info(f'Sending this keys {keys} for this element {locator} with waiting {self.timeout} sec to be visible.')
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(locator)
            )
            element.send_keys(keys)
        except TimeoutException as e:
            logger.error(f'Element isn\'t found or not visible! Locator: {locator}, Error: {str(e)}')
            raise
        except WebDriverException as e:
            logger.error(f'An error occurred while trying to send keys to an element! Locator:{locator}. Error: {str(e)}')
            raise

    def get_current_url(self) -> str:
        """
        Gets the current URL of the browser.

        :return: The current URL as a string.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            logger.info('Getting current URL.')
            url = self.driver.current_url
            logger.info(f'Current URL: {url}')
            return url
        except WebDriverException as e:
            logger.error(f'An error occurred while trying to get the current URL. Error: {str(e)}')
            raise

    def get_title(self) -> str:
        """
        Get the title of the current page.

        :return: The page title as a string.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            logger.info('Getting title.')
            title = self.driver.title
            logger.info(f'Title: {title}')
            return title
        except WebDriverException as e:
            logger.error(f'An error occurred while trying to get the title of the current page. Error: {str(e)}')
            raise

    def switch_to_frame(self, frame_reference) -> None:
        """
        Switch to a specific iframe on the page.

        :param frame_reference: The frame element, index, or name to switch to.
        :return: None.
        :raises TimeoutException: If the frame is not available within the timeout.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            logger.info(f'Waiting {self.timeout} sec to be available to switch to frame: {frame_reference}.')
            WebDriverWait(self.driver, self.timeout).until(
                ec.frame_to_be_available_and_switch_to_it(frame_reference)
            )
        except TimeoutException as e:
            logger.error(f'Frame isn\'t available! Error: {str(e)}')
            raise
        except WebDriverException as e:
            logger.error(f'An error occurred while trying to switch to frame! Error: {str(e)}')
            raise
