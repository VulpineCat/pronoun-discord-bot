import pytest
import rose.profile.social as social


class TestProfileFields(object):
    class TestTwitterField:
        def test_twitter_url(self):
            twitter_profile = social.TwitterProfileField("https://twitter.com/real_praxis")
            assert twitter_profile.username == "real_praxis"

        def test_twitter_odd_url(self):
            twitter_profile = social.TwitterProfileField("https://twitter.com/real_praxis/")
            assert twitter_profile.username == "real_praxis"

        def test_twitter_at(self):
            twitter_profile = social.TwitterProfileField("@real_praxis")
            assert twitter_profile.username == "real_praxis"

        def test_twitter_username(self):
            twitter_profile = social.TwitterProfileField("real_praxis")
            assert twitter_profile.username == "real_praxis"

        def test_twitter_generate_url(self):
            twitter_profile = social.TwitterProfileField("real_praxis")
            assert twitter_profile.url == "https://twitter.com/real_praxis"

        def test_twitter_flavour_text(self):
            twitter_profile = social.TwitterProfileField("real_praxis")
            assert twitter_profile.flavour_text == ":bird: Tweet Tweet :bird:"

        def test_twitter_empty_input(self):
            with pytest.raises(TypeError):
                twitter_profile = social.TwitterProfileField()

    class TestTelegramField:
        def test_telegram_url(self):
            telegram_profile = social.TelegramProfileField("https://t.me/good_praxis")
            assert telegram_profile.username == "good_praxis"

        def test_telegram_odd_url(self):
            telegram_profile = social.TelegramProfileField("https://t.me/good_praxis/")
            assert telegram_profile.username == "good_praxis"

        def test_telegram_at(self):
            telegram_profile = social.TelegramProfileField("@good_praxis")
            assert telegram_profile.username == "good_praxis"

        def test_telegram_username(self):
            telegram_profile = social.TelegramProfileField("good_praxis")
            assert telegram_profile.username == "good_praxis"

        def test_telegram_generate_url(self):
            telegram_profile = social.TelegramProfileField("good_praxis")
            assert telegram_profile.url == "https://t.me/good_praxis"

        def test_telegram_flavour_text(self):
            telegram_profile = social.TelegramProfileField("good_praxis")
            assert telegram_profile.flavour_text == "Have fun chatting!"

        def test_telegram_empty_input(self):
            with pytest.raises(TypeError):
                telegram_profile = social.TelegramProfileField()

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
