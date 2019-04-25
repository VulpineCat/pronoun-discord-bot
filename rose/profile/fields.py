import re


class SimpleProfileField:
    def __init__(self, key=None, value=None):
        self._KEY = key
        self._user_data = {"username": value}

    @property
    def username(self):
        """Username on platform"""
        return self._user_data["username"]
    @username.getter
    def username(self):
        return self._user_data["username"]

    @username.setter
    def username(self, value):
        self._user_data["username"] = value

    @property
    def flavour_text(self):
        """Flavour text of service"""
        return self._FLAVOUR_TEXT

    def __eq__(self, other):
        return self.username == other.username


class SwitchProfileField(SimpleProfileField):
    def __init__(self, value):
        super().__init__("switch", value)
        self._FLAVOUR_TEXT = ":joy: :spy: Get it? It's a ***joy con***"


class DSProfileField(SimpleProfileField):
    def __init__(self, value):
        super().__init__("ds", value)
        self._FLAVOUR_TEXT = "Happy Gaming!"


class PlaystationProfileField(SimpleProfileField):
    def __init__(self, value):
        super().__init__("playstation", value)
        self._FLAVOUR_TEXT = "BE MOVED"


class XBoxProfileField(SimpleProfileField):
    def __init__(self, value):
        super().__init__("xbox", value)
        self._FLAVOUR_TEXT = "added your :regional_indicator_x::regional_indicator_b:" \
                             ":regional_indicator_o::negative_squared_cross_mark:!"


class UbisoftProfileField(SimpleProfileField):
    def __init__(self, value):
        super().__init__("ubisoft", value)
        self._FLAVOUR_TEXT = "Glad to have your username there! ~~At least it's not origin!~~"


class OriginProfileField(SimpleProfileField):
    def __init__(self, value):
        super().__init__("origin", value)
        self._FLAVOUR_TEXT = "Glad to have your username there! ~~At least it's not uplay!~~"


class EpicProfileField(SimpleProfileField):
    def __init__(self, value):
        super().__init__("epic", value)
        self._FLAVOUR_TEXT = "What do ya say? Fortnite 2nite?"


class ProfileField(SimpleProfileField):
    def __init__(self, key=None, value=None, extract_pattern_list=[r'^(?:(?:.*?/?@?))(?P<username>\w+)(?:/?)$']):
        super().__init__(key)
        self._KEY = key
        self._EXTRACT_PATTERN_LIST = extract_pattern_list
        self._user_data = self.extract_user_data(value)

    @SimpleProfileField.username.setter
    def username(self, value):
        self._user_data = self.extract_user_data(value)

    @property
    def url(self):
        """URL to profile on service"""
        return self._URL.format(self._user_data["username"])

    def extract_user_data(self, value):
        for pattern in self._EXTRACT_PATTERN_LIST:
            if re.match(pattern, value):
                return re.match(pattern, value).groupdict()
        raise ValueError


class TwitterProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("twitter", value)
        self._FLAVOUR_TEXT = ":bird: Tweet Tweet :bird:"
        self._URL = "https://twitter.com/{}"


class TelegramProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("telegram", value)
        self._FLAVOUR_TEXT = "Have fun chatting!"
        self._URL = "https://t.me/{}"


class FacebookProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("facebook", value, [r'(?:\w+://\w+?\.\w+\.\w+/)(?P<username>[\w\.]+)'])
        self._FLAVOUR_TEXT = ":eyes: Mark will be watching"
        self._URL = "https://www.facebook.com/{}"


class TumblrProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("tumblr", value, [r'(?:http[s]?://)?(?P<username>\w+)'])
        self._FLAVOUR_TEXT = "Let's keep it rolling!"
        self._URL = "https://{}.tumblr.com/"


class YoutubeProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("youtube", value, [r'(?:[\w+:/.]+)(?:/)(?P<username>\w+)(?:\?.*)*$'])
        self._FLAVOUR_TEXT = ":play_pause: We'll get people to smash that subscribe button before long! :raised_hands:"
        self._URL = "https://www.youtube.com/channel/{}"


class TwitchProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("twitch", value)
        self._FLAVOUR_TEXT = ":play_pause: Stream On!"
        self._URL = "https://www.twitch.tv/{}"


class DeviantArtProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("deviantart", value)
        self._FLAVOUR_TEXT = "Whether :paintbrush: or :writing_hand:, we too appreciate art here~!"
        self._URL = "https://www.deviantart.com/{}"


class EtsyProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("etsy", value, [r'(?:[\w:/.]+/)(?P<username>\w+)(?:\?.*)*$'])
        self._FLAVOUR_TEXT = ":money_with_wings: One of your best merch, please! :money_with_wings:"
        self._URL = "https://www.etsy.com/shop/{}"


class FuraffinityProfileField(ProfileField):
    def __init__(self, value):
        super().__init__("furaffinity", value)
        self._FLAVOUR_TEXT = ":cat: :dog: :bird: :crocodile: uwu"
        self._URL = "https://www.furaffinity.net/user/{}/"


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
        super().__init__("mastodon",
                         value,
                         [r'^((?:http(?:s)?://(?:www\.)?)?(?P<domain>\w+\.\w+)/@)(?P<username>\w+)',
                          r'^(?:@?)(?P<username>\w+)(?:@)(?P<domain>\w+\.\w+)'])
        self._FLAVOUR_TEXT = "See you in the Fediverse!"
        self._URL = "https://{}/@{}"


class SteamProfileField(DomainProfileField):
    def __init__(self, value):
        super().__init__("steam",
                         value,
                         [r'^(?:[\w:/\.]+)/(?P<domain>\w+)/(?P<username>\w+)/?$'])
        self._FLAVOUR_TEXT = ":joystick: Full *Steam* Ahead!\nGet it?"
        self._URL = "https://steamcommunity.com/{}/{}/"

