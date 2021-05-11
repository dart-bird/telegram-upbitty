from telegram.ext import CommandHandler
from telegram import ParseMode

class TargetAll():
    @staticmethod
    def enroll(dispatcher, upbitutil):
        def execute(update, context):
            argv = update.message.text.split(' ')
            if len(argv) == 1 : interval = 'minute60'
            else : interval = argv[1]
            context.bot.send_message(chat_id=update.effective_chat.id, text="코인 분석중입니다...")
            tickers = upbitutil.get_tickers()
            text = '총 {0} 개의 코인을 분석합니다. 조금 걸려요...'.format(len(tickers))
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)
            tickers = upbitutil.get_target_tickers(tickers=tickers, interval=interval, default=False)
            if tickers == []: 
                context.bot.send_message(chat_id=update.effective_chat.id, text='모든 코인 중에 매수할 코인이 아직 없어요 ㅠ', parse_mode=ParseMode.MARKDOWN)
                return
            text = '*[떨어질 대로 떨어진 코인 >.<]*\n\n'
            text += "*{0}* 주기 데이터예요.\n\n".format(interval)
            for ticker in tickers:
                price = "{:,}".format(int(upbitutil.get_ticker_price(ticker=ticker)))
                rsi = upbitutil.get_rsi(ticker=ticker, interval=interval)
                text += '*[{0}]*\n가격 : *{1}* 원\nRSI : *{2}*'.format(ticker, price, round(rsi, 2)) + '\n'
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('targetall', execute)
        dispatcher.add_handler(handler)
