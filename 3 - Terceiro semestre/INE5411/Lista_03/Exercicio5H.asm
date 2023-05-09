.data
	a: .word, 0
	b: .word, 0
	c: .word, 0
	mensagemA: .asciiz "Digite um valor para A: "
	mensagemB: .asciiz "Digite um valor para B: "
	mensagemC: .asciiz "Digite um valor para C: "

.text
main:
	la $s0, a
	la $s1, b
	la $s2, c

	li $v0, 4
	la $a0, mensagemA
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0

	li $v0, 4
	la $a0, mensagemB
	syscall
	
	li $v0, 5
	syscall
	move $t1, $v0
	
	li $v0, 4
	la $a0, mensagemC
	syscall
	
	li $v0, 5
	syscall
	move $t2, $v0

	beq $t0, 1, f1
	beq $t0, 2, f2
	
	sw $t0, 0($s0)
	sw $t2, 0($s1)
	sw $t2, 0($s2)
	li $v0, 10
	syscall
	
f1:
	addi $t1, $t2, 1
	sw $t0, 0($s0)
	sw $t1, 0($s1)
	sw $t2, 0($s2)
	li $v0, 10
	syscall

f2:
	addi $t1, $t2, 2
	sw $t0, 0($s0)
	sw $t1, 0($s1)
	sw $t2, 0($s2)
	li $v0, 10
	syscall

