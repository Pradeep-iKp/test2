from telethon import events, Button
from bot import tbot 

TXT = """Telethon testing"""
BOT_USERNAME = "@YJustATestBot"

@tbot.on(events.NewMessage(pattern="[/]tel"))
async def help(event):
    if event.is_group:
       await event.reply("Contact me in PM to get available help menu!", buttons=[
       [Button.url("Help And Commands!", "t.me/{}?start=tel".format(BOT_USERNAME))]])
       return
    await event.reply(TXT)
    
@tbot.on(events.NewMessage(pattern="^/start tel"))
async def _(event):
    await event.reply(TXT)
    
@tbot.on(events.callbackquery.CallbackQuery(data="tel"))
async def _(event):
     await event.edit(TXT)
