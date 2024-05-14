from behave import given, then, when
from pages.rodapePage import RodapePage


@given(u'que estou em uma pagina do Bem da sorte')
def step_impl(context):
    context.rodape = RodapePage(context.browser)
    context.rodape.paginaHome()


@when(u'clico no link Duvidas Frequentes')
def step_impl(context):
    context.rodape.clicarDuvidas()


@then(u'valido do direcionamento para pagina faq')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaAtendimento()


@when(u'clico no menu do rodape {opcao}')
def step_impl(context, opcao):
    context.rodape.clicarTermos(opcao)


@then(u'verifico o direcionamento para pagina {escolhida}')
def step_impl(context, escolhida):
    context.rodape.verificarSeEstaNaPagina(escolhida)


@when(u'clico na rede social {opcao}')
def step_impl(context, opcao):
    context.rodape.clicarNaRedeSocial(opcao)


@then(u'valido o direcionamento para pagina das redes sociais {opcao}')
def step_impl(context, opcao):
    context.rodape.verificarSeEstaNaPaginaRedesSociais(opcao)


@when(u'clico no icone {opcao}')
def step_impl(context, opcao):
    context.rodape.clicarIconeLogo(opcao)


@then(u'valido o direcionamento para pagina da home')
def step_impl(context):
    context.rodape.mudarDeAba('home')
    context.rodape.verificarSeEstaNaPaginaHome()


@then(u'valido o direcionamento para pagina da brasilcap')
def step_impl(context):
    context.rodape.mudarDeAba('brasilcap')
    context.rodape.verificarSeEstaNaPaginaBrasilCap()