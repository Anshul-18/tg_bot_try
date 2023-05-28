import telegram.ext

Token = "6184320063:AAHB9ASgGknvS4RpnSqMipfYMVgdm_gJrTk"

updater = telegram.ext.updater("6184320063:AAHB9ASgGknvS4RpnSqMipfYMVgdm_gJrTk", use_context = True)
dispatcher = updater.dispatcher

def start(update, context) :
    update.message.reply_text("Hello Welcome Sir")

def help(update, context) :
    update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> this particular message
        /content -> about various playlist of yours sir
        /Python -> 1st video from python playlist
        /C++ -> 1st video from C++ playlist
        /JAVA -> 1st video from JAVA playlist
        /contact -> contact information
        """
    )


def content(update, context) : 
    update.message.reply_text("we have various playlists and articles available.")

def Python(update, context) :
    update.message.reply_text("tutorial playlist link : https://www.youtube.com/playlist?list=PLKKfKV1b9e8r_GAb4BQNc2ZSh6S7NwK9W")

def Cpp(update, context) :
    update.message.reply_text("tutorial playlist link : https://www.youtube.com/playlist?list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ")

def JAVA(update, context) : 
    update.message.reply_text("tutorial playlist link : https://www.youtube.com/playlist?list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop")

def contact(update, context) :
    update.message.reply_text("you can contact on the registered email id provided on the website")



dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('Python', Python))
dispatcher.add_handler(telegram.ext.CommandHandler('Cpp', Cpp))
dispatcher.add_handler(telegram.ext.CommandHandler('JAVA', JAVA))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()
