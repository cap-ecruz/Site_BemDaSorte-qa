@compra
  Funcionalidade: efetuar fluxo de compra

  Contexto: acessar pagina compra
    Dado que estou na pagina de carrinho de compra
    E ao adicionar um titulo
    E clicar no botao aceite condicoes gerais
    E clicar no botao aceite da ficha de cadastro
    E clicar no botao comprar
    E validar o direcionamento para pagina pagamento
    
  Cenario: Efetuar uma compra
    Quando ao clicar na opcao cartao de credito
    E inserir o numero do cartao 5031433215406351
    E inseir a bandeira mastercard
    E inserir o nome do titular APRO da Silva
    E inserir o data de validade 1230
    E inserir codigo de seguranca 123
    E clicar no botao finalizar compra
    E validar o direcionamento para pagina confirmacao de compra
    E verifique a forma de pagamento Cartão de crédito Mastercard
    E valor da compra R$ 5,00
    Então a campanha atual


