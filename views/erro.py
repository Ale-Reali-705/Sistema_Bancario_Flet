import flet as ft

# TODO - add designer
# TODO - revisar tela de erro

def view(page: ft.Page):
    return ft.View(
    route="/erro",
    controls=[
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Erro 404: Página não encontrada"),
                    ft.ElevatedButton("Home", on_click=lambda _: page.go("/menu")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )
    ],
)