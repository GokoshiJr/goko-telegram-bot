from telegram import ChatAction

def escribiendo(chat) -> None:
  chat.send_action(
    action=ChatAction.TYPING,
    timeout=None
  )

def enviando_foto(chat, file_name, metodo) -> None:
  chat.send_action(
    action=ChatAction.UPLOAD_PHOTO,
    timeout=None
  )
  chat.send_photo(
    photo=open(file_name, metodo)
  )