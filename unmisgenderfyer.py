import os
from pathlib import Path
import discord
from dotenv import load_dotenv

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

API_TOKEN = os.getenv("API_TOKEN")

ROLENAME_HE = "He/Him"
ROLENAME_SHE = "She/Her"
ROLENAME_THEY = "They/Their"


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

@CLIENT.event
async def on_ready():
    for server in CLIENT.servers:
        await check_or_create_role(server, ROLENAME_HE)
        await check_or_create_role(server, ROLENAME_SHE)
        await check_or_create_role(server, ROLENAME_THEY)

@CLIENT.event
async def on_message(message):
    if message.content.startswith('!he'):
        await CLIENT.add_roles(message.author, grab_role(message.server, ROLENAME_HE))
        await CLIENT.send_message(message.channel, "Sucessfully added role!")
    elif message.content.startswith('!unhe'):
        await CLIENT.remove_roles(message.author, grab_role(message.server, ROLENAME_HE))
        await CLIENT.send_message(message.channel, "Sucessfully removed role!")
    elif message.content.startswith('!she'):
        await CLIENT.add_roles(message.author, grab_role(message.server, ROLENAME_SHE))
        await CLIENT.send_message(message.channel, "Sucessfully added role!")
    elif message.content.startswith('!unshe'):
        await CLIENT.remove_roles(message.author, grab_role(message.server, ROLENAME_SHE))
        await CLIENT.send_message(message.channel, "Sucessfully removed role!")
    elif message.content.startswith('!they'):
        await CLIENT.add_roles(message.author, grab_role(message.server, ROLENAME_THEY))
        await CLIENT.send_message(message.channel, "Sucessfully added role!")
    elif message.content.startswith('!unthey'):
        await CLIENT.remove_roles(message.author, grab_role(message.server, ROLENAME_THEY))
        await CLIENT.send_message(message.channel, "Sucessfully removed role!")

CLIENT.run(API_TOKEN)
