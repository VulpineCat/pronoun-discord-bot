import pytest
import rose.profile.social as social


class TestProfileFields(object):
    class TestTwitterField:
        def test_twitter_url(self):
            profile_field = social.TwitterProfileField("https://twitter.com/real_praxis")
            assert profile_field.username == "real_praxis"

        def test_twitter_odd_url(self):
            profile_field = social.TwitterProfileField("https://twitter.com/real_praxis/")
            assert profile_field.username == "real_praxis"

        def test_twitter_at(self):
            profile_field = social.TwitterProfileField("@real_praxis")
            assert profile_field.username == "real_praxis"

        def test_twitter_username(self):
            profile_field = social.TwitterProfileField("real_praxis")
            assert profile_field.username == "real_praxis"

        def test_twitter_generate_url(self):
            profile_field = social.TwitterProfileField("real_praxis")
            assert profile_field.url == "https://twitter.com/real_praxis"

        def test_twitter_flavour_text(self):
            profile_field = social.TwitterProfileField("real_praxis")
            assert profile_field.flavour_text == ":bird: Tweet Tweet :bird:"

        def test_twitter_empty_input(self):
            with pytest.raises(TypeError):
                profile_field = social.TwitterProfileField()

    class TestTelegramField:
        def test_telegram_url(self):
            profile_field = social.TelegramProfileField("https://t.me/good_praxis")
            assert profile_field.username == "good_praxis"

        def test_telegram_odd_url(self):
            profile_field = social.TelegramProfileField("https://t.me/good_praxis/")
            assert profile_field.username == "good_praxis"

        def test_telegram_at(self):
            profile_field = social.TelegramProfileField("@good_praxis")
            assert profile_field.username == "good_praxis"

        def test_telegram_username(self):
            profile_field = social.TelegramProfileField("good_praxis")
            assert profile_field.username == "good_praxis"

        def test_telegram_generate_url(self):
            profile_field = social.TelegramProfileField("good_praxis")
            assert profile_field.url == "https://t.me/good_praxis"

        def test_telegram_flavour_text(self):
            profile_field = social.TelegramProfileField("good_praxis")
            assert profile_field.flavour_text == "Have fun chatting!"

        def test_telegram_empty_input(self):
            with pytest.raises(TypeError):
                profile_field = social.TelegramProfileField()

    class TestMastodonField:
        def test_mastodon_url(self):
            profile_field = social.MastodonProfileField("https://vulpine.club/@praxis")
            assert profile_field.username == "praxis"
            assert profile_field.domain == "vulpine.club"

        def test_mastodon_username_preceeding_at(self):
            profile_field = social.MastodonProfileField("@praxis@vulpine.club")
            assert profile_field.username == "praxis"
            assert profile_field.domain == "vulpine.club"
            assert profile_field.url == "https://vulpine.club/@praxis"

        def test_mastodon_username_without_preceeding_at(self):
            profile_field = social.MastodonProfileField("praxis@vulpine.club")
            assert profile_field.username == "praxis"
            assert profile_field.domain == "vulpine.club"
            assert profile_field.url == "https://vulpine.club/@praxis"

        def test_mastodon_flavour_text(self):
            profile_field = social.MastodonProfileField("praxis@vulpine.club")
            assert profile_field.flavour_text == "See you in the Fediverse!"

    class TestSteamField:
        def test_steam_id_url(self):
            profile_field = social.SteamProfileField("https://steamcommunity.com/id/PraxisCat/")
            assert profile_field.username == "PraxisCat"
            assert profile_field.domain == "id"
            assert profile_field.url == "https://steamcommunity.com/id/PraxisCat/"

        def test_steam_profiles_url(self):
            profile_field = social.SteamProfileField("https://steamcommunity.com/profiles/76561198042059463")
            assert profile_field.username == "76561198042059463"
            assert profile_field.domain == "profiles"
            assert profile_field.url == "https://steamcommunity.com/profiles/76561198042059463/"

        def test_steam_flavour_text(self):
            profile_field = social.SteamProfileField("https://steamcommunity.com/id/PraxisCat/")
            assert profile_field.flavour_text == ":joystick: Full *Steam* Ahead!\nGet it?"

    class TestOtherFields:
        def test_facebook_field(self):
            profile_field = social.FacebookProfileField("https://www.facebook.com/zuck")
            assert profile_field._KEY == "Facebook"
            assert profile_field.flavour_text == ":eyes: Mark will be watching"
            assert profile_field.username == "zuck"
            assert profile_field.url == "https://www.facebook.com/zuck"

        def test_facebook_field_long_name(self):
            profile_field = social.FacebookProfileField("https://www.facebook.com/Karl.Marx.Marxism")
            assert profile_field.username == "Karl.Marx.Marxism"
            assert profile_field.url == "https://www.facebook.com/Karl.Marx.Marxism"

        def test_tumblr_field(self):
            profile_field = social.TumblrProfileField("https://littleanimalgifs.tumblr.com/")
            assert profile_field._KEY == "Tumblr"
            assert profile_field.flavour_text == "Let's keep it rolling!"
            assert profile_field.username == "littleanimalgifs"
            assert profile_field.url == "https://littleanimalgifs.tumblr.com/"

        def test_youtube_field(self):
            profile_field = social.YoutubeProfileField("https://www.youtube.com/channel/UC6FHHzDg0lRAQ2Rw5ESNz_g")
            assert profile_field._KEY == "Youtube"
            assert profile_field.flavour_text == \
                ":play_pause: We'll get people to smash that subscribe button before long! :raised_hands:"

            assert profile_field.username == "UC6FHHzDg0lRAQ2Rw5ESNz_g"
            assert profile_field.url == "https://www.youtube.com/channel/UC6FHHzDg0lRAQ2Rw5ESNz_g"

        def test_youtube_field_with_url_parameters(self):
            profile_field = social.YoutubeProfileField(
                "https://www.youtube.com/channel/UC6FHHzDg0lRAQ2Rw5ESNz_g?view_as=subscriber")

            assert profile_field.username == "UC6FHHzDg0lRAQ2Rw5ESNz_g"

        def test_twitch_field(self):
            profile_field = social.TwitchProfileField("https://www.twitch.tv/good_praxis")
            assert profile_field._KEY == "Twitch"
            assert profile_field.flavour_text == ":play_pause: Stream On!"
            assert profile_field.username == "good_praxis"
            assert profile_field.url == "https://www.twitch.tv/good_praxis"

        def test_deviant_art_field(self):
            profile_field = social.DeviantArtProfileField("https://www.deviantart.com/spyed")
            assert profile_field._KEY == "DeviantArt"
            assert profile_field.flavour_text == "Whether :paintbrush: or :writing_hand:, we too appreciate art here~!"
            assert profile_field.username == "spyed"
            assert profile_field.url == "https://www.deviantart.com/spyed"

        def test_etsy_field(self):
            profile_field = social.EtsyProfileField("https://www.etsy.com/shop/404")
            assert profile_field._KEY == "Etsy"
            assert profile_field.flavour_text == ":money_with_wings: One of your best merch, please! :money_with_wings:"
            assert profile_field.username == "404"
            assert profile_field.url == "https://www.etsy.com/shop/404"

        def test_etsy_field_with_url_parameters(self):
            profile_field = social.EtsyProfileField("https://www.etsy.com/shop/404?ref=simple-shop-header-name&listing_id=473799330")
            assert profile_field.username == "404"

        def test_furaffinity_field(self):
            profile_field = social.FuraffinityProfileField("https://www.furaffinity.net/user/vulpinecat/")
            assert profile_field._KEY == "Furaffinity"
            assert profile_field.flavour_text == ":cat: :dog: :bird: :crocodile: uwu"
            assert profile_field.username == "vulpinecat"
            assert profile_field.url == "https://www.furaffinity.net/user/vulpinecat/"