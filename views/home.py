import flet as ft
from componentes import referencias as ref
from componentes import functions_home as fun

# TODO - melhorar o designer
# TODO - revisar tela

def view(page: ft.Page) -> ft.View:
    return ft.View(
        route="/menu",
        padding=100,
        appbar=ft.AppBar(
            title=ft.Text("Menu Principal"),
            center_title=True,
            color=ft.Colors.BLUE,
            bgcolor=ft.Colors.WHITE,
        ),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.TextField(
                            label="Usuário",
                            autofocus=True,
                            expand=True,
                            ref=ref.textfield_home1["usuario"],
                            on_submit=fun.proximo_textfield,
                            on_change=fun.ativar_botao,
                            on_focus=fun.focar,
                            on_blur=fun.desfocar,
                        ),
                        ft.TextField(
                            label="Senha",
                            password=True,
                            can_reveal_password=True,
                            expand=True,
                            ref=ref.textfield_home1["senha"],
                            on_submit=fun.proximo_textfield,
                            on_change=fun.ativar_botao,
                            on_focus=fun.focar,
                            on_blur=fun.desfocar,
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "Cadastrar",
                                    on_click=lambda _: page.go("/cadastro")
                                ),
                                ft.ElevatedButton(
                                    "Entrar",
                                    disabled=True,
                                    ref=ref.button["menu_entrar"],
                                    on_click=fun.entrar
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        ),
                        ft.TextButton(
                            text="Esqueci minha senha",
                            on_click=fun.trocar_campo,
                        )
                    ],
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    ref=ref.column["menu_entrar"],
                ),
                width=500,
                alignment=ft.alignment.center,
                padding=10,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                border=ft.border.all(2, ft.Colors.BLUE),
                visible=True,
                ref=ref.container["menu_entrar"],
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.TextField(
                            label="Usuário",
                            autofocus=True,
                            expand=True,
                            ref=ref.textfield_home2["usuario"],
                            on_submit=fun.proximo_textfield,
                            on_change=fun.ativar_botao,
                            on_focus=fun.focar,
                            on_blur=fun.desfocar,
                        ),
                        ft.TextField(
                            label="data de nascimento",
                            hint_text="dd/mm/aaaa",
                            max_length=10,
                            expand=True,
                            ref=ref.textfield_home2["data_nascimento"],
                            on_submit=fun.proximo_textfield,
                            on_change=fun.formatar_data_nascimento,
                            on_focus=fun.focar,
                            on_blur=fun.desfocar,
                        ),
                        ft.TextField(
                            label="Senha",
                            password=True,
                            can_reveal_password=True,
                            expand=True,
                            ref=ref.textfield_home2["senha"],
                            on_submit=fun.proximo_textfield,
                            on_change=fun.confirmar_requisitos_senha,
                            on_focus=fun.focar,
                            on_blur=fun.desfocar,
                        ),
                        ft.TextField(
                            label="Confirmar Senha",
                            password=True,
                            can_reveal_password=True,
                            expand=True,
                            ref=ref.textfield_home2["confirmar_senha"],
                            on_submit=fun.proximo_textfield,
                            on_change=fun.ativar_botao,
                            on_focus=fun.focar,
                            on_blur=fun.desfocar,
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(
                                    name=ft.Icons.CLOSE,
                                    ref=ref.icone_senha["minimo"],
                                    color=ft.Colors.RED_400,
                                    size=20,
                                ),
                                ft.Text(
                                    value="• Mínimo de 6 caracteres;",
                                ),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(
                                    name=ft.Icons.CLOSE,
                                    ref=ref.icone_senha["letras"],
                                    color=ft.Colors.RED_400,
                                    size=20,
                                ),
                                ft.Text(
                                    value="• Letras maiúsculas e minusculas;",
                                ),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(
                                    name=ft.Icons.CLOSE,
                                    ref=ref.icone_senha["numeros"],
                                    color=ft.Colors.RED_400,
                                    size=20,
                                ),
                                ft.Text(
                                   value="• Números e letras;",
                                ),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(
                                    name=ft.Icons.CLOSE,
                                    ref=ref.icone_senha["especial"],
                                    color=ft.Colors.RED_400,
                                    size=20,
                                ),
                                ft.Text(
                                    value="• Caracteres especiais;",
                                ),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Cancelar",
                                    on_click=fun.trocar_campo,
                                ),
                                ft.ElevatedButton(
                                    text="Alterar senha",
                                    disabled=True,
                                    ref=ref.button["alterar_senha"],
                                    on_click=fun.alterar_senha
                                ),
                            ]
                        )
                    ],
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    ref=ref.column["alterar_senha"],
                ),
                width=500,
                alignment=ft.alignment.center,
                padding=10,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                border=ft.border.all(2, ft.Colors.BLUE),
                visible=False,
                ref=ref.container["alterar_senha"],
            )
        ]
    )
