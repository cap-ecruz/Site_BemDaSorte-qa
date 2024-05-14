from behave import given, then, when
from pages.compraPage import CompraPage
from utils.utils import Utils as info


@given(u'que estou na pagina de carrinho de compra')
def step_impl(context):
    context.compra = CompraPage(context.browser)
    context.compra.paginaCarrinho()
    try:
        context.compra.clicarNoBotaoEntendiPoliticaDeCookies()
    except:
        ...


@when(u'ao adicionar um titulo')
def step_impl(context):
    context.compra.clicarNoBotaoAdicionarTitulo()


@when(u'clicar no botao comprar')
def step_impl(context):
    context.compra.clicarNoBotaoComprar()


@then(u'validar o direcionamento para pagina pagamento')
def step_impl(context):
    context.compra.verificarSeEstaNaPagamento()


@then(u'clicar no botao aceite condicoes gerais')
def step_impl(context):
    context.compra.clicarNoBotaoCondicoesGerais()


@when(u'ao clicar na opcao cartao de credito')
def step_impl(context):
    context.compra.clicarNoCartaoCredito()


@when(u'inserir o numero do cartao {dado}')
def step_impl(context, dado):
    context.compra.inserirNumeroDoCartao(dado)


@when(u'inseir a bandeira mastercard')
def step_impl(context):
    context.compra.clicarOpcaoBandeiraCartaoMastercard()


@when(u'inserir o nome do titular {dado}')
def step_impl(context, dado):
    context.compra.inserirNomeTitular(dado)


@when(u'inserir o data de validade {dado}')
def step_impl(context, dado):
    context.compra.inserirDataValidadeCartao(dado)


@when(u'inserir codigo de seguranca {dado}')
def step_impl(context, dado):
    context.compra.inserirCodigoSeguranca(dado)


@when(u'clicar no botao finalizar compra')
def step_impl(context):
    context.compra.clicarBotaoFinalizarCompra()


@then(u'validar o direcionamento para pagina confirmacao de compra')
def step_impl(context):
    context.compra.verificarSeEstaNaConfirmacaoCompra()


@then(u'verifique a forma de pagamento {dado}')
def step_impl(context, dado):
    context.compra.verificarMensagemFormaDePagamento(dado)


@then(u'valor da compra {dado}')
def step_impl(context, dado):
    context.compra.verificarMensagemValorDeCompra(dado)


@then(u'a campanha atual')
def step_impl(context):
    context.compra.verificarMensagemCampanhaAtual(info.CAMPANHA_ATUAL)
