[BITS 64]

section .text

global _start

_start:
    push rax
    mov rbp, rsp

    ;read from stdin
    xor rdx, rdx
    add dx, 0xffff
    mov rsi, rax
    xor rdi, rdi
    xor rax, rax
    syscall

    ret
