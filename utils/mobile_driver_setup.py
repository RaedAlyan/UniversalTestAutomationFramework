import logging
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from appium.options.android import UiAutomator2Options
from logging_config import setup_logger
from config_parser import ConfigParser

setup_logger()
logger = logging.getLogger(__name__)


class MobileDriverSetup:

    def __init__(self):
        self.driver = None
        self.appium_server_url = self.get_appium_server_url()
        self.desired_capabilities = self.get_mobile_desired_capabilities()
        self.config = ConfigParser()

    def create_driver(self):
        """Create a mobile Driver instance based on the specified desired capabilities."""
        try:
            logger.info('Attempting to initialize Mobile WebDriver')
            desired_capabilities = UiAutomator2Options().load_capabilities(self.desired_capabilities)
            self.driver = webdriver.Remote(self.appium_server_url, options=desired_capabilities)
            logger.info('Mobile driver successfully initialized')
        except WebDriverException as e:
            logger.error(f'Mobile driver encountered an issue: {str(e)}')
            raise
        except Exception as e:
            logger.error(f'An unexpected error occurred while initializing the mobile driver: {str(e)}')
            raise
        return self.driver

    def get_mobile_desired_capabilities(self):
        """Retrieves the mobile desired capabilities from the config.json file"""
        return self.config.get_mobile_desired_capabilities()

    def get_appium_server_url(self):
        """Retrieves the appium server url from the config.json file"""
        return self.config.get_mobile_appium_server()

    def quit_driver(self):
        """Quit the Mobile Driver instance."""
        if self.driver:
            try:
                logger.info('Attempting to quit the Mobile driver instance')
                self.driver.quit()
                logger.info('Mobile driver instance successfully quited')
            except WebDriverException as e:
                logger.error(f'Failed to quit the Mobile driver instance: {str(e)}')
                raise
            finally:
                self.driver = None
