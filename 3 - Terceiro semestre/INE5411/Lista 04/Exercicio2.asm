.data 
	a: .word, 4
	b: .word, 10
	val: .word, 0
	
.text
main:
	la $s0, a
	la $s1, b
	la $s2, val
	
	lw $a0, 0($s0)
	lw $a1, 0($s1)

	jal calculaAreaQuadrado

	li $v0, 10
	syscall
	
calculaAreaQuadrado:
	mul $t0, $a0, $a1
	sw $t0, 0($s2)
	jr $ra




