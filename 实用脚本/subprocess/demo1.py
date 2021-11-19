import subprocess
import time
def main():
    # subprocess.call("dir /a", shell=True)  # 写法
    # subprocess.Popen("md helel_test1", shell=True, cwd='e:')   # Popen例子
    # # 打开记事本，3秒后关闭
    # notepad_process = subprocess.Popen("notepad.exe")   # Popen例子
    # time.sleep(3)
    # notepad_process.kill()
    open_process = subprocess.Popen("python.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    open_process.stdin.write(f"print('hello')\n".encode())
    open_process.stdin.write(f"print('hello' + 1)".encode())
    open_process.stdin.close()

    cmd_out = open_process.stdout.read().decode()
    open_process.stdout.close()
    print(cmd_out)

    error = open_process.stderr.read().decode()
    open_process.stderr.close()
    print(error)

if __name__ == '__main__':
    main()