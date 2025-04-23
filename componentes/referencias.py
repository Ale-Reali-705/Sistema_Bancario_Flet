import flet as ft

# TODO - separar referencias por view
# TODO - revisar referencias

# View sing up
textfield_sign_up1 = {
    "nome": ft.Ref[ft.TextField](),
    "cpf": ft.Ref[ft.TextField](),
    "data_nascimento": ft.Ref[ft.TextField](),
    "email": ft.Ref[ft.TextField](),
    "telefone": ft.Ref[ft.TextField](),
}

textfield_sign_up2 = {
    "usuario": ft.Ref[ft.TextField](),
    "senha": ft.Ref[ft.TextField](),
    "confirmar_senha": ft.Ref[ft.TextField](),
}

# View home
textfield_home1 = {
    "usuario": ft.Ref[ft.TextField](),
    "senha": ft.Ref[ft.TextField](),
}

textfield_home2 = {
    "usuario": ft.Ref[ft.TextField](),
    "data_nascimento": ft.Ref[ft.TextField](),
    "senha": ft.Ref[ft.TextField](),
    "confirmar_senha": ft.Ref[ft.TextField](),
}

# Elementos gerais
icone_senha = {
    "minimo": ft.Ref[ft.Icon](),
    "letras": ft.Ref[ft.Icon](),
    "numeros": ft.Ref[ft.Icon](),
    "especial": ft.Ref[ft.Icon](),
}

container = {
    "menu_entrar": ft.Ref[ft.Container](),
    "alterar_senha": ft.Ref[ft.Container](),
    "dados_usuario": ft.Ref[ft.Container](),
    "criar_usuario": ft.Ref[ft.Container](),
    "menu_contas": ft.Ref[ft.Container](),
}

column = {
    "menu_entrar": ft.Ref[ft.Column](),
    "alterar_senha": ft.Ref[ft.Column](),
    "dados_usuario": ft.Ref[ft.Column](),
    "criar_usuario": ft.Ref[ft.Column](),
}

button = {
    "menu_entrar": ft.Ref[ft.ElevatedButton](),
    "alterar_senha": ft.Ref[ft.ElevatedButton](),
    "dados_usuario": ft.Ref[ft.ElevatedButton](),
    "criar_usuario": ft.Ref[ft.ElevatedButton](),
}

dropdown = {
    "dominio": ft.Ref[ft.Dropdown](),
}