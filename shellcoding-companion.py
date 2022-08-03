#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : shellcode_parser.py
# Author             : Ooggle (@Ooggle_)
# Date created       : 21 Jun 2022

import os
import sys
from lib.shellcode_parser import asm_parse, asm_build
from binascii import unhexlify
import argparse

version_number = '1.0.1'

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

class CustomParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('Error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def parse_args():
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-o", "--output", default=None, help="Output file for the shellcode.")
    parser.add_argument("--show", default=False, action="store_true", help="Show the output shellcode.")

    group = parser.add_argument_group(description="Output languages")
    group.add_argument("-p2", "--python2", default=False, action="store_true", help='Output python2 command to generate the shellcode from command line.')
    group.add_argument("-p3", "--python3", default=False, action="store_true", help='Output python3 command to generate the shellcode from command line.')
    group.add_argument("-P", "--perl", default=False, action="store_true", help='Output perl command to generate the shellcode from command line.')

    parser.add_argument("source", nargs="+", help="NASM source(s) file(s). (Example: shellcode.s)")
    args = parser.parse_args()
    
    return args


if __name__ == '__main__':
    print(banner)
    args = parse_args()


    if len(os.popen("which nasm").read()) == 0:
        print("\x1b[1;31m[!] Missing requirement: nasm\x1b[0m")
        exit(0)

    if len(os.popen("which objdump").read()) == 0:
        print("\x1b[1;31m[!] Missing requirement: objdump\x1b[0m")
        exit(0)

    # building shellcode(s)
    print(f'\x1b[1;32m[+] Building shellcode(s): {args.source}\x1b[0m')
    for source in args.source:
        print(f'\x1b[0;32m[+] {source} ...\x1b[0m', end='')
        if asm_build(source) != 0:
            print(f'\x1b[1;31m[!] ERROR: build failed for "{source}"\x1b[0m')
            exit(1)
        print(f'\x1b[1;32m Success!\x1b[0m')

    # parsing shellcode(s)
    print('\n\x1b[1;32m[+] Parsing shellcode(s)\x1b[0m')
    bytecodes = []
    for source in args.source:
        print(f'\x1b[0;32m[+] {source}.bin ...\x1b[0m')
        (tmpbytes, _) = asm_parse(f'{source}.bin', '<.text>')
        bytecodes.append([unhexlify(b) for b in tmpbytes.split(' ') if b != ''])

    # saving final shellcode to file
    if args.output:
        print(f'\n\x1b[1;32m[+] Saving shellcode to "{args.output}"\x1b[0m')

        with open(args.output, 'wb') as f:
            for bytecode in bytecodes:
                for b in bytecode:
                    f.write(b)

        print(f'\x1b[0;32m[+] Done! {sum([len(b) for b in bytecodes])} bytes written to {args.output}\x1b[0m')

    if args.python2:
        print(f'\n\x1b[1;32m[+] Generating python command\x1b[0m')

        hex_bytecodes = ""
        for bytecode in bytecodes:
            hex_bytecode = ''.join([
                '\\x' + hex(int.from_bytes(c, 'big'))[2:].rjust(2, '0')
                for c in bytecode
            ])
            hex_bytecodes += hex_bytecode

        print(f'python2 -c \'print "{hex_bytecodes}"\'')

    if args.python3:
        print(f'\n\x1b[1;32m[+] Generating python command\x1b[0m')

        hex_bytecodes = ""
        for bytecode in bytecodes:
            hex_bytecode = ''.join([
                '\\x' + hex(int.from_bytes(c, 'big'))[2:].rjust(2, '0')
                for c in bytecode
            ])
            hex_bytecodes += hex_bytecode

        print(f'python3 -c \'print "{hex_bytecodes}"\'')

    if args.perl:
        print(f'\n\x1b[1;32m[+] Generating perl command\x1b[0m')

        hex_bytecodes = ""
        for bytecode in bytecodes:
            hex_bytecode = ''.join([
                '\\x' + hex(int.from_bytes(c, 'big'))[2:].rjust(2, '0')
                for c in bytecode
            ])
            hex_bytecodes += hex_bytecode

        print(f'perl -e \'print "{hex_bytecodes}"\'')

    if args.show:
        print(f'\n\x1b[1;32m[+] Showing output shellcode\x1b[0m')

        for source in args.source:
            print(f'\x1b[0;32m[+] {source}.bin ...\x1b[0m')
            (tmpbytes, _) = asm_parse(f'{source}.bin', '<.text>', show=True)

    print('\n\x1b[1;32m[+] Done!\x1b[0m\n')
