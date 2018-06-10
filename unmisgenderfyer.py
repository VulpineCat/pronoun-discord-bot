import os
from pathlib import Path
import discord
from dotenv import load_dotenv

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

API_TOKEN = os.getenv("API_TOKEN")

ROLENAME_HE = "He/Him"
ROLENAME_SHE = "She/Her"
ROLENAME_THEY = "They/Them"


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
    await check_or_create_role(server, ROLENAME_HE)
    await check_or_create_role(server, ROLENAME_SHE)
    await check_or_create_role(server, ROLENAME_THEY)

async def add_or_remove_role(message, rolename):
    if member_has_role(message.author, rolename):
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


@CLIENT.event
async def on_ready():
    for server in CLIENT.servers:
        await start_or_join_routine(server)

@CLIENT.event
async def on_server_join(server):
        await start_or_join_routine(server)

@CLIENT.event
async def on_message(message):
    if not message.content.startswith('!'):
        return

    elif message.content.startswith('!help') or message.content.startswith('!list'):
        await CLIENT.send_message(
            message.channel,
            ("There are three gender pronoun roles available:\n\n" +
             "`She/Her`      -        assign/unassign me with `!she`\n" +
             "`He/Him`       -        assign/unassign me with `!he`\n" +
             "`They/Them`    -        assign/unassign me with `!they`\n\n\n" +
             "Anything else you need? Hit up my **owner** at VulpineCat#0001 or `hello@vulpinecat.com`\n\n" +
             "Love You\n- ***Unmisgenderfyer**"
            ))


    elif message.content.startswith('!he'):
        await add_or_remove_role(message, ROLENAME_HE)
    elif message.content.startswith('!she'):
        await add_or_remove_role(message, ROLENAME_SHE)
    elif message.content.startswith('!they'):
        await add_or_remove_role(message, ROLENAME_THEY)


    elif message.content.startswith('!unhe'):
        await CLIENT.remove_roles(message.author, grab_role(message.server, ROLENAME_HE))
        await CLIENT.send_message(message.channel, "Sucessfully removed role!")
    elif message.content.startswith('!unshe'):
        await CLIENT.remove_roles(message.author, grab_role(message.server, ROLENAME_SHE))
        await CLIENT.send_message(message.channel, "Sucessfully removed role!")
    elif message.content.startswith('!unthey'):
        await CLIENT.remove_roles(message.author, grab_role(message.server, ROLENAME_THEY))
        await CLIENT.send_message(message.channel, "Sucessfully removed role!")

CLIENT.run(API_TOKEN)
