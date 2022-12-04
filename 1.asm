includelib libcmt.lib

.data
szFilename db "1.txt", 0
szReadMode db "r", 0
szPart1 db "Part 1: %d", 10, 0
szPart2 db "Part 2: %d", 10, 0

.data?
elf_count dq ?
calories dq 256 dup (?)
strbuf db 32 dup (?)

.code
extern printf:near
extern fopen:near
extern fclose:near
extern fgets:near
extern atoi:near

main proc
	sub rsp, 38h
	call read_input
	cmp rax, -1
	je return
	call part1
	mov rcx, offset szPart1
	mov rdx, rax
	call printf
	call part2
	mov rcx, offset szPart2
	mov rdx, rax
	call printf
	mov rax, 0
return:
	add rsp, 38h
	ret
main endp

part1 proc
	push rbp
	mov rbp, rsp
	sub rsp, 40h
	mov r14, 0 ;max
	xor rax, rax ;index into calories
loop1:
	mov r13, [calories+rax*8]
	cmp r14, r13
	jge @F
	mov r14, r13
@@:
	inc rax
	cmp rax, [elf_count]
	jne loop1
	mov rax, r14
return:
	mov rsp, rbp
	pop rbp
	ret
part1 endp

part2 proc
	push rbp
	mov rbp, rsp
	sub rsp, 40h
	mov r9, [elf_count]
	sub r9, 3 ;top 3
	;remove the smallest elements, leaving behind the 3 max
scan_loop:	
	mov r14, -1 ;min
	mov r10, 0 ;index of smallest
	;find smallest index in this iteration
	xor rax, rax
loop1:
	mov r13, [calories+rax*8]
	cmp r14, r13
	jb @F
	mov r14, r13
	mov r10, rax
@@:
	inc rax
	cmp rax, [elf_count]
	jne loop1
	;replace value with -1
	mov [calories+r10*8], -1
	dec r9
	jz sum_max3
	jmp scan_loop
sum_max3:
	xor rax, rax
	xor rbx, rbx
loop2:
	;sum the 3 values that aren't equal to -1
	mov r14, [calories+rbx*8]
	cmp r14, -1
	je @F
	add rax, r14
@@:
	inc rbx
	cmp rbx, [elf_count]
	jne loop2
return:
	mov rsp, rbp
	pop rbp
	ret
part2 endp

read_input proc
	sum equ [rbp - 12]
	filehandle equ [rbp - 8]
	push rbp
	mov rbp, rsp
	sub rsp, 40h
	;open file
	mov rcx, offset szFilename
	mov rdx, offset szReadMode
	call fopen
	cmp rax, 0
	jne fopen_success
	mov rax, -1
	jmp return
fopen_success:
	mov filehandle, rax
	mov dword ptr elf_count, 0
	xor r13, r13 ;elf index
	xor r14, r14 ; sum
read_loop:
	mov r8, filehandle
	mov rdx, 32
	mov rcx, offset strbuf
	;char *fgets(char *str, int n, FILE *stream)
	call fgets
	cmp eax, 0
	je eof
end_line:
	mov r12b, byte ptr [strbuf]
	cmp r12, 0ah
	jne add_calories
	;record
	mov [calories+r13*8], r14
	xor r14, r14
	inc r13
add_calories:
	mov rcx, offset strbuf
	call atoi
	add r14, rax
	jmp read_loop
eof:
	cmp r14, 0
	je @F
	mov [calories+r13*8], r14
	inc r13
@@:
	mov rcx, filehandle
	call fclose
	mov elf_count, r13
	xor rax, rax
return:
	mov rsp, rbp
	pop rbp
	ret
read_input endp

END