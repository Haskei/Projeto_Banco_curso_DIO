saldo=float(0)
extrato=[]
nun_saque=int(0)
i=0
j=0
while i != 1:
    print("""
          Aperte S e enter parra fazer Saque
          Aperte D e enter para fazer um deposito
          Aperte E e enter para ver o extrato
          aperte T e enterpara Terminar o programa""")
    menu=input()
    menu.upper()
    if menu=="S":
        if nun_saque >= 3:
            print("Numero de saque diários excedidos!")
        else:
            print("Quanto dinheiro você gostaria de sacar?(Limite de R$500,00)")
            din=float(input())
            if din>saldo:
                print("Não há saldo suficiente.")
            elif din>500:
                print("Limite de saque excedido.")
            else:
                saldo = saldo - din
                din = -din
                format(din, ".2f")  
                extrato.append(din)
                nun_saque = nun_saque + 1
                print("Foi retirado",din,"reais da sua conta, há", saldo, "reais restando")
    elif menu=="D":
        print("Quanto dinheiro você ira depósitar?")
        depo=float(input())
        format(depo, ".2f")
        extrato.append(depo)
        saldo = saldo + depo
        print("Foram adicionados R$",depo," a sua conta.")
        print("Seu saldo agora é R$",saldo)
    elif menu=="E":
        if len(extrato)>0:
            while j<len(extrato):
                print("R$",extrato[j])
                j= j+1
        else:
            print("Não foram realizadas movimentações.")
    elif menu=="T":
        print("Muito Obrigado, Volte sempre")
        i=1
