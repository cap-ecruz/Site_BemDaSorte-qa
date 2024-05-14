@homeDeslogado
Funcionalidade: Home - deslogado

  Contexto: Abrir pagina home
    Dado que eu estou na pagina home

  Cenario: Mensagem de cookie
    Entao verifico a exibicao da mensagem de cookie Utilizamos cookies para analisar o uso do nosso site, direcionar conteúdos e oferecer ótima experiência para você. Para maiores informações consulte nossa POLÍTICA DE PRIVACIDADE, ou para seguir, declare estar ciente.

  Cenario: Link Politica privacidade
    Quando ao clicar no link Politica de privacidade
    Entao verifica o direcionamento para pagina Politica de Privacidade

  Cenario: Clicar no botao da banner principal
    Quando ao clicar no botao do banner principal
    Entao valido o direcionamento para pagina compra do produto

  Cenario: validar o valor unitario
    Entao valido na home o valor R$ 5,00

  Cenario: botao comprar desativado com valor 0
    Entao valido o valor TOTAL: R$ 0,00
    E valido botao comprar desativado

  #quantidade maxima por pedido 25
  Cenario: selecionar a quantidade maxima de titulos
    Quando ao clicar no botao mais 30 vezes
    Entao valido o valor TOTAL: R$ 125,00
    E valido botao comprar ativado

  Cenario: selecionar a quantidade minima de titulos
    Quando ao clicar no botao mais 5 vezes
    Quando ao clicar no botao menos 7
    Entao valido o valor TOTAL: R$ 0,00
    E valido botao comprar desativado

  Cenario: Validar o botão + 5
    Quando ao clicar no botao +5
    Entao valido o valor TOTAL: R$ 25,00

  Cenario: Validar o botão +10
    Quando ao clicar no botao +10
    Entao valido o valor TOTAL: R$ 50,00

  Cenario: Selecionar a quantidade maxima com o botão +5
    Quando ao clicar no botao +5 5 vezes
    Entao valido o valor TOTAL: R$ 125,00
    E valido botao comprar ativado

  Cenario: Selecionar a quantidade maxima com o botão +10
    Quando ao clicar no botao +10 3 vezes
    Entao valido o valor TOTAL: R$ 125,00
    E valido botao comprar ativado

  Cenario: validar o botão limpar (Quantidade de titulo por pedido)
    Quando ao clicar no botao mais 5 vezes
    Entao valido o valor TOTAL: R$ 25,00
    Quando ao clicar no botao limpar
    Entao valido o valor TOTAL: R$ 0,00
    E valido botao comprar desativado

  Cenario: comprar titulo na home
    Quando ao clicar no botao mais 5 vezes
    E ao clicar no botao comprar
    Entao valido o direcionamento para a pagina checkout carrinho deslogado

  Cenario: clicar no banner vantagens do bem da sorte
    Quando ao clicar no banner vantagens do bem da sorte
    Entao valido o direcionamento para pagina compra do produto

  Cenario: premiacao sem complicacao - pagina premiacoes - deslogado
    Quando ao clicar no botao clique aqui e confira seus resultados
    Entao valido o direcionamento para pagina login

  Esquema do Cenario: meus atalhos logado- <opcaoatalho>
    Quando ao clicar no card <opcaoatalho>
    Entao valido o direcionamento para pagina <paginadirecionada>

  Exemplos:
  |opcaoatalho              |paginadirecionada          |
  |conferir sorteios        |resultados                 |
  |meus pedidos             |login                      |
  |meus titulos             |login                      |

#validar o campo login
  Cenario: clicar o botao veja mais sobre a fundacao abrinq
    Quando ao clicar no botao veja mais sobre a fundacao abrinq
    Entao valido o direcionamento para pagina Instituicao beneficiada

  Esquema do Cenario: Secao tem alguma duvida acesse nossa faq - <linkfaq>
    Quando ao clicar no link da faq <linkfaq>
    Entao valido o direcionamento para pagina da duvida frequentes <paginadirecionada>

  Exemplos:
  |linkfaq                        |paginadirecionada         |
  |ler mais 1                     |faq1                      |
  |ler mais 2                     |faq2                      |
  |ver mais duvidas frequentes    |faq                       |


#  Cenario: Cadastre se na nossa newsletter - dados em branco
#    Quando ao focar no campo nome
#    E ao focar no campo email
#    Entao verificar a mensagem no campo nome Preenchimento obrigatório
#    E verificar a mensagem no campo email Preenchimento obrigatório
#    E verificar o botao cadastrar esta desativado