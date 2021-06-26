## reff_db
#module for working with refferal system database




#Example:
```python
db.create_tables([Users])

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

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
