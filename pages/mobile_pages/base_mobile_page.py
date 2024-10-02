from appium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (NoSuchElementException, ElementNotInteractableException,
                                        InvalidElementStateException, StaleElementReferenceException,
                                        TimeoutException, WebDriverException, MoveTargetOutOfBoundsException)


class BaseMobilePage(BasePage):

    def __init__(self, driver: webdriver.Remote, timeout: int = 10):
        super().__init__(driver, timeout)

    def perform_double_tap_using_w3c_actions_api(self, element: WebElement) -> None:
        """
        Perform a double tap gesture using the W3C Actions API.

        :param element:  A web element to perform a double tap gesture on.
        :return: None.
        :raises NoSuchElementException: If the element isn't found to perform a double tap gesture.
        :raises ElementNotInteractableException: If the element isn't interactable to perform a double tap gesture.
        :raises InvalidElementStateException: If the element is not in a valid state to perform a double tap gesture.
        :raises StaleElementReferenceException: If the element is no longer attached to the DOM to perform a double tap gesture.
        :raises TimeoutException: If the double tap gesture takes too long to complete.
        :raises WebDriverException: If WebDriver encounters an error while performing a double tap gesture.
        """
        try:
            self.logger.info('Getting the current location of the element.')
            element_location = element.location
            self.logger.info(f'Current location of the element: {element_location}')
            self.logger.info(f'Performing a double tap gesture using W3C Actions API')
            self.driver.tap([(element_location['x'], element_location['y'])])
            self.logger.info('The double tap gesture is performed successfully using W3C Actions API.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform a double tap gesture using W3C Actions API. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a double tap gesture using W3C Actions API. '
                              f'Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element isn\'t in a valid state to perform a double tap gesture using W3C Actions API. '
                              f'Error: {e}')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM to perform a double tap gesture '
                              f'using W3C Actions API. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while performing a double tap gesture using W3C Actions API. '
                              f'Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a double tap gesture using '
                              f'W3C Actions API. Error: {e}.')
            raise

    def perform_double_tap_gesture_using_mobile_gestures_command(self, element: WebElement) -> None:
        """
        Perform a double tap gesture using the Mobile Gestures Command.

        :param element:  The web element to perform a double tap gesture on.
        :return: None.
        :raises NoSuchElementException: If the element isn't found to perform a double tap gesture.
        :raises ElementNotInteractableException: If the element isn't interactable to perform a double tap gesture.
        :raises InvalidElementStateException: If the element is not in a valid state to perform a double tap gesture.
        :raises StaleElementReferenceException: If the element is no longer attached to the DOM to perform a double tap gesture.
        :raises TimeoutException: If the double tap gesture takes too long to complete.
        :raises WebDriverException: If WebDriver encounters an error while performing a double tap gesture.
        """
        try:
            self.logger.info('Getting the current location of the element.')
            element_location = element.location
            self.logger.info(f'Current location of the element: {element_location}')
            self.logger.info(f'Performing a double tap gesture using the Mobile Gestures Command.')
            self.logger.info(f'Performing A double tap gesture using the Mobile Gestures Command.')
            self.driver.execute_script('mobile: doubleClickGesture', {'x': element_location['x'],
                                                                      'y': element_location['y']})
            self.logger.info('Double tap gesture is performed successfully using the Mobile Gestures Command.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform a double tap gesture using the Mobile Gestures Command.'
                              f'Error: {e}.')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a double tap gesture using the Mobile Gestures '
                              f'Command. Error: {e}.')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state to perform a double tap gesture using the Mobile '
                              f'Gestures Command. Error: {e}')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while performing a double tap gesture. Error: {e}.')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a double tap gesture. Error: {e}.')
            raise

    def perform_drag_and_drop_gesture_using_w3c_actions_api(self, draggable_element: WebElement,
                                                            droppable_element: WebElement) -> None:
        """
        Perform a drag and drop gesture using the W3C Actions API.

        :param draggable_element: the element to be dragged.
        :param droppable_element: the element to drop the draggable element onto.
        :return: None.
        :raises NoSuchElementException: If the draggable or droppable element isn't found to perform drag and drop gesture.
        :raises StaleElementReferenceException: If the elements are no longer attached to the DOM to perform drag and drop gesture.
        :raises ElementNotInteractableException: If the draggable or droppable element isn't interactable to perform a drag and drop gesture.
        :raises InvalidElementStateException: If the elements aren't in a state to perform a drag and drop gesture.
        :raises TimeoutException: If the drag-and-drop gesture takes too long to perform.
        :raises MoveTargetOutOfBoundsException: If the target element is outside the viewport to perform a drag and drop gesture.
        :raises WebDriverException: If WebDriver encounters an error while performing a drag and drop gesture.
        """
        try:
            self.logger.info("Performing drag and drop action using W3C Actions API.")
            self.driver.drag_and_drop(draggable_element, droppable_element)
            self.logger.info("Drag and drop is performed successfully using W3C Actions API.")
        except NoSuchElementException as e:
            self.logger.error(f'Draggable or droppable element isn\'t found to perform a drag and drop gesture using '
                              f'the W3C Actions API. Error: {e}.')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM to perform a drag and drop gesture using '
                              f'the W3C Actions API. Error {e}.')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a drag and drop gesture using the '
                              f'W3C Actions API. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state to perform a drag and drop gesture using the '
                              f'W3C Actions API. Error: {e}.')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing drag and drop gesture using the W3C Actions API. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Target element is outside the viewport to perform a drag and drop gesture using '
                              f'the W3C Actions API. Error: {e}.')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a drag and drop gesture using '
                              f'the W3C Actions API. Error: {e}.')

    def perform_drag_and_drop_using_mobile_gestures_command(self, draggable_element: WebElement,
                                                            droppable_element: WebElement) -> None:
        """
        Perform a drag and drop gesture using the Mobile Gestures Command.

        :param draggable_element: the element to be dragged.
        :param droppable_element: the element to drop the draggable element onto.
        :return: None.
        :raises NoSuchElementException: If the element isn't found to perform a drag and drop gesture.
        :raises StaleElementReferenceException: If the element is no longer attached to the DOM to perform a drag and drop gesture.
        :raises ElementNotInteractableException: If the element isn't interactable to perform a drag and drop gesture.
        :raises InvalidElementStateException: If the element in a state where it can't perform a drag and drop gesture.
        :raises TimeoutException: If the drag and drop gesture takes too long to perform.
        :raises MoveTargetOutOfBoundsException: If element is outside the viewport to perform a drag and drop gesture.
        :raises WebDriverException: If WebDriver encounters an error while performing a drag and drop gesture.
        """
        try:
            self.logger.info("Performing drag and drop gesture using the Mobile Gestures Command.")
            self.driver.execute_script('mobile: dragGesture', {
                'elementId': draggable_element,
                'endX': droppable_element.location['x'],
                'endY': droppable_element.location['y']
            })
            self.logger.info("Drag and drop gesture is performed successfully using the Mobile Gestures Command.")
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform a drag and drop gesture using the Mobile Gestures '
                              f'Command. Error: {e}.')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM to perform a drag and drop gesture using '
                              f'the Mobile Gestures Command. Error: {e}.')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a drag and drop gesture using the Mobile Gesture'
                              f'Command. Error: {e}.')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state to perform a drag and drop gesture using the Mobile'
                              f'Gesture command. Error: {e}.')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing a drag and drop gesture using the Mobile Gesture Command. '
                              f'Error: {e}.')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Target element is outside the viewport to perform a drag and drop gesture using the '
                              f'Mobile Gesture Command. Error: {e}.')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a drag and drop gesture using the '
                              f'Mobile Gestures Command. Error: {e}.')
