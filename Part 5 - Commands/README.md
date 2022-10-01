# Part 5 - Commands

Hey Guys! This is the Fifth episode of this series Creating a Discord Bot with Python using Hikari API. In this [video](https://youtu.be/jlhZXFfS40s) 
we will be learning how to create Commands using 2 different methods, for getting a response from our bot.


[![Thumbnail](Thumbnail.png)](https://youtu.be/jlhZXFfS40s)

## Creating Commands

### Using Message Events

```python
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

```

### Using hikari-lightbulb

```python
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
```

## Resources

[Lightbulb Documentation](https://hikari-lightbulb.readthedocs.io/en/latest/)
[Hikari Documentation](https://www.hikari-py.dev/hikari)
Read the docs for better understanding of the code.

[Discord Developer](https://discord.com/developers/applications)
Create your very own Discord Bot here!

## License

[MIT](https://github.com/kshgr/Discord-Bot-with-Python-using-Hikari/blob/main/LICENSE)
