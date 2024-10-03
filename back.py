Sigma = ['m25','m50', 'm100', 'b']   # conjunto de símbolos 
Q = [0, 1, 2, 3, 4, 5, 6, 7, 8]   # conjunto de estados
q0 = 0              # estado inicial
F = [1]             # conjunto de estados finais
# tabela de transição de estados ('0' - col. 0; '1' - col. 1)
delta = [ [0, 1], [2, 1], [1, 1] ]
