# importing ConfigProvider class
from config.config_provider import ConfigProvider


def main():
    # creating an instance of ConfigProvider class
    config = ConfigProvider().load_config()
    # printing the name of the browser
    print(config.web_driver_configuration.browser_name)
    # printing the password
    print(config.application_configuration.password)


# calling the main function
main()
