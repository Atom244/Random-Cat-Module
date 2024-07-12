import requests
import urllib.request


def cat(filename: str = 'default_cat_img', format: str = 'jpg'):
    """
    Will return a random cat.
    """
    img_data = requests.get('https://cataas.com/cat').content
    with open(f'{filename}.{format}', 'wb') as handler:
        handler.write(img_data)


def cat_say(filename: str = 'default_cat_say_img', text: str = 'Hello', format: str = 'jpg'):
    """
    Will return a random cat saying <text>. The text does not support special characters and emoticons or it may not work correctly.
    """
    img_data = requests.get(f'https://cataas.com/cat/says/{text}?fontSize=50&fontColor=white').content
    with open(f'{filename}.{format}', 'wb') as handler:
        handler.write(img_data)


def cat_gif(filename: str = 'default_cat_gif'):
    """
    Will return a random gif cat.
    """
    urllib.request.urlretrieve('https://cataas.com/cat/gif', f'{filename}.gif')


def cat_say_edit(filename: str = 'default_cat_say_edit_img', text: str = 'Hello', fontSize: int = 50, fontColor: str = 'red', format: str = 'jpg'):
    """
    Will return a random cat saying <text> with text's <fontSize> and text's <fontColor>.
    """
    img_data = requests.get(f'https://cataas.com/cat/says/{text}?fontSize={fontSize}&fontColor={fontColor}').content
    with open(f'{filename}.{format}', 'wb') as handler:
        handler.write(img_data)
