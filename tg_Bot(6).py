import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from keras.models import load_model
import keras.utils as image
import numpy as np

BOT_TOKEN = "6899719830:AAHC9G9JzX4JupoQkgxkkrooDwLGmJaJ06U"

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

list_with_fruits = [['яблоко', 'apple'], ['банан', 'banana'], ['голубика', 'blueberry'], ['вишня', 'cherry'],
                    ['киви', 'kiwi'], ['лайм', 'lime'], ['апельсин', 'orange'], ['малина', 'raspberry'],
                    ['клубника', 'strawberry'], ['арбуз', 'watermelon']]


def load_image(img_path):

    img = image.load_img(img_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    return img_tensor

model = load_model("my_model_v5")

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ распознаю яблоко, банан, голубику, вишню, киви, лайм, апельсин, '
                         'малину, клубнику и арбуз!\nПришли мне картинку')

@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.bot.download(file=message.photo[-1].file_id, destination="my_test_img.jpg")
    new_image = load_image("my_test_img.jpg")
    pred = model.predict(new_image)
    indx = np.argmax(pred)
    answer = list_with_fruits[indx][0]
    print(f"Это похоже на: {answer}")
    await message.reply(text=answer)
    os.remove("my_test_img.jpg")

@dp.message()
async def send_echo(message: Message):
    await message.reply(text="Я понимаю только картинки, отправь мне картинку")

if __name__ == '__main__':
    dp.run_polling(bot)
