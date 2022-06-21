![](./.github/banner.png)

<p align="center">
    A python script to automatically generate shellcode payload from assembly files.
    <br>
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/Ooggle/shellcoding-companion">
    <img alt="img last commit" src="https://img.shields.io/github/last-commit/Ooggle/shellcoding-companion.svg">
    <img alt="img last release" src="https://img.shields.io/github/release/Ooggle/shellcoding-companion.svg?color=red">
    <a href="https://twitter.com/intent/follow?screen_name=Ooggle_" title="Follow"><img src="https://img.shields.io/twitter/follow/Ooggle_?label=Ooggle_&style=social"></a>
    <br>
</p>

## Requirements

To use this tool, you first need to install `nasm`, `objdump` and `python3`. You can install them with:

```sh
sudo apt install nasm
```

## Usage

```
$ ./shellcoding-companion.py -h

 __ _          _ _               _ _                      
/ _\ |__   ___| | | ___ ___   __| (_)_ __   __ _          
\ \| '_ \ / _ \ | |/ __/ _ \ / _` | | '_ \ / _` |         
_\ \ | | |  __/ | | (_| (_) | (_| | | | | | (_| |         
\__/_| |_|\___|_|_|\___\___/ \__,_|_|_| |_|\__, |_v1.0.0
           / __\___  _ __ ___  _ __   __ _ |___/(_) ___  _ __
          / /  / _ \| '_ ` _ \| '_ \ / _` | '_ \| |/ _ \| '_ \ 
         / /__| (_) | | | | | | |_) | (_| | | | | | (_) | | | |
         \____/\___/|_| |_| |_| .__/ \__,_|_| |_|_|\___/|_| |_|
                    By Ooggle |_| https://twitter.com/Ooggle_


usage: ./shellcoding-companion.py [-h] [-o OUTPUT] [-p2] [-p3] [-P] source [source ...]

positional arguments:
  source                NASM source(s) file(s) (Example: shellcode.s)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file for the shellcode. (default: None)

  Output languages

  -p2, --python2        Output python2 command to generate the shellcode from command line. (default: False)
  -p3, --python3        Output python3 command to generate the shellcode from command line. (default: False)
  -P, --perl            Output perl command to generate the shellcode from command line. (default: False)
```

## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.
