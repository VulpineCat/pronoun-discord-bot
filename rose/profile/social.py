import re


class ProfileField:
    def __init__(self, key=None, value=None, extract_pattern_list=[r'^(?:(?:.*?/?@?))(?P<username>\w+)(?:/?)$']):
        self._KEY = key
        self._EXTRACT_PATTERN_LIST = extract_pattern_list
        self._user_data = self.extract_user_data(value)

    @property
    def username(self):
        """Username on platform"""
        return self._user_data["username"]

    @username.getter
    def username(self):
        return self._user_data["username"]

    @username.setter
    def username(self, value):
        self._user_data = self.extract_user_data(value)

    @property
    def flavour_text(self):
        """Flavour text of service"""
        return self._FLAVOUR_TEXT

    @property
    def url(self):
        """URL to profile on service"""
        return self._URL.format(self._user_data["username"])

    def extract_user_data(self, value):
        for pattern in self._EXTRACT_PATTERN_LIST:
            if re.match(pattern, value):
                return re.match(pattern, value).groupdict()
        raise ValueError


class DomainProfileField(ProfileField):
    def __init__(self, key=None, value=None, extract_pattern_list=[r'(\w+$|\w+(?=/?$))']):
        super().__init__(key, value, extract_pattern_list)

    @property
    def domain(self):
        """Domain which user uses"""
        return self._user_data["domain"]

    @domain.getter
    def domain(self):
        return self._user_data["domain"]

    @domain.setter
    def domain(self, value):
        self._user_data,  = self.extract_username(value)

    @property
    def url(self):
        """URL to profile on domain"""
        return self._URL.format(self._user_data["domain"], self._user_data["username"])


class MastodonProfileField(DomainProfileField):
    def __init__(self, value):
        super().__init__("Mastodon",
                         value,
                         [r'^((?:http(?:s)?://(?:www\.)?)?(?P<domain>\w+\.\w+)/@)(?P<username>\w+)',
                          r'^(?:@?)(?P<username>\w+)(?:@)(?P<domain>\w+\.\w+)'])
        self._FLAVOUR_TEXT = "See you in the Fediverse!"
        self._URL = "https://{}/@{}"


class SteamProfileField(DomainProfileField):
    def __init__(self, value):
        super().__init__("Steam",
                         value,
                         [r'^(?:[\w:/\.]+)/(?P<domain>\w+)/(?P<username>\w+)/?$'])
        self._FLAVOUR_TEXT = ":joystick: Full *Steam* Ahead!\nGet it?"
        self._URL = "https://steamcommunity.com/{}/{}/"


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
        super().__init__("Facebook", value, [r'(?:\w+://\w+?\.\w+\.\w+/)(?P<username>[\w\.]+)'])
        self._FLAVOUR_TEXT = ":eyes: Mark will be watching"
        self._URL = "https://www.facebook.com/{}"


class TumblrProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Tumblr", value, [r'(?:http[s]?://)?(?P<username>\w+)'])
        self._FLAVOUR_TEXT = "Let's keep it rolling!"
        self._URL = "https://{}.tumblr.com/"


class YoutubeProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Youtube", value, [r'(?:[\w+:/.]+)(?:/)(?P<username>\w+)(?:\?.*)*$'])
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
        super().__init__("Etsy", value, [r'(?:[\w:/.]+/)(?P<username>\w+)(?:\?.*)*$'])
        self._FLAVOUR_TEXT = ":money_with_wings: One of your best merch, please! :money_with_wings:"
        self._URL = "https://www.etsy.com/shop/{}"


class FuraffinityProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Furaffinity", value)
        self._FLAVOUR_TEXT = ":cat: :dog: :bird: :crocodile: uwu"
        self._URL = "https://www.furaffinity.net/user/{}/"

class SwitchProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("Switch", value, [r'(?P<username>[\w-]+)'])
        self._FLAVOUR_TEXT = ":joy: :spy: Get it? It's a ***joy con***"
        self._URL = "{}"

class DSProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("3DS", value, [r'(?P<username>[\w-]+)'])
        self._FLAVOUR_TEXT = "Happy Gaming!"
        self._URL = "{}"
