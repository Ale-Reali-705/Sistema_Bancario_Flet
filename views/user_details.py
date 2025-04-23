import flet as ft

# TODO - melhorar tela de detalhes de usuario
# TODO - criar funcoes para detalhes de usuario
# TODO - add designer
# TODO - revisar tela de detalhes de usuario

def view(page: ft.Page, usuario: str, detalhes: str):
    return ft.View(
        route="/usuario/" + usuario + "/" + detalhes,
        controls=[
            ft.Text("Detalhes de " + detalhes),
            ft.ElevatedButton("Back", on_click=lambda _: page.go("/menu")),
        ]
    )