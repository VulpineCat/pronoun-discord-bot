import pytest
import rose.profile.social as social

class TestProfileField(object):

    def test_twitter_url(self):
        twitter_profile = social.TwitterProfileField("https://twitter.com/real_praxis")
        assert twitter_profile.username == "real_praxis"

    def test_twitter_at(selfs):
        twitter_profile = social.TwitterProfileField("@real_praxis")
        assert twitter_profile.username == "real_praxis"

    def test_twitter_username(self):
        twitter_profile = social.TwitterProfileField("real_praxis")
        assert twitter_profile.username == "real_praxis"

