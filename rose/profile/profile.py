import rose.profile.field_factory as factory
from rose.profile.fields import ProfileField

class Profile:
    def __init__(self, id):
        self._id = id
        self._fields = dict()

    @property
    def fields(self):
        """returns a set of all profile field objects"""
        return self._fields

    @fields.getter
    def fields(self):
        return self._fields

    @staticmethod
    def generate_external_profile(id, username):
        profile = Profile(id)
        return profile.generate_profile(username)

    def generate_profile(self, username):
        if self._fields:
            ret = ["{}:    {}\n".format(k, v.url) if isinstance(v, ProfileField) else
                   "{}:    {}\n".format(k, v.username) for k, v in self._fields.items()]
            ret.sort()
            return self.profile_header(username) + "".join(ret)

        else:
            return self.profile_header(username) + "Oh, there hasn't been anything added yet!"

    def profile_header(self, username):
        return "**Profile of {}**\n\n".format(username)

    def add_field(self, key, value):
        self._fields[key] = (factory.get_field_for(key, value))
