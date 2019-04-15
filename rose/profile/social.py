class TwitterProfileField:
    def __init__(self, value):
        self._KEY = "Twitter"
        self._username = self.extract_username(value)

    @property
    def username(self):
        """Username on Twitter"""
        return self._username

    @username.getter
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = self.extract_username(self, value)

    @property
    def url(self):
        """URL to profile on Twitter"""
        return 'https://twitter.com/{}'.format(self._username)

    @property
    def flavour_text(self):
        """Flavour text of service"""
        return ":bird: Tweet Tweet :bird:"

    def extract_username(self, value):
        import re
        return re.findall(r'(\w+$|\w+(?=/?$))', value)[0]

class TelegramProfileField:
    def __init__(self, value):
        self._KEY = "Telegram"
        self._username = self.extract_username(value)

    @property
    def username(self):
        """Username on Telegram"""
        return self._username

    @username.getter
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = self.extract_username(self, value)

    @property
    def url(self):
        """URL to profile on Telegram"""
        return 'https://t.me/{}'.format(self._username)

    @property
    def flavour_text(self):
        """Flavour text of service"""
        return "Have fun chatting!"

    def extract_username(self, value):
        import re
        return re.findall(r'(\w+$|\w+(?=/?$))', value)[0]
