#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : shellcode_parser.py
# Author             : Ooggle (@Ooggle_)
# Date created       : 21 Jun 2022

import os


def asm_parse(pathname, label_start, opcode_end=False, debug=False):
    objdump = os.popen(f'objdump -d {pathname}').read().split('\n')

    # skip to start of shellcode
    i = 0
    for i in range(len(objdump)):
        if label_start in objdump[i]:
            break
    i += 1

    shellcode = ''
    # start parsing
    while i < len(objdump):
        if objdump[i][10:32].rstrip() != '':
            shellcode += objdump[i][10:32].rstrip() + ' '
            if opcode_end:
                if opcode_end in objdump[i]:
                    break
            i += 1
        else:
            break

    shellcode_len = len(shellcode.split(' ')) - 1
    if debug:
        print(f'Shellcode length: {(shellcode_len)}')
        print(shellcode)
    return shellcode, shellcode_len


def asm_build(program_name):
    ret = os.system(f'nasm -f elf64 {program_name} -o {program_name}.o && ld -s ./{program_name}.o -o ./{program_name}.bin')
    os.system(f'rm -rf {program_name}.o')
    return ret
