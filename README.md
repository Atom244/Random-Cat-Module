<h1 align="center">
  <br>
  <a href="https://github.com/Atom244"><img src="https://github.com/Atom244/icons-for-projects/blob/main/rndcatpreviewpng.png" alt="Random cat module" width="1024"></a>
  <br>
  rnd_cat
  <br>
</h1>

<h4 align="center">A simple python module for receiving random images with cats.</h4>



<p align="center">
  <a href="#download">Download</a> •
  <a href="#how-to-use">How To Use</a>

</p>

## Download
To clone this module, you'll need [Git](https://git-scm.com) 
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
• cat_gif() - Will return a random gif cat.    
Arguments: filename
```py
import rnd_cat
rnd_cat.cat_gif(filename='default_cat_gif')
```
• cat_say_edit() - Will return a random gif cat.    
Arguments: filename, format, text, fontSize, fontColor
```py
import rnd_cat
rnd_cat.cat_say_edit(filename='default_cat_gif', text+'Hello', fontSize=50, fontColor='red', format='jpg')
```


## Credits

The module is based on getting images from this site:

- [CATAAS](https://cataas.com/)

<h1 align="center">
  <br>
  <a href="https://github.com/Atom244"><img src="https://github.com/Atom244/icons-for-projects/blob/main/cat.png" alt="Alien cat" width="256"></a>
  <br>
  Thanks for using my module or viewing my repository!!!
  <br>
</h1>
