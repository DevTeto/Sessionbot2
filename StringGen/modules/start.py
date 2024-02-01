from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"""
           ◍ أهلا بك عزيزي {message.from_user.first_name} في بوت استخراج الجلسات

◍ يمكنك استخراج التالي :

◍  تيليثون 

◍ بايروجرام 1 ، 2 

◍ تم انشاء البوت بواسطة: @WX_PM """,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
    
