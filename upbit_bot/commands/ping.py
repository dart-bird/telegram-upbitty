from telegram.ext import CommandHandler
from telegram import ParseMode

class Ping():
    @staticmethod
    def enroll(dispatcher):
        def execute(update, context):
            context.bot.send_message(chat_id=update.effective_chat.id, text="pong", parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('ping', execute)
        dispatcher.add_handler(handler)
