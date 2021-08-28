import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters, commandhandler
import os
from instaloader import Instaloader, Profile
import time


'''Coded by Nxt Stark 😃😃😃😃'''
L = Instaloader()
TOKEN = os.getenv("BOT_TOKEN")
APP_NAME = os.getenv("APP_NAME")
TELEGRAM_USERNAME = os.getenv("TELEGRAM_USERNAME")

welcome_msg = '''<b>Welcome To the Bot</b>🖐🖐
 <i>Send me anyones instagram username to get their DP</i>
 ex : <b>nxtstark</b> , <b>h_tech_media</b> etc
 
 <b>Made By @HTechMedia</b>'''
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel🏡', url='https://telegram.me/HTechMedia'),
        InlineKeyboardButton('Support🦼', url='https://telegram.me/HTechMediaSupport')
        ],[
        InlineKeyboardButton('Creator🚀', url='https://telegram.me/NxtStark'),
        InlineKeyboardButton('Website🪐', url='https://htechmediayt.wixsite.com/htechmedia'),
        InlineKeyboardButton('Youtube🌏', url='https://youtube.com/c/HTechMedia')
        ]]
    )
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def acc_type(val):
    if(val):
        return "🔒Private🔒"
    else:
        return "🔓Public🔓"

# Start the Bot


def start(update, context):
    id = update.message.chat_id
    name = update.message.from_user['username']
    keyboard = 
        [[
        InlineKeyboardButton('Channel🏡', url='https://telegram.me/HTechMedia'),
        InlineKeyboardButton('Support🦼', url='https://telegram.me/HTechMediaSupport')
        ],[
        InlineKeyboardButton('Creator🚀', url='https://telegram.me/NxtStark'),
        InlineKeyboardButton('Website🪐', url='https://htechmediayt.wixsite.com/htechmedia'),
        InlineKeyboardButton('Youtube🌏', url='https://youtube.com/c/HTechMedia')
        ],]
     
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_html(welcome_msg)   
     
def help_msg(update, context):
    keyboard = [[InlineKeyboardButton(
        "Devoloper👀", url=f"telegram.me/NxtStark")],[InlineKeyboardButton("Support😎", url=f"telegram.me/HTechMedia")], ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Nothing to help.This is way to simple 😂😂', reply_markup=reply_markup)
    
def contact(update, context):
    keyboard = [[InlineKeyboardButton(
        "Devoloper👀", url=f"telegram.me/NxtStark")],[InlineKeyboardButton("Support😎", url=f"telegram.me/HTechMedia")], ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Contact The Maker:', reply_markup=reply_markup)

# get the username and send the DP


def username(update, context):
    msg = update.message.reply_text("Downloading...")
    query = update.message.text
    chat_id = update.message.chat_id
    try:
        user = Profile.from_username(L.context, query)
        caption_msg = f'''📛*Name*📛: {user.full_name} \n😁*Followers*😁: {user.followers} \n🤩*Following*🤩: {user.followees}\
         \n🧐*Account Type*🧐: {acc_type(user.is_private)} \nThank You For Using The bot 😀😀 \n\n*@NxtStark❤*'''
        context.bot.send_photo(
            chat_id=chat_id, photo=user.profile_pic_url,
            caption=caption_msg, parse_mode='MARKDOWN')
        msg.edit_text("finished.")
        time.sleep(5)
    except Exception:
        msg.edit_text("Try again 😕😕 Check the username correctly")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    updater = Updater(TOKEN, use_context=True)
    PORT = int(os.environ.get('PORT', '8443'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_msg))
    dp.add_handler(CommandHandler("contact", contact))
    dp.add_handler(MessageHandler(Filters.text, username))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN,
                          webhook_url=f"https://{APP_NAME}.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
