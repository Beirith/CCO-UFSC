.data 
	base: .word, 0
	expoente: .word, 0
	result: .word, 0
	i: .word, 0
	mensagem1: .asciiz "Digite o valor da base: "
	mensagem2: .asciiz "Digite o valor do expoente: "
	mensagem3: .asciiz "O resultado é: "
	
.text
main:
	la $s0, base
	la $s1, expoente
	la $s2, result
	la $s3, i
	
	li $v0, 4
	la $a0, mensagem1		# Printa a mensagem ao usuário
	syscall
	
	li $v0, 5		
	syscall 
	sw $v0, 0($s0)		
	
	li $v0, 4
	la $a0, mensagem2
	syscall
	
	li $v0, 5
	syscall
	sw $v0, 0($s1)
	
	lw $a0, 0($s0)		# A
	lw $a1, 0($s1)		# B
	lw $a2, 0($s2)		# Result
	lw $a3, 0($s3)		# I

	jal pow
	
	li $v0, 4
	la $a0, mensagem3
	syscall
	li $v0, 1
	lw $a0, 0($s2)
	syscall

	li $v0, 10
	syscall
	
pow:
	addi $a2, $a2, 1
	j loopPow
	jr $ra

loopPow:
	mul $a2, $a2, $a0
	addi $a3, $a3, 1
	bne $a3, $a1, loopPow
	sw $a2, 0($s2)
	sw $a3, 0($s3)
	jr $ra
	
	

