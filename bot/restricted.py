from functools import wraps
from config import Config

def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        userId = Config.USERID
        user_id = update.effective_user.id
        if user_id != int(userId):
            print("Unauthorized access denied for {0}. Allowed users: {1}".format(user_id,userId))
            context.bot.send_message(chat_id=user_id, text="You are not authorized to use this bot! Make your own YeetMeet bot from https://github.com/1337w0rm/YeetMeet")
            return
        return func(update, context, *args, **kwargs)
    return wrapped
