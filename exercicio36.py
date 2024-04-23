import time

#########- PROGRAMA DE EMPRESTIMO BANCARIO -##########

print("BEM VINDO AO SISTEMA DE EMPRÉSTIMO DA CAIXA!")
time.sleep(1.5)

#######-Variaveis-############

val_imovel = int(input("Insira o valor do seu imovel: "))
time.sleep(0.5)

sal = int(input("Insira o valor do seu salário: "))
time.sleep(0.3)

anos = int(input("Em quantos anos você irá pagar:"))
time.sleep(1.5)

print("Estamos calculando...")

time.sleep(1.5)

#######-Calculo-############

parcela = anos * 12
parcela_mes= val_imovel / parcela

#########- Lógica -##########

print(f"O valor da parcela mensal é de: R${parcela_mes:.2f}")

if parcela_mes > 0.3 * sal:
    print("O emprestimo está reprovado")

else:
    print("O empréstimo está aprovado")