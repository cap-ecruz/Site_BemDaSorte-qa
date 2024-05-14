import time
from behave import given, then, when
from pages.homePage import HomePage


@given(u'que eu estou na pagina home')
def step_impl(context):
    time.sleep(0.5)
    context.home = HomePage(context.browser)
    context.home.paginaHome()


@then(u'verifico a exibicao da mensagem de cookie {msg}')
def step_impl(context, msg):
    context.home.verificarMensagemCookie(msg)


@when(u'ao clicar no link Politica de privacidade')
def step_impl(context):
    context.home.clicarNoLinkPoliticaDePrivacidade()


@then(u'verifica o direcionamento para pagina Politica de Privacidade')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaPoliticaDePrivacidade()


@when(u'ao clicar no botao do banner principal')
def step_impl(context):
    context.home.clicarNoBotaoDoBannerPrincipalHome()


@then(u'valido na home o valor R$ {valor},00')
def step_impl(context, valor):
    valor = 'R$\n' + valor + '\n,00'
    context.home.verificarValorUnitarioTiutlo(valor)


@then(u'valido o valor {valor}')
def step_impl(context, valor):
    context.home.validarOValorTotal(valor)


@then(u'valido botao comprar desativado')
def step_impl(context):
    context.home.validarBotaoCompraDesativado()


@when(u'ao clicar no botao mais {qtd} vezes')
def step_impl(context, qtd):
    context.home.adicionarTituloCompraHome(qtd)


@then(u'valido botao comprar ativado')
def step_impl(context):
    context.home.validarBotaoCompraAtivado()


@when(u'ao clicar no botao menos {qtd}')
def step_impl(context, qtd):
    context.home.removerTituloCompraHome(qtd)


@when(u'ao clicar no botao comprar')
def step_impl(context):
    context.home.clicarNoBotaoComprarDaPaginaHome()


@then(u'valido na pagina checkout o valor na pagina checkout carrinho {valor}')
def step_impl(context, valor):
    context.home.verificarValorTotalPaginaCheckout(valor)


@then(u'valido na pagina checkout o {valor}')
def step_impl(context, valor):
    context.home.verificarSubTotalPaginaCheckout(valor)


@when(u'ao clicar no botao +5')
def step_impl(context):
    context.home.clicarNoBotaoMais5()


@when(u'ao clicar no botao +10')
def step_impl(context):
    context.home.clicarNoBotaoMais10()


@when(u'ao clicar no botao +5 {qtd} vezes')
def step_impl(context, qtd):
    for clicar in range(int(qtd)):
        context.home.clicarNoBotaoMais5()


@when(u'ao clicar no botao +10 {qtd} vezes')
def step_impl(context, qtd):
    for clicar in range(int(qtd)):
        context.home.clicarNoBotaoMais10()


@when(u'ao clicar no botao limpar')
def step_impl(context):
    context.home.clicarNoBotaoLimpar()


#  clicar no banner vantagens do bem da sorte

@when(u'ao clicar no banner vantagens do bem da sorte')
def step_impl(context):
    context.home.clicarNoBannerVantagensDoBemDaSorte()


# premiacao sem complicacao - pagina premiacoes logado

@when(u'ao clicar no botao clique aqui e confira seus resultados')
def step_impl(context):
    context.home.clicarNoBotaoCliqueAquiEConfiraSeusResultados()


@then(u'valido o direcionamento para pagina minhas premiacoes')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaMinhasPremiacoes()


# meus atalhos logado- <opcaoatalho>


@when(u'ao clicar no card conferir sorteios')
def step_impl(context):
    context.home.clicarNoCardConferirSorteio()


@when(u'ao clicar no card meus pedidos')
def step_impl(context):
    context.home.clicarNoCardMeusPedidos()


@when(u'ao clicar no card meus titulos')
def step_impl(context):
    context.home.clicarNoCardMeusTitulos()


# clicar no banner cadastre seu bem da sorte fisico

@when(u'ao clicar no banner cadastre seu bem da sorte fisico')
def step_impl(context):
    context.home.clicarNoBannerCadastreSeuBemDaSorteFisico()


# clicar o botao veja mais sobre a fundacao abrinq

@when(u'ao clicar no botao veja mais sobre a fundacao abrinq')
def step_impl(context):
    context.home.clicarNoBotaoVejaMaisSobreAFundacaoAbrinq()


# -------------------
@then(u'valido o direcionamento para pagina compra do produto')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaDeComrpaDoProduto()


@then(u'valido o direcionamento para pagina resultados')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaResultados()


@then(u'valido o direcionamento para pagina Instituicao beneficiada')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaInstituicaoBeneficiada()


@then(u'valido o direcionamento para pagina login')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaLogin()

# ---- validar campo de login da pagina de cadastro titulo fisico
@then(u'valido o campo login na pagina cadastro de titulo')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaCadastroTituloDeslogado()

# --- validar campo de login na pagina de compra
@then(u'valido o direcionamento para a pagina checkout carrinho deslogado')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaCheckoutDeslogado()

# ----- faq home
@when(u'ao clicar no link da faq {link}')
def step_impl(context, link):
    context.home.clicarNoLinkDaFaq(link)


@then(u'valido o direcionamento para pagina da duvida frequentes faq1')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaDuvidasFrequentesFaq1()


@then(u'valido o direcionamento para pagina da duvida frequentes faq2')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaDuvidasFrequentesFaq2()


@then(u'valido o direcionamento para pagina da duvida frequentes faq')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaDuvidasFrequentes()