import defs  # 包含了一些定义好的函数和变量。
import config  # 一些配置参数。

if_error = False  # 初始化一个变量if_error，用来标识是否遇到错误。

error=''  # 初始化一个空字符串error，用来存储错误信息。

def first_code():  # 定义一个函数first_code，它负责处理第一次代码执行的流程。
    global error  # 声明error为全局变量，这样可以在函数内部修改它。
    
    user_input = input("You: ")  # 从用户获取输入。

    # 下面一行模拟调用API，传入用户输入的内容，并返回相应的代码片段。
    code_in_md = defs.fake_api(config.ask_code + user_input, "gpt-3.5-turbo", True)
    
    code_list = defs.get_code(code_in_md)  # 从返回的markdown中提取代码段。
    code = code_list[0]  # 假设返回的是一个列表，取第一个元素作为要执行的代码。

    # 打开（或创建）一个名为run.py的文件，并写入提取的代码。
    with open("run.py", "w", encoding="utf-8") as r:
        r.write(code)
    
    terminal_return = defs.terminal("python run.py")  # 通过自定义的terminal函数执行run.py文件，并获取返回结果。

    print("\n\n")  # 打印空行，可能是为了视觉上的分隔。

    # 再次模拟调用API，检查终端返回的内容是否包含错误。
    gpt_check = defs.fake_api(config.check_return + terminal_return+"\ncode:\n" + code, "gpt-3.5-turbo", True)

    if "error" in gpt_check or "错" in gpt_check:  # 如果返回结果中包含错误。
        defs.print_color("\n\n出错了!\n\n" + terminal_return, "red")  # 使用红色打印错误信息。

        error = terminal_return+"\n"+code  # 将错误信息和代码赋值给error变量。
        return 1  # 返回1表示有错误发生。
    
    else:
        defs.print_color("\n\n成功运行!\n\n" + terminal_return, "green")  # 使用绿色打印成功信息。
        return 0  # 返回0表示成功。

# debug_code函数的定义与first_code类似，它负责在发现错误时尝试调试代码。
def debug_code():
    global error  # 同样声明error为全局变量。
    ask = config.debug + error  # 将配置的debug字符串和错误信息组合。
    reply = defs.fake_api(ask, "gpt-3.5-turbo", True)  # 模拟调用API来获取调试后的代码。

    code_list = defs.get_code(reply)  # 提取代码段。
    code = code_list[0]  # 取第一个代码段。

    # 将调试后的代码写入run.py文件。
    with open("run.py", "w", encoding="utf-8") as r:
        r.write(code)

    terminal_return = defs.terminal("python run.py")  # 执行调试后的代码。

    # 检查执行结果是否还包含错误。
    gpt_check = defs.fake_api(config.check_return + terminal_return+"\ncode:\n" + code, "gpt-3.5-turbo", True)

    if "错" in gpt_check:  # 如果包含错误。
        defs.print_color("\n\n出错了!\n\n" + terminal_return, "red")  # 用红色打印错误信息。
        error = terminal_return+"\n"+code
        return 1  # 返回1表示错误仍然存在。
    
    else:
        defs.print_color("\n\n成功运行!\n\n" + terminal_return, "green")  # 用绿色打印成功信息。
        return 0  # 返回0表示成功。

while True:  # 开始一个无限循环。

    if first_code() == 1:  # 如果第一次执行代码有错误。
        if_error = True  # 将if_error设置为True。
    else:
        break  # 如果没有错误，跳出循环。
    
    while True:  # 另一个无限循环用于调试。
        if debug_code() == 0:  # 如果调试成功。
            break  # 跳出循环。