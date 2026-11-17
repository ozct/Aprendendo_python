# CONVERSOR DE TEMPERATURA
continuar = True
parar = False

conversao = continuar

temp_final = 0

while conversao:
    valor_temp = float(input("Digite uma temperatura: "))
    tipo_tempo_inicial = input("Digite a unidade de temperatura inicial (C, F ou K): ")
    tipo_tempo_final = input("Digite a unidade de temperatura para a qual deseja converter (C, F ou K): ")

    # Funções para a conversão entre Célsius e Fahrenheit
    funcao_cf = ((valor_temp * 1.8) + 32) # C --> F
    funcao_fc = ((valor_temp - 32) / 1.8) # F --> C

    # Funções para a conversão entre Célcius e Kelvin
    funcao_ck = (valor_temp + 273.15) # C --> K
    funcao_kc = (valor_temp - 273.15) # K --> C

    # Funções para a conversão entre Fahrenheit e Kelvin
    funcao_fk = ((valor_temp + 459.67) / 1.8) # F --> K
    funcao_kf = ((valor_temp * 1.8) - 459.67) # K --> F

    if tipo_tempo_inicial == "C" and tipo_tempo_final == "F":
        temp_final = funcao_cf
        print(f"O resultado da conversão: {valor_temp}°{tipo_tempo_inicial}  -->  {temp_final}°{tipo_tempo_final}")

    elif tipo_tempo_inicial == "F" and tipo_tempo_final == "C":
        temp_final = funcao_fc
        print(f"O resultado da conversão: {valor_temp}°{tipo_tempo_inicial}  -->  {temp_final}°{tipo_tempo_final}")

    elif tipo_tempo_inicial == "C" and tipo_tempo_final == "K":
        temp_final = funcao_ck
        print(f"O resultado da conversão: {valor_temp}°{tipo_tempo_inicial}  -->  {temp_final}{tipo_tempo_final}")

    elif tipo_tempo_inicial == "K" and tipo_tempo_final == "C":
        temp_final = funcao_kc
        print(f"O resultado da conversão: {valor_temp}{tipo_tempo_inicial}  -->  {temp_final}°{tipo_tempo_final}")
    
    elif tipo_tempo_inicial == "F" and tipo_tempo_final == "K":
        temp_final = funcao_fk
        print(f"O resultado da conversão: {valor_temp}°{tipo_tempo_inicial}  -->  {temp_final}{tipo_tempo_final}")

    elif tipo_tempo_inicial == "K" and tipo_tempo_final == "F":
        temp_final = funcao_kf
        print(f"O resultado da conversão: {valor_temp}{tipo_tempo_inicial}  -->  {temp_final}°{tipo_tempo_final}")
    
    print()
    
    continuacao = input("Se deseja continuar para a próxima conversão digite 'continua', e 'parar' para finalizar: ")
    if continuacao == "continua":
        conversao = continuar
    elif continuacao == "parar":
        conversao = parar
    print()