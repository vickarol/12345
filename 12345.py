import math

def calculadora():
    operacoes = "+ - * / ** sqrt".split()
    
    while True:
        print("\nOperações disponíveis:", ", ".join(operacoes))
        operacao = input("Digite a operação desejada ou 'sair' para encerrar: ").strip().lower()
        
        if operacao == "sair":
            break
        
        if operacao not in operacoes:
            print("Operação inválida.")
            continue
        
        if operacao == "sqrt":
            num = float(input("Digite um número para calcular a raiz quadrada: "))
            print(f"A raiz quadrada de {num} é {math.sqrt(num)}")
        else:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    print("Erro: divisão por zero.")
                    continue
                resultado = num1 / num2
            elif operacao == "**":
                resultado = num1 ** num2
            
            print(f"Resultado: {resultado}")

# Exemplo de uso:
# calculadora()
