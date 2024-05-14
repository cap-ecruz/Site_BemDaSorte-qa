from utils.setup import Setup as setup

def before_all(context):
    setup.dadosDoUsuario(context)
    setup.escolherDimensaoTela(context)
    setup.escolherBrowser(context)
    setup.desejaTirarPrint(context)
    setup.abrirBrowser(context)
    setup.acessarHomeBemDaSorte(context)
    # setup.esperarHCaptcha(context)

def before_scenario(context, scenario):
    setup.abrirNovaAba(context)

def after_step(context, scenario):
    setup.gerarPrint(context, scenario, scenario.status)

def after_scenario(context, scenario):
    setup.gerarPrint(context, scenario, scenario.status)
    setup.fecharAba(context)

def after_all(context):
    context.browser.quit()
