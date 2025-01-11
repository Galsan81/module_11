import os
from PIL import Image, ImageDraw, ImageFont


class PostCardMaker:

    def __init__(self, name, template=None, font_path=None):
        self.name = name
        # Путь к изображению-шаблону (если не передан, используется путь по умолчанию)
        self.template = "D:\\python uchoba\\module_11\\post_card.jpg" if template is None else template

        # Путь к шрифту (по умолчанию используется Arial)
        if font_path is None:
            self.font_path = "C:\\Windows\\Fonts\\ARIALN.TTF"  # Путь к шрифту Arial
        else:
            self.font_path = font_path

    def make(self, resize=False, out_path=None):
        # Проверка существования файла шаблона
        if not os.path.exists(self.template):
            raise FileNotFoundError(f"Шаблон {self.template} не найден.")

        # Открытие изображения
        im = Image.open(self.template)

        # Если нужно изменить размер
        if resize:
            w, h = im.size
            im = im.resize((w // 2, h // 2))

        # Создание объекта для рисования на изображении
        draw = ImageDraw.Draw(im)

        # Загрузка шрифта
        font = ImageFont.truetype(self.font_path, size=27)

        # Вставка первого текста (с именем)
        y = im.size[1] - 30 - (10 + font.size) * 2
        message = f"Привет, {self.name}!"
        draw.text((10, y), message, font=font, fill=(255, 0, 0))  # Красный цвет

        # Вставка второго текста
        y = im.size[1] - 50 - font.size
        message = f"С прошедшими праздниками тебя!\n Поставьте Зачет!!!"
        draw.text((10, y), message, font=font, fill=(255, 0, 0))  # Красный цвет

        # Путь для сохранения изображения (по умолчанию 'probe.jpg')
        out_path = out_path if out_path else 'probe.jpg'

        # Сохранение изображения
        im.save(out_path)
        print(f'Post card saved as {out_path}')


if __name__ == '__main__':
    # Создание объекта и генерация открытки
    maker = PostCardMaker(name='Проверяющий')
    maker.make(resize=True)
