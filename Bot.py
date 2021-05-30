import Constants as keys
from telegram.ext import *
import Model as model

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something and get a sentiment analysis')
    
def help_command(update, context):
    update.message.reply_text('I will analyze your text and tell you what sentiment it has! I am 70% accurate!!')
    
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = model.input(text)
    
    update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} caused error {context.error}")
    
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start_command))
    
    dp.add_handler(CommandHandler("help", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    dp.add_error_handler(error)
    
    updater.start_polling()
    
    updater.idle()

if __name__ == '__main__':
    main()