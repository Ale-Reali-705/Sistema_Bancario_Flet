import flet as ft
import re
from datetime import datetime
from componentes import referencias as ref
from bd import banco_de_dados as bd

def ativar_botao(e: ft.ControlEvent) -> None:
    '''Verifica se todos os campos de texto foram preenchidos e ativa o botão de continuar/criar'''
    campo_ativo = "dados_usuario" if ref.container["dados_usuario"].current.visible else "criar_usuario"
    refs_textfields = ref.textfield_sign_up1 if campo_ativo == "dados_usuario" else ref.textfield_sign_up2
    textfields = [ref.current for ref in refs_textfields.values()]
    ref.button[campo_ativo].current.disabled = False if all([campo.value for campo in textfields]) else True
    e.page.update()

def textfield_proximo(e: ft.ControlEvent) -> None:
    '''Foca no próximo campo de texto ou ativa o botão de continuar/criar'''
    campo_ativo = "dados_usuario" if ref.container["dados_usuario"].current.visible else "criar_usuario"
    refs_textfields = ref.textfield_sign_up1 if campo_ativo == "dados_usuario" else ref.textfield_sign_up2
    textfields = [ref.current for ref in refs_textfields.values()]
    if any(campo.error_text for campo in textfields) or any(not campo.value for campo in textfields):
        for campo in textfields:
            if not campo.value or campo.error_text:
                campo.focus()
                break
        e.page.update()    
    # Clica no botão de continuar/criar se todos os campos estiverem preenchidos e não houver erros
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

def formatar_cpf(e: ft.ControlEvent) -> None:
    '''Formata o CPF'''
    cpf = re.sub(r"[^0-9]", "", ref.textfield_sign_up1["cpf"].current.value)
    if len(cpf) <= 3:
        cpf_formatado = cpf
    elif len(cpf) <= 6:
        cpf_formatado = f"{cpf[:3]}.{cpf[3:]}"
    elif len(cpf) <= 9:
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}"
    else:
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    ref.textfield_sign_up1["cpf"].current.value = cpf_formatado
    ativar_botao(e)

def formatar_data_nascimento(e: ft.ControlEvent) -> None:
    '''Formata a data de nascimento'''
    data_nascimento = re.sub(r"[^0-9]", "", ref.textfield_sign_up1["data_nascimento"].current.value)
    if len(data_nascimento) <=2:
        data_nascimento_formatada = data_nascimento
    elif len(data_nascimento) <= 4:
        data_nascimento_formatada = f"{data_nascimento[:2]}/{data_nascimento[2:]}"
    else:
        data_nascimento_formatada = f"{data_nascimento[:2]}/{data_nascimento[2:4]}/{data_nascimento[4:]}"
    ref.textfield_sign_up1["data_nascimento"].current.value = data_nascimento_formatada
    ativar_botao(e)

def formatar_telefone(e: ft.ControlEvent) -> None:
    '''Formata o telefone'''
    telefone = re.sub(r"[^0-9]", "", ref.textfield_sign_up1["telefone"].current.value)
    if not telefone:
        telefone_formatado = ""
    elif len(telefone) <= 2:
        telefone_formatado = f"({telefone}"
    elif len(telefone) <= 7:
        if telefone[2] == "9":
            telefone_formatado = f"({telefone[:2]}) {telefone[2:]}"
        else:
            telefone_formatado = f"({telefone[:2]}) 9{telefone[2:]}"
    else:
        telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    ref.textfield_sign_up1["telefone"].current.value = telefone_formatado
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

def validar_informacoes(e: ft.ControlEvent) -> None:
    '''Valida as informações pessoais do usuario'''
    if re.search(r"[^a-zA-Z ]", ref.textfield_sign_up1["nome"].current.value):
        ref.textfield_sign_up1["nome"].current.error_text = "Nome inválido"
    if len(ref.textfield_sign_up1["cpf"].current.value) != 14:
        ref.textfield_sign_up1["cpf"].current.error_text = "CPF inválido"
    elif ref.textfield_sign_up1["cpf"].current.value in bd.procurar_campo("cpf"):
        ref.textfield_sign_up1["cpf"].current.error_text = "CPF ja cadastrado"
    try:
        if datetime.strptime(ref.textfield_sign_up1["data_nascimento"].current.value, "%d/%m/%Y") > datetime.now():
            raise ValueError("Data inválida")
    except ValueError:
        ref.textfield_sign_up1["data_nascimento"].current.error_text = "Data inválida"
    if "@" in ref.textfield_sign_up1["email"].current.value:
        ref.textfield_sign_up1["email"].current.error_text = "E-mail inválido"
    if len(ref.textfield_sign_up1["telefone"].current.value) != 15:
        ref.textfield_sign_up1["telefone"].current.error_text = "Telefone inválido"
    if any(campo.current.error_text for campo in ref.textfield_sign_up1.values()):
        e.page.update()
    else:
        trocar_campo(e)

def trocar_campo(e: ft.ControlEvent) -> None:
    '''Troca entre os campos de cadastro de usuário'''
    ref.container["dados_usuario"].current.visible = not ref.container["dados_usuario"].current.visible
    ref.container["criar_usuario"].current.visible = not ref.container["criar_usuario"].current.visible
    e.page.update()

def criar_usuario(e: ft.ControlEvent) -> None:
    '''Verifica as informações de cadastro de usuário e cria o usuario no banco de dados'''
    try:
        if ft.Icons.CLOSE in [icone.current.name for icone in ref.icone_senha.values()]:
            raise ValueError("senha", "Senha inválida")
        if ref.textfield_sign_up2["senha"].current.value != ref.textfield_sign_up2["confirmar_senha"].current.value:
            raise ValueError("confirmar_senha", "Senhas diferentes")
        if not any(campo.current.error_text for campo in ref.textfield_sign_up2.values()):
            usuario = {
                "nome": ref.textfield_sign_up1["nome"].current.value.title().strip(),
                "cpf": ref.textfield_sign_up1["cpf"].current.value,
                "data_nascimento": ref.textfield_sign_up1["data_nascimento"].current.value,
                "email": ref.textfield_sign_up1["email"].current.value + ref.dropdown["dominio"].current.value,
                "telefone": ref.textfield_sign_up1["telefone"].current.value,
                "usuario": ref.textfield_sign_up2["usuario"].current.value.lower(),
                "senha": ref.textfield_sign_up2["senha"].current.value
            }
            if not bd.criar_usuario(usuario):
                raise ValueError("usuario", "Usuário ja cadastrado")
            for campo in ["nome", "cpf", "data_nascimento", "email", "telefone"]:
                ref.textfield_sign_up1[campo].current.value = ""
                ref.textfield_sign_up1[campo].current.error_text = None
            for campo in ["usuario", "senha", "confirmar_senha"]:
                ref.textfield_sign_up2[campo].current.value = ""
                ref.textfield_sign_up2[campo].current.error_text = None
            e.page.update()
            e.page.go(f"/usuario/{usuario.get('usuario')}")
    except ValueError as erro:
        ref.textfield_sign_up2[erro.args[0]].current.error_text = erro.args[1]
        e.page.update()
