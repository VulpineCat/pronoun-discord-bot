import rose.profile.field_factory as factory

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
    def generate_profile(id, username):
        profile = Profile(id)
        if profile.fields:
            return "ERROR"
        else:
            return "Profile of {}\n\nOh, there hasn't been anything added yet!".format(username)

    def add_field(self, key, value):
        self._fields[key] = (factory.get_field_for(key, value))
