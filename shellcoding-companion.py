#!/usr/bin/env python3

from lib.shellcode_parser import asm_parse, asm_build
from binascii import unhexlify
import argparse

version_number = '0.2.0'

banner = f"""\x1b[0;33m
 __ _          _ _               _ _                      
/ _\ |__   ___| | | ___ ___   __| (_)_ __   __ _          
\ \| '_ \ / _ \ | |/ __/ _ \ / _` | | '_ \ / _` |         
_\ \ | | |  __/ | | (_| (_) | (_| | | | | | (_| |         
\__/_| |_|\___|_|_|\___\___/ \__,_|_|_| |_|\__, |_\x1b[1;33mv{version_number}\x1b[0;33m
           / __\___  _ __ ___  _ __   __ _ |___/(_) ___  _ __
          / /  / _ \| '_ ` _ \| '_ \ / _` | '_ \| |/ _ \| '_ \ 
         / /__| (_) | | | | | | |_) | (_| | | | | | (_) | | | |
         \____/\___/|_| |_| |_| .__/ \__,_|_| |_|_|\___/|_| |_|
                    \x1b[0;1;3mBy Ooggle\x1b[0;33m |_| \x1b[0;1mhttps://twitter.com/Ooggle_\x1b[0m

"""

print(banner)

def parse_args():
    parser = argparse.ArgumentParser(
        prog='shellcoding-companion.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o', '--output', nargs=1, help='output file for the shellcode')
    parser.add_argument('-p', '--python', action=argparse.BooleanOptionalAction, help='output python command to generate the shellcode from command line', metavar='')
    parser.add_argument('source', nargs='+', help='nasm source(s) file(s) (Example: shellcode.s)')
    args = parser.parse_args()
    #parser.print_help()
    return args

if __name__ == '__main__':
    args = parse_args()
    
    # building shellcode(s)
    print(f'\x1b[1;32m[+] building shellcode(s): {args.source}\x1b[0m')
    for source in args.source:
        print(f'\x1b[0;32m[+] {source}...\x1b[0m', end='')
        if asm_build(source) != 0:
            print(f'\x1b[1;31m[-] ERROR: build failed for "{source}"\x1b[0m')
            quit(1)
        print(f'\x1b[1;32m success\x1b[0m')


    # parsing shellcode(s)
    print('\n\x1b[1;32m[+] parsing shellcode(s)\x1b[0m')
    bytecodes = []
    for source in args.source:
        print(f'\x1b[0;32m[+] {source}.bin...\x1b[0m')
        (tmpbytes, _) = asm_parse(f'{source}.bin', '<.text>')
        bytecodes.append([unhexlify(b) for b in tmpbytes.split(' ') if b != ''])


    # saving final shellcode to file
    if args.output:
        print(f'\n\x1b[1;32m[+] saving shellcode to "{args.output[0]}"\x1b[0m')
        
        with open(args.output[0], 'wb') as f:
            for bytecode in bytecodes:
                for b in bytecode:
                    f.write(b)
        print(f'\x1b[0;32m[+] done\x1b[0m')

    if args.python:
        print(f'\n\x1b[1;32m[+] generating python command\x1b[0m')

        print('python2 -c \'print "', end='')
        for bytecode in bytecodes:
            for c in bytecode:
                print('\\x' + hex(int.from_bytes(c, 'big'))[2:].rjust(2, '0'), end='')

        print('"\'')

    print('\n\x1b[1;32m[+] done\x1b[0m\n')
