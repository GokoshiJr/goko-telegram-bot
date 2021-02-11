import logging, actions, urllib.request as r
from bs4 import BeautifulSoup
from user import User

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__+".py")

def dolar_request() -> str:
  try:
    data = r.urlopen("https://exchangemonitor.net/dolar-promedio-venezuela").read().decode()
    soup = BeautifulSoup(data, features="html.parser")
    tags = soup("h2")
    return f"El precio promedio del dolar es: {tags[0].get_text()}"
  except:
    return "Disculpe hubo un error"

def price(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("ha pedido el precio del dolar."))
  actions.escribiendo(update.message.chat) # el bot esta escribiendo
  update.message.reply_text(dolar_request()) 
