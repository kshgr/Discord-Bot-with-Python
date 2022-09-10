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
    #Event Triggered when Bot joins a server

    guild = event.guild                 #Returns Name of server that bot has joined
    guild_id = event.guild_id           #Returns Unique Numeric GuildID
    members = event.members             #Returns Mapping of user IDs to Members in server
    presences = event.presences         #Returns Mapping of user IDs to presences in server
    roles = event.roles                 #Returns Mapping of role IDs to roles in server 
    shard = event.shard                 #Returns Unique ShardID
    voice_states = event.voice_states   #Returns Mapping of user IDs to voice states in server
    
    print(guild, guild_id, members, presences, roles, shard, voice_states)

@bot.listen(hikari.GuildLeaveEvent)
async def GuildLeaveEvent(event):
    #Event Triggered when Bot leaves a server

    guild_id = event.guild_id           #Returns Unique Numeric GuildID
    old_guild = event.guild             #Returns Name of server that bot has left
    shard = event.shard                 #Returns Unique ShardID
    
    print(guild_id, old_guild, shard)

@bot.listen(hikari.GuildUnavailableEvent)
async def GuildUnavailableEvent(event):
    #Event Triggered when a server becomes Unavailable
    
    guild_id = event.guild_id           #Returns Unique Numeric GuildID
    shard = event.shard                 #Returns Unique ShardID
    
    print(guild_id, shard)

@bot.listen(hikari.GuildAvailableEvent)
async def GuildAvailableEvent(event):
    #Event Triggered when a server becomes Available
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
    #Event Triggered when details of a server are updated
    guild = event.guild
    guild_id = event.guild_id
    old_guild = event.old_guild
    roles = event.roles
    shard = event.shard
    emojis = event.emojis

    print(guild, guild_id, old_guild, roles, shard, emojis)

@bot.listen(hikari.EmojisUpdateEvent)
async def EmojisUpdateEvent(event):
    #Event Triggered when emojis on a server are updated
    emojis = event.emojis
    guild_id = event.guild_id
    old_emojis = event.old_emojis
    shard = event.shard

    print(emojis, guild_id, old_emojis, shard)


bot.run()