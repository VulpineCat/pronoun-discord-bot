import re


class ProfileField:
    def __init__(self, key=None, value=None, extract_pattern=r'\w*'):
        self._KEY = key
        self._EXTRACT_PATTERN = extract_pattern
        self._username = self.extract_username(value)

    @property
    def username(self):
        """Username on platform"""
        return self._username

    @username.getter
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = self.extract_username(value)

    @property
    def flavour_text(self):
        """Flavour text of service"""
        return self._FLAVOUR_TEXT

    @property
    def url(self):
        """URL to profile on profile"""
        return self._URL.format(self._username)

    def extract_username(self, value):
        return re.findall(self._EXTRACT_PATTERN, value)[0]


class TwitterProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Twitter", value, r'(\w+$|\w+(?=/?$))')
        self._FLAVOUR_TEXT = ":bird: Tweet Tweet :bird:"
        self._URL = "https://twitter.com/{}"


class TelegramProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Telegram", value, r'(\w+$|\w+(?=/?$))')
        self._FLAVOUR_TEXT = "Have fun chatting!"
        self._URL = "https://t.me/{}"
