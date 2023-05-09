.data 
	g: .word, 0
	h: .word, 0
	i: .word, 0
	j: .word, 0
	f: .word, 0
	mensagem: .asciiz "Digite 4 valores: "

.text
main:
	la $s0, g
	la $s1, h
	la $s2, i
	la $s3, j
	la $s4, f
	
	li $v0, 4
	la $a0, mensagem		# Printa a mensagem ao usuário
	syscall
	
	li $v0, 5		
	syscall 
	sw $v0, 0($s0)			# Variável G recebe o valor digitado
	li $v0, 5
	syscall 
	sw $v0, 0($s1)			# Variável H recebe o valor digitado
	li $v0, 5
	syscall 
	sw $v0, 0($s2)			# Variável I recebe o valor digitado
	li $v0, 5
	syscall 
	sw $v0, 0($s3)			# Variável J recebe o valor digitado

	lw $a0, 0($s0)
	lw $a1, 0($s1)
	lw $a2, 0($s2)
	lw $a3, 0($s3)
	
	jal calcula

	li $v0, 10
	syscall
	
calcula:
	add $t0, $a0, $a1
	add $t1, $a2, $a3
	sub $t0, $t0, $t1
	sw $t0, 0($s4)
	jr $ra




