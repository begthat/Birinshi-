from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

new_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Registration',callback_data='awa')]
    ]
)
menu_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Restoran',callback_data='restik'),
         InlineKeyboardButton(text='Avto sawda',callback_data='avto'),
         InlineKeyboardButton(text='Muzika',callback_data='music')],
        [InlineKeyboardButton(text='Artqa',callback_data='back'),InlineKeyboardButton(text='About',callback_data='biz')]
    ]
)

admin_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Statistika'),KeyboardButton(text='Reklama jiberiw')],
        [KeyboardButton(text='User magliwmatlari')]
    ]
)
saylaw_menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Awa',callback_data='AWA'),InlineKeyboardButton(text='Yaq',callback_data='YAQ')]
    ]
)