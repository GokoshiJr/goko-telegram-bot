import logging
from telegram.ext import Updater, CommandHandler
from keys import TOKEN

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update, context) -> None:
    update.message.reply_text("Hello World")
    
def help(update, context) -> None:
    update.message.reply_text("Help Command")

def main():
    """Start the bot."""
    # updater - para saber las peticiones que recibimos de los usuarios
    updater = Updater(token=TOKEN, use_context=True) 

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == "__main__":
    main()