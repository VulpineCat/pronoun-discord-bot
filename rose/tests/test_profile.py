import rose.profile.profile as prof
import rose.profile.fields as fields

class TestProfile(object):
    def test_profile_instantiation(self):
        profile = prof.Profile("133750022779961344")
        assert profile._id == "133750022779961344"

    def test_profile_generate_empty_profile(self):
        assert prof.Profile.generate_external_profile("123456789123456789", "Admin") == "**Profile of Admin**\n\nOh, " \
                                                                                        "there hasn't been anything " \
                                                                                        "added yet!"

    def test_profile_empty_fields(self):
        profile = prof.Profile("133750022779961344")
        assert profile.fields == dict()

    def test_profile_add_field(self):
        profile = prof.Profile("133750022779961344")
        profile.add_field("Twitter", "@real_praxis")
        field = fields.TwitterProfileField("@real_praxis")
        assert profile.fields == {'Twitter': field}

    def test_profile_add_field_overwrite(self):
        profile = prof.Profile("133750022779961344")
        profile.add_field("Twitter", "@fake_praxis")
        old_field = profile.fields["Twitter"]
        assert old_field.username == "fake_praxis"
        profile.add_field("Twitter", "@real_praxis")
        assert profile.fields["Twitter"].username != old_field.username

    def test_profile_generate_one_field(self):
        profile = prof.Profile("1")
        profile.add_field("Twitter", "@real_praxis")
        assert profile.generate_profile("Praxis") == "**Profile of Praxis**\n\nTwitter:    " \
                                                     "https://twitter.com/real_praxis\n"