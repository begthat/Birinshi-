from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command


api = '8212962559:AAHYOi_HLcnn6KTNVFU0PHyEYDp9IlVV_JE'
bot = Bot(api)
dp=Dispatcher()


class AutoMobile(StatesGroup):
    ati = State()
    jili = State()
    suwreti = State()
    karobkasi = State()
    bahasi = State()
    probegi = State()
 


@dp.message(Command('start'))
async def send_hi(sms:types.Message):
    await sms.answer(text='Salem '+str(sms.from_user.id))
@dp.message(Command('add'))
async def start_adding(sms:types.Message,state:FSMContext):
    await sms.answer('OOO , jana mashina. Bizge mashina atin jazin:')
    await state.set_state(AutoMobile.ati)

@dp.message(AutoMobile.ati)
async def save_ati(sms:types.Message,state:FSMContext):
    await state.update_data(ati=sms.text)
    await sms.answer(text='Endi bizge jilin jazin:')
    await state.set_state(AutoMobile.jili)



@dp.message(AutoMobile.jili)
async def save_year(sms:types.Message,state:FSMContext):
    await state.update_data(jili=sms.text)
    await sms.answer(text='Zor, endi bizge suwretin jiberin')
    await state.set_state(AutoMobile.suwreti)

@dp.message(AutoMobile.suwreti)
async def save_photo(sms:types.Message,state:FSMContext):
    await state.update_data(suwreti=sms.photo[0].file_id)
    await sms.answer(text='Qanday karobkali?')
    await state.set_state(AutoMobile.karobkasi)

@dp.message(AutoMobile.karobkasi)
async def save_karobka(sms:types.Message,state:FSMContext):
    await state.update_data(karobkasi=sms.text)
    await sms.answer(text='Bahasi qansha ekenin jiberin')
    await state.set_state(AutoMobile.bahasi)

@dp.message(AutoMobile.bahasi)
async def save_bahasi(sms:types.Message,state:FSMContext):
    await state.update_data(bahasi=sms.text)
    await sms.answer(text='Probegin jazin')
    await state.set_state(AutoMobile.probegi)

@dp.message(AutoMobile.probegi)
async def save_probegi(sms:types.Message,state:FSMContext):
    # print(sms.photo[0].file_id)
    
    await state.update_data(probegi=sms.text)

    magliwmatlar = await state.get_data()
    # await sms.answer_photo(
    #     photo=types.FSInputFile(

    #     ),
        
    # )
    print(magliwmatlar)
    await bot.send_photo(
        chat_id=5570471897,
        photo=magliwmatlar['suwreti'],
        caption=f'''mashina ati:{magliwmatlar['ati']},
mashina jili:{magliwmatlar['jili']}
mashina karobkasi:{magliwmatlar['karobkasi']}
'''
    )
#     await bot.send_message(
#         chat_id=5570471897,
#         text=f'''mashina ati:{magliwmatlar['ati']},
# mashina jili:{magliwmatlar['jili']}

#     ''')
    await state.clear()



async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
