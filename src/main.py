import telegram, qr_handler, handlers, dolar_handler
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from keys import TOKEN

if __name__ == "__main__":
    # bot info
    bot = telegram.Bot(TOKEN)
    print(bot.get_me())
    
    # updater - para saber las peticiones que recibimos de los usuarios
    updater = Updater(token=TOKEN, use_context=True)
    
    # get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", handlers.start))
    dispatcher.add_handler(CommandHandler("commands", handlers.commands)) 
    dispatcher.add_handler(CommandHandler("dev", handlers.dev_social)) 
    dispatcher.add_handler(CommandHandler("dolar", dolar_handler.price))

    # manejador/handler de conversacion
    dispatcher.add_handler(ConversationHandler(
        entry_points=[ # La conversacion inicia al mandar el comando /qrcode
            CommandHandler("qrcode", qr_handler.qr_code)
        ],
        states={
            qr_handler.INPUT_TEXT:[
                MessageHandler(Filters.text, qr_handler.input_text)
            ]
        },
        fallbacks=[]
    ))

    # start the Bot
    updater.start_polling() # verifica si esta recibiendo mensajes
    updater.idle() # terminar bot ctrl + c