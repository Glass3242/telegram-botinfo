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
    await message.answer('\n1. /Gta5 \n2. /Skyrim \n3. /Minecraft \n4. /Assasin_Creed \n5. /Cyberpunk2077 \n6. /The_Wither \n7. /STALKER \n8. /Portal \n9. /Metro_Last_Light \n10. /Dota2 \n11. /Call_of_Duty \n12. /Far_Cry \n13. /CSGO \n14. /Fortnite \n15. /Rocket_League \n16. /Dead_Space \n17. /Layers_of_Fear \n18. /Resident_Evil2_Remake \n19. /Resident_Evil7_Remake \n20. /PT \n21. /The_Beast_Inside \n22. /Song_of_Horror \n23. /Phasmophobia \n24. /Alan_Wake2 \n25. /Little_Nightmares \n26. /The_Mortuary_Assistant \n27. /Ghost_Wathers \n28. /The_Evil_Within \n29. /Genshin_Impact \n30. /Dota2 \n31. /World_of_Warcraft \n32. /Bloodborne \n33. /The_Wither2 \n34. /The_Wither3 \n35. /Dark_Souls2 \n36. /Hollow_Knight \n37. /Sekiro_Shadows_Die_Twice \n38. /Nioh ')

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

@dp.message(Command('Dead_Space'))
async def cmd_smart(message:types.Message):
    await message.answer('медиафраншиза, объединяющая ряд компьютерных игр в жанре survival horror, анимационных фильмов, книг и комиксов по их мотивам. Лежащие в основе медиафраншизы игры были разработаны студией Visceral Games под руководством геймдизайнера Глена Скофилда; их издавала компания Electronic Arts. Действие игр серии, выполненных в духе научной фантастики и фильмов ужасов, происходит в будущем — в XXVI веке, в космосе и на других планетах')

@dp.message(Command('Layers_of_Fear'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре психологического хоррора, разработанная польской студией Bloober Team и изданная Aspyr. Выпуск игры состоялся 16 февраля 2016 года для персональных компьютеров на операционных системах Windows, Linux и macOS, а также для игровых приставок PlayStation 4 и Xbox One. 21 февраля 2018 года вышла Layers of Fear: Legacy — версия игры для Nintendo Switch.')

@dp.message(Command('Resident_Evil2_Remake'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре survival horror, разработанная Capcom R&D Division 1 и изданная Capcom 25 января 2019 года для PlayStation 4, Xbox One и Windows. Ремейк одноимённой игры 1998 года. Сюжетная кампания игры рассказывает о полицейском-новичке Леоне Скотте Кеннеди и студентке Клэр Редфилд, которые пытаются выбраться из города Раккун-сити, поражённого зомби-вирусом.')

@dp.message(Command('Resident_Evil7_Remake'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре survival horror, являющаяся девятой по счёту в основной серии Resident Evil[2]. Разработана и выпущена компанией Capcom в 2017 году для PlayStation 4, Xbox One и Microsoft Windows. Версия игры для PlayStation 4 также поддерживает режим виртуальной реальности через шлем PlayStation VR. В июне 2022 года были выпущены версии для PlayStation 5 и Xbox Series X/S. Выпущена в честь 20-летия серии игр Resident Evil.')

@dp.message(Command('PT'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре психологического хоррора, разработанная Kojima Productions под псевдонимом «7780s Studio» и изданная Konami. Игра была срежиссирована и разработана Хидео Кодзимой в сотрудничестве с режиссером Гильермо дель Торо и была выпущена бесплатно на PlayStation 4.')

@dp.message(Command('The_Beast_Inside'))
async def cmd_smart(message:types.Message):
    await message.answer('то хоррор-адвенчура, в которой криптоаналитику ЦРУ Адаму предстоит расследовать таинственное убийство 100-летней давности, ставящее под угрозу его собственную жизнь. По сюжету Адам со своей женой Эммой переезжает в тихий загородный дом, чтобы спокойно поработать над взломом военного шифра и изменить ход Холодной войны, но обнаруженный в подвале дневник внезапно запускает в настоящее кошмарные призраки прошлого.')

@dp.message(Command('Song_of_Horror'))
async def cmd_smart(message:types.Message):
    await message.answer('это игра в жанре приключения. По сюжету игры знаменитый писатель Себастьян П. Хашер пропал вместе со всей своей семьёй. Встревожившись, его редактор отправил помощника в дом писателя на поиски, но тот так и не вернулся... Эти исчезновения запускают цепочку событий, раскрывающих нечто ужасное: причиной всему оказывается безымянное тёмное существо, известное как Присутствие.')

@dp.message(Command('Phasmophobia'))
async def cmd_smart(message:types.Message):
    await message.answer('многопользовательская компьютерная игра в жанре survival horror, разработанная и выпущенная британской студией Kinetic Games. Игра была выпущена в Steam для Windows в сентябре 2020 года в раннем доступе вместе с поддержкой VR. В Phasmophobia игроки принимают на себя роли охотников за привидениями, исследующих тот или иной дом в поисках паранормальной активности; игра использует технологию распознавания речи, так что обитающее в доме привидение реагирует на речь игроков в голосовом чате. Phasmophobia приобрела значительную популярность благодаря видеороликам и стримингу в сервисах Twitch и YouTube.')

@dp.message(Command('Alan_Wake2'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре survival-horror, разработанная Remedy Entertainment и изданная Epic Games Publishing. Игра является прямым продолжением Alan Wake, вышедшей в 2010 году. Игра выпущена на платформах Microsoft Windows, PlayStation 5 и Xbox Series X/S 27 октября 2023 года.')

@dp.message(Command('Little_Nightmares'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре платформера с элементами квеста и хоррора, разработанная шведской компанией Tarsier Studios и выпущенная компанией Bandai Namco Entertainment. Игра вышла 28 апреля 2017 года на платформах Windows, PlayStation 4, Xbox One. 12 декабря 2023 года вышло мобильное издание игры на iOS и Android.')

@dp.message(Command('The_Mortuary_Assistant'))
async def cmd_smart(message:types.Message):
    await message.answer(' это игра в жанрах ужасов 2022 года, разработанная DarkStone Digital и изданная DreadXP. Действие происходит в 1998 году в маленьком городке в штате Коннектикут, игроки управляют недавно нанятым помощником в морге с привидениями.')

@dp.message(Command('Ghost_Wathers'))
async def cmd_smart(message:types.Message):
    await message.answer('это кооперативный хоррор, в котором игроки посещают зловещие заброшенные здания и пытаются найти и поймать обитающих в них призраков. В режиме кооператива исследуют объекты четыре человека, которым противостоят десять видов различных призраков. На вооружении игроков двадцать точных инструментов, с помощью которых можно найти все улики и определить ауру приведения.')

@dp.message(Command('The_Evil_Within'))
async def cmd_smart(message:types.Message):
    await message.answer('компьютерная игра в жанрах survival horror и шутера от третьего лица, разработанная компанией Tango Gameworks и выпущенная компанией Bethesda Softworks для платформ Windows, PlayStation 3, Xbox 360, PlayStation 4 и Xbox One в 2014 году. Игра была разработана под руководством Синдзи Миками, создателя серии Resident Evil. Она не имеет сюжетной связи с Resident Evil, но включает в себя ряд схожих тем, образов и элементов геймплея.')

@dp.message(Command('Genshin_Impact'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре action-adventure с открытым миром и элементами RPG, разработанная китайской компанией miHoYo Limited. Игра распространяется посредством цифровой дистрибуции по модели free-to-play, но имеет внутриигровой магазин, использующий реальную валюту. В основе Genshin Impact лежит система «гатя», называемая в игре «молитвой».')

@dp.message(Command('Dota2'))
async def cmd_smart(message:types.Message):
    await message.answer(' многопользовательская командная компьютерная игра в жанре MOBA, разработанная и изданная корпорацией Valve. Игра является продолжением DotA — пользовательской карты-модификации для игры Warcraft III: Reign of Chaos и дополнения к ней Warcraft III: The Frozen Throne. Игра изображает сражение на карте особого вида; в каждом матче участвуют две команды по пять игроков, управляющих разными «героями» — персонажами с различными наборами способностей и характеристиками. Для победы в матче команда должна уничтожить особый объект — «крепость», принадлежащий вражеской стороне, и защитить от уничтожения собственную «крепость». Dota 2 работает по модели free-to-play с элементами микроплатежей.')

@dp.message(Command('World_of_Warcraft'))
async def cmd_smart(message:types.Message):
    await message.answer(' массовая многопользовательская ролевая онлайн-игра, разработанная и издаваемая компанией Blizzard Entertainment. Действие World of Warcraft происходит в фэнтезийной вселенной Warcraft. Игра тесно связана с предыдущими играми серии — стратегиями в реальном времени; каждый игрок управляет одним персонажем и может взаимодействовать с другими игроками в общем виртуальном мире. Игра была анонсирована в 2001 году и выпущена 23 ноября 2004 года, к 10-летней годовщине Warcraft: Orcs & Humans.')

@dp.message(Command('Bloodborne'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре Action/RPG, разработанная совместно японскими компаниями FromSoftware и SCE Japan Studio эксклюзивно для игровой приставки PlayStation 4 под руководством геймдизайнера Хидэтаки Миядзаки. Выпуск игры состоялся 24 марта 2015 года. 24 ноября того же года состоялся релиз единственного дополнения к игре — Bloodborne: The Old Hunters.')

@dp.message(Command('The_Wither2'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная ролевая игра, разработанная польской компанией CD Projekt RED по мотивам серии романов «Ведьмак» известного польского писателя Анджея Сапковского, продолжение (сиквел) компьютерной игры «Ведьмак» 2007 года выпуска. Игра вышла 16 мая 2011 года — в России, 17 мая — в Европе и США и 17 апреля 2012 года на Xbox 360[. В мае 2015 года состоялся релиз третьей части серии — «Ведьмак 3: Дикая Охота».')

@dp.message(Command('The_Wither3'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре action/RPG, разработанная и изданная польской студией CD Projekt RED. Изначально игра была выпущена 19 мая 2015 года на Windows, PlayStation 4 и Xbox One, затем 15 октября 2019 года на Nintendo Switch, а 14 декабря 2022 года — на PlayStation 5 и Xbox Series X/S. Является продолжением игр «Ведьмак» (2007) и «Ведьмак 2: Убийцы королей» (2011). Это третья игра, действие которой происходит в литературной вселенной книжной серии «Ведьмак», созданной польским писателем Анджеем Сапковским, а также последняя, которая повествует о приключениях Геральта из Ривии.')

@dp.message(Command('Dark_Souls2'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре Action/RPG с открытым миром, разработанная и выпущенная компанией From Software для Xbox 360, PlayStation 3 и Microsoft Windows в 2014 году. За пределами Японии изданием игры занималась Bandai Namco. Игра является продолжением Dark Souls (2011).')

@dp.message(Command('Hollow_Knight'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре метроидвания, выпущенная инди-студией Team Cherry 24 февраля 2017 года для Windows. Месяцем позже была портирована разработчиками на Linux и macOS. Разработка игры была спонсирована через сервис Kickstarter.')

@dp.message(Command('Sekiro_Shadows_Die_Twice'))
async def cmd_smart(message:types.Message):
    await message.answer(' компьютерная игра в жанре Action-adventure, разработанная японской компанией FromSoftware и изданная Activision (издателем на территории Японии была сама FromSoftware) для платформ Microsoft Windows, PlayStation 4 и Xbox One. Выход игры состоялся 22 марта 2019 года.')

@dp.message(Command('Nioh'))
async def cmd_smart(message:types.Message):
    await message.answer('компьютерная игра в жанре action/RPG с историческим уклоном, разработанная японской студией Team Ninja. Игра издана компаниями Koei Tecmo и Sony Interactive Entertainment для PlayStation 4. Изначально игра была анонсирована как Oni в 2004 году. В сентябре 2015 игра была вновь представлена публике с новым названием Nioh. 7 ноября 2017 года была выпущена версия Nioh для Windows.')
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
