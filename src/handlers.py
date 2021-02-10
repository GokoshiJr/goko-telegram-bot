import logging, actions
from user import User

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__+".py")

def start(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("ha iniciado el bot."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(f"¡Hola bienvenido {user.get_name()}!, soy un bot y estoy en desarrollo \n\n Puedes usar los siguientes comandos:\n\n /help \n /qrcode") 
    
def help(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicito ayuda."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text("Help Command")
