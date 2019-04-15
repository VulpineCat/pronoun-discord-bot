import pytest
import rose.profile.social as social

class TestProfileField(object):

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