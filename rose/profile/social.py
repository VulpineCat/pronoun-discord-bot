import re


class ProfileField:
    def __init__(self, key=None, value=None, extract_pattern=r'(\w+$|\w+(?=/?$))'):
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
        """URL to profile on service"""
        return self._URL.format(self._username)

    def extract_username(self, value):
        return re.findall(self._EXTRACT_PATTERN, value)[0]


class MastodonProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Mastodon", value)
        self._FLAVOUR_TEXT = "See you in the Fediverse!"
        self._URL = "https://{}/@{}"
        self._instance = self.extract_instance(value)

    @property
    def username(self):
        """Instance and Username on Mastodon"""
        return (self._username + '@' + self._instance)

    @username.getter
    def username(self):
        return (self._username + '@' + self._instance)

    @username.setter
    def username(self, value):
        self._username = self.extract_username(value)
        self._instance = self.extract_instance(value)

    @property
    def url(self):
        """URL to profile on mastodon instance"""
        return self._URL.format(self._instance, self._username)

    def extract_username(self, value):  #FIXME this code is kind of sad, maybe
        if re.findall(r'^(?:@?)(\w+)(?:@)', value):
            return re.findall(r'^(?:@?)(\w+)', value)[0]
        else:
            return re.findall(r'(\w+$|\w+(?=/?$))', value)[0]

    def extract_instance(self, value):
        if re.findall(r'(?://)(.*)(?:/)', value):
            return re.findall(r'(?://)(.*)(?:/)', value)[0]
        else:
            return re.findall(r'(?:@)(\w+\.\w+)$', value)[0]


class TwitterProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Twitter", value)
        self._FLAVOUR_TEXT = ":bird: Tweet Tweet :bird:"
        self._URL = "https://twitter.com/{}"


class TelegramProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Telegram", value)
        self._FLAVOUR_TEXT = "Have fun chatting!"
        self._URL = "https://t.me/{}"


class FacebookProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Facebook", value, r'([\w.]+$|[\w.]+(?=/?$))')
        self._FLAVOUR_TEXT = ":eyes: Mark will be watching"
        self._URL = "https://www.facebook.com/{}"


class TumblrProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Tumblr", value, r'(?:http[s]?://)?(\w+)')
        self._FLAVOUR_TEXT = "Let's keep it rolling!"
        self._URL = "https://{}.tumblr.com/"


class YoutubeProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Youtube", value, r'(?:/)(\w+)(?:\?.*)*$')
        self._FLAVOUR_TEXT = ":play_pause: We'll get people to smash that subscribe button before long! :raised_hands:"
        self._URL = "https://www.youtube.com/channel/{}"


class TwitchProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Twitch", value)
        self._FLAVOUR_TEXT = ":play_pause: Stream On!"
        self._URL = "https://www.twitch.tv/{}"


class DeviantArtProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("DeviantArt", value)
        self._FLAVOUR_TEXT = "Whether :paintbrush: or :writing_hand:, we too appreciate art here~!"
        self._URL = "https://www.deviantart.com/{}"


class EtsyProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Etsy", value, r'(?:/)(\w+)(?:\?.*)*$')
        self._FLAVOUR_TEXT = ":money_with_wings: One of your best merch, please! :money_with_wings:"
        self._URL = "https://www.etsy.com/shop/{}"


class FuraffinityProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Furaffinity", value)
        self._FLAVOUR_TEXT = ":cat: :dog: :bird: :crocodile: uwu"
        self._URL = "https://www.furaffinity.net/user/{}/"
