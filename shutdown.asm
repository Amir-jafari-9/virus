section .data
    message db 'HACKED', 0xA  ; Message to send (with newline)
    msg_len equ $ - message     ; Length of the message

section .text
    global _start

_start:
    ; Send message to all users using the write system call
    mov rax, 1          ; syscall: sys_write
    mov rdi, 1          ; file descriptor: stdout
    mov rsi, message    ; pointer to message
    mov rdx, msg_len    ; message length
    syscall              ; invoke syscall

    ; Sleep for 1 second (using sleep syscall)
    mov rax, 35         ; syscall: sys_nanosleep
    mov rdi, rsp        ; pointer to timespec (not used here)
    xor rsi, rsi        ; seconds = 1
    xor rdx, rdx        ; nanoseconds = 0
    syscall              ; invoke syscall

    ; Shutdown the system
    mov rax, 60         ; syscall: sys_exit
    xor rdi, rdi        ; exit code 0
    syscall              ; invoke syscall
