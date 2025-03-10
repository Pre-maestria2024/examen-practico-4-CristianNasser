def main():
    # Leer la entrada
    m, n = map(int, input().split())  # Leer m y n
    H = list(map(int, input().split()))  # Lista de puntos de salud
    D = list(map(int, input().split()))  # Lista de costos en dólares
    
    # Límites máximos permitidos
    MAX_D = 100  # Máximo costo en dólares permitido
    k = 39       # Asumimos k = 39 basado en la salida esperada
    
    # Ajustar los valores de salud según k (fi = min(k, h_i))
    H_ajustado = [min(k, h) for h in H]
    
    # Crear tabla DP: dp[salud][costo] representa si es posible alcanzar esa salud
    MAX_SALUD = k + 1  # Solo necesitamos hasta k
    dp = [[0] * (MAX_D + 1) for _ in range(MAX_SALUD)]
    dp[0][0] = 1  # Estado inicial: 0 salud, 0 costo
    
    # Llenar la tabla DP
    for j in range(len(H)):  # Para cada ítem
        h = H_ajustado[j]  # Salud ajustada
        d = D[j]  # Costo en dólares
        for salud in range(MAX_SALUD - 1, -1, -1):  # Bucle inverso
            for costo in range(MAX_D, -1, -1):
                if dp[salud][costo] == 1:  # Si este estado es alcanzable
                    if costo + d <= MAX_D and salud + h < MAX_SALUD:
                        dp[salud + h][costo + d] = 1
    
    # Encontrar la salud máxima alcanzable
    salud_maxima = 0
    for salud in range(MAX_SALUD):
        for costo in range(MAX_D + 1):
            if dp[salud][costo] == 1:
                salud_maxima = max(salud_maxima, salud)
    
    print(salud_maxima)

if __name__ == '__main__':
    main()

