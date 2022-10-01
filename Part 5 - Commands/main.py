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

# Register the command to the bot
@bot.command
# Use the command decorator to convert the function into a command
@lightbulb.command("ping", "Returns the Latency for our Bot.")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context):
    # Send a message to the channel the command was used in
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")

bot.run()

'''
                Command via Message Event

bot = hikari.GatewayBot(token=TOKEN)

# Register the event to the Bot
@bot.listen(hikari.MessageCreateEvent)
# Define the events's callback. The callback should take a single argument which will be
# an instance of a subclass of hikari.Events
async def ping(event=hikari.MessageCreateEvent):
    # Create a condition to accept commands only from Human Users.
    if event.is_human:
        # Create a condition to read the content to check if command is called
        if event.content.strip() == "!ping":
            # Send a message to the channel the command was used in
            await event.message.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")

'''