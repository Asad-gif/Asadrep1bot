from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

database = list()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dictionary_users = dict()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравствуйте!\nЭто anticorruptionBot!\nНапишите ваше имя, затем нажмите на /help и следуйте инструкции")





@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Чтобы начать рассматривать дело, мы должны получить некоторые данные.\nДля начала:\nОтправьте паспорт в pdf-формате и комментарий с места событий в Word-формате")




@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def download_doc(message: types.Message):
    # Скачивание в каталог с ботом с созданием подкаталогов по типу файла
    await message.document.download()

    await message.reply("Нажмите на /argue, если вы всё отправили. Если не отправили - отправьте")




@dp.message_handler(commands=['argue'])
async def process_help_command(message: types.Message):
    await message.reply("Докажите, что вы говорите правду, оставив фото с места события.")


@dp.message_handler(content_types=["photo"])
async def download_photo(message: types.Message):
    # Убедитесь, что каталог /tmp/somedir существует!
    await message.photo[-1].download()
    await message.reply("Ждите ответа!")








@dp.message_handler()
async def echo_message(msg: types.Message):
    global dictionary_users  # empty dictionary of users
    print("# User Name", msg.from_user.first_name)
    print("# Last Name", msg.from_user.last_name)
    print("id", msg.from_user.id)
    print("Username: ", msg.from_user.username)
    print("language: ", msg.from_user.locale)



    name = msg.from_user.first_name
    dictionary_users[name] = dictionary_users.get(name, 0) + 1



executor.start_polling(dp)


if __name__ == '__main__':
    executor.start_polling(dp)