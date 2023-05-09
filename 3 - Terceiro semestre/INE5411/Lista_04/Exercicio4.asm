.data
	n1: .word 0
	n2: .word 0
	mensagem1: .asciiz "\nDigite o valor do primeiro número: "
	mensagem2: .asciiz "\nDigite o valor do segundo número: "
	mensagem3: .asciiz "\nO resultado da soma é: "

.text
main:
	la $s1, n1
	la $s2, n2
	
	jal soma
	li $v0, 4
	la $a0, mensagem3
	syscall
	li $v0, 1
	lw $a0, 0($sp)
	syscall
	
	addi $sp, $sp, 8
	
	li $v0, 10
	syscall

soma:
	addi $sp, $sp, -8
	sw $ra, 4($sp)
	
	jal leitura
	
	lw $t1, 0($s1)
	lw $t2, 0($s2)
	
	add $t0, $t1, $t2
	sw $t0, 0($sp)
	
	lw $ra, 4($sp)
	jr $ra
	
leitura:
	li $v0, 4
	la $a0, mensagem1
	syscall
	li $v0, 5
	syscall
	sw $v0, 0($s1)

	li $v0, 4
	la $a0, mensagem2
	syscall
	li $v0, 5
	syscall
	sw $v0, 0($s2)
	
	jr $ra
