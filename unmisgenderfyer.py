import os
import json
from pathlib import Path
import discord
from dotenv import load_dotenv

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

##############################################################################
API_TOKEN = os.getenv("API_TOKEN")

# Gender
ROLENAME_HE = "He/Him"
ROLENAME_SHE = "She/Her"
ROLENAME_THEY = "They/Them"

# Games
ROLENAME_STEAM = "Steam"
ROLENAME_SWITCH = "Nintendo Switch"
ROLENAME_3DS = "Nintendo 3DS"
ROLENAME_PSN = "Playstation Network"
ROLENAME_UPLAY = "Uplay"
ROLENAME_ORIGIN = "Origin"
ROLENAME_XBOX = "Xbox"
ROLENAME_EPIC = "Epic Games"

# Social Media
ROLENAME_TWITTER = "Twitter"
ROLENAME_TELEGRAM = "Telegram"
ROLENAME_FACEBOOK = "Facebook"
ROLENAME_TUMBLR = "Tumblr"
ROLENAME_MASTO = "Mastodon"
ROLENAME_YOUTUBE = "Youtube"
ROLENAME_TWITCH = "Twitch"
ROLENAME_DA = "deviantArt"
ROLENAME_ETSY = "Etsy"
ROLENAME_FA = "FurAffinity"


# JSON
EMPTY_USER = {"games":{"steam": None,"switch": None,"3ds": None,"psn": None,"uplay": None,"origin": None,"xbox": None,"epic": None},"social_media":{"twitter": None,"facebook": None,"tumblr": None, "mastodon": None, "youtube": None,"deviantart": None,"etsy": None,"furaffinity": None,"telegram": None,"twitch": None}}
##############################################################################

CLIENT = discord.Client()

async def check_or_create_role(server, rolename):
    found = False
    for role in server.role_hierarchy:
        if role.name == rolename:
            found = True
            break

    if not found:
        await CLIENT.create_role(server, name=rolename)

def grab_role(server, rolename):
    for role in server.role_hierarchy:
        if role.name == rolename:
            return role

async def start_or_join_routine(server):
    await check_or_create_roles(server)
    validate_users_json(server)



async def check_or_create_roles(server):
    await check_or_create_role(server, ROLENAME_HE)
    await check_or_create_role(server, ROLENAME_SHE)
    await check_or_create_role(server, ROLENAME_THEY)
    await check_or_create_role(server, ROLENAME_STEAM)
    await check_or_create_role(server, ROLENAME_SWITCH)
    await check_or_create_role(server, ROLENAME_3DS)
    await check_or_create_role(server, ROLENAME_PSN)
    await check_or_create_role(server, ROLENAME_UPLAY)
    await check_or_create_role(server, ROLENAME_ORIGIN)
    await check_or_create_role(server, ROLENAME_XBOX)
    await check_or_create_role(server, ROLENAME_EPIC)
    await check_or_create_role(server, ROLENAME_TWITTER)
    await check_or_create_role(server, ROLENAME_TELEGRAM)
    await check_or_create_role(server, ROLENAME_FACEBOOK)
    await check_or_create_role(server, ROLENAME_TUMBLR)
    await check_or_create_role(server, ROLENAME_MASTO)
    await check_or_create_role(server, ROLENAME_YOUTUBE)
    await check_or_create_role(server, ROLENAME_TWITCH)
    await check_or_create_role(server, ROLENAME_DA)
    await check_or_create_role(server, ROLENAME_ETSY)
    await check_or_create_role(server, ROLENAME_FA)

async def reset_roles(message):
    await remove_role_if_owned(message, ROLENAME_STEAM)
    await remove_role_if_owned(message, ROLENAME_SWITCH)
    await remove_role_if_owned(message, ROLENAME_3DS)
    await remove_role_if_owned(message, ROLENAME_PSN)
    await remove_role_if_owned(message, ROLENAME_UPLAY)
    await remove_role_if_owned(message, ROLENAME_ORIGIN)
    await remove_role_if_owned(message, ROLENAME_XBOX)
    await remove_role_if_owned(message, ROLENAME_EPIC)
    await remove_role_if_owned(message, ROLENAME_TWITTER)
    await remove_role_if_owned(message, ROLENAME_TELEGRAM)
    await remove_role_if_owned(message, ROLENAME_FACEBOOK)
    await remove_role_if_owned(message, ROLENAME_TUMBLR)
    await remove_role_if_owned(message, ROLENAME_MASTO)
    await remove_role_if_owned(message, ROLENAME_YOUTUBE)
    await remove_role_if_owned(message, ROLENAME_TWITCH)
    await remove_role_if_owned(message, ROLENAME_DA)
    await remove_role_if_owned(message, ROLENAME_ETSY)
    await remove_role_if_owned(message, ROLENAME_FA)

def validate_users_json(server):
    obj = None
    with open('data.json', 'r') as file:
        obj = json.loads(file.read())

    for member in server.members:
        if member.id in obj:
            continue
        else:
            obj[member.id] = EMPTY_USER
    with open('data.json', 'w') as file:
        json.dump(obj, file)



async def add_or_remove_role(message, rolename):
    if not member_has_role(message.author, rolename):
        await CLIENT.add_roles(message.author, grab_role(message.server, rolename))
        await CLIENT.send_message(message.channel, "Sucessfully added role!")
    else:
        await CLIENT.remove_roles(message.author, grab_role(message.server, rolename))
        await CLIENT.send_message(message.channel, "Sucessfully removed role!")

async def add_role_if_missing(message, role):
    if not member_has_role(message.author, role):
        await CLIENT.add_roles(message.author, grab_role(message.server, role))

async def remove_role_if_owned(message, role):
    if member_has_role(message.author, role):
        await CLIENT.remove_roles(message.author, grab_role(message.server, role))



def member_has_role(member, rolename):
    for role in member.roles:
        if role.name == rolename:
            return True
    return False


def check_for_json():
    if os.path.isfile("data.json"):
        return
    file = open("data.json", "w+")
    json.dump({}, file)
    file.close()


@CLIENT.event
async def on_ready():
    check_for_json()
    for server in CLIENT.servers:
        await start_or_join_routine(server)

@CLIENT.event
async def on_server_join(server):
    await start_or_join_routine(server)

@CLIENT.event
async def on_member_join(member):
    if not check_if_user_exists:
        reset_user(member.id)


@CLIENT.event
async def on_message(message):
    if not message.content.startswith('!'):
        return

    elif message.content == '!help' or message.content == '!list':
        await CLIENT.send_message(
            message.channel,
            ("There are three gender pronoun roles available:\n\n" +
             "`She/Her                       -        assign/unassign me with !she `\n" +
             "`He/Him                        -        assign/unassign me with !he  `\n" +
             "`They/Them                     -        assign/unassign me with !they`\n\n\n" +
             "`!profile` will display your own bot profile `!profile @user` will display theirs!\n" +
             "You can add the following game services to your bot profile:\n\n" +
             "`Steam                         -        add the url to your profile with !addsteam or !as`\n" +
             "`Switch                        -        add your friendscode with !addswitch or !ans`\n" +
             "`3DS                           -        add your friendscode with !add3ds or !a3`\n" +
             "`Playstation Network           -        add your PSN-ID with !addpsn or !aps`\n" +
             "`Uplay                         -        add your Uplay username with !adduplay or !au`\n" +
             "`Origin                        -        add your Origin username with !addorigin or !ao`\n"))
        await CLIENT.send_message(
            message.channel,
            ("`Xbox                          -        add your Gamertag with !addxbox or !ax`\n" +
             "`Epic Games                    -        add your Epic Games username with !addepic or !aep`\n\n\n" +
             "You can also add a few of your social media handles:\n\n" +
             "`Twitter                       -        add your twitter username or url via !addtwitter or !atw`\n" +
             "`Telegram                      -        add your telegram handle or url via !addtelegram or !atg`\n" +
             "`Facebook                      -        add your facebook profile !addfacebook or !afb`\n" +
             "`Tumblr                        -        add your tumblr blog with !addtumblr`\n" +
             "`Mastodon                      -        add your mastodon with instance with !addmasto or !ama`\n" +
             "`Youtube                       -        add your channel with !addyoutube or !ayt`\n" +
             "`Twitch                        -        add your stream with !addtwitch`\n" +
             "`deviantArt                    -        add your dA page via !adddeviant or !ada`\n" +
             "`Etsy                          -        add your Etsy Store with !addetsy or !aet`\n" +
             "`FurAffinity                   -        add your sins via !addfur or !afa`\n\n\n" +
             "To delete any entry type `!del[command]`, so for example `!delsteam` or `!delfur`. `!dfb` also works to delete facebook, and so on.\n" +
             "`!delall` will delete your **entire** profile!\n\n\n" +
             "Anything else you need? Hit up my *owner* at VulpineCat#0001 or `hello@vulpinecat.com`\n\n" +
             "Love You\n- ***Unmisgenderfyer***"
            ))

    elif message.content == '!he':
        await add_or_remove_role(message, ROLENAME_HE)
    elif message.content == '!she':
        await add_or_remove_role(message, ROLENAME_SHE)
    elif message.content == '!they':
        await add_or_remove_role(message, ROLENAME_THEY)

    elif message.content.startswith("!profile"):
        command = message.content.split(" ")
        obj = None
        user = None
        message_buffer = None

        if len(command) > 2:
            return

        if len(command) == 1:
            obj = get_json_for_user(message.author)
            user = message.author
        if len(command) == 2 and message.mentions:
            obj = get_json_for_user(message.mentions[0])
            user = message.mentions[0]

        if not obj:
            await CLIENT.send_message(
                message.channel,
                ("Weird, I can't seem to find this user in my data... :robot:"))
            return

        message_buffer = "***Profile of " + user.name + "***"

        message_buffer += "\n**Game Accounts**:\n"

        has_game_account = False
        if obj["games"]["steam"]:
            has_game_account = True
            message_buffer += "Steam: " + obj["games"]["steam"] + "\n"

        if obj["games"]["switch"]:
            has_game_account = True
            message_buffer += "Nintendo Switch FC: `" + obj["games"]["switch"] + "`\n"

        if obj["games"]["3ds"]:
            has_game_account = True
            message_buffer += "Nintendo 3DS FC: `" + obj["games"]["3ds"] + "`\n"

        if obj["games"]["psn"]:
            has_game_account = True
            message_buffer += "Playstation Network tag: `" + obj["games"]["psn"] + "`\n"

        if obj["games"]["uplay"]:
            has_game_account = True
            message_buffer += "Uplay Username: `" + obj["games"]["uplay"] + "`\n"

        if obj["games"]["origin"]:
            has_game_account = True
            message_buffer += "Origin Username: `" + obj["games"]["origin"] + "`\n"

        if obj["games"]["xbox"]:
            has_game_account = True
            message_buffer += "Xbox Gamertag: `" + obj["games"]["xbox"] + "`\n"

        if obj["games"]["epic"]:
            has_game_account = True
            message_buffer += "Epic Games Username: `" + obj["games"]["epic"] + "`\n"

        if not has_game_account:
            message_buffer += "Seems like they don't have any games account added! \n\n"
        else:
            message_buffer += "\n"


        message_buffer += "**Social Media**:\n"


        has_social_media_account = False
        if obj["social_media"]["twitter"]:
            has_social_media_account = True
            message_buffer += "Twitter: https://www.twitter.com/" + obj["social_media"]["twitter"] + "\n"

        if obj["social_media"]["telegram"]:
            has_social_media_account = True
            message_buffer += "Telegram: https://t.me/" + obj["social_media"]["telegram"] + "\n"

        if obj["social_media"]["facebook"]:
            has_social_media_account = True
            message_buffer += "Facebook: " + obj["social_media"]["facebook"] + "\n"

        if obj["social_media"]["tumblr"]:
            has_social_media_account = True
            message_buffer += "Tumblr: https://" + obj["social_media"]["tumblr"] + ".tumblr.com\n"

        if obj["social_media"]["mastodon"]:
            has_social_media_account = True
            message_buffer += "Mastodon: " + obj["social_media"]["tumblr"]

        if obj["social_media"]["youtube"]:
            has_social_media_account = True
            message_buffer += "Youtube Channel: " + obj["social_media"]["youtube"] + "\n"

        if obj["social_media"]["twitch"]:
            has_social_media_account = True
            message_buffer += "Twitch: https://www.twitch.tv/" + obj["social_media"]["twitch"] + "\n"

        if obj["social_media"]["deviantart"]:
            has_social_media_account = True
            message_buffer += "deviantArt: https://" + obj["social_media"]["deviantart"] + ".deviantart.com\n"

        if obj["social_media"]["etsy"]:
            has_social_media_account = True
            message_buffer += "Etsy Store: " + obj["social_media"]["etsy"] + "\n"

        if obj["social_media"]["furaffinity"]:
            has_social_media_account = True
            message_buffer += "FurAffinity: https://www.furaffinity.net/user/" + obj["social_media"]["furaffinity"] + "\n"

        if not has_game_account and not has_social_media_account:
            message_buffer = "Sorry, this user doesn't have a profile yet!"
        elif not has_social_media_account:
            message_buffer += "Seems like they didn't set up their social media handles! \n\n"


        await CLIENT.send_message(message.channel, message_buffer)





    elif message.content.startswith("!addsteam") or message.content.startswith("!as"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "games", "steam", command[1])
        await add_role_if_missing(message, ROLENAME_STEAM)

        await CLIENT.send_message(message.channel, ":joystick: Full *Steam* Ahead!\nGet it?")

    elif message.content.startswith("!addswitch") or message.content.startswith("!ans"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "games", "switch", command[1])
        await add_role_if_missing(message, ROLENAME_SWITCH)

        await CLIENT.send_message(message.channel, ":joy: :spy: Get it? It's a ***joy con***")

    elif message.content.startswith("!add3") or message.content.startswith("!a3"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "games", "3ds", command[1])
        await add_role_if_missing(message, ROLENAME_3DS)

        await CLIENT.send_message(message.channel, "Happy Gaming!")

    elif message.content.startswith("!addpsn") or message.content.startswith("!aps"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "games", "psn", command[1])
        await add_role_if_missing(message, ROLENAME_PSN)

        await CLIENT.send_message(message.channel, "BE MOVED")

    elif message.content.startswith("!addu") or message.content.startswith("!au"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "games", "uplay", command[1])
        await add_role_if_missing(message, ROLENAME_UPLAY)

        await CLIENT.send_message(message.channel, "Glad to have your username there! ~~At least it's not origin!~~")

    elif message.content.startswith("!addo") or message.content.startswith("!ao"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "games", "origin", command[1])
        await add_role_if_missing(message, ROLENAME_ORIGIN)

        await CLIENT.send_message(message.channel, "Glad to have your username there! ~~At least it's not uplay!~~")

    elif message.content.startswith("!addx") or message.content.startswith("!ax"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "games", "xbox", command[1])
        await add_role_if_missing(message, ROLENAME_XBOX)

        await CLIENT.send_message(message.channel, "added your :regional_indicator_x::regional_indicator_b::regional_indicator_o::negative_squared_cross_mark:!")

    elif message.content.startswith("!addep") or message.content.startswith("!aep"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "games", "epic", command[1])
        await add_role_if_missing(message, ROLENAME_EPIC)

        await CLIENT.send_message(message.channel, "What do ya say? Fortnite 2nite?")


    elif message.content.startswith("!addtwitter") or message.content.startswith("!atw"):
        command = message.content.split(" ")
        twitter_handle = None

        if len(command) != 2:
            return

        if message.mentions:
            twitter_handle = message.author.name
        elif command[1].startswith("@"):
            twitter_handle = command[1][1:]
        elif command[1].startswith("http"):
            twitter_handle = command[1].split("/")[-1]
        else:
            twitter_handle = command[1]

        write_to_json(message.author.id, "social_media", "twitter", twitter_handle)
        await add_role_if_missing(message, ROLENAME_TWITTER)

        await CLIENT.send_message(message.channel, ":bird: Updated your Twitter handle! :bird:")

    elif message.content.startswith("!addtelegram") or message.content.startswith("!atg"):
        command = message.content.split(" ")
        telegram_handle = None

        if len(command) != 2:
            return

        if message.mentions:
            telegram_handle = message.author.name
        elif command[1].startswith("@"):
            telegram_handle = command[1][1:]
        elif command[1].startswith("http"):
            telegram_handle = command[1].split("/")[-1]
        else:
            telegram_handle = command[1]

        write_to_json(message.author.id, "social_media", "telegram", telegram_handle)
        await add_role_if_missing(message, ROLENAME_TELEGRAM)

        await CLIENT.send_message(message.channel, "Have fun chatting!")

    elif message.content.startswith("!addfacebook") or message.content.startswith("!afb"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "social_media", "facebook", command[1])
        await add_role_if_missing(message, ROLENAME_FACEBOOK)

        await CLIENT.send_message(message.channel, ":eyes: Mark will be watching")

    elif message.content.startswith("!addtumblr"):
        command = message.content.split(" ")
        username = None

        if len(command) != 2:
            return

        if command[1].startswith("http"):
            var = command[1].split("/")
            username = var.split(".")[0]
        else:
            username = command[1]

        write_to_json(message.author.id, "social_media", "tumblr", username)
        await add_role_if_missing(message, ROLENAME_TUMBLR)

        await CLIENT.send_message(message.channel, "Sorry, I don't really use Tumblr, so I don't have anything witty to say. Sucessfully saved!")

    elif message.content.startswith("!addmasto") or message.content.startswith("!ama"):
        command = message.content.split(" ")
        username = None

        if len(command) != 2:
            return

        username = command[1]

        write_to_json(message.author.id, "social_media", "mastodon", username)
        await add_role_if_missing(message, ROLENAME_MASTO)

        await CLIENT.send_message(message.channel, "See you in the Fediverse!")


    elif message.content.startswith("!addyoutube") or message.content.startswith("!ayt"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "social_media", "youtube", command[1])
        await add_role_if_missing(message, ROLENAME_YOUTUBE)

        await CLIENT.send_message(message.channel, ":play_pause: We'll get people to smash that subscribe button before long! :raised_hands:")

    elif message.content.startswith("!addtwitch"):
        command = message.content.split(" ")
        username = None

        if len(command) != 2:
            return

        if command[1].startswith("http"):
            username = command[1].split("/")[-1]
        else:
            username = command[1]

        write_to_json(message.author.id, "social_media", "twitch", username)
        await add_role_if_missing(message, ROLENAME_TWITCH)

        await CLIENT.send_message(message.channel, ":play_pause: Stream On!")

    elif message.content.startswith("!adddeviant") or message.content.startswith("!ada"):
        command = message.content.split(" ")
        username = None

        if len(command) != 2:
            return

        if command[1].startswith("http"):
            var = command[1].split("/")
            username = var.split(".")[0]
        else:
            username = command[1]


        write_to_json(message.author.id, "social_media", "deviantart", username)
        await add_role_if_missing(message, ROLENAME_DA)

        await CLIENT.send_message(message.channel, "Whether :paintbrush: or :writing_hand:, we too appreciate art here~!")

    elif message.content.startswith("!addetsy") or message.content.startswith("!aet"):
        command = message.content.split(" ")

        if len(command) != 2:
            return

        write_to_json(message.author.id, "social_media", "etsy", command[1])
        await add_role_if_missing(message, ROLENAME_ETSY)

        await CLIENT.send_message(message.channel, ":money_with_wings: One of your best merch, please! :money_with_wings:")

    elif message.content.startswith("!addfur") or message.content.startswith("!afa"):
        command = message.content.split(" ")
        username = None

        if len(command) != 2:
            return

        if command[1].startswith("http"):
            username = command[1].split("/")[-2]
        else:
            username = command[1]

        write_to_json(message.author.id, "social_media", "furaffinity", username)
        await add_role_if_missing(message, ROLENAME_FA)

        await CLIENT.send_message(message.channel, ":cat: :dog: :bird: :crocodile: uwu")



    elif message.content.startswith("!delsteam") or message.content.startswith("!ds"):
        write_to_json(message.author.id, "games", "steam", None)
        await remove_role_if_owned(message, ROLENAME_STEAM)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delswitch") or message.content.startswith("!dns"):
        write_to_json(message.author.id, "games", "switch", None)
        await remove_role_if_owned(message, ROLENAME_SWITCH)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!del3") or message.content.startswith("!d3"):
        write_to_json(message.author.id, "games", "3ds", None)
        await remove_role_if_owned(message, ROLENAME_3DS)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delpsn") or message.content.startswith("!dps"):
        write_to_json(message.author.id, "games", "psn", None)
        await remove_role_if_owned(message, ROLENAME_PSN)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delu") or message.content.startswith("!du"):
        write_to_json(message.author.id, "games", "uplay", None)
        await remove_role_if_owned(message, ROLENAME_UPLAY)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")


    elif message.content.startswith("!delo") or message.content.startswith("!do"):
        write_to_json(message.author.id, "games", "origin", None)
        await remove_role_if_owned(message, ROLENAME_ORIGIN)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delx") or message.content.startswith("!dx"):
        write_to_json(message.author.id, "games", "xbox", None)
        await remove_role_if_owned(message, ROLENAME_XBOX)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delep") or message.content.startswith("!dep"):
        write_to_json(message.author.id, "games", "epic", None)
        await remove_role_if_owned(message, ROLENAME_EPIC)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")


    elif message.content.startswith("!deltwitter") or message.content.startswith("!dtw"):
        write_to_json(message.author.id, "social_media", "twitter", None)
        await remove_role_if_owned(message, ROLENAME_TWITTER)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!deltelegram") or message.content.startswith("!dtg"):
        write_to_json(message.author.id, "social_media", "telegram", None)
        await remove_role_if_owned(message, ROLENAME_TELEGRAM)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delfacebook") or message.content.startswith("!dfb"):
        write_to_json(message.author.id, "social_media", "facebook", None)
        await remove_role_if_owned(message, ROLENAME_TWITTER)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!deltumblr"):
        write_to_json(message.author.id, "social_media", "tumblr", None)
        await remove_role_if_owned(message, ROLENAME_TUMBLR)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delmasto") or message.content.startswith("!dma"):
        write_to_json(message.author.id, "social_media", "mastodon", None)
        await remove_role_if_owned(message, ROLENAME_MASTO)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")


    elif message.content.startswith("!delyoutube") or message.content.startswith("!dyt"):
        write_to_json(message.author.id, "social_media", "youtube", None)
        await remove_role_if_owned(message, ROLENAME_YOUTUBE)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!deltwitch"):
        write_to_json(message.author.id, "social_media", "twitch", None)
        await remove_role_if_owned(message, ROLENAME_TWITCH)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!deldeviant") or message.content.startswith("!dda"):
        write_to_json(message.author.id, "social_media", "deviantart", None)
        await remove_role_if_owned(message, ROLENAME_DA)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!deletsy") or message.content.startswith("!det"):
        write_to_json(message.author.id, "social_media", "etsy", None)
        await remove_role_if_owned(message, ROLENAME_ETSY)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delfur") or message.content.startswith("!dfa"):
        write_to_json(message.author.id, "social_media", "furaffinity", None)
        await remove_role_if_owned(message, ROLENAME_FA)

        await CLIENT.send_message(message.channel, "Sucessfully deleted that entry!")

    elif message.content.startswith("!delall"):
        reset_user(message.author.id)
        await reset_roles(message)

        await CLIENT.send_message(message.channel, "Deleted your entire profile!")

    elif message.content.startswith("!showall"):
        command = message.content.split(" ")
        social_media = [key for key in EMPTY_USER["social_media"]]
        games = [key for key in EMPTY_USER["games"]]
        possible_commands = social_media + games

        TWITTER_URL = "https://www.twitter.com/"
        TWITCH_URL = "https://www.twitch.tv/"
        TELEGRAM_URL = "https://t.me/"
        FUR_URL = "https://www.furaffinity.net/user/"
        HT = "https://"


        if len(command) == 1:
            await CLIENT.send_message(message.channel, "The following roles are available: " + ", ".join(possible_commands))
        elif len(command) == 2:
            if command[1] in possible_commands:
                message_buffer = ""
                container = None
                if command[1] in games:
                    container = "games"
                else:
                    container = "social_media"
                for member in message.server.members:
                    if get_json_for_user(member)[container][command[1]]:
                        if(command[1] == "twitter"):
                            message_buffer += member.name + ": " + TWITTER_URL + get_json_for_user(member)[container][command[1]] + "\n"
                        elif(command[1] == "twitch"):
                            message_buffer += member.name + ": " + TWITCH_URL + get_json_for_user(member)[container][command[1]] + "\n"
                        elif(command[1] == "telegram"):
                            message_buffer += member.name + ": " + TELEGRAM_URL + get_json_for_user(member)[container][command[1]] + "\n"
                        elif(command[1] == "furaffinity"):
                            message_buffer += member.name + ": " + FUR_URL + get_json_for_user(member)[container][command[1]] + "\n"
                        elif(command[1] == "deviantart"):
                            message_buffer += member.name + ": " + HT + get_json_for_user(member)[container][command[1]] + ".deviantart.com\n"
                        elif(command[1] == "tumblr"):
                            message_buffer += member.name + ": " + HT + get_json_for_user(member)[container][command[1]] + ".tumblr.com\n"
                        else:
                            message_buffer += member.name + ": " + get_json_for_user(member)[container][command[1]] + "\n"
                if message_buffer == "":
                    await CLIENT.send_message(message.channel, "None of the users have this key!")
                else:
                    await CLIENT.send_message(message.channel, message_buffer)

            else:
                await CLIENT.send_message(message.channel, "Key not recognized!")





def write_to_json(user, container, service, value):
    file = open("data.json", 'r')
    obj = json.loads(file.read())
    file.close()

    obj[user][container][service] = value


    file = open("data.json", 'w')
    json.dump(obj, file)
    file.close()

def reset_user(user):
    file = open("data.json", 'r')
    obj = json.loads(file.read())
    file.close()

    obj[user] = EMPTY_USER

    file = open("data.json", 'w')
    json.dump(obj, file)
    file.close()

def get_json_for_user(user):
    file = open("data.json", 'r')
    obj = json.loads(file.read())
    file.close()

    return obj[user.id]

def check_if_user_exists(user):
    file = open("data.json", 'r')
    obj = json.loads(file.read())
    file.close()

    return user.id in obj





CLIENT.run(API_TOKEN)
