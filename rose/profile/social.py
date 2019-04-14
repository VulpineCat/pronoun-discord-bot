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

    def extract_username(self, value):
        import re
        return re.findall(r'\w+\\?$', value)[0]
