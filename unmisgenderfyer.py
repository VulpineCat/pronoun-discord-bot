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
ROLENAME_FACEBOOK = "Facebook"
ROLENAME_TUMBLR = "Tumblr"
ROLENAME_YOUTUBE = "Youtube"
ROLENAME_DA = "deviantArt"
ROLENAME_ETSY = "Etsy"
ROLENAME_FA = "FurAffinity"

# JSON
EMPTY_USER = '{"games":{"steam":null,"switch":null,"3ds":null,"psn":null,"uplay":null,"origin":null,"xbox":null,"epic":null},"social_media":{"twitter":null,"facebook":null,"tumblr":null,"youtube":null,"deviantart":null,"etsy":null,"furaffinity":null}}'
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
    await check_or_create_role(server, ROLENAME_FACEBOOK)
    await check_or_create_role(server, ROLENAME_TUMBLR)
    await check_or_create_role(server, ROLENAME_YOUTUBE)
    await check_or_create_role(server, ROLENAME_DA)
    await check_or_create_role(server, ROLENAME_ETSY)
    await check_or_create_role(server, ROLENAME_FA)

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
async def on_message(message):
    if not message.content.startswith('!'):
        return

    elif message.content == '!help' or message.content == '!list':
        await CLIENT.send_message(
            message.channel,
            ("There are three gender pronoun roles available:\n\n" +
             "`She/Her       -        assign/unassign me with !she `\n" +
             "`He/Him        -        assign/unassign me with !he  `\n" +
             "`They/Them     -        assign/unassign me with !they`\n\n\n" +
             "Anything else you need? Hit up my *owner* at VulpineCat#0001 or `hello@vulpinecat.com`\n\n" +
             "Love You\n- ***Unmisgenderfyer***"
            ))


    elif message.content == '!he':
        await add_or_remove_role(message, ROLENAME_HE)
    elif message.content == '!she':
        await add_or_remove_role(message, ROLENAME_SHE)
    elif message.content == '!they':
        await add_or_remove_role(message, ROLENAME_THEY)

    elif message.content.startswith("!addtwitter") or message.content.startswith("!at"):
        command = message.content.split(" ")
        twitter_handle = None
        
        if len(command) is not 2:
            return
        if command[1].startswith("@"):
            twitter_handle = command[1][1:]

        file = open("data.json", 'r')
        obj = json.loads(file.read())
        file.close

        obj[message.author.id]["social_media"]["twitter"] = twitter_handle

        file = open("data.json", 'w')
        json.dump(obj, file)
        file.close

        if not member_has_role(message.author, ROLENAME_TWITTER):
            await CLIENT.add_roles(message.author, grab_role(message.server, ROLENAME_TWITTER))

        await CLIENT.send_message(message.channel, ":bird: Updated your Twitter handle! :bird:")







CLIENT.run(API_TOKEN)
