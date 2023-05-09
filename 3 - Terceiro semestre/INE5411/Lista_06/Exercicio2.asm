.data
	input: .float 0.0
	cinco: .float 5.0
	nove: .float 9.0
	trinta: .float 32.0
	
	mensagem: .asciiz "\nDigite a temperatura em fahrenheit: "
	mensagem2: .asciiz "\nA temperatura em celsius é: "
	ponto: .asciiz "."
	
.text
	la $s0, input
	la $s1, cinco
	la $s2, nove
	la $s3, trinta
	
	li $v0, 4
	la $a0, mensagem
	syscall
	
	li $v0, 6
	syscall
	swc1 $f12, 0($s0)
	
	# Argumentos para a função
	lwc1 $f2, 0($s1)	# 5
	lwc1 $f4, 0($s2)	# 9
	lwc1 $f6, 0($s3)	# 32
	jal converte
	
	li $v0, 4
	la $a0, mensagem2
	syscall
	
	li $v0, 2
	mov.s $f12, $f0
	syscall

	li $v0, 10
	syscall

converte:
	sub.s $f0, $f0, $f6	# Temperatura - 32
	div.s $f0, $f0, $f4	
	mul.s $f0, $f0, $f2
	
	jr $ra
	
	
