```
poetry run geraimg -fg=#FF0000 -bg=#000000 -o arquivo --format jpeg -t "Olá Mundo" -b64 | base64 --decode > file.jpg
poetry run geraimg -fg=#FF0000 -bg=#000000 -o arquivo jpeg -t "Olá Mundo" -b64 | base64 --decode > file.jpg
poetry run geraimg -fg=#00FFFF -bg=#FFF000 -o asd jpeg -t a -t asdasdasd -t sleep -t %20 -b64
python geraimg/gera.py | base64 --decode > file.jpg
```
