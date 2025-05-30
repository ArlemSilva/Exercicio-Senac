while True:
    try:
        num2 = int(input('Digite outro numero inteiro: '))
        if operacao == '/' and num2 == 0:
            raise ValueError('Não possivel dividir por zero. ')
        break
    except ValueError as e:
        print(f'erro {e}')


