.data
	a: .word, 1
	b: .word, 2
	i: .word, 0

.text
main:
	la $s0, a
	la $s1, b
	la $s2, i

	lw $t0, 0($s0)
	lw $t1, 0($s1)
	lw $t2, 0($s2)
	
	li $t3, 5
	
	slt $t4, $t2, $t3
	beq $t4, 1, soma
	
	sw $t0, 0($s0)
	sw $t1, 0($s1)
	li $v0, 10
	syscall
	
soma:
	addi $t0, $t1, 1
	addi $t1, $t1, 3
	addi $t2, $t2, 1
	sw $t0, 0($s0)
	sw $t1, 0($s1)
	sw $t2, 0($s2)
	j main

