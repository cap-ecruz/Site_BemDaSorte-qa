@barraDeslogado
Funcionalidade: barra de navegacao - deslogado

  Contexto: abrir a pagina home
    Dado que eu estou na home

  Cenario: barra de navegacao - Logo Bem da sorte
    Quando clico na logo
    Entao valido o direcionamento para pagina home

  Esquema do Cenario: barra de navegacao <opcaomenu>
    Quando clico no menu <opcaomenu>
    Entao valido o direcionamento para a pagina <paginadirecionada>

  Exemplos:
  |opcaomenu                |paginadirecionada          |
  |resultados               |resultados                 |
  |cadastre seu titulo      |cadastro de titulo         |
  |Instituicao beneficiada  |Instituicao beneficiada    |
  |compre ja                |compra do produto          |
  |carrinho                 |checkout carrinho          |
  |botao login              |login                      |