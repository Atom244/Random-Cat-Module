<h1 align="center">
  <br>
  <a href="https://github.com/Atom244"><img src="https://raw.githubusercontent.com/Atom244/icons-for-projects/main/rndcatpreviewpng.png" alt="Random cat module" width="1024"></a>
  <br>
  rnd_cat
  <br>
</h1>

<h4 align="center">A simple python module for receiving random images with cats.</h4>

<p align="center">
  <a href="#installing">Installing</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a>

</p>

[![GitHub tag](https://img.shields.io/badge/repo-Random_Cat_Module-green)](https://github.com/Atom244/Random-Cat-Module/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](/LICENSE)  
<a href="README.md"><kbd>**EN**</kbd></a>/<a href="README_RU.md"><kbd>**RU**</kbd></a>



## Installing

#### The module is already on PyPi!

<a href="https://pypi.org/project/rnd-cat/"><image src="https://raw.githubusercontent.com/Atom244/icons-for-projects/main/pypicat.png" alt="Flying cat" width="50%"></a>

- Installing with [pip](https://pypi.org/project/pip/) :

```bash
pip install rnd_cat
```

- Installing with [Git](https://git-scm.com) :

```bash
# Clone this repository to your python project
$ git clone https://github.com/Atom244/Random-Cat-Module.git
```

> **Note**
> The module uses the requests library. It will need to be installed.

```bash
pip install requests
```

## How To Use

Import rnd_cat to your py-file:

```py
import rnd_cat
```

#### Functions:

• cat() - Will return a random cat.  
Arguments: filename, format

```py
import rnd_cat
rnd_cat.cat(filename='default_cat_img', format='jpg')
```

> **Note**
> The arguments are also duplicated in the module, and each function has default values for the arguments (it is not necessary to edit them)

• cat_say() - Will return a random cat saying text. The text does not support special characters and emoticons.  
Arguments: filename, format, text

```py
import rnd_cat
rnd_cat.cat_say(filename='default_cat_say_img', text='Hello', format='jpg')
```

• cat_gif() - Will return a random cat gif.  
Arguments: filename

```py
import rnd_cat
rnd_cat.cat_gif(filename='default_cat_gif')
```

• cat_say_edit() - Will return a random cat saying editable text.  
Arguments: filename, format, text, fontSize, fontColor

```py
import rnd_cat
rnd_cat.cat_say_edit(filename='default_cat_gif', text='Hello', fontSize=50, fontColor='red', format='jpg')
```

• cat_tag() - Will return a random cat with a tag, You can combine multiple tags with tag separator. [All tags here](https://cataas.com/api/tags)

Arguments: filename, format, tag

```py
import rnd_cat
rnd_cat.cat_tag(filename="default_cat_tag_img", format="jpg", tag="orange,cute")
```

• cat_tag_say() - Will return a random cat with a tag and saying text.

Arguments: filename, format, tag, text

```py
import rnd_cat
rnd_cat.cat_tag_say(filename="default_cat_tag_say_img", format="jpg", tag="orange,cute", text="Hello")
```

• cat_type() - Will return a random cat with image <type> (xsmall, small, medium or square).  
Arguments: filename, format, type

```py
import rnd_cat
rnd_cat.cat_type(filename = "default_cat_type_img", format = "jpg", type = "square")
```

• cat_filter() - Will return a random cat with image filtered by filter (blur, mono, negate).

Arguments: filename, format, filter

```py
import rnd_cat
rnd_cat.cat_filter(filename = "default_cat_filter_img", format = "jpg", filter = "mono")
```

<a href="https://pypi.org/project/rnd-cat/"><image src="https://raw.githubusercontent.com/Atom244/icons-for-projects/main/ggdd.png" alt="Flying cat" width="20%"></a>

• cat_combo() - A mix of most of the arguments!  
Arguments: filename, is_gif, is_say, filter, is_filtered, text, fontSize, fontColor, type, format

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

## Credits

The module is based on getting images from this site:

- [CATAAS](https://cataas.com/)  
###### Released under [MIT](/LICENSE) by [@Atom244](https://github.com/Atom244).

<h1 align="center">
  <br>
  <a href="https://github.com/Atom244"><img src="https://raw.githubusercontent.com/Atom244/icons-for-projects/main/cat.png" alt="Alien cat" width="256"></a>
  <br>
  Thanks for using my module or viewing my repository!!!
  <br>
</h1>
