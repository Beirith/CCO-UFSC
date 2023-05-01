.data
	A: .word 10
	B: .word 15
	C: .word 20
	D: .word 25
	E: .word 30
	F: .word 35
	G: .space, 16
	H: .space, 16

.text
main: 
	la $s0, A
	la $s1, B
	la $s2, C
	la $s3, D
	la $s4, E
	la $s5, F
	la $s6, G
	la $s7, H

	lw $t1, 0($s1)	        # Armazena B em $st1
	lw $t2, 0($s2) 	        # Armazena C em $st2
	add $t0, $t1, $t2       # B + C e armazena em $t0	
	
	lw $t1, 0($s0)		# Armazena A em $t1
	lw $t2, 0($s5)		# Armazena F em $t2
	sub $t0, $t1, $t0	# A - (B + C) e armazena em $t0
	add $t0, $t0, $t2	# A - (B + C) + F e armazena em $t0
	
	sw $t0, 0($s6)		# Armazena o resultado em G[0]
	
	lw $t1, 0($s0)		# Armazena A em $t1
	lw $t2, 0($s1)		# Armazena B em $t2
	sub $t0, $t1, $t2	# A - B e armazena em $t0
	
	lw $t1, 0($s2) 		# Armazena C em $t1
	sub $t1, $t2, $t1	# B - C e armazena em $t1
	
	mul $t0, $t0, $t1	# (A - B) * (B - C) e armazena em $t0
	
	lw $t1, 0($s4)		# Armazena E em $t1
	
	sub $t0, $t1, $t0 	# E - (A - B) * (B - C) e armazena em $t0
	
	sw $t0, 4($s6)		# Armazena o resultado em G[1]
	
	lw $t1, 4($s6)		# Armazena G[1] em $t1
	lw $t2, 0($s2)		# Armazena C em $t2
	
	sub $t0, $t1, $t2	# G[1] - C e armazena em $t0
	
	sw $t0, 8($s6)		# Armazena o resultado em G[2]
	
	lw $t1, 8($s6) 		# Armazena G[2] em $t1
	lw $t2, 0($s6)		# Armazena G[0] em $t2
	
	add $t0, $t1, $t2	# G[2] + G[0] e armazena em $t0
	
	sw $t0, 12($s6)		# Armazena o resultado em G[3]
	
	lw $t1, 0($s1)		# Armazena B em $t1
	lw $t2, 0($s2)		# Armazena C em $t2
	
	sub $t0, $t1, $t2	# B - C e armazena em $t0
	
	sw $t0, 0($s7)		# Armazena o resultado em H[0]
	
	lw $t1, 0($s0)		# Armazena A em $t1
	
	add $t0, $t1, $t2	# A + C e armazena em $t0
	
	sw $t0, 4($s7)		# Armazena o resultado em H[1]
	
	lw $t1, 0($s1)		# Armazena B em $t1
	
	sub $t0, $t1, $t2	# B - C e armazena em $t0
	
	lw $t1, 12($s6) 	# Armazena G[3] em $t1
	
	add $t0, $t0, $t1	# B - C + G[3] e armazena em $t0
	
	sw $t0, 8($s7)		# Armazena o resultado em H[2]
	
	lw $t1, 0($s1)		# Armazena B em $t1
	lw $t2, 0($s6)		# Armazena G[0] em $t2
	lw $t3, 0($s3)		# Armazena D em $t3
	
	sub $t0, $t1, $t2	# B - G[0] e armazena em $t0
	add $t0, $t0, $t3 	# B - G[0] + D e armazena em $t0
	
	sw $t0, 12($s7)		# Armazena o resultado em H[3]
	
	
	
	
	

	
	
	
	
	
	
	
	
	