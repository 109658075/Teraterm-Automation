import os
import subprocess
from threading import Timer


# 设置Tera Term的TTPMacro.exe工具路径
ttmacro_path = r'C:\Program Files (x86)\teraterm\ttpmacro.exe' 

current_working_directory = os.getcwd()
print(f'Current Working directory : {current_working_directory}')

# 设置TTL脚本文件路径
ttl_script_path = fr'{current_working_directory}\Testmode On_CBN.ttl'
ttl_33M_48M = fr'{current_working_directory}\'
ttl_QAM_74M = fr'{current_working_directory}\'



# 构建命令
command = [ttmacro_path, ttl_script_path, Timer(30)]

print(f'Command {" ".join(s for s in command)}')
# 使用subprocess模块执行命令
subprocess.run(command)