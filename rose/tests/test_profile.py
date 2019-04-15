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

