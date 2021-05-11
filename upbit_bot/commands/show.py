from telegram.ext import CommandHandler
from telegram import ParseMode

class Show():
    @staticmethod
    def enroll(dispatcher, upbitutil):
        def execute(update, context):
            tickers = upbitutil.get_favorite()
            if tickers == []:
                text = '현재 관심에 등록된 코인이 없어요.'
                context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)
                return
            text = ""
            for ticker in tickers:
                text += '*[ %s ]*' % ticker + "\n"
                current_price = int(upbitutil.get_ticker_price(ticker=ticker))
                current_price = "{:,}".format(current_price)
                rsi = upbitutil.get_rsi(ticker=ticker)
                text += '현재 가격 : {0} 원\nRSI 14 : {1}'.format(current_price, rsi) + "\n\n"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('show', execute)
        dispatcher.add_handler(handler)
