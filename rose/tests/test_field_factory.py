import rose.profile.field_factory as factory
import rose.profile.fields as fields
import pytest


class TestFieldFactory:
    def test_field_factory_twitter(self):
        field = factory.get_field_for("Twitter", "@real_praxis")
        assert isinstance(field, fields.TwitterProfileField)

    def test_all_factory_branches(self):
        test_dict = {'Twitter': '@real_praxis',
                     'Switch': 'SW0000-0000-0000',
                     'DS': '0000-0000-0000',
                     'Playstation': 'username',
                     'XBox': 'username',
                     'Ubisoft': 'username',
                     'Origin': 'username',
                     'Epic': 'username',
                     'Telegram': '@good_praxis',
                     'Facebook': 'https://www.facebook.com/zuck',
                     'Tumblr': 'https://littleanimalgifs.tumblr.com/',
                     'Youtube': 'https://www.youtube.com/channel/UC6FHHzDg0lRAQ2Rw5ESNz_g',
                     'Twitch': 'https://www.twitch.tv/good_praxis',
                     'DeviantArt': 'https://www.deviantart.com/spyed',
                     'Etsy': 'https://www.etsy.com/shop/404',
                     'Furaffinity': 'https://www.furaffinity.net/user/vulpinecat/',
                     'Mastodon': '@praxis@vulpine.club',
                     'Steam': 'https://steamcommunity.com/id/PraxisCat/'}

        for k, v in test_dict.items():
            field = factory.get_field_for(k, v)
            assert field._KEY == k.lower()

    def test_raise_value_error_if_unknow_key(self):
        with pytest.raises(ValueError):
            factory.get_field_for("IDunno", "Lol")