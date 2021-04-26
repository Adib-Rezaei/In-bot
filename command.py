from telegram import Update
from telegram.ext import CallbackContext
from setting import Setting

def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!'
    )


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def tof(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{Setting.cnt} عدد تف در قبر امیر ارسال شد ')


def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="نفهمیدم چی گفتی, پس تف تو قبر امیر")