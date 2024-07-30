# GERAIMG

Quick tool to generate images with text.

```
$ git clone
$ cd geraimg
$ poetry install

$ poetry run geraimg --help
usage: geraimg [-h] [-f {jpeg}] [-t TEXT] [-b64] [-o OUTPUT] [-bg BACKGROUND] [-fg FOREGROUND]

options:
  -h, --help            show this help message and exit
  -f {jpeg}, --format {jpeg}
                        Output format
  -t TEXT, --text TEXT  Text, repeat to include multiple lines.
  -b64, --base64        Return base64-encoded image to STDOUT.
  -o OUTPUT, --output OUTPUT
                        Output file.
  -bg BACKGROUND, --background BACKGROUND
                        Background color.
  -fg FOREGROUND, --foreground FOREGROUND
                        Foreground color.
```

```
poetry run geraimg -fg=#FF0000 -bg=#000000 -o arquivo --format jpeg -t "Olá Mundo" -t "Hello World" -b64
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQE...
```
![arquivo.jpeg](arquivo.jpeg "arquivo.jpeg")