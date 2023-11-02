import defs
import config

if_error = False

error=[]

def first_code():
    user_input = input("You: ")

    code_in_md = defs.fake_api(config.ask_code + user_input, "gpt-3.5-turbo", True)
    code_list = defs.get_code(code_in_md)
    code = code_list[0]

    with open("run.py", "w", encoding="utf-8") as r:
        r.write(code)
    
    terminal_return = defs.terminal("python run.py")

    print("\n\n")

    gpt_check = defs.fake_api(config.check_return + terminal_return+"\ncode:\n" + code, "gpt-3.5-turbo", True)

    if "error" in gpt_check or "错" in gpt_check:
        defs.print_color("\n\n出错了!\n\n" + terminal_return, "red")
        error.append(terminal_return+"\n"+code)
        return 1
    
    else:
        defs.print_color("\n\n成功运行!\n\n" + terminal_return, "green")
        return 0

def debug_code():
    ask = config.debug + error
    fake_api = defs.fake_api(ask, "gpt-3.5-turbo", True)

    code_list = defs.get_code(fake_api)
    code = code_list[0]

    with open("run.py", "w", encoding="utf-8") as r:
        r.write(code)

    terminal_return = defs.terminal("python run.py")

    gpt_check = defs.fake_api(config.check_return + terminal_return+"\ncode:\n" + code, "gpt-3.5-turbo", True)

    if "error" in gpt_check or "错" in gpt_check:
        defs.print_color("\n\n出错了!\n\n" + terminal_return, "red")
        error = terminal_return+"\n"+code
        return 1
    
    else:
        defs.print_color("\n\n成功运行!\n\n" + terminal_return, "green")
        return 0

while True:

    if first_code() == 1:
        if_error = True
    else:
        break
    
    while True:
        if debug_code() == 0:
            break