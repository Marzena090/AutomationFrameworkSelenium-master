# importing json library (already built in Python)
import json
# importing Configuration, ApplicationCanfiguration and WebDriverConfiguration class from config.config file
from config.config import Configuration, ApplicationConfiguration, WebDriverConfiguration


class ConfigProvider:

    # method to load json and return our configuration
    def load_config(self):
        # opening a file as config, r = read, w = edit
        with open("C:/Users/marze/Desktop/AutomationFrameworkSelenium-master/config/config.json", "r") as config:
            # assigning to config_json the method json.loads to load the file as dictionary variable
            # ! navigating through the dictionary: config_json["application_configuration"], if nested:
            # config_json["application_configuration"]["base_url"] to be more specific
            config_json = json.loads(config.read())
            # assigning to webdriver_config this what's inside the section web_driver_configuration
            # from our config_json dictionary
            webdriver_config = WebDriverConfiguration(**config_json['web_driver_configuration'])
            # assigning to app_configuration this what's inside the section application_configuration
            # from our config_json dictionary
            app_configuration = ApplicationConfiguration(**config_json['application_configuration'])
            # creating instance of class Configuration where property application_configuration is app_configuration
            # and web_driver_cnofiguration is webdriver_config
            configuration = Configuration(application_configuration=app_configuration,
                                          web_driver_configuration=webdriver_config)
            # return the configuration
            return configuration
