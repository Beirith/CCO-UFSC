.data
	A: .word
.text
loop:
	la $s0, A
	addi $t0, $t0, 1	# Soma 1 ao registrador que contém o valor de A
	sw $t0, 0($s0)		# Armazena esse valor em A
	j main			# Volta para main

main: 
	la $s0, A
	
	lw $t0, 0($s0)	# Armazena o valor de A em $t0
	li $t1, 5	# Armazena o valor 1 em $t1

	bne $t0, $t1, loop	# Compara os valores de $t0 e $t1
	sw $t0, 0($s0) 		# Armazena o valor do somatório em $s0
