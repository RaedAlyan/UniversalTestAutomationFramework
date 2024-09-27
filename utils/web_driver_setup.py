import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException
from logging_config import setup_logger
from config_parser import ConfigParser


setup_logger()
logger = logging.getLogger(__name__)


class WebDriverSetup:

    def __init__(self):
        self.driver = None
        self.browser = self.get_specified_browser()
        self.config = ConfigParser()

    def get_specified_browser(self):
        """Get the specified browser from the config.json"""
        return self.config.get_web_browser()

    def create_driver(self):
        """Create a WebDriver instance based on the specified browser."""
        try:
            logger.info(f'Attempting to initialize WebDriver for browser: {self.browser}')
            self._initialize_driver()
            logger.info(f'{self.browser.capitalize()} WebDriver successfully initialized')
        except SessionNotCreatedException as e:
            logger.error(f'Session could not be created: {str(e)}')
            raise
        except WebDriverException as e:
            logger.error(f'WebDriver encountered an issue: {str(e)}')
            raise
        except ValueError as e:
            logger.error(f'ValueError: {str(e)}')
            raise
        except Exception as e:
            logger.error(f'An unexpected error occurred: {str(e)}')
            raise
        return self.driver

    def _initialize_driver(self):
        """Initialize WebDriver based on browser type."""
        if self.browser == 'chrome':
            logger.info('Initializing Chrome WebDriver')
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif self.browser == 'edge':
            logger.info('Initializing Edge WebDriver')
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        elif self.browser == 'firefox':
            logger.info('Initializing Firefox WebDriver')
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            logger.error(f'Unsupported browser: {self.browser}')
            raise ValueError(f'Unsupported browser: {self.browser}')

    def quit_driver(self):
        """Quit the WebDriver instance."""
        if self.driver is not None:
            try:
                logger.info('Quitting the WebDriver instance')
                self.driver.quit()
            except WebDriverException as e:
                logger.error(f'Failed to quit the WebDriver: {str(e)}')
                raise
            finally:
                self.driver = None
