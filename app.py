import os

tools = []

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"


def cyber_print(message, color=CYAN):
    print(f"{color}{message}{RESET}")


def clear_terminal():
    os.system("clear" if os.name != "nt" else "cls")


def press_by_return():
    input(f"{MAGENTA}Pressione qualquer tecla para voltar ao terminal...{RESET}")


def show_name_program():
    banner = """
███████████████████████████████████████▀████████████████████████████████████████████
█─█─██▀▄─██─▄▄▄─█▄─█─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄███─▄▄▄▄█─▄─▄─██▀▄─██─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█
█─▄─██─▀─██─███▀██─▄▀███─███─█▄▀─██─██▄─███▄▄▄▄─███─████─▀─████─████─██─██─██─█▄▀─██
▀▄▀▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀

[ terminal access // tool registry // stealth mode ]
    """
    cyber_print(banner, CYAN)


def show_options():
    cyber_print("[1] Registrar ferramenta", GREEN)
    cyber_print("[2] Listar ferramentas", GREEN)
    cyber_print("[3] Ativar ferramenta", YELLOW)
    cyber_print("[4] Sair do sistema", RED)
    cyber_print("[5] Limpar arsenal", RED)


def exit_app():
    clear_terminal()
    cyber_print("\nSessão finalizada. Rede silenciosa. Até a próxima.", MAGENTA)


def register_new_tool():
    clear_terminal()
    cyber_print("[BOOT] Cadastro de ferramenta", MAGENTA)
    name_tool = input("\n> Nome da ferramenta: ").strip()
    if not name_tool:
        cyber_print("[ERRO] Nome inválido. Operação abortada.", RED)
        press_by_return()
        return

    tools.append(name_tool)
    cyber_print(f"[OK] Ferramenta '{name_tool}' registrada no arsenal.", GREEN)
    press_by_return()
    clear_terminal()


def list_tools():
    clear_terminal()
    if not tools:
        cyber_print("[INFO] Nenhuma ferramenta registrada no banco local.", YELLOW)
        press_by_return()
        return

    cyber_print("[LISTA] Ferramentas ativas:", MAGENTA)
    for tool in tools:
        cyber_print(f"  - {tool}", GREEN)
    press_by_return()


def destroy():
    password = "154"
    cyber_print(
        """
    ░▒▓█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▓▒░
    ░▒▓█   MATRIX MODE REQUESTED    █▓▒░
    ░▒▓█   AUTHENTICATION REQUIRED  █▓▒░
    ░▒▓█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▓▒░
    """,
        RED,
    )
    confirmation = (
        input("\n[SYSTEM] Remover o registro local de ferramentas? (s/n): ")
        .strip()
        .lower()
    )
    if confirmation != "s":
        cyber_print(
            "\n[ABORTADO] Nenhuma ação executada. A rede continua em silêncio.", YELLOW
        )
        press_by_return()
        return

    input_key = input("[AUTH] Digite a chave de acesso: ")
    if input_key == password:
        tools.clear()
        cyber_print("\n[OK] Lista de ferramentas removida.", GREEN)
        cyber_print("[SIMULACAO] Nenhum arquivo, sessão ou banco foi afetado.", YELLOW)
        cyber_print("[FIM] Transmissão encerrada.", MAGENTA)
        press_by_return()
        return

    cyber_print("\n[ACESSO NEGADO] Chave incorreta. Registro mantido.", RED)
    press_by_return()


def select_option():
    try:
        option_selected = int(input("\n> Escolha uma opção: "))
        clear_terminal()

        match option_selected:
            case 1:
                register_new_tool()
            case 2:
                list_tools()
            case 3:
                cyber_print("[STATUS] Ativando ferramenta...", YELLOW)
                press_by_return()
            case 4:
                exit_app()
                return False
            case 5:
                destroy()
                return False
            case _:
                cyber_print("[ERRO] Opção inválida.", RED)
    except ValueError:
        cyber_print("[ERRO] Entrada inválida.", RED)

    return True


def main():
    while True:
        show_name_program()
        show_options()
        if not select_option():
            break


if __name__ == "__main__":
    main()
