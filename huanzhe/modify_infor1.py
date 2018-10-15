from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import MySQLdb
from PIL import Image,ImageTk
from sql_func import *
from doctorresult import result
from privatedoctorresult import privateresult

class runtime():

    def run(window, usr_name):
        root = tk.Toplevel(window)
        canvas = Canvas(root, width=1000, height=100, bg='white')
        root.title("doctor online system")
        canvas.create_text(100, 55, text='患者', font=("Arial", 24), fill='black')

        usr_allergic_history = ""
        usr_disease_history = ""
        usr_medicine_history = ""
        usr_family_disease = ""
        usr_family_disease = ""
        usr_disease_description = ""
        usr_hospital = ""
        usr_workspan = ""
        usr_workplace = "0"
        usr_main_description = ""
        if(usr_name[-1] == '0'):
            print(usr_name[-1])
            print("患者")
            connection = MySQLdb.connect("52.15.135.11", "root", "rootsql", "doctor", charset="utf8")
            c = connection.cursor()
            command = '''SELECT * FROM '''+usr_name
            c.execute(command)
            #_, usr_gender, usr_nickname, usr_age, usr_year, usr_month, usr_date, usr_allergic_history, disease_history,medicine_history, disease_description, family_disease = c.fetchall()
            _ = c.fetchone()
            print(_)
            usr_gender = _[1]
            usr_nickname = _[2]
            usr_age = _[3]
            usr_allergic_history = _[7]
            usr_disease_history = _[8]
            usr_medicine_history = _[9]
            usr_disease_description = _[10]
            usr_family_disease = _[11]
            connection.commit()
            connection.close()
        elif(usr_name[-1] == '1'):
            print(usr_name[-1])
            print("医生")
            connection = MySQLdb.connect("52.15.135.11", "root", "rootsql", "doctor", charset="utf8")
            c = connection.cursor()
            command = '''SELECT * FROM '''+usr_name
            c.execute(command)
            #_, usr_gender, usr_nickname, usr_age, usr_year, usr_month, usr_date, usr_allergic_history, disease_history,medicine_history, disease_description, family_disease = c.fetchall()
            _ = c.fetchone()
            print(_)
            usr_gender = _[1]
            usr_nickname = _[2]
            usr_workspan = _[3]
            usr_age = _[4]
            usr_hospital = _[5]
            usr_workplace = _[6]
            usr_main_description = _[7]
            connection.commit()
            connection.close()


        def printWindow():
            print('quit')
        bt = Button(canvas, text='退出', command=printWindow)
        canvas.create_window((950, 20), window=bt, anchor=W)

        i = 2


        def printwaiting():
            print('waitingnumber' + str(i))
        bt1 = Button(canvas, text='代办事项' + str(i), command=printwaiting, relief=GROOVE)
        name = usr_name[0:-1]
        if usr_gender == 0:
            gender = "先生"
        else:
            gender = "女士"


        image = Image.open("title.jpg")
        im = ImageTk.PhotoImage(image)
        canvas.create_image(400,0,image=im)
        canvas.create_text(930, 90, text='欢迎您，' + usr_nickname + gender,
                   font=("Arial", 12), fill='black')
        canvas.create_window((870, 20), window=bt1, anchor=W)

        canvas.pack(side=TOP,fill=BOTH) 
        patient_name = "陈金坤"

        canvas_down = Canvas(root, width=150, height=650, bg='red')
        image2 = Image.open("left.jpg")
        im2 = ImageTk.PhotoImage(image2)
        canvas_down.create_image(10,500,image=im2)


        def showresult():
            root.withdraw()
            result.showdoctorresult(root,patient_name)
        bt2 = Button(canvas_down, text='查看医生消息', command=showresult,
             font=("Arial", 16), bg='blue')
        canvas_down.create_window((30, 30), window=bt2, anchor=W)
        canvas_down.pack(side=LEFT, fill=BOTH)


        def showprivatdoctorresult():
            root.withdraw()
            privateresult.showprivateresult(root,patient_name)
        bt2 = Button(canvas_down, text='查看私人医生消息', command=showprivatdoctorresult,
             font=("Arial", 16), bg='blue')
        canvas_down.create_window((15, 80), window=bt2, anchor=W)
        canvas_down.pack(side=LEFT, fill=BOTH)


        frm=Frame(root)

        #############
        class frame:
            frm_1=Frame(frm)
            frm_2=Frame(frm)
            frm_canvas=Frame(frm)
            canvas_modify = Canvas(frm_canvas, width=850, height=650)
            canvas_patient = Canvas(canvas_modify, width=850, height=570)
            canvas_doctor = Canvas(canvas_modify, width=850, height=570)
        # frm_1=Frame(frm)
        # frm_2=Frame(frm)
        

        def write_syptom():
            # frm.pack_forget()
            frame.frm_1.pack_forget()
            # global frm_2
            frame.frm_2=Frame(frm)
            frame.frm_canvas.pack_forget()
            frame.canvas_modify.pack_forget()
            frm_3=Frame(frame.frm_2)
            t=Label(frm_3,width=8,height=1,text='症状：',font=('Arial',15))
            t.pack(side=LEFT)

# t1=Entry(frm_4,width=75,font=('Arial',15),borderwidth=2)
# t1.pack()           

            class symptom_desc:
                frm_add=Frame(frm_3)
                t3=Entry(frm_add,width=80,font=('Arial',15),borderwidth=3)

            def addline():
                symptom_desc.t3.pack()
                symptom_desc.frm_add.pack()

            t2 = Button(frm_3,text = '添加症状',command = addline,bg='blue')
            t2.pack(side=RIGHT)

            frm_3.pack(side=TOP,fill=BOTH)

            frm_4=Frame(frame.frm_2)
            t=Label(frm_4,width=8,height=1,text='症状图片：',font=('Arial',15))
            t.pack(side=LEFT)

            def uploadpic():
                print("上传图片")
                frm_add=Frame(frm_4)
                t5=Text(frm_4,height=1,font=('Arial',15))
                t5.tag_config('t2',foreground='black',underline=True)
                t5.insert(1.0,'无','t2')
                t5.pack(side=LEFT)
            t6 = Button(frm_4,text = '上传图片',command = uploadpic,bg='blue')
            t6.pack(side=RIGHT)

            frm_4.pack(side=TOP,fill=BOTH)

            frm_5=Frame(frame.frm_2)
            fenlei=('不确定','骨科','神经外科','胸外科','心血管外科',
                '泌尿外科','烧伤科','整形科','普外科',
                '小儿外科','消化内科','肾脏内科','心血管内科',
                '呼吸内科','血液内科','内分泌科','风湿免疫科',
                '变态反应/过敏反应科','感染/传染科','神经内科',
                '肿瘤内科','耳鼻喉科','眼科','口腔科','神经科',
                '皮肤科','疼痛科','妇产科','儿科学')
            t=Label(frm_5,width=8,height=1,text='选择科室',font=('Arial',15))
            t.pack(side=LEFT)

            number = StringVar()
            t31 = ttk.Combobox(frm_5, width=25,height=1, textvariable=number)
            t31['values'] = fenlei    # 设置下拉列表的值
            t31.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
            t31.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

            frm_5.pack(side=TOP,fill=BOTH)

            frm_6=Frame(frame.frm_2)
            def upload():
                symptom = symptom_desc.t3.get()
                if t31.get() != "":
                    commit_question(usr_name,symptom,department=t31.get())
                else:
                    commit_question(usr_name,symptom)
                print("提交成功")

            t6 = Button(frm_6,text = '提交',command = upload,bg='blue')
            t6.pack(side=TOP)

            frm_6.pack(side=TOP,fill=BOTH)
            frame.frm_2.pack(side=TOP,fill=BOTH)

        # frm_2.pack(side=TOP,fill=BOTH)



        bt3 = Button(canvas_down, text='填写症状给普通医生', command=write_syptom,
                 font=("Arial", 16), bg='blue')
        canvas_down.create_window((6, 130), window=bt3, anchor=W)






        #################

        def write_syptom_to_private():
            # global frm_1
            frame.frm_1=Frame(frm)
            # frm.pack_forget()
            frame.frm_2.pack_forget()
            frame.frm_canvas.pack_forget()
            frame.canvas_modify.pack_forget()
            frame.canvas_patient.place_forget()
            frame.canvas_doctor.place_forget()
            # frm_3.pack_forget()
            # frm_4.pack_forget()
            # frm_5.pack_forget()
            # frm_6.pack_forget()
            print("write_syptom_to_private")

            frm_7=Frame(frame.frm_1)
            t=Label(frm_7,width=8,height=1,text='症状：',font=('Arial',15))
            t.pack(side=LEFT)

# t1=Entry(frm_4,width=75,font=('Arial',15),borderwidth=2)
# t1.pack()

            class symptom_desc:
                frm_add=Frame(frm_7)
                t3=Entry(frm_add,width=80,font=('Arial',15),borderwidth=3)
            
            def addline():
                symptom_desc.t3.pack()
                symptom_desc.frm_add.pack()
            t2 = Button(frm_7,text = '添加症状',command = addline,bg='blue')
            t2.pack(side=RIGHT)

            frm_7.pack(side=TOP,fill=BOTH)

            frm_8=Frame(frame.frm_1)
            t=Label(frm_8,width=8,height=1,text='症状图片：',font=('Arial',15))
            t.pack(side=LEFT)

            def uploadpic():
                print("上传图片")
                frm_add=Frame(frm_8)
                t5=Text(frm_8,height=1,font=('Arial',15))
                t5.tag_config('t2',foreground='black',underline=True)
                t5.insert(1.0,'无','t2')
                t5.pack(side=LEFT)
            t6 = Button(frm_8,text = '上传图片',command = uploadpic,bg='blue')
            t6.pack(side=RIGHT)

            frm_8.pack(side=TOP,fill=BOTH)

            # frm_9=Frame(frame.frm_1)
            # t=Label(frm_9,width=8,height=1,text='身高情况：',font=('Arial',15))
            # t.pack(side=LEFT)

            # t3=Entry(frm_9,width=10,font=('Arial',15),borderwidth=3)
            # t3.pack(side=LEFT)

            # t4=Label(frm_9,width=8,height=1,text='体重情况：',font=('Arial',15))
            # t4.pack(side=LEFT)

            # t5=Entry(frm_9,width=10,font=('Arial',15),borderwidth=3)
            # t5.pack(side=LEFT)

            # frm_9.pack(side=TOP,fill=BOTH)

#             frm_10=Frame(frame.frm_1)
#             t=Label(frm_10,width=8,height=1,text='疑惑：',font=('Arial',15))
#             t.pack(side=LEFT)

# # t1=Entry(frm_4,width=75,font=('Arial',15),borderwidth=2)
# # t1.pack()

#             def addline():
#                 frm_add=Frame(frame.frm_10)
#                 t3=Entry(frm_add,width=80,font=('Arial',15),borderwidth=3)
#                 t3.pack()
#                 frm_add.pack()
#             t2 = Button(frm_10,text = '添加疑惑',command = addline,bg='blue')
#             t2.pack(side=RIGHT)

#             frm_10.pack(side=TOP,fill=BOTH)

            frm_11=Frame(frame.frm_1)
            def upload():
                symptom = symptom_desc.t3.get()
                commit_question(usr_name,symptom,toprivatedoc=True)
                print("提交成功")
            t6 = Button(frm_11,text = '提交',command = uploadpic,bg='blue')
            t6.pack(side=TOP)

            frm_11.pack(side=TOP,fill=BOTH)



            frame.frm_1.pack(side=TOP,fill=BOTH)
        



        bt3 = Button(canvas_down, text='填写症状给私人医生', command=write_syptom_to_private,
                 font=("Arial", 16), bg='blue')
        canvas_down.create_window((6, 180), window=bt3, anchor=W)




        #################


        # def printWindow():
        #     print('查看该用户历史病例')
        # bt3 = Button(canvas_down, text='查看该用户历史病例',
        #      command=printWindow, font=("Arial", 16), bg='blue')
        # canvas_down.create_window((6, 80), window=bt3, anchor=W)


        # def printpic():
        #     print('查看症状图片')
        # bt4 = Button(canvas_down, text='查看症状图片', command=printpic,
        #      font=("Arial", 16), bg='blue')
        # canvas_down.create_window((30, 130), window=bt4, anchor=W)

        # canvas_down.pack(side=LEFT, fill=BOTH)  


        # def printhealth():
        #     print('查看用户饮食情况')
        # bt4 = Button(canvas_down, text='查看用户健康数据', command=printhealth,
        #      font=("Arial", 16), bg='blue')
        # canvas_down.create_window((15, 180), window=bt4, anchor=W)



# 新增内容
##########################################################################

        frm.pack(side=TOP,fill=BOTH)
        usr_type = [0,1,1]
        if(usr_name[-1]=='1'):
            usr_type = [1, 0, 1]
        else:
            usr_type = [0,1,1]

        def show_mordify():
            # frm.pack_forget()
            frame.frm_1.pack_forget()
            frame.frm_2.pack_forget()
            # frm_whole.pack_forget()
            # frm_button1.pack_forget()
            # frame.canvas_modify.pack_forget()

            frame.canvas_modify.pack(side=TOP, fill=BOTH)
            frame.frm_canvas.pack(side=TOP,fill=BOTH)
            if(usr_type[1] == 0):
                frame.canvas_doctor.place(x=0,y=180)
            elif(usr_type[0] == 0):
                frame.canvas_patient.place(x=0,y=180)
            print(usr_type)

        bt5 = Button(canvas_down, text='修改个人信息', command=show_mordify,
                 font=("Arial", 16), bg='blue')
        canvas_down.create_window((30, 230), window=bt5, anchor=W)

        canvas_down.pack(side=LEFT, fill=BOTH)  

        frame.canvas_modify = Canvas(frame.frm_canvas, width=850, height=650)
        frame.canvas_modify.pack(side=TOP, fill=BOTH)

        frame.canvas_patient = Canvas(frame.canvas_modify, width=850, height=570)
        frame.canvas_patient.place(x=0, y=180)


        m_count_label = tk.Label(frame.canvas_modify, text="你的账户是" + usr_name[0:-1], font=("Arial", 16))



        m_type = IntVar()
        m_type.set(0)
        print(usr_type)
        for i in range(3):
            if(i == 0):
                Radiobutton(frame.canvas_modify, variable=m_type, text='患者', value=usr_type[0],
                    font=("Arial", 16), state=DISABLED).place(x=500, y=80)
            elif(i == 1):
                Radiobutton(frame.canvas_modify, variable=m_type, text='医生', value=usr_type[1],
                    font=("Arial", 16), state=DISABLED).place(x=600, y=80)
            elif(i == 2):
                Radiobutton(frame.canvas_modify, variable=m_type, text='私人医生', value=usr_type[2],
                    font=("Arial", 16), state=DISABLED).place(x=700, y=80)


        m_sex_label = tk.Label(frame.canvas_modify, text='你的性别', font=("Arial", 16))
        m_sex_label.place(x=500, y=130)
        m_sex = IntVar()
        m_sex.set(0)
        show_gender = [0,1]
        if usr_gender == 0:
            show_gender = [0,1]
        else:
            show_gender = [1,0]
        for i in range(2):
            if(i == 0):
                Radiobutton(frame.canvas_modify, variable=m_sex, text='男', value=show_gender[0],
                    command = lambda: man(), font=("Arial", 16), state=DISABLED).place(x=650, y=130)
            elif(i == 1):
                Radiobutton(frame.canvas_modify, variable=m_sex, text='女', value=show_gender[1],
                    command = lambda: woman(), font=("Arial", 16), state=DISABLED).place(x=750, y=130)


        m_count_label.place(x=40, y=30)
        m_name_label = tk.Label(frame.canvas_modify, text='昵称', font=("Arial", 16))
        m_name_label.place(x=40, y=80)
        m_name_text = tk.StringVar()
        m_name_text.set(usr_nickname)
        m_name_entry = tk.Entry(
            frame.canvas_modify, textvariable=m_name_text, font=("Arial", 16), width=10)
        m_name_entry.place(x=120, y=80)



        m_age = StringVar()
        m_age.set(usr_age)
        m_age_label = tk.Label(frame.canvas_modify, text="年龄", font=("Arial", 16))
        m_age_label.place(x=40, y=130)
        m_age_entry = tk.Entry(frame.canvas_modify, textvariable=m_age,
                       font=("Arial", 16), width=5)
        m_age_entry.place(x=120, y=130)


        frame.canvas_patient = Canvas(frame.canvas_modify, width=850, height=570)
        frame.canvas_patient.place(x=0, y=180)

        frame.canvas_doctor = Canvas(frame.canvas_modify, width=850, height=570)
        frame.canvas_doctor.place(x=0, y=180)


        tk.Label(frame.canvas_patient, text='--------------------------------------' +
         '-----------------------------------------------------------------' +
         '--------------------------------',
         font=("Arial", 16)).place(y=0)


        m_allergic_label = tk.Label(frame.canvas_patient, text='过敏史', font=("Arial", 16))
        m_allergic_label.place(x=40, y=40)
        allergic = StringVar()
        allergic.set(usr_allergic_history)
        m_allergic_entry = tk.Entry(
            frame.canvas_patient, textvariable=allergic, font=("Arial", 16))
        m_allergic_entry.place(x=140, y=40, width=660)

        m_disease_label = tk.Label(frame.canvas_patient, text='疾病史', font=("Arial", 16))
        m_disease_label.place(x=40, y=90)
        disease = StringVar()
        disease.set(usr_disease_history)
        m_disease_entry = tk.Entry(
            frame.canvas_patient, textvariable=disease, font=("Arial", 16))
        m_disease_entry.place(x=140, y=90, width=660)

        m_medicine_label = tk.Label(frame.canvas_patient, text='用药史', font=("Arial", 16))
        m_medicine_label.place(x=40, y=140)
        medicine = StringVar()
        medicine.set(usr_medicine_history)
        m_medicine_entry = tk.Entry(
            frame.canvas_patient, textvariable=medicine, font=("Arial", 16))
        m_medicine_entry.place(x=140, y=140, width=660)

        m_symptom_label = tk.Label(frame.canvas_patient, text='症状描述', font=("Arial", 16))    
        m_symptom_label.place(x=40, y=190)
        m_symptom_text = tk.Text(
        frame.canvas_patient,font=("Arial", 16))
        m_symptom_text.insert(INSERT,usr_disease_description)
        m_symptom_text.place(x=140, y=190, width=260, height=200)

        m_famdis_label = tk.Label(frame.canvas_patient, text='家庭病史', font=("Arial", 16))
        m_famdis_label.place(x=430, y=190)
        m_famdis_text = tk.Text(
            frame.canvas_patient,font=("Arial", 16))
        m_famdis_text.insert(INSERT,usr_family_disease)
        m_famdis_text.place(x=530, y=190, width=260, height=200)


        frame.canvas_patient.place_forget()   

        tk.Label(frame.canvas_doctor, text='--------------------------------------' +
         '-----------------------------------------------------------------' +
         '--------------------------------',
         font=("Arial", 16)).place(y=0)
        m_workspan_label = tk.Label(frame.canvas_doctor, text="医龄", font=("Arial", 16))
        m_workspan_label.place(x=40, y=40)
        workspan = StringVar()
        workspan.set(usr_workspan)
        m_workspan_entry = tk.Entry(
            frame.canvas_doctor, textvariable=workspan, font=("Arial", 16),width=3)
        m_workspan_entry.place(x=120, y=40)

        m_hospital_label = tk.Label(frame.canvas_doctor, text="医院", font=("Arial", 16))
        m_hospital_label.place(x=40, y=90)
        hospital = StringVar()
        hospital.set(usr_hospital)
        m_hospital_entry = tk.Entry(
            frame.canvas_doctor, textvariable=hospital, font=("Arial", 16),width=20)
        m_hospital_entry.place(x=120, y=90)

        m_workplace_label = tk.Label(frame.canvas_doctor, text="科室", font=("Arial", 16))
        m_workplace_label.place(x=40, y=140)
        workplace = StringVar()
        workplace.set(usr_workplace)
        m_workplace_combox = ttk.Combobox(
            frame.canvas_doctor, textvariable=workplace, font=("Arial", 16),width=20)
        m_workplace_combox.place(x=120, y=140)
        m_workplace_combox['values']=('骨科', '神经外科', '胸外科', '心血管外科',
          '泌尿外科', '烧伤科', '整形科', '普外科',
          '小儿外科', '消化内科', '肾脏内科', '心血管内科',
          '呼吸内科', '血液内科', '内分泌科', '风湿免疫科',
          '变态反应/过敏反应科', '感染/传染科', '神经内科',
          '肿瘤内科', '耳鼻喉科', '眼科', '口腔科', '神经科',
          '皮肤科', '疼痛科', '妇产科', '儿科学')
        m_workplace_combox.current(int(usr_workplace))

        m_description_label = tk.Label(frame.canvas_doctor, text="主要描述", font=("Arial", 16))
        m_description_label.place(x=40, y=190)
        m_description_text = tk.Text(frame.canvas_doctor, font=("Arial", 16),width=29,height=10)
        m_description_text.insert(INSERT,usr_main_description)
        m_description_text.place(x=40, y=240)


        def change_password():
            change_top = tk.Toplevel(frame.canvas_modify,width = 500 ,height =200)
            tk.Label(change_top, text="请输入修改后的密码：", font=("楷体", 12)).place(x=40, y=30)
            tk.Label(change_top, text="请再次确认您的密码：",
                 font=("楷体", 12)).place(x=40, y=70)
            change_usr_pwd = StringVar()
            change_entry_usr_pwd = tk.Entry(
                change_top, textvariable=change_usr_pwd, font=("宋体", 12), show='*', width=25)
            change_entry_usr_pwd.place(x=250, y=30)
            change_usr_pwd2 = StringVar()
            change_entry_usr_pwd2 = tk.Entry(
                change_top, textvariable=change_usr_pwd2, font=("宋体", 12), show='*', width=25)
            change_entry_usr_pwd2.place(x=250, y=70)


            def change_confirm():
                temp1 = change_entry_usr_pwd.get()
                temp2 = change_entry_usr_pwd2.get()
                if(len(temp1) == 0 or len(temp2) == 0):
                    tk.messagebox.showerror(change_top, message='您还未填写完整信息，请继续。')
                elif(temp1 != temp2):
                    tk.messagebox.showerror(change_top, message='两次输入密码不一致，请重新输入')
                else:
                    connection = MySQLdb.connect(
                        "52.15.135.11", "root", "rootsql", "doctor", charset="utf8")
                    c = connection.cursor()
                    print(usr_name)
                    print(temp1)
                    command = "UPDATE BASIC_INFORMATION SET PASSWORD = '%s' WHERE NAME = '%s'" %(temp1, usr_name)
                    c.execute(command)
                    connection.commit()
                    connection.close()
                    change_top.destroy()

            btn_confirm = tk.Button(change_top,text="确定", command = lambda:change_confirm(), font=("宋体", 12))
            btn_confirm.place(x=40,y=110)
            def change_cancel():
                change_top.destroy()
            btn_cancel = tk.Button(change_top,text="取消", command = lambda:change_cancel(), font=("宋体", 12))
            btn_cancel.place(x=120,y=110)


        btn_modify_basic_information = Button(
            frame.canvas_modify, text='修改密码', font=("Arial", 16), 
            command=lambda: change_password(), width=10)
        btn_modify_basic_information.place(x=500, y=30)

        def confirm():
            if(usr_name[-1] == '0'):
                usr_nickname = m_name_entry.get()
                usr_age = m_age_entry.get()
                usr_allergic_history = m_allergic_entry.get()
                usr_disease_history = m_disease_entry.get()
                usr_medicine_history = m_medicine_entry.get()
                usr_disease_description = m_symptom_text.get("0.0","end")
                usr_family_disease = m_famdis_text.get("0.0","end")
                connection = MySQLdb.connect(
                            "52.15.135.11", "root", "rootsql", "doctor", charset="utf8")
                c = connection.cursor()
                command = "UPDATE " + usr_name +" SET `NICKNAME` = '%s'" % (usr_nickname)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `AGE` = '%s'" % (usr_age)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `ALLERGIC_HISTORY` = '%s'" % (usr_allergic_history)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `DISEASE_HISTORY` = '%s'" % (usr_disease_history)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `MEDICINE_HISTORY` = '%s'" % (usr_medicine_history)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `DISEASE_DESCRIPTION` = '%s'" % (usr_disease_description)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `FAMILY_DISEASE` = '%s'" % (usr_family_disease)
                c.execute(command)
                connection.commit()
                connection.close()
            else:
                usr_nickname = m_name_entry.get()
                usr_age = m_age_entry.get()
                usr_workspan = m_workspan_entry.get()
                usr_main_description = m_description_text.get("0.0","end")
                usr_hospital = m_hospital_entry.get()
                usr_workplace = str(m_workplace_combox.current())
                print("workplace test")
                connection = MySQLdb.connect(
                            "52.15.135.11", "root", "rootsql", "doctor", charset="utf8")
                c = connection.cursor()
                command = "UPDATE " + usr_name +" SET `NICKNAME` = '%s'" % (usr_nickname)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `AGE` = '%s'" % (usr_age)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `WORKSPAN` = '%s'" % (usr_workspan)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `HOSPITAL` = '%s'" % (usr_hospital)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `WORKPLACE` = '%s'" % (usr_workplace)
                c.execute(command)
                command = "UPDATE " + usr_name +" SET `MAIN_DESCRIPTION` = '%s'" % (usr_main_description)
                c.execute(command)
                connection.commit()
                connection.close()
                print(usr_workplace)
        btn_modify_OK = Button(
            frame.canvas_modify, text='确认修改', font=("Arial", 16), 
            command=lambda: confirm(), width=10)
        btn_modify_OK.place(x=680, y=30)


        frame.canvas_modify.pack_forget()
        frame.canvas_patient.place_forget()
        frame.canvas_doctor.place_forget()


##########################################################################

        frm = Frame(root)


        frm.pack(side=TOP, fill=BOTH)

        root.mainloop()


if __name__ == '__main__':
    window = tk.Tk()
    runtime.run(window)