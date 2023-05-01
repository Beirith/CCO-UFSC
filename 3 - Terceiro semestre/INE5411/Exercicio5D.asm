.data
	a: .word, 0
	b: .word, 0
	mensagemA: .asciiz "Digite o valor de A: "
	mensagemB: .asciiz "Digite o valor de B: "

.text
main:
	la $s0, a
	la $s1, b
	
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
	
	beq $t1, $t0, faznada
	sw $t0, 0($s0)
	sw $t1, 0($s1)
	li $v0, 10
	syscall
	
faznada:
	move $t0, $t1
	sw $t0, 0($s0)
	sw $t1, 0($s1)
	li $v0, 10
	syscall
