import requests
import urllib.request


def cat(filename: str = "default_cat_img", format: str = "jpg"):
    """
    Will return a random cat.
    """
    img_data = requests.get("https://cataas.com/cat").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_say(
    filename: str = "default_cat_say_img", text: str = "Hello", format: str = "jpg"
):
    """
    Will return a random cat saying <text>. The text does not support special characters and emoticons or it may not work correctly.
    """
    img_data = requests.get(
        f"https://cataas.com/cat/says/{text}?fontSize=50&fontColor=white"
    ).content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_gif(filename: str = "default_cat_gif"):
    """
    Will return a random gif cat.
    """
    urllib.request.urlretrieve("https://cataas.com/cat/gif", f"{filename}.gif")


def cat_say_edit(
    filename: str = "default_cat_say_edit_img",
    text: str = "Hello",
    fontSize: int = 50,
    fontColor: str = "red",
    format: str = "jpg",
):
    """
    Will return a random cat saying <text> with text's <fontSize> and text's <fontColor>.
    """
    img_data = requests.get(
        f"https://cataas.com/cat/says/{text}?fontSize={fontSize}&fontColor={fontColor}"
    ).content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_tag(
    filename: str = "default_cat_tag_img", format: str = "jpg", tag: str = "orange,cute"
):
    """
    Will return a random cat with a <tag>, You can combine multiple tags with <tag> separator.
    """
    img_data = requests.get(f"https://cataas.com/cat/{tag}").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_tag_say(
    filename: str = "default_cat_tag_say_img",
    format: str = "jpg",
    tag: str = "orange,cute",
    text: str = "Hello",
):
    """
    Will return a random cat with a <tag> and saying <text>.
    """
    img_data = requests.get(f"https://cataas.com/cat/{tag}/says/{text}").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_type(
    filename: str = "default_cat_type_img", format: str = "jpg", type: str = "square"
):
    """
    Will return a random cat with image <type> (xsmall, small, medium or square).
    """
    img_data = requests.get(f"https://cataas.com/cat?type={type}").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_filter(
    filename: str = "default_cat_filter_img", format: str = "jpg", filter: str = "mono"
):
    """
    Will return a random cat with image filtered by <filter> (blur, mono, negate).
    """
    img_data = requests.get(f"https://cataas.com/cat?filter={filter}").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_combo(
    filename: str = "default_cat_combo",
    is_gif: bool = True,
    is_say: bool = True,
    filter: str = "mono",
    is_filtered: bool = True,
    text: str = "Hello",
    fontSize: int = 20,
    fontColor: str = "orange",
    type: str = "square",
    format: str = "jpg",
):
    """
    A mix of most of the arguments!
    """
    if is_gif == True:
        gif = "/gif"
        form = "gif"
    else:
        gif = "/"
        form = str(format)

    if is_say == True:
        say = "/says/"
        say_text = str(text + "?")
        color = str("fontColor=" + fontColor)
        size = str("fontSize=" + str(fontSize))
    else:
        say = "/"
        say_text = ""
        color = ""
        size = ""
    if is_say == False and is_gif == False:
        say = "?"
        gif = ""
    if is_filtered == True:
        filt = filter
    else:
        filt = ""

    img_data = requests.get(
        f"https://cataas.com/cat{gif}{say}{say_text}filter={filt}&{color}&{size}&type={type}"
    ).content
    with open(f"{filename}.{form}", "wb") as handler:
        handler.write(img_data)
