import os
import subprocess
import time

def run_teraterm_script(script_path):
    teraterm_path = r'C:\Program Files (x86)\teraterm\ttermpro.exe'  # 根据您的安装路径进行调整
    command = [teraterm_path, script_path]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = process.communicate()

    print(f"脚本 {script_path} 输出：", output)
    print(f"脚本 {script_path} 错误：", errors)


    # print(f'Command {" ".join(s for s in command)}')

if __name__ == "__main__":
    # 列出要依次运行的 TTL 脚本的路径
    current_working_directory = os.getcwd()
    print(f'Current Working directory : {current_working_directory}')

    ttl_scripts = [
        fr'{current_working_directory}\Testmode On_CBN.ttl', 
        fr'{current_working_directory}\5.5.2.1.2_OFDMA_33MHz_BW48M_63dBmV_CBN - 1226test.ttl', 
        fr'{current_working_directory}\5.5.2.1.2_OFDMA_59MHz_BW72M_63dBmV_CBN - 0102test.ttl', 
        fr'{current_working_directory}\5.5.2.1.2_OFDMA_33MHz_BW48M_63dBmV_CBN - 1226test.ttl', 
        fr'{current_working_directory}\5.5.2.1.2_OFDMA_152MHz_BW94.8M_63dBmV_CBN - 0102test.ttl', 
        fr'{current_working_directory}\5.5.2.1.2_OFDMA_59MHz_BW94.8M_63dBmV_CBN - 0102test.ttl'
    ]

    # 依次运行每个 TTL 脚本
    for script_path in ttl_scripts:
        run_teraterm_script(script_path)