import pytest
import builtins
from unittest.mock import patch, mock_open
import rnd_cat  # замените на имя своего файла, если он другой


# ===== Фиктивные байты изображения =====
FAKE_IMG = b"fake-image-data"


@pytest.mark.parametrize("func,args,url_part", [
    (rnd_cat.cat, {"filename": "test1"}, "/cat"),
    (rnd_cat.cat_say, {"filename": "test2", "text": "Hello"}, "/cat/says/Hello"),
    (rnd_cat.cat_gif, {"filename": "test3"}, "/cat/gif"),
    (rnd_cat.cat_say_edit, {"filename": "test4", "text": "Hi", "fontSize": 30, "fontColor": "blue"}, "/cat/says/Hi"),
    (rnd_cat.cat_tag, {"filename": "test5", "tag": "cute"}, "/cat/cute"),
    (rnd_cat.cat_tag_say, {"filename": "test6", "tag": "cute", "text": "Hey"}, "/cat/cute/says/Hey"),
    (rnd_cat.cat_type, {"filename": "test7", "type": "square"}, "/cat?type=square"),
    (rnd_cat.cat_filter, {"filename": "test8", "filter": "mono"}, "/cat?filter=mono"),
])
def test_functions_with_requests(func, args, url_part):
    with patch("requests.get") as mock_get, patch("builtins.open", mock_open()) as mock_file:
        mock_get.return_value.content = FAKE_IMG
        func(**args)
        mock_get.assert_called_once()
        assert url_part in mock_get.call_args[0][0]  # Проверка URL


def test_cat_gif_uses_urlretrieve():
    with patch("urllib.request.urlretrieve") as mock_urlretrieve:
        rnd_cat.cat_gif("gifcat")
        mock_urlretrieve.assert_called_once_with("https://cataas.com/cat/gif", "gifcat.gif")


def test_cat_combo_jpg():
    with patch("requests.get") as mock_get, patch("builtins.open", mock_open()) as mock_file:
        mock_get.return_value.content = FAKE_IMG
        rnd_cat.cat_combo(
            filename="combo1",
            is_gif=False,
            is_say=True,
            is_filtered=True,
            text="Hello",
            fontSize=30,
            fontColor="green",
            type="square",
            format="jpg"
        )
        call_url = mock_get.call_args[0][0]
        assert "says/Hello?" in call_url
        assert "fontColor=green" in call_url
        assert "fontSize=30" in call_url
        assert "filter=mono" in call_url
        assert "type=square" in call_url


def test_cat_combo_gif_only():
    with patch("requests.get") as mock_get, patch("builtins.open", mock_open()) as mock_file:
        mock_get.return_value.content = FAKE_IMG
        rnd_cat.cat_combo(filename="combo2", is_gif=True, is_say=False, is_filtered=False)
        call_url = mock_get.call_args[0][0]
        assert "/gif" in call_url
        assert "filter=" in call_url  # will be empty string


def test_cat_combo_no_gif_no_say():
    with patch("requests.get") as mock_get, patch("builtins.open", mock_open()) as mock_file:
        mock_get.return_value.content = FAKE_IMG
        rnd_cat.cat_combo(filename="combo3", is_gif=False, is_say=False, is_filtered=False)
        call_url = mock_get.call_args[0][0]
        assert call_url.startswith("https://cataas.com/cat?")
