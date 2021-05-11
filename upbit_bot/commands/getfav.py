from telegram.ext import CommandHandler
from telegram import ParseMode

class Getfav():
    @staticmethod
    def enroll(dispatcher, upbitutil):
        def execute(update, context):
            tickers = upbitutil.get_favorite()
            text = '관심 코인 목록이예요.\n'
            for num in range(len(tickers)):
                text += '{0}) {1}'.format(num+1, tickers[num]) + '\n'
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('getfav', execute)
        dispatcher.add_handler(handler)
