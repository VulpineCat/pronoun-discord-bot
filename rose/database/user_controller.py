import sqlite3


class UserController:
    def __init__(self, location=":memory:"):
        self._connection = sqlite3.connect(location)

    def __del__(self):
        self._connection.close()

    @property
    def empty_changeset(self):
        return {'id': None,
                'steam': None,
                'switch': None,
                'ds': None,
                'playstation': None,
                'uplay': None,
                'origin': None,
                'xbox': None,
                'epic': None,
                'twitter': None,
                'telegram': None,
                'facebook': None,
                'tumblr': None,
                'mastodon': None,
                'youtube': None,
                'twitch': None,
                'deviantart': None,
                'etsy': None,
                'furaffinity': None
                }

    def create_user(self, id):
        cur = self._connection.cursor()
        cur.execute("INSERT INTO users(id) VALUES ({})".format(id))
        self._connection.commit()

    def read_user(self, id):
        cur = self._connection.cursor()
        cur.execute("SELECT * FROM users WHERE id={}".format(id))
        columns = [column[0] for column in cur.description]
        row = cur.fetchone()
        return self.humanize(columns, list(row))

    def update_user(self, id, changeset):
        cur = self._connection.cursor()
        for k, v in changeset.items():
            if v is None:
                continue
            cur.execute("UPDATE users SET {}='{}' WHERE id={}".format(k, v, id))
        self._connection.commit()

    @staticmethod
    def humanize(columns, row):
        return dict(zip(columns, row))