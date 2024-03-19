import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6891079855:AAE8FJuJ9H8gId0Vs7CZQL88NmaOYsP1zNw")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer("Приветствую тебя! Этот бот поможет тебе выбрать любимую игру и предоставит тебе информацию о ней!")

        return
    else:
        await message.answer(f'Приветствую тебя,{command.args}! Этот бот поможет тебе выбрать любимую игру и предоставит тебе информацию о ней!')
        return

@dp.message(F.text.lower()=='привет')
async def cmd_start(message: types.Message):
    await message.answer('Привет, я BotGame! Ты можешь найти игру себе по душе, а так же информацию о ней')

@dp.message(F.text.lower()=='кто тебя создал?')
async def cmd_start(message: types.Message):
    await message.answer('Меня создал один великолепный создатель Finzyyy!')

@dp.message(F.text.lower()=='на каком языке ты написан?')
async def cmd_smart(message: types.Message):
    await message.answer('Я написан на языке Python')

@dp.message(Command("help"))
async def cmd_smart(message: types.Message):
    await message.answer('\n1. /start \n2./populargame \n3. /horrorgames \n4. /fantasygames \n5. /actiongames \n6. /simulatorgames \n7. /racinggames \n8. /gameinfo')

@dp.message(Command("populargame"))
async def cmd_smart(message: types.Message):
    await message.answer('\n1. Grand Then Auto 5 \n2. Skyrim \n3. Minecraft \n4. Assasin Creed \n5. Cyberpunk 2077 \n6. The Wither \n7. S.T.A.L.K.E.R \n8. Portal \n9. Metro. Last light \n10. Dota 2 \n11. Call of Duty \n12. Far Cry 1,2,3,4,5 \n13. CS:GO \n14. Fortnite \n15. Rocket League  ')

@dp.message(Command("horrorgames"))
async def cmd_smart(message: types.Message):
    await message.answer('\n1. Dead Space \n2. Layers of Fear \n3. Resident Evil 2: Remake \n4. Resident Evil 7: Biohazard \n5. P.T. \n6. The Beast Inside \n7. Song of Horror \n8. Phasmophobia \n9. Alan Wake 2 \n10. Little Nightmares \n11. The Mortuary Assistant \n12. Ghost Watchers \n13. The Evil Within ')

@dp.message(Command("actiongames"))
async def cmd_smart(message: types.Message):
    await message.answer('\n1. Atomic Heart \n2. Starfield \n3. Hogwarts Legacy \n4. Lords of the Fallen \n5. Everspace 2 \n6. One Piece Odyssey \n7. Atlas Fallen \n8. Blazing Sails \n9. Deceit 2 \n10. PERISH \n11. Lunacid \n12. Paranoid \n13. Sea of Craft \n14. Dead Island 2:Haus')

@dp.message(Command('simulatorgames'))
async def cmd_smart(message: types.Message):
    await message.answer('\n1. Shieldwall \n2. Thief Simulator 2 \n3. Bum Simulator \n4. Farmer Life \n5. Contraband Police \n6. EA Sports FC 24 \n7. Car for Sale Simulator 2023 \n8. House Flipper 2 \n9. Russian Train Trip 2 \n10. NBA 2K24 \n11. Metro Simulator 2 \n12. Euro Truck Simulator 2 \n13. In Truck Driving \14. Arma Reforger ')

@dp.message(Command('racinggames'))
async def cmd_smart(message: types.Message):
    await message.answer('\n1. Forza Horizon 5 \n2. Need for speed Heat \n3. Gran turismo 7 \n4. The crew 2 \n5 Assetto Corsa Competizione \n6. Forza Motorsport 7 \n7. Grid 2 \n8. The Crew \n9. Dirt Rally 2 \n10. Shift 2 Unleashed')
# Запуск процесса поллинга новых апдейтов

@dp.message(Command('fantasygames'))
async def cmd_smart(message:types.Message):
    await message.answer('\n1. Genshin Impact \n2. Dota 2 \n3. World of Warcraft \n4. Bloodborne \n5. The Wither 2 \n6. The wither 3 \n7 Dark Souls 2 \n8. Hollow Knight \n9. Sekiro: Shadows Die Twice \n10. Nioh')
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
