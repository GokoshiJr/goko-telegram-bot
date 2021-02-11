import logging, actions, buttons
from user import User

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__+".py")

def start(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("ha iniciado el bot."))
  actions.escribiendo(update.message.chat) # el bot esta escribiendo
  update.message.reply_text(f"¡Bienvenido {user.get_name()}! \n\n Soy un bot y me encuentro en desarrollo \n\n Dale click o escribe /commands para ver los comandos disponibles.") 
    
def commands(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó los comandos."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text("Lista de Comandos: \n\n /start \n /commands \n /dev")

def dev_social(update, context) -> None:
  update.message.reply_text(text="Contacto con el desarrolador", reply_markup=buttons.dev_social_markup)
