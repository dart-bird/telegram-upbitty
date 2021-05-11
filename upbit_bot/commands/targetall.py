from telegram.ext import CommandHandler
from telegram import ParseMode

class TargetAll():
    @staticmethod
    def enroll(dispatcher, upbitutil):
        def execute(update, context):
            argv = update.message.text.split(' ')
            interval = argv[0]
            context.bot.send_message(chat_id=update.effective_chat.id, text="코인 분석중입니다...")
            tickers = upbitutil.get_tickers()
            text = '{0}초 정도 소요됩니다...'.format(int(len(tickers)*0.04))
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)
            tickers = upbitutil.get_target_tickers(tickers=tickers, interval=interval, default=False)
            if tickers == []: 
                context.bot.send_message(chat_id=update.effective_chat.id, text='모든 코인 중에 매수할 코인이 아직 없어요 ㅠ', parse_mode=ParseMode.MARKDOWN)
                return
            text = '*[떨어질 대로 떨어진 코인 >.<]*\n'
            for ticker in tickers:
                price = "{:,}".format(int(upbitutil.get_ticker_price(ticker=ticker)))
                rsi = upbitutil.get_rsi(ticker=ticker)
                text += '*[{0}]*\n가격 : *{1}* 원\nRSI 14 : *{2}*'.format(ticker, price, round(rsi, 2)) + '\n'
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('targetall', execute)
        dispatcher.add_handler(handler)
