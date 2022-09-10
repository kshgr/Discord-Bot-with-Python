import hikari
from secret import TOKEN
bot = hikari.GatewayBot(token=TOKEN)

"""
GuildEvent
    
    GuildJoinEvent
        guild, guild_id, members, presences, roles, shard, voice_states
    GuildLeaveEvent
        guild_id, old_guild, shard
    
    GuildUnavailableEvent
        guild_id, shard
    GuildAvailableEvent
        channels, emojis, guild, guild_id, members, presences, roles, shard, voice_states
    
    GuildUpdateEvent
        guild, guild_id, old_guild, roles, shard, emojis
    EmojisUpdateEvent
        emojis, guild_id, old_emojis, shard

"""

@bot.listen(hikari.GuildJoinEvent)
async def GuildJoinEvent(event):
    guild = event.guild
    guild_id = event.guild_id
    members = event.members
    presences = event.presences
    roles = event.roles
    shard = event.shard
    voice_states = event.voice_states
    
    print(guild, guild_id, members, presences, roles, shard, voice_states)

@bot.listen(hikari.GuildLeaveEvent)
async def GuildLeaveEvent(event):
    guild_id = event.guild_id
    old_guild = event.old_guild
    shard = event.shard

    print(guild_id, old_guild, shard)

@bot.listen(hikari.GuildUnavailableEvent)
async def GuildUnavailableEvent(event):
    guild_id = event.guild_id
    shard = event.shard

    print(guild_id, shard)

@bot.listen(hikari.GuildAvailableEvent)
async def GuildAvailableEvent(event):
    channels = event.channels
    emojis = event.emojis
    guild = event.guild
    guild_id = event.guild_id
    members = event.members
    presences = event.presences
    roles = event.roles
    shard = event.shard
    voice_states = event.voice_states

    print(channels, emojis, guild, guild_id, shard, members, presences, roles, voice_states)

@bot.listen(hikari.GuildUpdateEvent)
async def GuildUpdateEvent(event):
    guild = event.guild
    guild_id = event.guild_id
    old_guild = event.old_guild
    roles = event.roles
    shard = event.shard
    emojis = event.emojis

    print(guild, guild_id, old_guild, roles, shard, emojis)

@bot.listen(hikari.EmojisUpdateEvent)
async def EmojisUpdateEvent(event):
    emojis = event.emojis
    guild_id = event.guild_id
    old_emojis = event.old_emojis
    shard = event.shard

    print(emojis, guild_id, old_emojis, shard)

    
bot.run()