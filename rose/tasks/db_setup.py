import sqlite3

def setup(name="data.db"):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE users(
        id INTEGER, 
        steam TEXT, 
        switch TEXT, 
        ds TEXT, 
        playstation TEXT, 
        uplay TEXT, 
        origin TEXT, 
        xbox TEXT, 
        epic TEXT, 
        twitter TEXT, 
        telegram TEXT, 
        facebook TEXT, 
        tumblr TEXT, 
        mastodon TEXT, 
        youtube TEXT, 
        twitch TEXT, 
        deviantart TEXT, 
        etsy TEXT, 
        furaffinity TEXT)
    ''')

    con.commit()
    con.close()
