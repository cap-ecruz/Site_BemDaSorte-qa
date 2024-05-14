from selenium.webdriver.common.by import By
from nose.tools import assert_equal
from pages.verificarPaginasPage import VerificarPaginas



class RodapeElementos(object):
    RODAPE_LOGO_BEM_DA_SORTE = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[1]/div/a')
    RODAPE_LOGO_BRASILCAP = (By.XPATH, '/html/body/app-root/app-footer/footer/section[1]/div/div/div['
                                       '1]/div/a/app-img/img')
    RODAPE_DUVIDAS = (By.XPATH, '//*[@title="Dúvidas Frequentes"]')
    RODAPE_RESULTADOS = (By.XPATH, '//*[@id="mainMenu"]/ul[1]/li[2]/a')
    RODAPE_CONDICOES_GERAIS = (By.XPATH, '//a[contains(text(), "Condições Gerais")]')
    RODAPE_TERMOS_LEGAL = (By.XPATH, '//a[contains(text(), "Termos Legais")]')
    RODAPE_TERMOS_USO = (By.XPATH, '//a[contains(text(), "Termos de Uso")]')
    RODAPE_TERMOS_PRIVACIDADE = (By.XPATH, '//a[contains(text(), "Política de Privacidade")]')
    RODAPE_TERMOS_COOKIE = (By.XPATH, '//a[contains(text(), "Política de Cookies")]')

    #  Redes Sociais Rodape
    RODAPE_FACEBOOK = (By.XPATH, '/html/body/app-root/app-footer/footer/section[2]/div/ul/li[1]/a')
    RODAPE_INSTAGRAM = (By.XPATH, '/html/body/app-root/app-footer/footer/section[2]/div/ul/li[2]/a')
    RODAPE_TIKTOK = (By.XPATH, '/html/body/app-root/app-footer/footer/section[2]/div/ul/li[3]/a')
    RODAPE_YOUTUBE = (By.XPATH, '/html/body/app-root/app-footer/footer/section[2]/div/ul/li[4]/a')


class RodapePage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = RodapeElementos()

    def paginaHome(self):
        self._comandos.navegar(self.PAGINA_HOME)

    def clicarDuvidas(self):
        self._comandos.clicar(self.elemento.RODAPE_DUVIDAS)

    def verificarSeEstaNaPaginaAtendimento(self):
        self._comandos.trocarAba(self.PAGINA_DUVIDAS_FREQUENTES)
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES)

    def clicarTermos(self, opcoes):
        if 'condicoes gerais' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_CONDICOES_GERAIS)
        elif 'termos legais' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_TERMOS_LEGAL)
        elif 'termos de uso' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_TERMOS_USO)
        elif 'politica de privacidade' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_TERMOS_PRIVACIDADE)
        elif 'politica de cookies' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_TERMOS_COOKIE)

    def clicarNaRedeSocial(self, opcao):
        if 'facebook' in opcao:
            self._comandos.clicar(self.elemento.RODAPE_FACEBOOK)
        elif 'instagram' in opcao:
            self._comandos.clicar(self.elemento.RODAPE_INSTAGRAM)
        elif 'tiktok' in opcao:
            self._comandos.clicar(self.elemento.RODAPE_TIKTOK)
        elif 'youtube' in opcao:
            self._comandos.clicar(self.elemento.RODAPE_YOUTUBE)

    def clicarIconeLogo(self, opcao):
        if 'bem da sorte' in opcao:
            self._comandos.clicar(self.elemento.RODAPE_LOGO_BEM_DA_SORTE)
        elif 'brasilcap' in opcao:
            self._comandos.clicar(self.elemento.RODAPE_LOGO_BRASILCAP)

    def verificarSeEstaNaPagina(self, escolhida):
        if 'condicoes gerais' in escolhida:
            self.verificarSeEstaNaPaginaCondicoesGerais()
        elif 'termos legais' in escolhida:
            self.verificarSeEstaNaPaginaTermosLegais()
        elif 'termos de uso' in escolhida:
            self.verificarSeEstaNaPaginaTermosUso()
        elif 'politica de privacidade' in escolhida:
            self.verificarSeEstaNaPaginaPoliticaDePrivacidade()
        elif 'politica de cookies' in escolhida:
            self.verificarSeEstaNaPaginaPolicitaDeCookies()

    def verificarSeEstaNaPaginaRedesSociais(self, opcao):
        if 'facebook' in opcao:
            self.verificarSeEstaNaPaginaFacebookBemDaSorte()
        elif 'instagram' in opcao:
            self.verificarSeEstaNaPaginaIstagramBemDaSorte()
        elif 'tiktok' in opcao:
            self.verificarSeEstaNaPaginaTikTokBemDaSorte()
        elif 'youtube' in opcao:
            self.verificarSeEstaNaPaginaYouTubeBemDaSorte()

    def mudarDeAba(self, pagina):
        if 'home' in pagina:
            self._comandos.trocarAba(self.PAGINA_HOME)
        elif 'brasilcap' in pagina:
            self._comandos.trocarAba(self.PAGINA_BRASILCAP)