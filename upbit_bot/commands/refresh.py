from telegram.ext import CommandHandler
from telegram import ParseMode

class Refresh():
    @staticmethod
    def enroll(dispatcher, upbitutil):
        def execute(update, context):
            upbitutil.reload_tickers()
            text = "코인 리스트가 업데이트 되었습니다."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('refresh', execute)
        dispatcher.add_handler(handler)
