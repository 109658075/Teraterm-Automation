import os
import subprocess
import time
import random
# from time import sleep


# 設定Tera Term的TTPMacro.exe工具路徑
ttmacro_path = r'C:\Program Files (x86)\teraterm\ttpmacro.exe' 

current_working_directory = os.getcwd()
print(f'Current Working directory : {current_working_directory}')

# 設定TTL腳本文件路徑
ttl_script_path = [fr'{current_working_directory}\5.5.2.1.2_OFDMA_33MHz_BW48M_63dBmV_CBN - 1226test.ttl', 
                   fr'{current_working_directory}\5.5.2.1.2_OFDMA_59MHz_BW72M_63dBmV_CBN - 0102test.ttl',  
                   fr'{current_working_directory}\5.5.2.1.2_OFDMA_59MHz_BW94.8M_63dBmV_CBN - 0102test.ttl']


'''
# 構建指令
command = [ttmacro_path, script_path]

print(f'Command {" ".join(s for s in command)}')
# 使用subprocess模組執行指令
subprocess.run(command)
'''

'''
 # 依序運行每個 TTL 脚本
for script_path in ttl_script_path:
        command = [ttmacro_path, script_path]
        print(f'Command {" ".join(s for s in command)}')
        subprocess.run(command)
'''

'''
# random 運行每個 TTL 腳本
random.shuffle(ttl_script_path)

for script_path in ttl_script_path:
        command = [ttmacro_path, script_path]
        print(f'Command {" ".join(s for s in command)}')
        subprocess.run(command)
        time.sleep(60)
'''
i = 0
while i < 10:
        random.shuffle(ttl_script_path)

        for script_path in ttl_script_path:
                command = [ttmacro_path, script_path]
                print(f'Command {" ".join(s for s in command)}')
                subprocess.run(command)
                time.sleep(60)
