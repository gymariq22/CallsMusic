from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

Saya adalah Asta, Bot Music yang bertujuan untuk melayani warga Group 𝚋𝚎𝚛𝚜𝚎𝚗𝚢𝚊𝚠𝚊.

Pencet tombol dibawah untuk mengetahui lebih tentang bot ini.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Contact Owner", url="https://t.me/aidkez"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/joinsenyawa"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/aughys"
                    )
                ]
                [
                    InlineKeyboardButton(
                        "💰 Store", url="https://t.me/jualannokos"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

Saya adalah Asta, Bot Music yang bertujuan untuk melayani warga Group 𝚋𝚎𝚛𝚜𝚎𝚗𝚢𝚊𝚠𝚊.

Pencet tombol dibawah untuk mengetahui lebih tentang bot ini.""",
        reply_markup=InlineKeyboardMarkup(
            [
                    InlineKeyboardButton(
                        "⚒ Contact Owner", url="https://t.me/aidkez"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/joinsenyawa"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/aughys"
                    )
                ]
                [
                    InlineKeyboardButton(
                        "💰 Store", url="https://t.me/jualannokos"
                    )
                ]
            ]
        )
    )
