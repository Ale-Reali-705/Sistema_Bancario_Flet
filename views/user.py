import flet as ft
from componentes import referencias as ref

def view(page: ft.Page, usuario: str) -> ft.View:
    return ft.View(
        route="/usuario/" + usuario,
        padding=0,
        appbar=ft.AppBar(
            title=ft.Text("Contas de " + usuario.title()),
            center_title=True,
            color=ft.Colors.BLUE,
            bgcolor=ft.Colors.WHITE,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.BLACK,
                on_click=lambda _: page.go("/menu"),
            ),
            actions=[
                ft.IconButton(ft.icons.SEARCH, tooltip="Pesquisar"),
                ft.IconButton(ft.icons.FAVORITE, tooltip="Favoritos"),
            ],
        ),
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.HOME_FILLED,
                                    tooltip="Home",
                                    on_click=lambda _: page.go("/menu")
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.SETTINGS,
                                    tooltip="Configurações",
                                    on_click=lambda _: page.go("/configuracoes")
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.START,
                            spacing=10,
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        bgcolor=ft.Colors.BLUE,
                        padding=10,
                        height=page.height-56,
                        width=100,
                        ref=ref.container["menu_contas"]
                    ),
                    ft.Column(
                        controls=[
                            ft.Text("Conteudo.")
                        ],
                        expand=True,
                        spacing=10,
                        scroll=ft.ScrollMode.AUTO,
                    )
                ],
                width=page.width-ref.container["menu_contas"].current.width,
                height=page.height-56,
            )
        ],
    )