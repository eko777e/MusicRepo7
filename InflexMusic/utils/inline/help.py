
from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from InflexMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_.get("CLOSEMENU_BUTTON", "❌ Menyu bağla"),
            callback_data="close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_.get("BACK_BUTTON", "⬅️ Geri"),
            callback_data="help_back",
        ),
        InlineKeyboardButton(
            text=_.get("CLOSEMENU_BUTTON", "❌ Menyu bağla"),
            callback_data="close"
        ),
    ]
    mark = second if START else first

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_.get("H_B_2", "⚙️ Ayarlar"),
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_.get("H_B_1", "📜 Komandalar"),
                    callback_data="help_callback hb1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_.get("H_B_3", "🎶 Musiqi"),
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text=_.get("H_B_4", "📡 Canlı yayım"),
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_.get("H_B_7", "📁 Fayllar"),
                    callback_data="help_callback hb7",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_.get("H_B_8", "ℹ️ Haqqında"),
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_.get("H_B_6", "💡 İpuçları"),
                    callback_data="help_callback hb5",
                ),
            ],
            mark,
        ]
    )


def help_back_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_.get("BACK_BUTTON", "⬅️ Geri"),
                    callback_data="settings_back_helper"
                ),
                InlineKeyboardButton(
                    text=_.get("CLOSE_BUTTON", "❌ Bağla"),
                    callback_data="close"
                ),
            ]
        ]
    )


def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(
                text=_.get("S_B_1", "📚 Kömək al"),
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
