import pytest
from rose.profile import fields


class TestProfileFields(object):
    class TestTwitterField:
        def test_twitter_url(self):
            profile_field = fields.TwitterProfileField("https://twitter.com/real_praxis")
            assert profile_field.username == "real_praxis"

        def test_twitter_odd_url(self):
            profile_field = fields.TwitterProfileField("https://twitter.com/real_praxis/")
            assert profile_field.username == "real_praxis"

        def test_twitter_at(self):
            profile_field = fields.TwitterProfileField("@real_praxis")
            assert profile_field.username == "real_praxis"

        def test_twitter_username(self):
            profile_field = fields.TwitterProfileField("real_praxis")
            assert profile_field.username == "real_praxis"

        def test_twitter_generate_url(self):
            profile_field = fields.TwitterProfileField("real_praxis")
            assert profile_field.url == "https://twitter.com/real_praxis"

        def test_twitter_flavour_text(self):
            profile_field = fields.TwitterProfileField("real_praxis")
            assert profile_field.flavour_text == ":bird: Tweet Tweet :bird:"

        def test_twitter_empty_input(self):
            with pytest.raises(TypeError):
                profile_field = fields.TwitterProfileField()

    class TestTelegramField:
        def test_telegram_url(self):
            profile_field = fields.TelegramProfileField("https://t.me/good_praxis")
            assert profile_field.username == "good_praxis"

        def test_telegram_odd_url(self):
            profile_field = fields.TelegramProfileField("https://t.me/good_praxis/")
            assert profile_field.username == "good_praxis"

        def test_telegram_at(self):
            profile_field = fields.TelegramProfileField("@good_praxis")
            assert profile_field.username == "good_praxis"

        def test_telegram_username(self):
            profile_field = fields.TelegramProfileField("good_praxis")
            assert profile_field.username == "good_praxis"

        def test_telegram_generate_url(self):
            profile_field = fields.TelegramProfileField("good_praxis")
            assert profile_field.url == "https://t.me/good_praxis"

        def test_telegram_flavour_text(self):
            profile_field = fields.TelegramProfileField("good_praxis")
            assert profile_field.flavour_text == "Have fun chatting!"

        def test_telegram_empty_input(self):
            with pytest.raises(TypeError):
                profile_field = fields.TelegramProfileField()

    class TestMastodonField:
        def test_mastodon_url(self):
            profile_field = fields.MastodonProfileField("https://vulpine.club/@praxis")
            assert profile_field.username == "praxis"
            assert profile_field.domain == "vulpine.club"

        def test_mastodon_username_preceeding_at(self):
            profile_field = fields.MastodonProfileField("@praxis@vulpine.club")
            assert profile_field.username == "praxis"
            assert profile_field.domain == "vulpine.club"
            assert profile_field.url == "https://vulpine.club/@praxis"

        def test_mastodon_username_without_preceeding_at(self):
            profile_field = fields.MastodonProfileField("praxis@vulpine.club")
            assert profile_field.username == "praxis"
            assert profile_field.domain == "vulpine.club"
            assert profile_field.url == "https://vulpine.club/@praxis"

        def test_mastodon_flavour_text(self):
            profile_field = fields.MastodonProfileField("praxis@vulpine.club")
            assert profile_field.flavour_text == "See you in the Fediverse!"
            assert profile_field._KEY == "Mastodon"

    class TestSteamField:
        def test_steam_id_url(self):
            profile_field = fields.SteamProfileField("https://steamcommunity.com/id/PraxisCat/")
            assert profile_field.username == "PraxisCat"
            assert profile_field.domain == "id"
            assert profile_field.url == "https://steamcommunity.com/id/PraxisCat/"

        def test_steam_profiles_url(self):
            profile_field = fields.SteamProfileField("https://steamcommunity.com/profiles/76561198042059463")
            assert profile_field.username == "76561198042059463"
            assert profile_field.domain == "profiles"
            assert profile_field.url == "https://steamcommunity.com/profiles/76561198042059463/"

        def test_steam_flavour_text(self):
            profile_field = fields.SteamProfileField("https://steamcommunity.com/id/PraxisCat/")
            assert profile_field.flavour_text == """:joystick: Full *Steam* Ahead!\nGet it?"""
            assert profile_field._KEY == "Steam"

    class TestOtherFields:
        def test_facebook_field(self):
            profile_field = fields.FacebookProfileField("https://www.facebook.com/zuck")
            assert profile_field._KEY == "Facebook"
            assert profile_field.flavour_text == ":eyes: Mark will be watching"
            assert profile_field.username == "zuck"
            assert profile_field.url == "https://www.facebook.com/zuck"

        def test_facebook_field_long_name(self):
            profile_field = fields.FacebookProfileField("https://www.facebook.com/Karl.Marx.Marxism")
            assert profile_field.username == "Karl.Marx.Marxism"
            assert profile_field.url == "https://www.facebook.com/Karl.Marx.Marxism"

        def test_tumblr_field(self):
            profile_field = fields.TumblrProfileField("https://littleanimalgifs.tumblr.com/")
            assert profile_field._KEY == "Tumblr"
            assert profile_field.flavour_text == "Let's keep it rolling!"
            assert profile_field.username == "littleanimalgifs"
            assert profile_field.url == "https://littleanimalgifs.tumblr.com/"

        def test_youtube_field(self):
            profile_field = fields.YoutubeProfileField("https://www.youtube.com/channel/UC6FHHzDg0lRAQ2Rw5ESNz_g")
            assert profile_field._KEY == "Youtube"
            assert profile_field.flavour_text == \
                ":play_pause: We'll get people to smash that subscribe button before long! :raised_hands:"

            assert profile_field.username == "UC6FHHzDg0lRAQ2Rw5ESNz_g"
            assert profile_field.url == "https://www.youtube.com/channel/UC6FHHzDg0lRAQ2Rw5ESNz_g"

        def test_youtube_field_with_url_parameters(self):
            profile_field = fields.YoutubeProfileField(
                "https://www.youtube.com/channel/UC6FHHzDg0lRAQ2Rw5ESNz_g?view_as=subscriber")

            assert profile_field.username == "UC6FHHzDg0lRAQ2Rw5ESNz_g"

        def test_twitch_field(self):
            profile_field = fields.TwitchProfileField("https://www.twitch.tv/good_praxis")
            assert profile_field._KEY == "Twitch"
            assert profile_field.flavour_text == ":play_pause: Stream On!"
            assert profile_field.username == "good_praxis"
            assert profile_field.url == "https://www.twitch.tv/good_praxis"

        def test_deviant_art_field(self):
            profile_field = fields.DeviantArtProfileField("https://www.deviantart.com/spyed")
            assert profile_field._KEY == "DeviantArt"
            assert profile_field.flavour_text == "Whether :paintbrush: or :writing_hand:, we too appreciate art here~!"
            assert profile_field.username == "spyed"
            assert profile_field.url == "https://www.deviantart.com/spyed"

        def test_etsy_field(self):
            profile_field = fields.EtsyProfileField("https://www.etsy.com/shop/404")
            assert profile_field._KEY == "Etsy"
            assert profile_field.flavour_text == ":money_with_wings: One of your best merch, please! :money_with_wings:"
            assert profile_field.username == "404"
            assert profile_field.url == "https://www.etsy.com/shop/404"

        def test_etsy_field_with_url_parameters(self):
            profile_field = fields.EtsyProfileField("https://www.etsy.com/shop/404?ref=simple-shop-header-name&listing_id=473799330")
            assert profile_field.username == "404"

        def test_furaffinity_field(self):
            profile_field = fields.FuraffinityProfileField("https://www.furaffinity.net/user/vulpinecat/")
            assert profile_field._KEY == "Furaffinity"
            assert profile_field.flavour_text == ":cat: :dog: :bird: :crocodile: uwu"
            assert profile_field.username == "vulpinecat"
            assert profile_field.url == "https://www.furaffinity.net/user/vulpinecat/"

        def test_switch_field(self):
            profile_field = fields.SwitchProfileField("SW-0000-0000-0000")
            assert profile_field._KEY == "Switch"
            assert profile_field.flavour_text == ":joy: :spy: Get it? It's a ***joy con***"
            assert profile_field.username == "SW-0000-0000-0000"

        def test_3ds_field(self):
            profile_field = fields.DSProfileField("0000-0000-0000")
            assert profile_field._KEY == "3DS"
            assert profile_field.flavour_text == "Happy Gaming!"
            assert profile_field.username == "0000-0000-0000"

        def test_playstation_field(self):
            profile_field = fields.PlaystationProfileField("username")
            assert profile_field._KEY == "Playstation"
            assert profile_field.flavour_text == "BE MOVED"
            assert profile_field.username == "username"

        def test_xbox_field(self):
            profile_field = fields.XBoxProfileField("username")
            assert profile_field._KEY == "XBox"
            assert profile_field.flavour_text == "added your :regional_indicator_x::regional_indicator_b:" \
                                                 ":regional_indicator_o::negative_squared_cross_mark:!"
            assert profile_field.username == "username"

        def test_ubisoft_field(self):
            profile_field = fields.UbisoftProfileField("Good_Praxis")
            assert profile_field._KEY == "Ubisoft"
            assert profile_field.flavour_text == "Glad to have your username there! ~~At least it's not origin!~~"
            assert profile_field.username == "Good_Praxis"

        def test_origin_field(self):
            profile_field = fields.OriginProfileField("ComradePraxis")
            assert profile_field._KEY == "Origin"
            assert profile_field.flavour_text == "Glad to have your username there! ~~At least it's not uplay!~~"
            assert profile_field.username == "ComradePraxis"

        def test_epic_field(self):
            profile_field = fields.EpicProfileField("GoodPraxis")
            assert profile_field._KEY == "Epic"
            assert profile_field.flavour_text == "What do ya say? Fortnite 2nite?"
            assert profile_field.username == "GoodPraxis"