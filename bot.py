"""
bot.py file!
"""
import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
import telegram
from telegram import ForceReply, Update, Bot, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
logging.basicConfig(format="%(asctime)s - %(name)s - %(Lavelname)s - %(message)s", level = logging.INFO)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message then the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id, text=rf"This is your chat_id {chat_id}!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    chat_id = update.message.chat_id
    await context.bot.send_chat_action(chat_id=chat_id, action=telegram.constants.ChatAction.TYPING)
    await update.message.reply_text("Help!")
   

async def create_invite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id, text=f"{Bot.edit_chat_invite_link(chat_id)}!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def send_doc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await context.bot.send_document(chat_id=chat_id, document=open('tests/test.jpg', 'rb'))
    

async def unknow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = (await context.bot.get_updates())[-1].message.chat_id
    echo_text = update.message.text
    await context.bot.send_message(chat_id, text=f"Сорян, Я не понемаю эту команду {echo_text}!")

async def test_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    custom_keyboard = [['top-left', 'top-right'],
                        ['bottom-left', 'botton-right']]
    chat_id = update.message.chat_id
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    await context.bot.send_message(chat_id, text='Custom Keyboard Test', reply_markup=reply_markup)

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("2117384417:AAGXVb3q9DDE_3YuxpW3gQ9U07_PyHrzLbs").build()
    unknow_handler = MessageHandler(filters.COMMAND, unknow)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("chat_id", chat_id))
    application.add_handler(CommandHandler("create_invite", create_invite))
    application.add_handler(CommandHandler("send_doc", send_doc))
    application.add_handler(CommandHandler("test_button", test_button))
    application.add_handler(unknow_handler)

    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()



if __name__ == "__main__":
    main()