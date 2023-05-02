.data
	A: .half 1, 2, -2, 3


.text
main:
	la $s1, A

	
	lh $t1, 0($s1)

	
	li $v0, 10
	syscall