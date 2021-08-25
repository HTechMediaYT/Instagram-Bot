import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters, commandhandler, Client
import os
from instaloader import Instaloader, Profile
import time


'''Coded by Nxt Stark 😃😃😃😃'''
L = Instaloader()
TOKEN = os.getenv("BOT_TOKEN")
APP_NAME = os.getenv("APP_NAME")
TELEGRAM_USERNAME = os.getenv("TELEGRAM_USERNAME")

START_TEXT = '''<b>Welcome To the Bot</b>🖐🖐
 <i>Send me anyones instagram username to get their DP</i>
 ex : <b>nxt.stark</b> , <b>h_tech_media</b> etc
 
 
<b>Made by @HTechMedia</b>'''
HELP_TEXT ='''
<b>Send any Instagram Username With Out '@' Simple.</b>

Made by @HTechMedia'''
ABOUT_TEXT = '''
<b>- Bot : QRCode-Telegram-bot</b>
<b>- Creator : [NxtStark](https://t.me/nxtstark)</b>
<b>- Channel : [HTechMedia](https://t.me/htechmedia)</b>
<b>- Source :[Click Here](https://github.com/HTechMediaYT/Instagram-Bot)</b>
<b>- Language : [Python3](https://python.org)</b>
<b>- Library : [Payogram](https://pyrogram.org)</b>
<b>- Server : [Herokku](https://heroku.com)</b>
'''
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/HTechMedia'),
        InlineKeyboardButton('Support', url='https://telegram.me/HTechMediaSupport')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ERROR_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Join Updates Channel', url='https://telegram.me/HTechMedia')
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

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )



def contact(update, context):
    keyboard = [[InlineKeyboardButton(
        "Contact", url=f"telegram.me/NxtStark")], ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Contact The Maker:', reply_markup=reply_markup)

# get the username and send the DP


def username(update, context):
    msg = update.message.reply_text("Downloading Baby...")
    query = update.message.text
    chat_id = update.message.chat_id
    try:
        user = Profile.from_username(L.context, query)
        caption_msg = f'''📛*Name*📛: {user.full_name} \n😁*Followers*😁: {user.followers} \n🤩*Following*🤩: {user.followees}\
         \n🧐*Account Type*🧐: {acc_type(user.is_private)} \n@NxtStark \n\nThank You For Using The bot 😀😀'''
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
