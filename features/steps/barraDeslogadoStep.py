from behave import given, then, when
from pages.barraDeNavegacaoPage import BarraDeNavegacaoPage


@given(u'que eu estou na home')
def step_impl(context):
    context.barraDeNavegacao = BarraDeNavegacaoPage(context.browser)
    context.barraDeNavegacao.paginaHome()


@when(u'clico na logo')
def step_impl(context):
    context.barraDeNavegacao.clicarNaLogo()


@then(u'valido o direcionamento para a pagina home')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaHome()


# removido na versão 2
# @when(u'clico no menu home')
# def step_impl(context):
#     context.barraDeNavegacao.clicarNaHome()

@when(u'clico no menu resultados')
def step_impl(context):
    context.barraDeNavegacao.clicarNaResultados()


@then(u'valido o direcionamento para a pagina resultados')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaResultados()


@when(u'clico no menu cadastre seu titulo')
def step_impl(context):
    context.barraDeNavegacao.clicarNoMenuCadastreSeuTitulo()


@then(u'valido o direcionamento para a pagina cadastro de titulo')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaCadastroDeTitulo()


@when(u'clico no menu Instituicao beneficiada')
def step_impl(context):
    context.barraDeNavegacao.clicarNoMenuInstituicaoBeneficiada()


@then(u'valido o direcionamento para a pagina Instituicao beneficiada')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaInstituicaoBeneficiada()


@when(u'clico no menu compre ja')
def step_impl(context):
    context.barraDeNavegacao.clicarNoMenuCompreJa()


@then(u'valido o direcionamento para a pagina compra do produto')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaDeComrpaDoProduto()


@when(u'clico no menu carrinho')
def step_impl(context):
    context.barraDeNavegacao.clicarNoCarrinho()


@then(u'valido o direcionamento para a pagina checkout carrinho')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaCheckoutCarrinho()


@when(u'clico no menu botao login')
def step_impl(context):
    context.barraDeNavegacao.clicarNoBotaoLogin()


@then(u'valido o direcionamento para a pagina login')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaLogin()