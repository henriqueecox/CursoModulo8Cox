from mean_var_std import calculate

try:
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print("Resultado:")
    print(result)
except Exception as e:
    print(f"Erro: {e}")
