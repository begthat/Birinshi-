from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from btns import new_menu,menu_menu,admin_menu,saylaw_menu
from datas import save_user,show_user
from aiogram.client.session.aiohttp import AiohttpSession


api = '8212962559:AAHYOi_HLcnn6KTNVFU0PHyEYDp9IlVV_JE'
session = AiohttpSession(proxy='http://proxy.server:3128')
bot = Bot(api, session=session)
dp=Dispatcher()

class AdminReklama(StatesGroup):
    photo = State()
    captionn= State()

class NewUsers(StatesGroup):
    ati = State()
    nomeri = State()
    adress = State()

@dp.message(Command('start'))
async def send_salem(sms:types.Message):
    if sms.from_user.id==6993430435:
        await sms.answer(text='Salem admin',reply_markup=admin_menu)
    else:
        users = await show_user()
        for i in users:
            if sms.from_user.id in i:
                await sms.answer(text='Qaytqaninizdan quwanishlimiz',reply_markup=menu_menu)
                break
        else:
            await sms.answer(text='Salem '+str(sms.from_user.id)+ ', jana paydalaniwshi',
                            reply_markup=new_menu)

@dp.message(F.text=='User magliwmatlari')
async def send_user_info(sms:types.Message):
    await sms.answer(text='Users information')
    paydalaniwshi = await show_user()
    await bot.send_message(
        sms.chat.id,
        f'{paydalaniwshi}'        
    )

@dp.message(F.text=='Statistika')
async def send_sani(sms:types.Message):
    paydalaniwshi = await show_user()
    await sms.answer(text=f'Paydalaniwshilar sani: {len(paydalaniwshi)}')

@dp.message(F.text=='Reklama jiberiw')
async def question(sms:types.Message,state:FSMContext):
    await sms.answer(text='Suwretin jiber')
    await state.set_state(AdminReklama.photo)
#     await sms.answer(text='Sureti barma?',reply_markup=saylaw_menu)
#     # if F.sms.text=='awa'.upper():
#     #     await sms.answer(text='Onda suwretin jiber')
#     #     await state.set_state(AdminReklama.photo)
#     # elif F.sms.text=='yaq'.upper():
#     #     await sms.answer(text='Onda reklama tekstin jiber')
#     #     await state.set_state(AdminReklama.captionn)
# @dp.message(F.data=='AWA')
# async def add_reklama_to_user(call:types.CallbackQuery,state:FSMContext):
#     await call.message.answer(text='Onda suwretin jiber')
#     await state.set_state(AdminReklama.photo)

# @dp.message(F.data=='YAQ')
# async def text(call:types.CallbackQuery,state:FSMContext):
#     await call.message.answer(text='Onda reklama tekstin jiber')
#     await state.set_state(AdminReklama.captionn)

@dp.message(AdminReklama.photo)
async def save_photo(sms:types.Message,state:FSMContext):
    await state.update_data(suwret=sms.photo[0].file_id)
    await sms.answer(text='Endi usi suwret reklamasinin tekstin jiber')
    await state.set_state(AdminReklama.captionn)

@dp.message(AdminReklama.captionn)
async def save_text(sms:types.Message,state:FSMContext):
    await state.update_data(tekst=sms.text)
    reklama = await state.get_data()
    paydalaniwshi = await show_user()
    for i in range(len(paydalaniwshi)):
        await bot.send_photo(
            chat_id=paydalaniwshi[i][0],
            photo=reklama['suwret'],
            caption=f'{reklama['tekst']}',
        )

@dp.callback_query(F.data=='awa')
async def start_reg(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer(text='Atinizdi jazin:')
    await state.set_state(NewUsers.ati)

@dp.message(NewUsers.ati)
async def save_name(sms:types.Message,state:FSMContext):
    await state.update_data(ati=sms.text)
    await sms.answer(text='Telefon nomerinizdi toliq jazin:')
    await state.set_state(NewUsers.nomeri)

@dp.message(NewUsers.nomeri)
async def save_nomeri(sms:types.Message,state:FSMContext):
    if not sms.text.isdigit() or len(sms.text)<9:
        await sms.answer(text='Siz qate magliwmat kirittiniz')
        await sms.answer(text='Jane urinip korin')
    else:
        await state.update_data(nomeri=sms.text)
        await sms.answer(text='Adressinizdi jazin(Qala,koshe,uy nomeri):')
        await state.set_state(NewUsers.adress)

@dp.message(NewUsers.adress)
async def save_adress(sms:types.Message,state:FSMContext):
    await state.update_data(adress=sms.text)
    await sms.answer(text='Dizimnen otkeniz ushin ushin raxmet')
    magliwmatlar = await state.get_data()

    await save_user(
        id=sms.from_user.id,
        name=magliwmatlar['ati'],
        phone=magliwmatlar['nomeri'],
        adress=magliwmatlar['adress']
    )
    # await bot.send_message(
    #     sms.chat.id,    
    #     f'Atiniz:{magliwmatlar['ati']}\n'
    #     f'Nomeriniz:{magliwmatlar['nomeri']}\n'
    #     f'Adressiniz:{magliwmatlar['adress']}\n'
    # )
    await state.clear()
    # await bot.send_photo(
    #     sms.chat.id,
    #     photo='download.png',
    #     caption='reklama'
    # )
# @dp.callback_query(F.data=='yaq')
# async def start_menu(call:types.CallbackQuery,state:FSMContext):
#     await call.message.answer(text='Menu:',
#                               reply_markup=menu_menu)

async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
