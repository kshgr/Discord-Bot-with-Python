# Part 6 - Logging Messages

Hey Guys! This is the Sixth episode of this series Creating a Discord Bot with Python using Hikari API. In this [video](https://www.youtube.com/watch?v=L4PaiXWLmo4) we will be learning how to create a Logging System for Messages using SQLite with our bot.

[![Thumbnail](Thumbnail.png)](https://www.youtube.com/watch?v=L4PaiXWLmo4)

## Initializing SQLite3

### Creating and Connecting to a Database

```python
try: 
    sqliteConnection = sqlite3.connect("SQLite_Python.db")
    cursor = sqliteConnection.cursor()
    print("DB created and connected successfully.")

    sqlite_select_query = "SELECT sqlite_version()"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("SQLite Database version is ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to SQLite: ", error)

```

### Creating a Table in Database

```python
try:
    sqlite_create_table_query = """
                                CREATE TABLE Message_Log
                                (GuildID    INTEGER   NOT NULL,
                                 ChannelID  INTEGER   NOT NULL,
                                 UserID     INTEGER   NOT NULL,
                                 Message    TEXT      NOT NULL,
                                 Date       TEXT      NOT NULL
                                );
                                """
    cursor = sqliteConnection.cursor()
    print("Successfully Connected.")

    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite Table created successfully.")
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a Table: ", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite connection is closed.")

```
## Creating Logging Function

### Message Log Function

```python
@bot.listen(hikari.GuildMessageCreateEvent)
async def CreateLog(event):
    GuildID = event.guild_id
    ChannelID = event.channel_id
    UserID = event.author_id
    Message = str(event.content)
    Date = datetime.datetime.now()
    
    if event.is_human:
      # Execute SQL Code to insert Records in Table
```

### Inserting Record into SQL Table

```python
        try:
            sqliteConnection = sqlite3.connect("SQLite_Python.db")
            cursor = sqliteConnection.cursor()
            print("Connected Successfully")

            SQLite_insert_record_query =    """
                                            INSERT INTO Message_Log
                                            (GuildID, ChannelID, UserID, Message, Date)
                                            VALUES
                                            (?,?,?,?,?)
                                            """
            data_tuple = (GuildID, ChannelID, UserID, Message, Date)

            cursor.execute(SQLite_insert_record_query, data_tuple)
            sqliteConnection.commit()

            print("Records inserted into the Table.", cursor.rowcount)
            cursor.close()
        
        except sqlite3.Error as error:
            print("Error while inserting records into the Table: ", error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("SQLite connection is closed.")
```


## Resources

[Lightbulb Documentation](https://hikari-lightbulb.readthedocs.io/en/latest/)
[Hikari Documentation](https://www.hikari-py.dev/hikari)
Read the docs for better understanding of the code.

[Discord Developer](https://discord.com/developers/applications)
Create your very own Discord Bot here!

## License

[MIT](https://github.com/kshgr/Discord-Bot-with-Python-using-Hikari/blob/main/LICENSE)
