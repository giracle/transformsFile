import socket
import tkinter as tk
import threading
from tkinter import *
import subprocess
import time, os


class FileTransform:
    # super().__init__()

    def __init__(self):
        # self.p = subprocess.Popen("python -m http.server 8881", shell=True)
        pass

    def startServer(self):
        button1['text'] = '不可点击'
        button1['state'] = DISABLED
        try:
            var.set("服务已开启...")
            # os.system("python -m http.server 8888")
            self.p = subprocess.Popen("python -m http.server 8888", shell=True)

        except Exception as e:
            print(e)
            var.set("服务开启失败！", e)

    def closeServer(self):
        try:
            self.p.kill()
            command = 'taskkill /F /IM python.exe'
            os.system(command)
            var.set("服务已关闭，等待3秒程序退出")
            time.sleep(3)
            root.destroy()  # 关闭
            # print("当前terminal已关闭")
        except Exception as e:
            var.set("服务未开启")
            print('Error:', e)

    def thread_it(self, func):
        # 创建
        t = threading.Thread(target=func)
        # 守护
        t.setDaemon(True)
        # 启动
        t.start()
        # 阻塞 ---卡死界面
        # t.join()

    def currentIP(self):
        # current ip
        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

            # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 在服务退出后，解除端口占用

            s.connect(('8.8.8.8', 80))

            ip = s.getsockname()[0]
            print("Current ip: ", ip)
            return ip
        except Exception as e:
            print(e)
        finally:
            s.close()


if __name__ == "__main__":
    ft = FileTransform()
    ip = ft.currentIP()
    root = tk.Tk()
    # root.iconbitmap("favicon.ico")
    root.title("局域网简易文件传输服务器")
    root.geometry("450x280")
    root.resizable(width=False, height=False)
    textLabel = tk.Label(root, text=" 请在目标主机的浏览器中输入{}:8888即可传输文件".format(ip))
    textLabel.place(x=10, y=100)
    var = tk.StringVar()
    labelVar = tk.Label(root, fg='red', textvariable=var)
    labelVar.place(x=100, y=130)

    button1 = tk.Button(root, text="开启服务", command=lambda: ft.thread_it(ft.startServer))
    button1.place(x=100, y=220, height=30, width=70)

    button2 = tk.Button(root, text="关闭服务", command=lambda: ft.thread_it(ft.closeServer))
    button2.place(x=250, y=220, height=30, width=70)
    labelCopyRight = tk.Label(root, text="\tCopyright ©  giracle\tEmail:giracle@yeah.net")
    labelCopyRight.place(x=40, y=260)
    root.mainloop()
