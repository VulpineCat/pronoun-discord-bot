import pytest
import rose.profile.social as social

class TestProfileField(object):

    def test_twitter_url(self):
        twitter_profile = social.TwitterProfileField("https://twitter.com/real_praxis")
        assert twitter_profile._username == "real_praxis"

