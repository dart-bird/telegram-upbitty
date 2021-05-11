from telegram.ext import CommandHandler
from telegram import ParseMode

class Target():
    @staticmethod
    def enroll(dispatcher, upbitutil):
        def execute(update, context):
            argv = update.message.text.split(' ')
            if len(argv) == 1 : interval = 'minute60'
            else : interval = argv[1]
            context.bot.send_message(chat_id=update.effective_chat.id, text="코인 분석중입니다...")
            tickers = upbitutil.get_favorite()
            tickers = upbitutil.get_target_tickers(tickers=tickers, interval=interval)
            if tickers == []: 
                context.bot.send_message(chat_id=update.effective_chat.id, text='관심 코인 중에 매수할 코인이 아직 없어요 ㅠ', parse_mode=ParseMode.MARKDOWN)
                return
            
            text = '*[떨어질 대로 떨어진 코인 >.<]*\n\n'
            text += "*{0}* 주기 데이터예요.\n\n".format(interval)
            for ticker in tickers:
                price = "{:,}".format(int(upbitutil.get_ticker_price(ticker=ticker)))
                rsi = upbitutil.get_rsi(ticker=ticker, interval=interval)
                text += '*[{0}]*\n가격 : *{1}* 원\nRSI : *{2}*'.format(ticker, price, round(rsi, 2)) + '\n'
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('target', execute)
        dispatcher.add_handler(handler)
