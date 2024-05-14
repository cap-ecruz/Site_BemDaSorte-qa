
  @pedido
  Funcionalidade: validar pagina meus pedidos

  Cenario: validar pedido aprovado
    Dado que estou na pagina meus pedidos
    Quando verifique o tipo de pedido como Compra
    E verifique a Forma de pagamento como Cartão de credito
    E verifique a quantidade 1
    E verifique o valor R$ 5,00
    E verifique o status Titulos entregues
    E verifique o step timeline 1 Pedido recebido
    E verifique o step timeline 2 Pagamento aprovado
    E verifique o step timeline 3 Títulos entregues
    E verifique a imagem da campanha atual
    E armazena o numero do titulo
    Então verifique o documento Ficha de cadastro é exibida