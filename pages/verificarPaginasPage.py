from utils.comandos import Comandos
from utils.urlPage import Paginas

from nose.tools import assert_equal
from selenium.webdriver.common.by import By


class VerificarPaginas(Paginas):
    def __init__(self, webdriver):
        self._comandos = Comandos(webdriver)

    def verificarSeEstaNaPaginaLogin(self):
        self._comandos.encontrarClassePrincipal("login-page")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_LOGIN)

    def verificarSeEstaNaPaginaCadastroPasso1(self):
        self._comandos.encontrarClassePrincipal("cadastro-page")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_PASSO1)

    def verificarSeEstaNaPaginaCadastroPasso2(self):
        self._comandos.encontrarClassePrincipal("cadastro-page")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_PASSO2)

    def verificarSeEstaNaPaginaCadastroPasso3(self):
        self._comandos.encontrarClassePrincipal("cadastro-page")
        self._comandos.esperarTexto(
            (By.XPATH, '/html/body/app-root/ng-component/main/app-breadcrumb/nav/ol/li[3]/span'), 'Senha e Aceites')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_PASSO3)

    def verificarSeEstaNaMinhaConta(self):
        self._comandos.encontrarClassePrincipal('minha-conta')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MINHA_CONTA)

    def verificarSeEstaNaPagamento(self):
        self._comandos.encontrarClassePrincipal('checkout-page')
        self._comandos.esperar_elemento((By.XPATH, '/html/body/app-root/ng-component/main/div/div['
                                                   '1]/app-checkout-formas-pagamento/div'))
        assert_equal(self._comandos.capturar_url(), self.PAGINA_COMPRA_PAGAMENTO)

    def verificarSeEstaNaConfirmacaoCompra(self):
        self._comandos.encontrarClassePrincipal('checkout-page')
        self._comandos.esperar_elemento((By.XPATH, '/html/body/app-root/ng-component/main/div/div['
                                                   '1]/app-checkout-pedido-status/div'))
        assert_equal(self._comandos.capturar_url(), self.PAGINA_COMPRA_CONFIRMACAO)




    def verificarSeEstaNaPaginaHome(self):
        self._comandos.encontrarClassePrincipal("page-home")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_HOME)

    def verificarSeEstaNaPaginaResultados(self):
        self._comandos.encontrarClassePrincipal('page-resultados')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_RESULTADOS)

    def verificarSeEstaNaPaginaCadastroDeTitulo(self):
        self._comandos.encontrarClassePrincipal('cadastro-titulo-page')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_DE_TITULO)

    def verificarSeEstaNaPaginaInstituicaoBeneficiada(self):
        self._comandos.encontrarClassePrincipal('page-entidade')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_INSTITUICAO_BENEFICIADA)

    def verificarSeEstaNaPaginaDeComrpaDoProduto(self):
        self._comandos.encontrarClassePrincipal('checkout-page')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_COMPREJA)

    def verificarSeEstaNaPaginaCheckoutCarrinho(self):
        self._comandos.encontrarClassePrincipal('checkout-page')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CARRINHO)

    def verificarSeEstaNaPaginaLogin(self):
        self._comandos.encontrarClassePrincipal('page-login')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_LOGIN)

    def verificarSeEstaNaPaginaMinhaConta(self):
        self._comandos.encontrarClassePrincipal('page-minha-conta')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MINHA_CONTA)

    def verificarSeEstaNaPaginaMeusTitulos(self):
        self._comandos.encontrarClassePrincipal('page-meus-titulos')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MEUS_TITULOS)

    def verificarSeEstaNaPaginaMeusPedidos(self):
        self._comandos.encontrarClassePrincipal('page-meus-pedidos')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MEUS_PEDIDOS)

    def verificarSeEstaNaPaginaMeusDados(self):
        self._comandos.encontrarClassePrincipal('page-meus-dados')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MEUS_DADOS)

    def verificarSeEstaNaPaginaMinhasPremiacoes(self):
        self._comandos.encontrarClassePrincipal('page-minhas-premiacoes')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MINHAS_PREMIACOES)

    def verificarSeEstaNaPaginaCondicoesGerais(self):
        self._comandos.encontrarClassePrincipal('page-condicoes-gerais')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CONDICOES_GERAIS)

    def verificarSeEstaNaPaginaTermosLegais(self):
        self._comandos.encontrarClassePrincipal('page-termos-legais')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_TERMOS_LEGAIS)

    def verificarSeEstaNaPaginaTermosUso(self):
        self._comandos.encontrarClassePrincipal('page-termos-de-uso')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_TERMOS_USO)

    def verificarSeEstaNaPaginaPoliticaDePrivacidade(self):
        self._comandos.encontrarClassePrincipal('page-politica-de-privacidade')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_POLITICA_DE_PRIVACIDADE)

    def verificarSeEstaNaPaginaPolicitaDeCookies(self):
        self._comandos.encontrarClassePrincipal('page-politica-de-privacidade')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_POLITICA_DE_COOKIES)

    def verificarSeEstaNaPaginaBrasilCap(self):
        time.sleep(5)
        assert_equal(self._comandos.capturar_url(), self.PAGINA_BRASILCAP)

    def verificarSeEstaNaPaginaDuvidasFrequentesFaq1(self):
        self._comandos.encontrarClassePrincipal('duvidas-frequentes-page')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES_FAQ1)

    def verificarSeEstaNaPaginaDuvidasFrequentesFaq2(self):
        self._comandos.encontrarClassePrincipal('duvidas-frequentes-page')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES_FAQ2)

    def verificarSeEstaNaPaginaDuvidasFrequentes(self):
        self._comandos.encontrarClassePrincipal('duvidas-frequentes-page')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES)

    def verificarSeEstaNaPaginaCadastroTituloDeslogado(self):
        self._comandos.encontrarClassePrincipal('cadastro-titulo-page')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_DE_TITULO)
        self._comandos.encontrarClassePrincipal('fl-login')
        # titulo do campo de login
        self._comandos.esperar_elemento((By.XPATH, '/html/body/app-root/div/ng-component/main/section/div/app-form'
                                                   '-login/div/form/div[1]'))

    def verificarSeEstaNaPaginaCheckoutDeslogado(self):
        self._comandos.encontrarClassePrincipal('checkout-page')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CARRINHO)
        self._comandos.encontrarClassePrincipal('fl-login')
        # titulo do campo de login
        self._comandos.esperar_elemento((By.XPATH, '/html/body/app-root/div/ng-component/main/section/div/div/div/div'
                                                   '/div/app-form-login/div/form/div[1]'))