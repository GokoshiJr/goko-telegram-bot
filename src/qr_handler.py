import qrcode, logging, os, actions
from telegram.ext import ConversationHandler
from user import User

INPUT_TEXT = 0

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__+".py")

def qr_code(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("quiere convertir una imagen a QR."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(f"{user.get_name()} enviame un texto para generar un codigo QR")
  return INPUT_TEXT

def input_text(update, context) -> None:
  chat = update.message.chat
  text = update.message.text
  actions.escribiendo(chat)
  update.message.reply_text(f"Julio dijo {text}")
  file_name = generate_qr(text)
  send_qr(file_name, chat)
  return ConversationHandler.END

def generate_qr(text):
  file_name = text + ".jpg"
  img = qrcode.make(file_name)
  img.save(file_name)
  return file_name

def send_qr(file_name, chat):
  actions.enviando_foto(chat, file_name, "rb")
  os.unlink(file_name)
