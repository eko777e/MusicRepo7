from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from InflexMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    """
    Help panel düymələri
    """
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
    """
    Geri düyməsi kliklənəndə istifadə ediləcək ana menyu düymələri
    """
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_.get("START_BUTTON", "🏠 Ana menyu"),
                    callback_data="start_panel"
                ),
                InlineKeyboardButton(
                    text=_.get("CLOSE_BUTTON", "❌ Bağla"),
                    callback_data="close"
                ),
            ]
        ]
    )


# Callback handler nümunəsi (Pyrogram)
@app.on_callback_query()
async def cb_handler(client, callback_query):
    data = callback_query.data
    if data == "help_back":
        # Geri düyməsinə basanda start panelinə keç
        await callback_query.message.edit_text(
            text="🏠 Ana menyu",  # Start mesajı şəkilsiz
            reply_markup=help_back_markup(_)
        )
        await callback_query.answer()
    elif data == "start_panel":
        # Ana menyudan düymə kliklənəndə lazım gələrsə
        await callback_query.message.edit_text(
            text="🏠 Ana menyu",  # Start mesajı
            reply_markup=None  # Burada istəsən start panel düymələrini əlavə edə bilərsən
        )
        await callback_query.answer()
