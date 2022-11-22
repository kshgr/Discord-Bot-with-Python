import hikari
import lightbulb
from secret import TOKEN

bot = lightbulb.BotApp( token=TOKEN,
                        intents=hikari.Intents.ALL_MESSAGES,
                        prefix="!",
                      )

import sqlite3
import datetime

# Initialize SQLite3

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


    # Create Table

try:
    sqlite_create_table_query = """
                                CREATE TABLE Message_Log
                                (GuildID INTEGER NOT NULL,
                                 ChannelID INTEGER NOT NULL,
                                 UserID INTEGER NOT NULL,
                                 Message TEXT NOT NULL,
                                 Date TEXT NOT NULL
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


# Create logging Function

@bot.listen(hikari.GuildMessageCreateEvent)
async def CreateLog(event):
    GuildID = event.guild_id
    ChannelID = event.channel_id
    UserID = event.author_id
    Message = str(event.content)
    Date = datetime.datetime.now()

    if event.is_human:
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




bot.run()