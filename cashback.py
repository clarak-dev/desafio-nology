def calcular_cashback(valor_produto, percentual_desconto, tipo_cliente):
    valor_final = valor_produto * (1 - percentual_desconto / 100)

    cashback_base = valor_final * 0.05

    bonus_vip = 0
    if tipo_cliente.lower() == "vip":
        bonus_vip = cashback_base * 0.10

    cashback = cashback_base + bonus_vip

    if valor_final > 500:
        cashback *= 2

    return round(cashback, 2)


if __name__ == "__main__":
    print("VIP, 600, 20%:", calcular_cashback(600, 20, "vip"))
    print("Normal, 600, 10%:", calcular_cashback(600, 10, "normal"))
    print("VIP, 600, 15%:", calcular_cashback(600, 15, "vip"))