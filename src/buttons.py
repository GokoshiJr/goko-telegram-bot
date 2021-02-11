from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# dev social
dev_telegram = InlineKeyboardButton(
  text="Telegram", 
  url="telegram.me/Gokoshi_Jr"
)
dev_twitter = InlineKeyboardButton(
  text="Twitter", 
  url="https://twitter.com/GokoshiJr"
)
dev_whatsapp = InlineKeyboardButton(
  text="WhatsApp", 
  url="wa.me/+584247300796"
)
dev_github = InlineKeyboardButton(
  text="GitHub", 
  url="github.com"
)

# markup
dev_social_markup = InlineKeyboardMarkup([
  [dev_whatsapp, dev_telegram],
  [dev_twitter, dev_github]
])