from behave import given, then, when
from pages.meusPedidosPage import MeusPedidosPage
from utils.utils import Utils as info


@given(u'que estou na pagina meus pedidos')
def step_impl(context):
    context.pedidos = MeusPedidosPage(context.browser)
    context.pedidos.paginaMeusPedidos()
    try:
        context.pedidos.clicarNoBotaoEntendiPoliticaDeCookies()
    except:
        ...


@when(u'ao clicar no botao mostrar detalhes')
def step_impl(context):
    context.pedidos.clicarNoBotaoMostrarDetalhes()


@then(u'verifique o tipo de pedido como {dado}')
def step_impl(context, dado):
    context.pedidos.verificarTipoDePedido(dado)


@then(u'verifique o valor {dado}')
def step_impl(context, dado):
    context.pedidos.verificarValorDoPedido(dado)


@then(u'verifique o status {dado}')
def step_impl(context, dado):
    context.pedidos.verificarStatus(dado)


@then(u'verifique a quantidade {qtd}')
def step_impl(context, qtd):
    context.pedidos.verificarQuantidade(qtd)


@then(u'verifique o total da compra {dado}')
def step_impl(context, dado):
    context.pedidos.verificarValorTotalDaCompra(dado)


@then(u'verifique o step timeline 1 {msg}')
def step_impl(context, msg):
    context.pedidos.verificarStepTimeLinePedidoRecebido(msg)


@then(u'verifique o step timeline 2 {msg}')
def step_impl(context, msg):
    context.pedidos.verificarStepTimeLinePagamentoAprovado(msg)


@then(u'verifique o step timeline 3 {msg}')
def step_impl(context, msg):
    context.pedidos.verificarStepTimeLineTitulosEntregues(msg)


@then(u'verifique a campanha atual')
def step_impl(context):
    context.pedidos.verificarCampanhaAtualNaPaginaMeusPedidos(info.CAMPANHA_ATUAL)


@then(u'armazena o numero do titulo')
def step_impl(context):
    context.pedidos.armazenarNumeroDoTitulo()


@then(u'verifique o valor')
def step_impl(context):
    context.pedidos.verificarDoValorDoTituloNovo()
