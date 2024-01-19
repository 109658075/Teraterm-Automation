import os
import subprocess
import time
import random
import win32com.client
from win32com.client import Dispatch

# 设置Tera Term的可执行文件路径
teraterm_path = r'C:\Program Files (x86)\teraterm\ttpmacro.exe'  # 根据您的安装路径进行调整

# 设置Tera Term的命令行参数（如果有的话）
teraterm_args = ['timeout = 10', "connect '192.168.100.1:23 /nossh / T=1'",'pause 1',
                 'wait "Enter Username:"','sendln "root"','wait "Enter Password:"','sendln "CBN"',
                 'wait "mainMenu>"','sendln "docsis"','wait "docsis>"','sendln "Production"','wait "Production>"',
                 'sendln "Test"','wait "Test>"','sendln "testmode"','wait "Test>"','sendln "quit"']  # 根据需要进行调整

# 构建命令
command = [teraterm_path] + teraterm_args

# 使用subprocess模块执行命令
subprocess.run(command)