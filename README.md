# REF_DB
### REF_DB - module for working with your refferal system database
### Desription
REDB - module for working with your refferal system database. You can create database and edit it soon 

### Requirements

You need to use python >=3.7



### Using:

Create DataBase:
```python
db.create_tables([Users])
```
To use u need to import REF_DB
```python
from REF_DB import *
```


### Examples:

```python
#part of real code 

def get_my_refs(message):
    count = Users.get_ref_count(message.chat.id)
    bot.reply_to(message, text=f'Count: {count}')

def get_my_ref(message):
    bot_name = bot.get_me().username
    bot.reply_to(message, text=ref_link.format(bot_name, message.chat.id))

def start(message):
    user_id = message.chat.id
    splited = message.text.split()
    if not Users.user_exists(user_id):
        Users.create_user(user_id)
        if len(splited) == 2:
            Users.increase_ref_count(splited[1])
    bot.reply_to(message, text=text_helloText)
```
### Contact me:
Telegram - @id
