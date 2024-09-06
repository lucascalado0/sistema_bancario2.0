import datetime 

def menu(): 
    mensagem_menu ="""
####### MENU #######
    
[D]Depósito
[S]Saque
[E]Extrato
[NC]Nova Conta
[LC]Listar contas
[NU]Novo usuário
[Q]Encerrar
 
"""
    return mensagem_menu


def boas_vindas(nome_usuario):
    mensagem = f"\nBem vindo {nome_usuario}, escolha uma opção: "
    
    return mensagem


def depositar(valor):
    global saldo
    global transacoes
    global valor_depositado
    global numero_deposito
    
    if valor > 0:
        numero_deposito += 1
        valor_depositado += valor
        saldo += valor
        transacoes += 1
        mensagem_deposito = f"\nR${valor:.2f} depositado com sucesso!\nSaldo atual: R${saldo:.2f}"
        
    else:
        mensagem_deposito = "\nO valor informado é inválido, tente novamente!"
        
    return mensagem_deposito


def sacar(valor):
    global saldo
    global transacoes
    global valor_sacado
    global numero_saque
    
    if valor < saldo and valor > 0:
        numero_saque +=1
        valor_sacado += valor
        saldo -= valor
        transacoes += 1
        
        mensagem_saque = f"R${valor:.2f} sacado com sucesso!\n Saldo atual da conta: R${saldo:.2f}"
    
    elif valor > saldo:
        mensagem_saque = "Saldo insuficiente!"
    
    else:
        mensagem_saque = "Valor inválido, tente novamente!"
        
    return mensagem_saque


def cadastrar_usuario(usuarios): 
    
    cadastro = """
    ######### NOVO CADASTRO ######### """
    
    print(cadastro)
    cpf = input("Informe o seu cpf(Somente os números): ")
    usuario_filtrado = filtrar_usuario(cpf, usuarios)
    
    if usuario_filtrado:
        print("\nUsuário ja existe em nosso sistema, tente novamente ! ")
        return 
    
    nome_usuario = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd/mm/aaaa):")
    endereco = input("Informe o seu endereço(rua, nº - bairro - cidade/sigla estado):")
    
    usuarios.append({"nome": nome_usuario, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    
    mensagem_cadastro = "\nUsuário cadastrado com sucesso :)!"
    
    print(mensagem_cadastro) 


def filtrar_usuario(cpf, usuarios):
    
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    

def cadastrar_conta(agencia, numero_conta, usuarios):
    
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


def listar_contas(contas):
    for conta in contas:
        lista = f"""
        Agência: {conta['agencia']}
        Conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("----------------------------------------------")
        print(lista)
    
    
def extrato():
    global novo_usuario
    horario_extrato = datetime.datetime.today()
    
    print(" Extrato Bancário ".center(44, "#"))
    
    extrato = f"""
    \nExtrato gerado em: {horario_extrato.strftime("%d/%m/%Y - %H:%M:%S")}
    \nAgência: {agencia}  Cliente: {novo_usuario}
    \nValor depositado: R${valor_depositado}
    \nValor sacado: R${valor_sacado}
    \nNº de transações: {transacoes}
    \nSaldo: R${saldo:.2f}
    """
    return extrato


def mensagem_encerramento(nome_usuario):
    mensagem = f"\nEncerrando atendimento...\nObrigado por utilizar os nossos serviços {nome_usuario}, volte sempre!"

    return mensagem

def main():
    
    

    novo_usuario = input("Para inicializar o atendimento, informe como você gostaria de ser chamado: ")
    cadastrar_usuario(usuarios)
    print(boas_vindas(novo_usuario))


    while True:
        print(menu())
        opcao = input("=> ").upper()
        
        if opcao == "D":
            valor = float(input("Informe o valor que você deseja depositar: "))
            
            print(depositar(valor))
        
        elif opcao == "S":
            valor = float(input("Informe o valor que você deseja sacar: "))
            
            if numero_saque == LIMITE_SAQUES:
                print("\nO limite diário de saques já foi atingido!")
            
            elif valor > limite:
                print("O seu limite por saque é R$500")
            
            else:
                print(sacar(valor))
                
                
        elif opcao == "E":
            if transacoes > 0:
                print(extrato())
                
            else:
                horario_extrato = datetime.datetime.today()
                print(f"""\n
                    \nExtrato gerado em: {horario_extrato.strftime("%d/%m/%Y - %H:%M:%S")}
                    \nAgência: {agencia}  Cliente: {novo_usuario}
                    \nNão houve movimentações na conta!""")
        
        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(agencia, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "LC":
            listar_contas(contas)
        
        elif opcao == "NU":
            cadastrar_usuario(usuarios)

        elif opcao == "Q":
            print(mensagem_encerramento(novo_usuario))
            break
        
        else:
            print("\nOpção inválida, informe novamente!")

contas = []
usuarios = []  
agencia = "0001"
saldo = 0
transacoes = 0
valor_depositado = 0
valor_sacado = 0
numero_deposito = 0
numero_saque = 0
limite = 500
LIMITE_SAQUES = 3
          

main()