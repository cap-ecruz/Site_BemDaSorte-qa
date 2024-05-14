import time

from selenium.webdriver.common.by import By

from pages.verificarPaginasPage import VerificarPaginas
from nose.tools import assert_equal


class CompraElementos(object):
    BOTAO_ENTENDI_POLITICA_COOKIES = (By.XPATH, '/html/body/div[1]/div/a')

    BOTAO_MAIS_PAGINA_CARRINHO = (By.CLASS_NAME, 'fa.fa-plus')
    BOTAO_COMPRAR_PAGINA_CARRINHO = (By.CLASS_NAME, 'btn-primary.btn-block.comprar')

    BOTAO_ACEITE_CONDICOES_GERAIS = (By.XPATH, '/html/body/app-root/ng-component/main/div/div['
                                               '1]/app-checkout-formas-pagamento/div/div/app-checkout-condicoes'
                                               '-gerais-aceitar/div/p[2]/button')

    OPCAO_CARTAO_CREDITO = (By.XPATH, '/html/body/app-root/ng-component/main/div/div['
                                      '1]/app-checkout-formas-pagamento/div/div/div/div[1]/div[1]/button')

    # dados do cartao
    NUMERO_DO_CARTAO = (By.ID, 'CardNumber')
    BANDEIRA_DO_CARTAO = (By.CSS_SELECTOR, '.is-mastercard')
    NOME_DO_TITULAR = (By.ID, 'CardName')
    DATA_VALIDADE = (By.ID, 'CardExpiration')
    CODIGO_SEGURANCA = (By.ID, 'SecurityCode')

    BOTAO_FINALIZAR_COMPRA = (By.ID, 'Finalizar')

    # PAGINA DE CONFIRMACAO DE PAGAMENTO

    DETALHE_FORMA_DE_PAGAMENTO = (By.ID, 'card')
    DETALHE_VALOR_DA_COMPRA = (By.ID, 'valor')
    DETALHE_CAMPANHA_ATUAL = (By.XPATH, '/html/body/app-root/ng-component/main/div/div['
                                        '1]/app-checkout-pedido-status/div/div[2]/p[1]/strong[3]')


class CompraPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = CompraElementos()

    def paginaCarrinho(self):
        self._comandos.navegar(self.PAGINA_COMPRA_CARRINHO)

    def clicarNoBotaoEntendiPoliticaDeCookies(self):
        self._comandos.clicar(self.elemento.BOTAO_ENTENDI_POLITICA_COOKIES)
        time.sleep(0.5)

    def clicarNoBotaoAdicionarTitulo(self):
        self._comandos.clicar(self.elemento.BOTAO_MAIS_PAGINA_CARRINHO)

    def clciarNoBotaoComprar(self):
        self._comandos.clicar(self.elemento.BOTAO_COMPRAR_PAGINA_CARRINHO)

    def clicarNoBotaoCondicoesGerais(self):
        try:
            self._comandos.clicar(self.elemento.BOTAO_ACEITE_CONDICOES_GERAIS)
        except:
            ...

    def clicarNoCartaoCredito(self):
        self._comandos.clicar(self.elemento.OPCAO_CARTAO_CREDITO)

    def inserirNumeroDoCartao(self, dado):
        self._comandos.inserirDado(self.elemento.NUMERO_DO_CARTAO, dado)

    def clicarOpcaoBandeiraCartaoMastercard(self):
        time.sleep(0.5)
        self._comandos.clicar(self.elemento.BANDEIRA_DO_CARTAO)

    def inserirNomeTitular(self, dado):
        self._comandos.inserirDado(self.elemento.NOME_DO_TITULAR, dado)

    def inserirDataValidadeCartao(self, dado):
        self._comandos.inserirDado(self.elemento.DATA_VALIDADE, dado)

    def inserirCodigoSeguranca(self, dado):
        self._comandos.inserirDado(self.elemento.CODIGO_SEGURANCA, dado)

    def clicarBotaoFinalizarCompra(self):
        self._comandos.clicar(self.elemento.BOTAO_FINALIZAR_COMPRA)

    def verificarMensagemFormaDePagamento(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.DETALHE_FORMA_DE_PAGAMENTO), msg)

    def verificarMensagemValorDeCompra(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.DETALHE_VALOR_DA_COMPRA), msg)

    def verificarMensagemCampanhaAtual(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.DETALHE_CAMPANHA_ATUAL), msg)
