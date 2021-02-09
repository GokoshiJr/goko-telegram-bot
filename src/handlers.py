import logging
from user import User

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__+".py")

def start(update, context) -> None:
  """ goko_bot = context.bot
  chat_id = update.message.chat_id """
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log())
  update.message.reply_text(f"Hola {user.get_name()} bienvenido, soy un bot estoy en desarrollo") 
    
def help(update, context) -> None:
  update.message.reply_text("Help Command")