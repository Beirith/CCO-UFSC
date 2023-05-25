# André Amaral Rocco
# Isaque Floriano Beirith

.data 
	A: .word 0
	B: .word 0
	C: .word 0
	D: .word 50
	E: .word 3

	FRASE: .asciiz "Digite um numero: "
.text
main:
	la  $s0, A
	la  $s1, B
	la  $s2, C
	la  $s3, D
	la  $s4, E

	# Escrever no terminal "Digite um numero: "
	li  $v0, 4	   # Comando para escrever STRING
	la  $a0, FRASE     # Carrega string (endereço) no argumento
	syscall            # Chama o sistema

	# Pedir o valor de B pelo terminal
	li  $v0, 5         # Comando para ler INT
	syscall
	move $t0, $v0      # $t0 = input()
	sw  $t0, 0($s1)    # $s1 = B = $t0

	li  $t1, 35

	add $t3, $t0, $t1   # $t3 = B + 35
	sw  $t3, 0($s0)     # Mem[$s0] = $t3

	lw  $t0, 0($s3)     # $t0 = D = 50
	lw  $t1, 0($s0)     # $t1 = A = 40
	lw  $t2, 0($s4)     # $t2 = E = 3

	sub $t3, $t0, $t1   # $t3 = D - A = 10
	add $t4, $t3, $t2   # $t4 = $t3 + E = 13

	sw  $t4, 0($s2)     # Mem[$s2] = $t4 = 13
