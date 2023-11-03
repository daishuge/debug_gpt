# debug_gpt, 一个能自己debug的chatgpt

适配pandora api(具体参考我主页fakegpt_with_history), 实现0消耗的api调用

同时给plus用户接入了gpt-4(暂时硬编码)

最重要的是, 给了chatgpt运行代码的能力, 同时也开放了pip安装权限, 使得它可以自己debug

## 逻辑

- 用户输入被用来启动代码生成流程。

- 生成的代码被执行，并且执行结果被检查。

- gpt检查代码是否出错

- 如果代码执行出现错误，程序会进入一个调试循环，尝试修复问题，并再次执行代码，直到没有错误。

## 文件结构

-  `config.py`：定义了用于与用户交互和指导程序行为的配置字符串。

-  `defs.py`：包含了实现项目功能的核心函数，如执行终端命令、从文本中提取代码块、模拟 API 调用以及在终端中彩色打印文本。

-  `main.py`：是程序的入口点，使用 defs.py 中定义的函数以及 config.py 中的配置来实现主要逻辑。

## 未来

接下来准备接入终端

## 这里放上一个理想运行的样例
```shell
You: 一个pygame小游戏
当创建一个pygame小游戏时，首先需要安装pygame库，然后编写游戏的代码。以下是一个简单的示例，展示如何创建一个基本的pygame小游戏，让玩家
控制一个移动的矩形方块：
```
```python
import pygame
import sys

# 初始化pygame
pygame.init()

# 设置游戏窗口尺寸
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("简单的Pygame小游戏")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 初始化玩家方块的位置和速度
player_x = 50
player_y = 50
player_speed = 5

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键状态
    keys = pygame.key.get_pressed()

    # 根据按键状态更新玩家方块的位置
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 清空屏幕
    win.fill(WHITE)

    # 绘制玩家方块
    pygame.draw.rect(win, RED, (player_x, player_y, 50, 50))

    # 刷新屏幕
    pygame.display.update()

# 退出pygame
pygame.quit()
sys.exit()
```
```shell
这个示例创建了一个窗口，玩家可以使用方向键控制一个红色的方块在窗口内移动。你可以根据自己的需求进一步扩展和修改这个示例，以创建更复杂
的pygame小游戏。希望这能帮助你入门pygame游戏开发！ERROR?
Traceback (most recent call last):
  File "C:\Users\diall_6tmma5x\Documents\python\debug_gpt\run.py", line 1, in <module>
    import pygame
ModuleNotFoundError: No module named 'pygame'




出错了

这个代码运行时出现了一个错误，提示找不到名为"pygame"的模块。这意味着你的Python环境中没有安装pygame模块。要解决这个问题，你需要先安装
pygame模块，可以使用以下命令来安装：

```
```shell
pip install pygame
``````
```

安装完成后，你应该能够成功运行这个代码，然后游戏窗口将会显示一个红色的方块，并且你可以使用键盘上的箭头键来控制方块的移动。希望这能帮
助你解决问题！如果你需要进一步的帮助，请随时告诉我。

出错了!

Traceback (most recent call last):
  File "C:\Users\diall_6tmma5x\Documents\python\debug_gpt\run.py", line 1, in <module>
    import pygame
ModuleNotFoundError: No module named 'pygame'

你好！下面是修改后的代码，包括了对pygame包的安装、代码的改进，以及注释的详细解释：
```
```python
# 在需要的地方添加以下代码来检查并安装pygame包
import subprocess
import sys

try:
    import pygame
except ImportError:
    print("未找到pygame包，正在尝试安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

# 初始化pygame
pygame.init()

# 设置游戏窗口尺寸
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("简单的Pygame小游戏")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 初始化玩家方块的位置和速度
player_x = 50
player_y = 50
player_speed = 5

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键状态
    keys = pygame.key.get_pressed()

    # 根据按键状态更新玩家方块的位置
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 清空屏幕
    win.fill(WHITE)

    # 绘制玩家方块
    pygame.draw.rect(win, RED, (player_x, player_y, 50, 50))

    # 刷新屏幕
    pygame.display.update()

# 退出pygame
pygame.quit()
sys.exit()
```

```shell
这段代码首先尝试导入pygame包，如果未找到包，它会尝试通过pip来安装pygame包。然后，它执行与原始代码相同的游戏逻辑。这样，无论是否已安
装pygame，代码都可以正常运行。

希望这个修改后的代码对你有帮助！如果你有任何问题或需要进一步的解释，请随时告诉我。ERROR?

[notice] A new release of pip is available: 23.2.1 -> 23.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip

这个代码和终端输出看起来是正常的。终端输出提醒你可以更新 pip 到版本 23.3.1，而代码部分是一个简单的 Pygame 小游戏，首先检查并安装了 pygame 包，然后创建了一个窗口，初始化了游戏循环，根据玩家的按键操作来移动方块，并且在屏幕上绘制了方块。最后，游戏结束后退出了 pygame
。

所以，回答是对的。如果您有任何进一步的问题或需要更多详细信息，请随时提出。

成功运行!


[notice] A new release of pip is available: 23.2.1 -> 23.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
```