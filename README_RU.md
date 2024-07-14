<h1 align="center">
  <br>
  <a href="https://github.com/Atom244"><img src="https://raw.githubusercontent.com/Atom244/icons-for-projects/main/rndcatpreviewpng.png" alt="Random cat module" width="1024"></a>
  <br>
  rnd_cat
  <br>
</h1>

<h4 align="center">Простой модуль на Python для получения случайных изображений с кошками.</h4>

<p align="center">
  <a href="#установка">Установка</a> •
  <a href="#как-использовать">Как использовать</a> •
  <a href="#благодарности">Благодарности</a>
</p>

<a href="README.md"><kbd>**EN**</kbd></a>/<a href="README_RU.md"><kbd>**RU**</kbd></a>

## Установка

#### Модуль уже доступен на PyPi!

<a href="https://pypi.org/project/rnd-cat/"><img src="https://raw.githubusercontent.com/Atom244/icons-for-projects/main/pypicat.png" alt="Летящий кот" width="50%"></a>

- Установка с помощью [pip](https://pypi.org/project/pip/) :

```bash
pip install rnd_cat
```

- Установка с помощью [Git](https://git-scm.com) :

```bash
# Клонируйте этот репозиторий в ваш проект на Python
$ git clone https://github.com/Atom244/Random-Cat-Module.git
```

> **Примечание**
> Модуль использует библиотеку requests. Её необходимо установить.

```bash
pip install requests
```

## Как использовать

Импортируйте rnd_cat в ваш py-файл:

```py
import rnd_cat
```

#### Функции:

• cat() - Возвращает случайную кошку.  
Аргументы: filename, format

```py
import rnd_cat
rnd_cat.cat(filename='default_cat_img', format='jpg')
```

> **Примечание**
> Аргументы также дублируются в модуле, и каждая функция имеет значения по умолчанию для аргументов (их необязательно изменять).

• cat_say() - Возвращает случайную кошку, говорящую текст. Текст не поддерживает специальные символы и эмодзи.  
Аргументы: filename, format, text

```py
import rnd_cat
rnd_cat.cat_say(filename='default_cat_say_img', text='Hello', format='jpg')
```

• cat_gif() - Возвращает случайный gif с кошкой.  
Аргументы: filename

```py
import rnd_cat
rnd_cat.cat_gif(filename='default_cat_gif')
```

• cat_say_edit() - Возвращает случайную кошку, говорящую редактируемый текст.  
Аргументы: filename, format, text, fontSize, fontColor

```py
import rnd_cat
rnd_cat.cat_say_edit(filename='default_cat_gif', text='Hello', fontSize=50, fontColor='red', format='jpg')
```

• cat_tag() - Возвращает случайную кошку с тегом. Можно комбинировать несколько тегов с разделителем. [Все теги здесь](https://cataas.com/api/tags)

Аргументы: filename, format, tag

```py
import rnd_cat
rnd_cat.cat_tag(filename="default_cat_tag_img", format="jpg", tag="orange,cute")
```

• cat_tag_say() - Возвращает случайную кошку с тегом и говорящую текст.

Аргументы: filename, format, tag, text

```py
import rnd_cat
rnd_cat.cat_tag_say(filename="default_cat_tag_say_img", format="jpg", tag="orange,cute", text="Hello")
```

• cat_type() - Возвращает случайную кошку с изображением <type> (xsmall, small, medium или square).  
Аргументы: filename, format, type

```py
import rnd_cat
rnd_cat.cat_type(filename = "default_cat_type_img", format = "jpg", type = "square")
```

• cat_filter() - Возвращает случайную кошку с фильтром изображения (blur, mono, negate).

Аргументы: filename, format, filter

```py
import rnd_cat
rnd_cat.cat_filter(filename = "default_cat_filter_img", format = "jpg", filter = "mono")
```

<a href="https://pypi.org/project/rnd-cat/"><img src="https://raw.githubusercontent.com/Atom244/icons-for-projects/main/ggdd.png" alt="Летящий кот" width="20%"></a>

• cat_combo() - Сочетание большинства аргументов!  
Аргументы: filename, is_gif, is_say, filter, is_filtered, text, fontSize, fontColor, type, format

```py
import rnd_cat
rnd_cat.cat_combo(
    filename = "default_cat_combo",
    is_gif = True,
    is_say = True,
    filter = "mono",
    is_filtered = True,
    text = "Hello",
    fontSize = 20,
    fontColor = "orange",
    type = "square",
    format = "jpg",
)
```

## Благодарности

Модуль основан на получении изображений с этого сайта:

- [CATAAS](https://cataas.com/)

<h1 align="center">
  <br>
  <a href="https://github.com/Atom244"><img src="https://raw.githubusercontent.com/Atom244/icons-for-projects/main/cat.png" alt="Инопланетный кот" width="256"></a>
  <br>
  Спасибо за использование моего модуля или просмотр моего репозитория!!!
  <br>
</h1>
