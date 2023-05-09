.data 
	mensagem: .asciiz "\nDigite uma palavra de até 8 caracteres: "
	mensagem2: .asciiz "\nA palavra digitada foi: "
	mensagem3: .asciiz "\nNúmero de caracteres iguais a 'a' na plavra digitada é: "
	palavra: .space 8
	contador: .word 0
	indice: .word 0
	
.text
	# Carregando endereços
	la $s0, palavra
	la $s1, contador
	la $s2, indice

	# Imprimindo mensagem
	li $v0, 4
	la $a0, mensagem
	syscall
	
	# Coletando a entrada do usuário
	li $v0, 8
	la $a0, palavra
	la $a1, 8
	syscall

	# Chamando a função
	jal calcula
	
calcula:
	lb $t0, 0($s0)			# Registrador $t0 possui o caractere no endereço $a0
	lw $t1, 0($s1)			# Registrador $t1 possui o valor de contador
	lw $t2, 0($s2)
		
	beq $t0, 'a', soma
	addi $s0, $s0, 1		# Soma 1 ao endereço de $a0, para percorrer a palavra
	addi $t2, $t2, 1		# Soma 1 ao valor do índice
	
	sw $t2, 0($s2)

	beq $t2, 8, fim
	j calcula 

soma:
	addi $s0, $s0, 1		# Soma 1 ao endereço de $t0, para percorrer a palavra
	addi $t1, $t1, 1		# Soma 1 ao valor de contador, para indicar uma letrar 'a' na palavra
	addi $t2, $t2, 1		# Soma 1 ao valor do índice
	sw $t1, 0($s1)
	sw $t2, 0($s2)
	j calcula
	
fim:
	# Imprime o número de letras 'a' na tela
	li $v0, 4
	la $a0, mensagem3
	syscall
	li $v0, 1
	la $a0, 0($t1)
	syscall
	
	# Encerra o programa
	li $v0, 10
	syscall

	
	
	