[BITS 64]

section .text

global _start

_start:
    %assign i 0
    %rep    10
        mov rax, i
        syscall
    %assign i i+1
    %endrep

    ret
