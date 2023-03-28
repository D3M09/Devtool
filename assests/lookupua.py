import re

class UserAgentValidator:
    def __init__(self, user_agent):
        self.user_agent = user_agent
        self.is_facebook_app = 'FBAN' in user_agent
        self.is_facebook_lite = 'FBAV' in user_agent and 'FBDV' in user_agent
        self.is_messenger_app = 'FBAN' in user_agent and 'Messenger' in user_agent
        match = re.search(r'\((.*?)\)', user_agent)
        if match:
            parts = match.group(1).split(';')
            self.app_system = parts[0].strip()
            self.browser_name = parts[-2].split()[0].strip()
    def validate(self):
        if self.is_facebook_app:
            print('\n\033[32mApp System: {}\nBrowser Name: {}\nIs Facebook App: True\nIs Facebook Lite: {}\nIs Messenger App: {}\033[0m'
                  .format(self.app_system, self.browser_name, self.is_facebook_lite, self.is_messenger_app))
        else:
            print('\n\033[31mApp System: {}\nBrowser Name: {}\nIs Facebook App: {}\nIs Facebook Lite: {}\nIs Messenger App: {}\033[0m'
                  .format(self.app_system, self.browser_name, self.is_facebook_app, self.is_facebook_lite, self.is_messenger_app))

user_agent = input('\nUseragent : ')
validator = UserAgentValidator(user_agent)
validator.validate()
