import flet as ft
from componentes import referencias as ref
from bd import banco_de_dados as bd
import re

def ativar_botao(e: ft.ControlEvent) -> None:
    '''Verifica se todos os campos de texto foram preenchidos'''
    campo_ativo = "menu_entrar" if ref.container["menu_entrar"].current.visible else "alterar_senha"
    refs_textfields = ref.textfield_home1 if campo_ativo == "menu_entrar" else ref.textfield_home2
    textfields = [ref.current for ref in refs_textfields.values()]
    ref.button[campo_ativo].current.disabled = False if all([campo.value for campo in textfields]) else True
    e.page.update()

def proximo_textfield(e: ft.ControlEvent) -> None:
    '''Foca no próximo campo de texto ou clica o botão de entrar'''
    campo_ativo = "menu_entrar" if ref.container["menu_entrar"].current.visible else "alterar_senha"
    refs_textfields = ref.textfield_home1 if campo_ativo == "menu_entrar" else ref.textfield_home2
    textfields = [ref.current for ref in refs_textfields.values()]
    if any(campo.error_text for campo in textfields) or any(not campo.value for campo in textfields):
        for campo in textfields:
            if not campo.value or campo.error_text:
                campo.focus()
                break
        e.page.update()
    # Clica no botão de entrar se todos os campos estiverem preenchidos e não houver erros
    else:
        ref.button[campo_ativo].current.on_click(e)

def focar(e: ft.ControlEvent) -> None:
    '''Limpa o error_text ao focar no campo de texto'''
    e.control.error_text = None
    e.page.update()

def desfocar(e: ft.ControlEvent) -> None:
    '''Verifica se a caixa de texto foi preenchida'''
    e.control.error_text = e.control.error_text if e.control.value else "Campo obrigatório"
    e.page.update()

def entrar(e: ft.ControlEvent) -> None:
    '''Verifica as informações de login e faz login no sistema'''
    usuario = ref.textfield_home1["usuario"].current.value.lower()
    senha = ref.textfield_home1["senha"].current.value
    dados = bd.procurar_usuario(usuario)

    if dados:
        if dados.get("senha") == senha:
            url = "/usuario/" + usuario
            e.page.go(url)
            for campo in ["usuario", "senha"]:
                ref.textfield_home1[campo].current.value = ""
                ref.textfield_home1[campo].current.error_text = None
        else:
            ref.textfield_home1["senha"].current.error_text = "Senha incorreta"
    else:
        ref.textfield_home1["usuario"].current.error_text = "Usuário não cadastrado"
    e.page.update()

def trocar_campo(e: ft.ControlEvent) -> None:
    '''Troca entre os campos de login e alterar senha'''
    ref.container["menu_entrar"].current.visible = not ref.container["menu_entrar"].current.visible
    ref.container["alterar_senha"].current.visible = not ref.container["alterar_senha"].current.visible
    e.page.update()

def formatar_data_nascimento(e: ft.ControlEvent) -> None:
    '''Formata a data de nascimento'''
    data_nascimento = re.sub(r"[^0-9]", "", ref.textfield_home2["data_nascimento"].current.value)
    if len(data_nascimento) <=2:
        data_nascimento_formatada = data_nascimento
    elif len(data_nascimento) <= 4:
        data_nascimento_formatada = f"{data_nascimento[:2]}/{data_nascimento[2:]}"
    else:
        data_nascimento_formatada = f"{data_nascimento[:2]}/{data_nascimento[2:4]}/{data_nascimento[4:]}"
    ref.textfield_home2["data_nascimento"].current.value = data_nascimento_formatada
    ativar_botao(e)

def confirmar_requisitos_senha(e: ft.ControlEvent) -> None:
    '''Verifica os requisitos da senha'''
    senha = e.control.value
    requisitos = {
        "minimo": len(senha) >= 6,
        "letras": re.search(r"[a-z]", senha) and re.search(r"[A-Z]", senha),
        "numeros": re.search(r"[0-9]", senha),
        "especial": re.search(r"[^a-zA-Z0-9]", senha)
    }
    # Altera os icones de acordo com os requisitos
    for referencia, requisito in requisitos.items():
        ref.icone_senha[referencia].current.name = ft.Icons.CHECK if requisito else ft.Icons.CLOSE
        ref.icone_senha[referencia].current.color = ft.Colors.GREEN_400 if requisito else ft.Colors.RED_400
    ativar_botao(e)

def alterar_senha(e: ft.ControlEvent) -> None:
    '''Verifica as informações no banco de dados e altera a senha do usuário'''
    usuario = {
        "usuario": ref.textfield_home2["usuario"].current.value.lower(),
        "data_nascimento": ref.textfield_home2["data_nascimento"].current.value,
        "senha": ref.textfield_home2["senha"].current.value
    }
    usuario_bd = bd.procurar_usuario(usuario.get("usuario"))
    try:
        if not usuario_bd:
            raise ValueError("usuario", "Usuário nao cadastrado")
        if not usuario_bd.get("data_nascimento") == usuario.get("data_nascimento"):
            raise ValueError("data_nascimento", "Data de nascimento inválida")
        if ft.Icons.CLOSE in [icone.current.name for icone in ref.icone_senha.values()]:
            raise ValueError("senha", "Senha inválida")
        if ref.textfield_home2["senha"].current.value != ref.textfield_home2["confirmar_senha"].current.value:
            raise ValueError("confirmar_senha", "Senhas diferentes")
        if not any(campo.current.error_text for campo in ref.textfield_home2.values()):
            bd.atualizar_usuario(usuario)
            for campo in ["usuario", "data_nascimento", "senha", "confirmar_senha"]:
                ref.textfield_home2[campo].current.value = ""
                ref.textfield_home2[campo].current.error_text = None
            e.page.update()
            e.page.go(f"/usuario/{usuario['usuario']}")
    except ValueError as erro:
        ref.textfield_home2[erro.args[0]].current.error_text = erro.args[1]
        e.page.update()
    