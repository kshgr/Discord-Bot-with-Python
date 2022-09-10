# Part 3 - Ban Events

This is the third episode of this series Creating a Discord Bot with Python using Hikari API. 
In this [video](https://youtu.be/yFiHXrp5k9Q) we will be focusing on events triggered when a user's Ban status is modified and understand their Properties


[![Thumbnail](Thumbnail.png)](https://youtu.be/yFiHXrp5k9Q)


## Types of Ban Events

```python
hikari.BanEvent                 #Triggered for all Ban status change events
hikari.BanCreateEvent           #Triggered when a user is banned from a server
hikari.BanDeleteEvent           #Triggered when a user's ban is revoked from a server

```


## BanCreateEvent Properties

```python
    guild_id = event.guild_id   #Returns Unique Numeric GuildID
    shard = event.shard         #Returns Unique ShardID
    user = event.user           #Returns Username#1234
    user_id = event.user_id     #Returns Unique Numeric UserID

```

## BanDeleteEvent Properties

```python
    
    guild_id = event.guild_id   #Returns Unique Numeric GuildID
    shard = event.shard         #Returns Unique ShardID
    user = event.user           #Returns Username#1234
```

## Resources

[Hikari Documentation for Ban Events](https://www.hikari-py.dev/hikari/events/guild_events.html#hikari.events.guild_events.BanEvent)
Read the docs for better understanding of the code.

[Discord Developer](https://discord.com/developers/applications)
Create your very own Discord Bot here!

## License

[MIT](https://github.com/kshgr/Discord-Bot-with-Python-using-Hikari/blob/main/LICENSE)
