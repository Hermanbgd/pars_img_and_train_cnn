from PIL import Image

list_with_fruits = [['яблоко', 'apple'], ['банан', 'banana'], ['голубика', 'blueberry'], ['вишня', 'cherry'],
                    ['киви', 'kiwi'], ['лайм', 'lime'], ['апельсин', 'orange'], ['малина', 'raspberry'],
                    ['клубника', 'strawberry'], ['арбуз', 'watermelon']]

for fruit in list_with_fruits:
    for i in range(1, 5001):
        try:
            im = Image.open(f"fruits_images/{fruit[1]}_images/{fruit[1]}.{i}.jpg")
        except IOError:
            print(f"problem with file {fruit[1]}.{i}")
