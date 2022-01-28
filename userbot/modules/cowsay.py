
import asyncio
from telethon import events
from cowpy import cow
from userbot.util import admin_cmd
from userbot import bot as borg


@borg.on(events.NewMessage(pattern=r"^.(\w+)say (.*)", outgoing=True))
async def univsaye(cowmsg):
    """ For .cowsay module, uniborg wrapper for cow which says things. """
    if cowmsg.text[0].isalpha() or cowmsg.text[0] in ("/", "#", "@", "!"):
        return

    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")
