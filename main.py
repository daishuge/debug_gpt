import subprocess
import re
import openai
import time
import os

def terminal(command):    # terminal("ipconfig")
    #传入终端命令,返回终端输出
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

        stdout = result.stdout
        stderr = result.stderr
        
        if stderr:
            print("ERROR?\n"+stderr)
            return stderr

        return stdout

    except Exception as e:
        return str(e)

def get_code(md_str):   # code_list=get_code(md_str)
    '''
    传入md文本,返回代码块列表
    调用方法:
    code_list=get_code(md_str)
    for item in code_list:
        print(item)
    '''
    code_blocks = re.findall(r"```(?:[a-zA-Z]+\n)?([\s\S]*?)```", md_str)
    
    code_blocks = [block.strip() for block in code_blocks]
    
    return code_blocks
  
def fake_api(query,if_print,tem,mod):     # fake_api("hi! are you gpt?",True,1,"gpt-3.5-turbo")

    openai.api_key = "YOUR_OPENAI_KEY"
    openai.api_base = "https://ai.fakeopen.com/v1/" 

    response = openai.ChatCompletion.create(
        model=mod,
        messages=[
            {'role': 'user', 'content': query}
        ],
        temperature=tem,
        max_tokens=2000,
        stream=True
    )

    result = ""

    for chunk in response:
        # 确保字段存在
        if 'choices' in chunk and 'delta' in chunk['choices'][0]:
            chunk_msg = chunk['choices'][0]['delta'].get('content', '')
            result += chunk_msg  # 将输出内容附加到结果字符串上

            if if_print:
                print(chunk_msg, end='', flush=True)
                time.sleep(0.05)

    return result

def write_to_reply(code):   #向reply.py写入代码(覆写)
    with open("reply.py","w",encoding="utf-8") as r:
        r.write(str(code))

def main(if_error):
    user_input=input("You: ")
    ask="分析用户意图并写出相应的python3程序,只给出一个代码块,reply in english: "

    reply=fake_api(ask+user_input,True,0.5,"gpt-3.5-turbo")

    while True:
        code_list=get_code(reply)
        try:
            code=code_list[0]
        except:
            print("未找到代码!")
            return 2

        write_to_reply(code)

        result=terminal("python reply.py")
            
        print("\n\n")

        if "Error" or "not" in result:
            print("\n\n\033[31m出错了!\n\n"+result+"\033[0m")
            return "1"        
        else:
            print("\n\n\033[32m运行成功!\n\n"+result+"\033[0m")
            break
            return "0"

while True:
    main(False)