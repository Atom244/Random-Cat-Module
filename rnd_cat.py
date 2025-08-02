import requests
import urllib.request


def cat(filename: str = "default_cat_img", format: str = "jpg") -> None:
    """
    Download a random cat image.

    Args:
        filename (str): The name of the saved image file without extension.
        format (str): The image format, typically 'jpg' or 'png'.

    Returns:
        None
    """
    img_data = requests.get("https://cataas.com/cat").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_say(filename: str = "default_cat_say_img", text: str = "Hello", format: str = "jpg") -> None:
    """
    Download a random cat image with a text message.

    Args:
        filename (str): The name of the saved image file without extension.
        text (str): Text that the cat will say.
        format (str): Image format to save as, usually 'jpg'.

    Returns:
        None
    """
    img_data = requests.get(f"https://cataas.com/cat/says/{text}?fontSize=50&fontColor=white").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_gif(filename: str = "default_cat_gif") -> None:
    """
    Download a random animated cat GIF.

    Args:
        filename (str): The name of the saved gif file without extension.

    Returns:
        None
    """
    urllib.request.urlretrieve("https://cataas.com/cat/gif", f"{filename}.gif")


def cat_say_edit(filename: str = "default_cat_say_edit_img", text: str = "Hello",
                 fontSize: int = 50, fontColor: str = "red", format: str = "jpg") -> None:
    """
    Download a cat image with custom text, font size and color.

    Args:
        filename (str): The name of the saved image file without extension.
        text (str): Message text for the cat.
        fontSize (int): Font size for the text.
        fontColor (str): Font color for the text.
        format (str): Image format, like 'jpg' or 'png'.

    Returns:
        None
    """
    img_data = requests.get(
        f"https://cataas.com/cat/says/{text}?fontSize={fontSize}&fontColor={fontColor}"
    ).content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_tag(filename: str = "default_cat_tag_img", format: str = "jpg", tag: str = "orange,cute") -> None:
    """
    Download a random cat image filtered by specific tags.

    Args:
        filename (str): Name of output file.
        format (str): Image format to save as.
        tag (str): Comma-separated tags to filter cats.

    Returns:
        None
    """
    img_data = requests.get(f"https://cataas.com/cat/{tag}").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_tag_say(filename: str = "default_cat_tag_say_img", format: str = "jpg",
                tag: str = "orange,cute", text: str = "Hello") -> None:
    """
    Download a tagged cat image with a text message.

    Args:
        filename (str): Output filename.
        format (str): Format of image.
        tag (str): Tags to filter cats.
        text (str): Message text.

    Returns:
        None
    """
    img_data = requests.get(f"https://cataas.com/cat/{tag}/says/{text}").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_type(filename: str = "default_cat_type_img", format: str = "jpg", type: str = "square") -> None:
    """
    Download a cat image with specific shape type.

    Args:
        filename (str): Output file name.
        format (str): Image format.
        type (str): Image type such as 'square', 'medium', etc.

    Returns:
        None
    """
    img_data = requests.get(f"https://cataas.com/cat?type={type}").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_filter(filename: str = "default_cat_filter_img", format: str = "jpg", filter: str = "mono") -> None:
    """
    Download a filtered cat image.

    Args:
        filename (str): Name of output file.
        format (str): Format of image.
        filter (str): Filter to apply ('blur', 'mono', 'negate').

    Returns:
        None
    """
    img_data = requests.get(f"https://cataas.com/cat?filter={filter}").content
    with open(f"{filename}.{format}", "wb") as handler:
        handler.write(img_data)


def cat_combo(filename: str = "default_cat_combo", is_gif: bool = True, is_say: bool = True,
              filter: str = "mono", is_filtered: bool = True, text: str = "Hello",
              fontSize: int = 20, fontColor: str = "orange", type: str = "square",
              format: str = "jpg") -> None:
    """
    Download a cat image or gif with optional filters, text, and styling.

    Args:
        filename (str): Output filename.
        is_gif (bool): Whether to download as GIF.
        is_say (bool): Whether to include text.
        filter (str): Image filter to apply.
        is_filtered (bool): Whether filtering is enabled.
        text (str): Message text.
        fontSize (int): Font size for text.
        fontColor (str): Font color.
        type (str): Image shape type.
        format (str): Format of image (used if not gif).

    Returns:
        None
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
