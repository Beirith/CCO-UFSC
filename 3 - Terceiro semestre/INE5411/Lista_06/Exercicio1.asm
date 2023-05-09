.data
	pi: .float 3.141592653589793
	area: .float 0
	mensagem: .asciiz "Digite o raio do círculo: "
	mensagem2: .asciiz "A área do círculo é: "
	
.text
	la $s0, pi
	la $s1, area
	lwc1 $f2, 0($s0)
	
	li $v0, 4
	la $a0, mensagem
	syscall
	li $v0, 6
	syscall
	
	mul.s $f0, $f0, $f0
	mul.s  $f2, $f2, $f0
	
	swc1 $f2, 0($s1)
	
	li $v0, 4
	la $a0, mensagem2
	syscall
	
	li $v0, 2
	lwc1 $f12, 0($s1)
	syscall