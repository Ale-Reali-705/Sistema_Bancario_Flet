import json

# TODO - terminar o banco de dados
# TODO - revisar o banco de dados

arquivo = "bd/usuarios.json"

def abrir_bd(arquivo: str) -> dict[str, dict[str, str]]:
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

    
def criar_usuario(dados: dict[str, str]) -> bool:
    usuarios = abrir_bd(arquivo)
    
    if dados["usuario"] in usuarios.keys():
        return False
    else:
        usuarios[dados["usuario"]] = dados
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(json.dumps(usuarios, indent=4, ensure_ascii=False))
        return True
    
def atualizar_usuario(usuario: dict[str, str]) -> bool:
    usuarios = abrir_bd(arquivo)
    if usuarios.get(usuario["usuario"]):
        for chave, valor in usuario.items():
            usuarios[usuario["usuario"]][chave] = valor
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(json.dumps(usuarios, indent=4, ensure_ascii=False))
        return True
    else:
        return False
    
def procurar_campo(campo: str) -> list[str]:
    usuarios = abrir_bd(arquivo)
    return [dicionario.get(campo) for dicionario in usuarios.values()]

def procurar_usuario(usuario: str) -> dict[str, str] | None:
    usuarios = abrir_bd(arquivo)
    return usuarios.get(usuario)