# André Amaral Rocco
# Isaque Floriano Beirith

.data 
	A: .word 0
	B: .word 5
	C: .word 0
	D: .word 50
	E: .word 3
.text
main:
	la  $s0, A
	la  $s1, B
	la  $s2, C
	la  $s3, D
	la  $s4, E

	lw  $t0, 0($s1)     # $t0 = B
	li  $t1, 35

	add $t3, $t0, $t1   # $t3 = B + 35
	sw  $t3, 0($s0)     # Mem[$s0] = $t3

	lw  $t0, 0($s3)     # $t0 = D = 50
	lw  $t1, 0($s0)     # $t1 = A = 40
	lw  $t2, 0($s4)     # $t2 = E = 3

	sub $t3, $t0, $t1   # $t3 = D - A = 10
	add $t4, $t3, $t2   # $t4 = $t3 + E = 13

	sw  $t4, 0($s2)     # Mem[$s2] = $t4 = 13
