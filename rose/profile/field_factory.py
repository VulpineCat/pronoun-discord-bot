from rose.profile import fields


def get_field_for(key, value):
    if key == "Twitter":
        return fields.TwitterProfileField(value)
    elif key == "Switch":
        return fields.SwitchProfileField(value)
    elif key == "3DS":
        return fields.DSProfileField(value)
    elif key == "Playstation":
        return fields.PlaystationProfileField(value)
    elif key == "XBox":
        return fields.XBoxProfileField(value)
    elif key == "Ubisoft":
        return fields.UbisoftProfileField(value)
    elif key == "Origin":
        return fields.OriginProfileField(value)
    elif key == "Epic":
        return fields.EpicProfileField(value)
    elif key == "Telegram":
        return fields.TelegramProfileField(value)
    elif key == "Facebook":
        return fields.FacebookProfileField(value)
    elif key == "Tumblr":
        return fields.TumblrProfileField(value)
    elif key == "Youtube":
        return fields.YoutubeProfileField(value)
    elif key == "Twitch":
        return fields.TwitchProfileField(value)
    elif key == "DeviantArt":
        return fields.DeviantArtProfileField(value)
    elif key == "Etsy":
        return fields.EtsyProfileField(value)
    elif key == "Furaffinity":
        return fields.FuraffinityProfileField(value)
    elif key == "Mastodon":
        return fields.MastodonProfileField(value)
    elif key == "Steam":
        return fields.SteamProfileField(value)
    else:
        raise ValueError
