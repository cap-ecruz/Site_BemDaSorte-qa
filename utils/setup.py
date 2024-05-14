import time
import PySimpleGUI as sg

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By

import utils.urlPage
from utils.utils import Utils as info


class Setup:

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.original_window = None
        self.browser = None
        self.browse = None
        self.opcaoPrint = None
        self.ambiente = ''

    def dadosDoUsuario(self):
        dados_do_usuario = [
            [sg.Text('Digite o CPF cadastrado: '), sg.InputText()],
            [sg.Text('Digite a SENHA cadastrada: '), sg.InputText(password_char='*')],
            [sg.Button('Login')]
        ]

        window = sg.Window('Login', dados_do_usuario, element_justification='c')

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                break
            if event == 'Login':
                info.CPF_CADASTRADO = values[0]
                info.SENHA_CADASTRADO = values[1]
                window.close()
                break

        window.close()

    def acessarHomeBemDaSorte(self):
        self.browser.get(utils.urlPage.Paginas.PAGINA_HOME)
        # self.browser.get('https://staging.bemdasorte.com.br/#/login.html')

        # self.browser.find_element(By.ID, 'cpf').send_keys(info.CPF_CADASTRADO)
        # self.browser.find_element(By.ID, 'Senha').send_keys(info.SENHA_CADASTRADO)
        # self.browser.execute_script("arguments[0].scrollIntoView();", self.browser.find_element(By.ID, 'Entrar'))
        # self.browser.find_element(By.ID, 'Entrar').click()

    def escolherDimensaoTela(self):
        escolher_dimensao_tela = [
            [sg.Text('escolha o browser')],
            [sg.Button('DESKTOP'), sg.Button('CELULAR'), sg.Button('TABLET')]
        ]
        window = sg.Window('qual browser você deseja testar?', escolher_dimensao_tela)

        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                break
            if event == 'DESKTOP':
                self.ambiente = event
                window.close()
                break
            if event == 'CELULAR':
                self.ambiente = event
                window.close()
                break
            if event == 'TABLET':
                self.ambiente = event
                window.close()
                break

        window.close()

    def escolherBrowser(self):
        escolha_do_browser = [
            [sg.Text('escolha o browser')],
            [sg.Button('Chrome'), sg.Button('FireFox'), sg.Button('Edge')]
        ]
        window = sg.Window('qual browser você deseja testar?', escolha_do_browser)

        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                break
            if event == 'Chrome':
                self.browse = 'Chrome'
                window.close()
                break
            if event == 'FireFox':
                self.browse = 'FireFox'
                window.close()
                break
            if event == 'Edge':
                self.browse = 'Edge'
                window.close()
                break

        window.close()

    def abrirBrowser(self):

        # os drives estao na pasta venv/script
        if self.browse.__eq__('Chrome'):
            self.browser = Chrome()

        elif self.browse.__eq__('FireFox'):
            self.browser = Firefox()

        elif self.browse.__eq__('Edge'):
            self.browser = Edge()

        else:
            self.browser.quit()

        if self.ambiente.__eq__('DESKTOP'):
            self.browser.maximize_window()

        if self.ambiente.__eq__('CELULAR'):
            self.browser.set_window_size(360, 800)

        if self.ambiente.__eq__('TABLET'):
            self.browser.set_window_size(810, 1080)
        self.original_window = self.browser.current_window_handle

    def desejaTirarPrint(self):
        deseja_tirar_print = [
            [sg.Text('Deseja tirar image?')],
            [sg.Button('SIM'), sg.Button('NÃO')]
        ]
        window = sg.Window('Gerando image', deseja_tirar_print)

        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                break
            if event == 'SIM':
                self.opcaoPrint = 'SIM'
                window.close()
                break
            if event == 'NÃO':
                self.opcaoPrint = 'NAO'
                window.close()
                break

        window.close()

    def gerarPrint(self, scenario, status):
        if self.opcaoPrint.__eq__('SIM'):
            if status.__eq__('failed'):
                time.sleep(2)
                # tira print
                self.browser.find_element(By.TAG_NAME, 'body').screenshot(
                    'print\\' + '(0_0) falhou_' + scenario.name + '.png')
            else:
                time.sleep(2)
                # tira print
                self.browser.find_element(By.TAG_NAME, 'body').screenshot('print\\' + scenario.name + '.png')

    # def esperarHCaptcha(self):
    #     espera = WebDriverWait(self.browser, 60)
    #
    #     self.browser.find_element(By.XPATH, '/html/body/app-root/ng-component/main/h2')
    #     time.sleep(40)
    #     espera.until(
    #         presence_of_element_located((By.XPATH, '/html/body/app-root/app-header/header[1]/nav/span/button[1]'))
    #     )

    def abrirNovaAba(self):
        self.browser.switch_to.new_window('tab')

    def fecharAba(self):
        self.browser.close()
        self.browser.switch_to.window(self.original_window)
