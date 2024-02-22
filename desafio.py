#Programa de cálculo de KPI

nome = input("Qual seu nome?")
salario = int(input("Qual o seu salário?"))
pct_bonus = float(input("Qual o seu percentual de bonus?"))
bonus_fixo = 1000

bonus = bonus_fixo + (salario * (1 + pct_bonus))

print(f"O bônus do {nome} possui o bonus de {bonus}")