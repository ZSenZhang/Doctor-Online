import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from register_ui import register
from modify_infor1 import runtime
import MySQLdb

connection = MySQLdb.connect("52.15.135.11", "root", "rootsql", "doctor")

# cursor object
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS BASIC_INFORMATION
    (NAME  CHAR(100) PRIMARY KEY   NOT NULL,
     PASSWORD  CHAR(100)           NOT NULL);''')


connection.commit()
connection.close()

# 设置登陆窗口属性
window = tk.Tk()
window.title('欢迎使用智能导医系统')

window.geometry("450x300")

# 登陆界面的信息
tk.Label(window, text="智能导医系统", font=("宋体", 32)).place(x=90, y=40)
tk.Label(window, text="账号：").place(x=120, y=105)
tk.Label(window, text="密码：").place(x=120, y=145)

v = IntVar()
v.set(0)
for i in range(3):
    if(i == 0):
        Radiobutton(window, variable=v, text='患者', value=i).place(x=120, y=180)
    elif(i == 1):
        Radiobutton(window, variable=v, text='医生', value=i).place(x=190, y=180)
    else:
        Radiobutton(window, variable=v, text='私人医生',
                    value=i).place(x=260, y=180)

var_usr_name = tk.StringVar()
# 显示默认账号
# var_usr_name.set('小明')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=180, y=105)
var_usr_pwd = tk.StringVar()
# 设置输入密码后显示*号
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=180, y=145)


def usr_login():
    # 获取输入的账号密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    usr_type = str(v.get())
    usr_name = usr_name + usr_type

    print(usr_name)
    if(len(usr_name) == 1):
        tk.messagebox.showerror(message='请输入账号！')
    elif(len(usr_pwd) == 0):
        tk.messagebox.showerror(message='请输入密码！')
    # 获取存储的账户信息，此处使用的是数据库，调用数据库查询函数，也可以使用其他方式，如文件等
    else:
        connection = MySQLdb.connect(
            "52.15.135.11", "root", "rootsql", "doctor")

# cursor object
        c = connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS BASIC_INFORMATION
             (NAME  CHAR(100) PRIMARY KEY   NOT NULL,
             PASSWORD  CHAR(100)           NOT NULL);''')

        c.execute(
            '''SELECT NAME, PASSWORD FROM BASIC_INFORMATION''')

        basic_information_list = c.fetchall()

        is_sign_up = False
        is_reg = False
        for item in basic_information_list:
            if usr_name == item[0]:
                is_reg = True
                if usr_pwd == item[1]:
                    window.withdraw()
                    runtime.run(window,usr_name)
                else:
                    tk.messagebox.showerror(message='对不起，输入错误，请重试！')
        if is_reg is False:
            is_sign_up = tk.messagebox.askyesno(
                'Welcome', '您还没有注册，是否现在注册呢？')
        connection.close()

#            mainwindow()

        if is_sign_up:
            usr_sign_up()
# 注册账号


def usr_sign_up():
    window.withdraw()
    register.show(window)


# 登陆和注册按钮
btn_login = tk.Button(window, text="登陆", command=lambda: usr_login())
btn_login.place(x=150, y=230)
btn_sign_up = tk.Button(window, text="注册", command=lambda: usr_sign_up())
btn_sign_up.place(x=250, y=230)

window.mainloop()
