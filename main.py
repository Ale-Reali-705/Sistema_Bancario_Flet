import flet as ft
from views import erro, home, user, sign_up, user_details
from componentes import referencias, functions_sign_up, functions_home, funcions_detals_user, classes
from bd import banco_de_dados as bd
import importlib

# TODO - criar as classes de usuario e de contas
# TODO - alterar estrutura lógica para comportar as classes
# TODO - terminar banco de dados
# TODO - criar tela de detalhes de usuario
# TODO - melhorar tela de erro 404
# TODO - melhorar tela de usuario
# TODO - melhorar tela de detalhes de usuario
# TODO - revisar tela de menu
# TODO - revisar tela de sing up
# TODO - revisar tela de usuario
# TODO - revisar tela de detalhes de usuario
# TODO - revisar banco de dados

def main(page: ft.Page):
    def controle_rotas(rota: ft.RouteChangeEvent):
        # Força o recarregamento dos módulos das views para não precisar rodar o código novamente
        importlib.reload(home)
        importlib.reload(sign_up)
        importlib.reload(user)
        importlib.reload(user_details)
        importlib.reload(erro)
        importlib.reload(referencias)
        importlib.reload(functions_sign_up)
        importlib.reload(functions_home)
        importlib.reload(funcions_detals_user)
        importlib.reload(classes)
        importlib.reload(bd)

        page.views.clear()
        partes_rota = rota.route.split("/")
        if rota.route == "/menu":
            page.views.append(home.view(page))
        elif rota.route == "/cadastro":
            page.views.append(sign_up.view(page))
        elif rota.route.startswith("/usuario/"):
            if len(partes_rota) == 3:
                page.views.append(user.view(page, partes_rota[2]))
            elif len(partes_rota) == 4:
                page.views.append(user_details.view(page, partes_rota[2], partes_rota[3]))
        else:
            page.views.append(erro.view(page))
        page.update()

    page.title = "Sistema Bancário"
    # page.url = "sitema-bancario"
    page.on_route_change = controle_rotas
    page.go("/")

ft.app(target=main, view=ft.WEB_BROWSER)