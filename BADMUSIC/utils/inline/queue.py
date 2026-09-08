import random
from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle

def Badbtn():
    return random.choice([
        ButtonStyle.SUCCESS,
        ButtonStyle.DANGER,
        ButtonStyle.PRIMARY
    ])


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl

def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="ʏᴛ-ᴀᴘɪ sᴛᴀᴛυs 📼", callback_data="api_status", style=Badbtn()),
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=Badbtn()),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=Badbtn()),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}", style=Badbtn()), 
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=Badbtn()), 
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=Badbtn()),
        ],
        [InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close", style=ButtonStyle.DANGER)]
    ]
    return buttons
