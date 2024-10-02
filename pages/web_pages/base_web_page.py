import logging
from selenium import webdriver
from utils.logging_config import setup_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (TimeoutException, WebDriverException, NoSuchElementException,
                                        ElementNotInteractableException, InvalidElementStateException,
                                        StaleElementReferenceException, MoveTargetOutOfBoundsException)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

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

    def perform_click_and_hold_gesture(self, source_element: WebElement, target_element: WebElement) -> None:
        """
         Perform a click and hold gesture on the source element, move it to the target element, and release it.

        :param source_element: The WebElement to click and hold.
        :param target_element: The WebElement to move to and release.
        :return: None.
        :raises NoSuchElementException: If the source or target element cannot be found.
        :raises ElementNotInteractableException: If the source or target element is not visible.
        :raises InvalidElementStateException: If the elements are not in a state where they can be interacted with.
        :raises StaleElementReferenceException: If the elements are no longer attached to the DOM.
        :raises TimeoutException: If the action takes too long to complete.
        :raises MoveTargetOutOfBoundsException: If the target element is outside the viewport.
        :raises WebDriverException: For other unexpected WebDriver-related issues.
        """
        try:
            self.logger.info('Attempting to perform click and hold gesture.')
            actions = ActionChains(self.driver)
            actions.click_and_hold(source_element).move_to_element(target_element).release().perform()
            self.logger.info('Click and hold gesture is completed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform click and hold gesture. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform click and hold gesture. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state. Error: {e}')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Action is timed out while performing click and hold gesture. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Target element is outside the viewport. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing click and hold gesture. Error: {e}')
            raise

    def perform_double_click_gesture(self, element: WebElement) -> None:
        """
        Perform double-click gesture on the specified web element.

        :param element: The WebElement to double-click.
        :return: None.
        :raises NoSuchElementException: If the element is not found in the DOM.
        :raises ElementNotInteractableException: If the element isn't interactable to perform double-click gesture.
        :raises TimeoutException: Timed out while performing double-click gesture.
        :raises WebDriverException: For any WebDriver-related issues during the action.
        """
        try:
            self.logger.info('Attempting to perform double-click action.')
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            self.logger.info('Double-click gesture is performed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found in the DOM to perform double-click gesture. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform double-click gesture. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing double-click gesture. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing double-click gesture. Error: {e}')

    def perform_drag_and_drop_gesture(self, source_element: WebElement, target_element: WebElement) -> None:
        """
         Perform a drag-and-drop gesture.
        :param source_element: The WebElement to drag.
        :param target_element: The WebElement to drop the dragged element into.
        :return: None.
        :raises NoSuchElementException: If the source or target element isn't found perform drag and drop gesture.
        :raises ElementNotInteractableException: If the source or target element isn't interactable.
        :raises MoveTargetOutOfBoundsException: If the target element is outside the viewport or unreachable.
        :raises TimeoutException: Timed out while performing drag and drop gesture.
        :raises WebDriverException: WebDriver encountered an error during performing drag and drop gesture.
        """
        try:
            self.logger.info('Attempting to perform drag and drop gesture.')
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_element, target_element).perform()
            self.logger.info('Drag and drop gesture is performed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Source or Target element isn\'t found to perform drag and drop gesture. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform drag and drop gesture. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Target element is out of bounds for drag and drop gesture. Error: {e}')
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing drag and drop gesture. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing drag and drop gesture. Error: {e}')
            raise

    def perform_hover_over_an_element_gesture(self, element: WebElement) -> None:
        """
        Perform a hover (mouse over) gesture over the specified element.

        :param element: The WebElement to hover over.
        :return: None.
        :raises NoSuchElementException: If the element is not found in the DOM to perform hover over gesture.
        :raises ElementNotInteractableException: If the element isn't interactable to perform hover over gesture.
        :raises MoveTargetOutOfBoundsException: If the element is outside the viewport to perform hover over gesture.
        :raises TimeoutException: If the element takes too long to become interactable.
        :raises WebDriverException: For any WebDriver-related issues during the action.
        """
        try:
            self.logger.info('Attempting to perform hover (mouse over) gesture.')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.logger.info('Hover (mouse over) gesture is performed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found in the DOM to perform hover over gesture. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform hover over gesture. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is out of bounds for hover over gesture. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing hover over gesture. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing hover gesture. Error: {e}')
            raise

    def perform_context_click_gesture(self, element: WebElement) -> None:
        """
        Perform a right-click (context-click) gesture on the specified element.

        :param element: The WebElement to perform the context-click on.
        :return: None.
        :raises NoSuchElementException: If the element is not found in the DOM to perform context-click gesture.
        :raises ElementNotInteractableException: If the element isn't interactable to perform context-click gesture.
        :raises MoveTargetOutOfBoundsException: If the element is outside the viewport to perform context-click gesture.
        :raises TimeoutException: If the element takes too long to become interactable.
        :raises WebDriverException: For any WebDriver-related issues during the action.

        """
        try:
            self.logger.info('Attempting to perform context click (right click) gesture.')
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            self.logger.info('Context click (right click) gesture is performed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found in the DOM to perform context click gesture. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element is interactable to perform context click gesture. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is out of bounds for context click gesture. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing context click gesture. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing context click gesture. Error: {e}')
            raise
