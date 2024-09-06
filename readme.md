 <h1>Simulador de Conta Bancária</h1>

<p>Este repositório é destinado a atualização do sistema bancário já realizado no bootcamp NTT Data - Engenharia de Dados com Python, na plataforma DIO.<p>

<hr>

 <h1>Requisitos e funcionalidades do desafio</h1>

 <h3> Operação Depósito <h3>

 <p>Deve ser possível depositar valores para a conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato<p>

 <h3> Operação Saque <h3>

 <p>O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informado que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.<p>

 <h3> Operação Extrato <h3>

 <p>Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45<p>

<h3>Cadastrar usuários e Filtrar usuário<h3>
<p>A função cadastrar permite o cadastro de novos usuários, solicitando nome completo, cpf, data de nascimento e endereço, caso aja usuário com o cpf já cadastrado, a função filtrar_usuário impede o cadastro de usuário com mesmo cpf<p>

<h3>Cadastrar conta<h3>
<p>A função cadastrar conta permite que um usuário já cadastrado possa criar novas contas, ela também utiliza a função filtrar cpf para verificar se o cpf informado já existe, caso exista, uma nova conta é cadastrada<p>

<h3>Listar conta<h3>
<p>Esta função lista contas existentes, informando agencia, nome do titular e número da conta<p>
<hr>

<h1>Tecnologia Utilizada <h1>

<img align="center" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />