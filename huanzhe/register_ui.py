from PIL import Image,ImageTk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import MySQLdb
from tkinter import ttk


class register():
    def show(window):
        window2 = tk.Toplevel(window)
        window2.title('欢迎使用智能导医系统')

        tk.Label(window2, text="请输入你的注册信息", font=(
            "宋体", 18)).place(x=140, y=10)
        tk.Label(window2, text="账号：", font=("楷体", 12)).place(x=40, y=60)
        tk.Label(window2, text="密码：", font=("楷体", 12)).place(x=200, y=60)
        tk.Label(window2, text="请再次确认您的密码：",
                 font=("楷体", 12)).place(x=40, y=100)
        reg_var_usr_name = StringVar()
    # var_usr_name.set('请输入您的账户名称')
        reg_entry_usr_name = tk.Entry(
            window2, textvariable=reg_var_usr_name, font=("宋体", 12), width=10)
        reg_entry_usr_name.place(x=90, y=60)
        reg_var_usr_pwd = StringVar()
        reg_entry_usr_pwd = tk.Entry(
            window2, textvariable=reg_var_usr_pwd, font=("宋体", 12), show='*', width=25)
        reg_entry_usr_pwd.place(x=250, y=60)
        reg_var_usr_pwd2 = StringVar()
        reg_entry_usr_pwd2 = tk.Entry(
            window2, textvariable=reg_var_usr_pwd2, font=("宋体", 12), show='*', width=25)
        reg_entry_usr_pwd2.place(x=250, y=100)

        reg_entry_usr_type = IntVar()
        reg_entry_usr_type.set(0)
        Radiobutton(window2, variable=reg_entry_usr_type, text='患者',
                    value=0, font=("楷体", 12)).place(x=60, y=135)
        Radiobutton(window2, variable=reg_entry_usr_type, text='医生',
                    value=1, font=("楷体", 12)).place(x=200, y=135)
        Radiobutton(window2, variable=reg_entry_usr_type, text='私人医生',
                    value=2, font=("楷体", 12)).place(x=340, y=135)

        reg_sex_label = tk.Label(
            window2, text='性别：', font=("楷体", 12))
        reg_sex_label.place(x=40, y=180)
        reg_sex_var = tk.IntVar()
        reg_sex_var.set(0)
        reg_sex_ma_radiobtn = Radiobutton(window2, variable=reg_sex_var,
                                          text='男', value=0, font=("楷体", 12))
        reg_sex_ma_radiobtn.place(x=100, y=180)
        reg_sex_fe_radiobtn = Radiobutton(window2, variable=reg_sex_var,
                                          text='女', value=1, font=("楷体", 12))
        reg_sex_fe_radiobtn.place(x=160, y=180)

        def cancel():
            window.update()
            window.deiconify()
            window2.destroy()

        def ok():
            reg_usr_type = str(reg_entry_usr_type.get())
            reg_usr_name = reg_entry_usr_name.get()
            reg_usr_pwd = reg_entry_usr_pwd.get()
            reg_usr_pwd2 = reg_entry_usr_pwd2.get()
            reg_usr_name = reg_usr_name + reg_usr_type
            reg_usr_gender = reg_sex_var.get()
            if(len(reg_usr_type) == 0 or len(reg_usr_name) == 0 or len(reg_usr_pwd) == 0 or len(reg_usr_pwd2) == 0):
                tk.messagebox.showerror(window2, message='您还未填写完整信息，请继续。')
            elif(reg_usr_pwd != reg_usr_pwd2):
                tk.messagebox.showerror(window2, message='两次输入密码不一致，请重新输入')
            else:
                connection = MySQLdb.connect(
                    "52.15.135.11", "root", "rootsql", "doctor", charset="utf8")
                c = connection.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS BASIC_INFORMATION
                        (NAME  CHAR(100) PRIMARY KEY   NOT NULL,
                        PASSWORD  CHAR(100)           NOT NULL);''')

                c.execute(
                    '''SELECT NAME, PASSWORD FROM BASIC_INFORMATION''' )
                basic_information_list = c.fetchall()
                print("select begin")
                reg_bool = False
                for item in basic_information_list:
                    if reg_usr_name == item[0]:
                        print(item[0])
                        tk.messagebox.showerror(message='用户已存在，请重新输入')
                        reg_bool = True
                print(reg_bool)
                print(reg_usr_name, reg_usr_pwd)
                if reg_bool is False:
                    print("test")
                    content = (reg_usr_name, reg_usr_pwd)
                    command = '''INSERT INTO BASIC_INFORMATION VALUES("{}","{}")'''.format(reg_usr_name,reg_usr_pwd)
                    print("test after")
                    c.execute(command)
                    print("test1")
                    connection.commit()
                    connection.close()
                    if reg_entry_usr_type.get() == 0:
                        print("患者")
                        connection = MySQLdb.connect(
                            "52.15.135.11", "root", "rootsql", "doctor", charset="utf8")
                        c = connection.cursor()
                        command = "CREATE TABLE IF NOT EXISTS " + reg_usr_name + "(NAME  CHAR(100) PRIMARY KEY NOT NULL, GENDER INT NOT NULL, NICKNAME CHAR(100),AGE CHAR(5),YEAR CHAR(5),MONTH CHAR(5),DATE CHAR(5),ALLERGIC_HISTORY CHAR(100),DISEASE_HISTORY CHAR(100),MEDICINE_HISTORY CHAR(100),DISEASE_DESCRIPTION CHAR(100),FAMILY_DISEASE CHAR(100));"
                        c.execute(command)
                        connection.commit()
                        command = '''INSERT INTO ''' + reg_usr_name + \
                            ''' VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'''.format(
                                reg_usr_name, reg_usr_gender, reg_usr_name[0:-1], "", "", "", "", "", "", "", "", "")
                        c.execute(command)
                        connection.commit()
                        connection.close()
                    else:
                        print("医生")
                        connection = MySQLdb.connect(
                            "52.15.135.11", "root", "rootsql", "doctor", charset="utf8")
                        c = connection.cursor()
                        command = '''CREATE TABLE IF NOT EXISTS ''' + reg_usr_name +'''(`NAME`  CHAR(100) PRIMARY KEY NOT NULL,
                        `GENDER` INT NOT NULL,
                        `NICKNAME` CHAR(100),
                        `WORKSPAN` CHAR(5),
                        `AGE`      CHAR(5),
                        `HOSPITAL` CHAR(20),
                        `WORKPLACE` CHAR(8),
                        `MAIN_DESCRIPTION` CHAR(100));'''
                        c.execute(command)
                        connection.commit()
                        command = '''INSERT INTO ''' + reg_usr_name + \
                            ''' VALUES("{}","{}","{}","{}", "{}","{}","{}","{}")'''.format(
                                reg_usr_name, reg_usr_gender, reg_usr_name[0:-1], "", "", "", "0", "")
                        c.execute(command)
                        connection.commit()
                        connection.close()
                    print("finish stage1")
                    print("insert finish")
                    window.update()
                    window.deiconify()
                    window2.withdraw()

        btn_login = tk.Button(window2, text="确定", font=(
            "楷体", 12), command=lambda: ok())
        btn_login.place(x=340, y=200)
        btn_sign_up = tk.Button(window2, text="取消", font=(
            "楷体", 12), command=lambda: cancel())
        btn_sign_up.place(x=410, y=200)

        window2.geometry("500x250")
        window2.mainloop()


if __name__ == '__main__':
    window = tk.Tk()
    register.show(window)
