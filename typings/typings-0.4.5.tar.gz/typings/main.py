import datetime
import logging
import os
import time

from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from info import *



async def paid(bot, update):
    user_id = update.from_user.id
    user_name = update.from_user.username
    user_first = update.from_user.first_name
    logger.info(
        f"👉 {update.text} 👈 Sent by User {user_first} {str(user_id)} @{user_name}"
    )
    SUB_BUTTONS = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Pay Now", url=f"https://t.me/{PAID_USERNAME}")],
        ]
    )
    if PAID_BOT.upper() == "YES":
        try:
            paid_status = await db.get_paid_status(user_id)
        except:
            await update.reply("⚠️ First Click on /start, Then try again")
            return
        if paid_status["is_paid"]:
            current_date = datetime.datetime.now()
            paid_duration = paid_status["paid_duration"]
            paid_on = paid_status["paid_on"]
            paid_reason = paid_status["paid_reason"]
            integer_paid_duration = int(paid_duration)
            will_expire = paid_on + datetime.timedelta(days=integer_paid_duration)
            if will_expire < current_date:
                try:
                    await db.remove_paid(user_id)
                except Exception as e:
                    logger.info(f"⚠️ Error: {e}")
                try:
                    await bot.send_message(
                        update.chat.id,
                        f"👋 Your paid plan has Expired on {will_expire}\n\nIf you want to use the bot, You can do so by Paying.",
                    )
                except Exception as e:
                    logger.info(f"⚠️ Error: {e}")
                for i in ADMINS:
                    try:
                        await bot.send_message(
                            i,
                            f"🌟 **Plan Expired:** \n\n**User Id:** `{update.from_user.id}`\n\n**User Name:** @{update.from_user.username}\n\n**Plan Validity:** {paid_duration} Days\n\n**Joined On** : {paid_on}\n\n**Discription** : {paid_reason}",
                        )
                    except Exception:
                        logger.info(f"⚠️ Not found id {i}")
                return

            else:
                pass

        else:
            await update.reply_text(
                text=f"{PAID_TEXT}",
                reply_markup=SUB_BUTTONS,
                disable_web_page_preview=True,
                quote=True,
            )
            return
