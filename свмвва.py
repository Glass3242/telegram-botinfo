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

@dp.message(Command('gameinfo'))
async def cmd_smart(message:types.Message):
    await message.answer('\n1. /Gta5 \n2. /Skyrim \n3. /Minecraft \n4. /Assasin_Creed \n5. /Cyberpunk2077 \n6. /The_Wither \n7. /STALKER \n8. /Portal \n9. /Metro_Last_Light \n10. /Dota2 \n11. /Call_of_Duty \n12. /Far_Cry \n13. /CSGO \n14. /Fortnite \n15. /Rocket_League')

@dp.message(Command('Gta5'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре action-adventure с открытым миром, разработанная компанией Rockstar North и изданная компанией Rockstar Games. Изначально игра была выпущена для игровых консолей PlayStation 3 и Xbox 360 в 2013 году, в 2014 году переиздана для PlayStation 4 и Xbox One, в 2015 году для Windows и в 2022 году для PlayStation 5 и Xbox Series X/S. ')

@dp.message(Command('Skyrim'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре action/RPG с открытым миром, разработанная студией Bethesda Game Studios и выпущенная компанией Bethesda Softworks. Это пятая часть в серии The Elder Scrolls. Игра была выпущена 11 ноября 2011 года для Windows, PlayStation 3 и Xbox 360. Позже для неё были выпущены три загружаемых дополнения под названиями Dawnguard, Hearthfire и Dragonborn, позже объединённых в издании The Elder Scrolls V: Skyrim — Legendary Edition. В 2016 году Bethesda перевыпустила игру в виде издания Special Edition, а в 2021 году — Anniversary Edition; эти издания отличались от оригинала улучшенной графикой и включали в себя различные дополнения и модификации.')

@dp.message(Command('Minecraft'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная инди-игра в жанре песочницы, созданная шведским программистом Маркусом Перссоном и выпущенная его студией Mojang AB. В 2009 году Перссон опубликовал начальную версию игры; в конце 2011 года была выпущена стабильная версия для компьютеров Windows, Linux и macOS с распространением через официальный сайт. В последующие годы Minecraft была портирована на мобильные устройства под управлением Android, iOS и Windows Phone; на игровые приставки PlayStation 3, PlayStation 4, PlayStation Vita, Xbox 360, Xbox One')


@dp.message(Command('Assasin_Creed'))
async def cmd_smart(message:types.Message):
    await message.answer('медиафраншиза компании Ubisoft, основанная на серии компьютерных игр. Первая игра вышла в 2007 году, последняя — Assassin’s Creed Mirage — 5 октября 2023 года. Большинство частей франшизы являются играми в жанре приключенческого боевика с открытым миром, где особое внимание уделяется скрытому перемещению и паркуру.')

@dp.message(Command('Cyberpunk2077'))
async def cmd_smart(message:types.Message):
    await message.answer('компьютерная игра в жанре Action/RPG в открытом мире, разработанная и изданная польской студией CD Projekt[14]. Действие игры происходит в 2077 году в Найт-Сити, вымышленном североамериканском городе из вселенной Cyberpunk, разработанной Майком ПондсмитомПерейти к разделу «#Сюжет». Игрок управляет настраиваемым протагонистом по имени Ви, который работает наёмником и владеет навыками взлома и бояПерейти к разделу «#Игровой процесс».')

@dp.message(Command('The_Wither'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная ролевая игра, разработанная польской компанией CD Projekt RED по мотивам одноимённой серии романов польского писателя Анджея Сапковского. Релиз игры на платформе Windows состоялся 24 октября 2007 года — в России, 26 октября — в Европе и 30 октября 2007 года — в США[7]. В 2012 году вышла версия для OS X.')

@dp.message(Command('STALKER'))
async def cmd_smart(message:types.Message):
    await message.answer('серия игр, разработанная украинской компанией GSC Game World. Создана в жанре шутера от первого лица и survival horror с элементами ролевой игры и action-adventure. События игр разворачиваются в наше время, в альтернативном мире на территории Украины, в Чернобыльской зоне отчуждения. Согласно сюжету серии, в 2006 году зона подверглась неожиданному аномальному воздействию (Выбросу), в результате которого физические, химические и биологические процессы на данной территории изменились. Появилось множество аномалий, артефактов и мутантов. В идеях игры можно увидеть влияние повести братьев Стругацких «Пикник на обочине» и снятого по ней фильма Андрея Тарковского Сталкер 2.')

@dp.message(Command('Portal'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре головоломки от первого лица[4][5], разработанная американской компанией Valve Corporation и выпущенная 10 октября 2007 года на платформах Windows и Xbox 360 в составе сборника The Orange Box. Портированная версия для приставки PlayStation 3 разрабатывалась британской студией EA UK и была выпущена 11 декабря 2007 года.')

@dp.message(Command('Metro_Last_Light'))
async def cmd_smart(message:types.Message):
    await message.answer('«Метро: Последний свет», в России издана под названием «Метро 2033: Луч надежды»[4]) — компьютерная игра в жанре постапокалиптического шутера от первого лица с элементами survival horror и стелса, разработанная украинской студией 4A Games и изданная британской компанией Deep Silver на Windows, PlayStation 3 и Xbox 360 в мае 2013 года. Игра является прямым продолжением первой части игровой франшизы Вселенной Метро 2033, вышедшей в 2010 году.')

@dp.message(Command('Dota2'))
async def cmd_smart(message:types.Message):
    await message.answer(' многопользовательская командная компьютерная игра в жанре MOBA, разработанная и изданная корпорацией Valve. Игра является продолжением DotA — пользовательской карты-модификации для игры Warcraft III: Reign of Chaos и дополнения к ней Warcraft III: The Frozen Throne. Игра изображает сражение на карте особого вида; в каждом матче участвуют две команды по пять игроков, управляющих разными «героями» — персонажами с различными наборами способностей и характеристиками. Для победы в матче команда должна уничтожить особый объект — «крепость», принадлежащий вражеской стороне, и защитить от уничтожения собственную «крепость». Dota 2 работает по модели free-to-play с элементами микроплатежей.')

@dp.message(Command('Call_of_Duty'))
async def cmd_smart(message:types.Message):
    await message.answer('серия компьютерных игр в жанре шутера от первого лица, выпускаемая американской компанией Activision. Разработкой игр серии занимались такие студии, как Infinity Ward, Treyarch и Sledgehammer Games. Ранние игры серии, начиная с самой первой игры 2003 года, были посвящены Второй мировой войне; в дальнейшем в рамках серии выходили и игры, действие которых разворачивалось во времена холодной войны, в недалёком будущем, и даже в космосе. Отдельные игры серии, объединённые общим временем действия, связаны друг с другом также повествованием и персонажами.')

@dp.message(Command('Far_Cry'))
async def cmd_smart(message:types.Message):
    await message.answer('франшиза, под которой выпускается серия компьютерных игр в жанре шутера от первого лица и action-adventure. Первая игра в серии, разработанная немецкой студией Crytek, демонстрировала возможности инновационного на тот момент движка CryEngine; последующие игры серии, созданные канадской студией Ubisoft Montreal и другими дочерними студиями компании Ubisoft, предлагают игроку обширные открытые миры, в которых игрок может самостоятельно искать себе интересные места и занятия. На 2021 год в серии выпущено шесть основных игр, а также ряд спин-оффов и дополненных версий.')

@dp.message(Command('CSGO'))
async def cmd_smart(message:types.Message):
    await message.answer(' многопользовательская компьютерная игра, разработанная компаниями Valve и Hidden Path Entertainment. Выпуск игры для персональных компьютеров на операционных системах Windows и macOS, также игровых приставках PlayStation 3 и Xbox 360 состоялся 21 августа 2012 года. Версия игры для Linux была выпущена в 2014 году[1], а в 2016 году игра, в рамках программы обратной совместимости, стала доступна на Xbox One[3]. В сентябре 2018 года была выпущена бесплатная версия с возможностью игры с реальными игроками и с ботами. Позже, в декабре того же года игра стала полностью бесплатной.')

@dp.message(Command('Fortnite'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная онлайн-игра, разработанная американской компанией Epic Games совместно с People Can Fly и выпущенная в ранний доступ в 2017 году[7]. Fortnite предлагает игрокам на выбор три раздельных режима: Fortnite: Save the World, кооперативный симулятор выживания с открытым миром, в котором игрокам предлагается сообща отбиваться от монстров, похожих на зомби, с помощью оружия и различных построек; Fortnite: Battle Royale — соревновательный режим в жанре королевской битвы')

@dp.message(Command('Rocket_League'))
async def cmd_smart(message:types.Message):
    await message.answer('аркадная гоночная игра в жанре футбола, разработанная и изданная компанией Psyonix для Windows, PlayStation 4. Выход игры состоялся 7 июля 2015 года для платформ Windows и PlayStation 4. В 2016 году игра выпускается для Xbox One[2] и для Linux и macOS, но поддержка последних была прекращена в 2020 году. В 2017 выпускается версия для Nintendo Switch. До конца лета 2020 года Psyonix планировала перевести игру из премиальной игры в бесплатную модель, но по непредвиденным обстоятельствам стала бесплатной только 23 сентября 2020 года.')
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
