import hikari
import lightbulb
from secret import TOKEN


bot = lightbulb.BotApp( token=TOKEN,
                        intents=hikari.Intents.ALL_MESSAGES,
                        prefix="!",
                      )

"""
                            Commands

- Using commands with Message Event
    -> event decorator
        ->@bot.listen(Hikari.Event)
    -> define function(event: hikari.MessageEvent)
        -> await event.message.respond(f"") 

- Using Lightbulb
    -> pip install hikari-lightbulb
    -> setup lightbulb as bot - bot = lightbulb.BotApp(token, intents, prefix)
    -> command decorator
        ->@bot.command
        ->@lightbulb.command(command, description)
        ->@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
    -> define function(ctx: lightbulb.Context)
        -> await ctx.respond(f"")

"""

@bot.command
@lightbulb.command("ping", "Returns the Latency for our Bot.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")



'''
                Command via Message Event
@bot.listen(hikari.MessageCreateEvent)
async def ping(event=hikari.MessageCreateEvent):
    if event.is_human:
        if event.content.strip() == "!ping":
            await event.message.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")
'''

bot.run()