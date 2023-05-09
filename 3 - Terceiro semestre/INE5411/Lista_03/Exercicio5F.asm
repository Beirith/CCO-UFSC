.data
	a: .word, 0
	b: .word, 0
	c: .word, 5

.text
main:
	la $s0, a
	la $s1, b
	la $s2, c
	
	lw $t0, 0($s0)
	lw $t1, 0($s1)
	lw $t2, 0($s2)
	
	slt $t3, $t0, $t2
	beq $t3, 1, soma
	
	sw $t0, 0($s0)
	sw $t1, 0($s1)
	li $v0, 10
	syscall
	
soma:
	addi $t0, $t0, 1
	addi $t1, $t1, 2
	sw $t0, 0($s0)
	sw $t1, 0($s1)
	j main

