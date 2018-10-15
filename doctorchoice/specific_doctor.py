from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from sql_func import *
from specific_doctor_jiezheng import jiezheng

root = Tk()
root.title("doctor online system")
root.geometry('1000x1000')

fenlei=('骨科','神经外科','胸外科','心血管外科',
	'泌尿外科','烧伤科','整形科','普外科',
	'小儿外科','消化内科','肾脏内科','心血管内科',
	'呼吸内科','血液内科','内分泌科','风湿免疫科',
	'变态反应/过敏反应科','感染/传染科','神经内科',
	'肿瘤内科','耳鼻喉科','眼科','口腔科','神经科',
	'皮肤科','疼痛科','妇产科','儿科学')

canvas = Canvas(root,width=1000,height=100,bg='#77ac98')
"""
image = Image.open("title.jpg")
im = ImageTk.PhotoImage(image)
"""
department = '骨科'
"""
canvas.create_image(400,0,image=im)
"""
canvas.create_text(40,55,text=department,font=("Arial",24),fill='#e8f0eb')
def printWindow():
    print('quit')
bt = Button(canvas,text = '退出',fg='#424242',bg='#e6ece9',command = printWindow)
#修改button在canvas上的对齐方式
canvas.create_window((950,20),window = bt,anchor = W)

i=2
def printwaiting():
    print('waitingnumber'+str(i))
bt1 = Button(canvas,text = '未读消息'+str(i),fg='#424242',bg='#e6ece9',command = printwaiting,relief=GROOVE)
#修改button在canvas上的对齐方式
name="张三"
gender="医生"
canvas.create_text(930,90,text='欢迎您，'+name+gender,font=("Arial",12),fill='#e8f0eb')
canvas.create_window((870,20),window = bt1,anchor = W)

canvas.pack()

canvas_down = Canvas(root,width=150,height=650,bg='#e6ece9')
"""
image2 = Image.open("left.jpg")
im2 = ImageTk.PhotoImage(image2)
canvas_down.create_image(10,500,image=im2)
"""
def printWindow():
    print('查看历史记录')
bt2 = Button(canvas_down,text = '查看历史记录',fg='#424242',bg='#e6ece9',command = printWindow,font=("Arial",20))
#修改button在canvas上的对齐方式
canvas_down.create_window((15,30),window = bt2,anchor = W)

# def printWindow():
#     print('查看未完成任务')
# bt3 = Button(canvas_down,text = '查看未完成任务',command = printWindow,font=("Arial",20))
# canvas_down.create_window((6,80),window = bt3,anchor = W)

canvas_down.pack(side=LEFT,fill=BOTH)

frm = Frame(root)
frm_1=Frame(frm)
t=Text(frm_1,width=25,height=1,fg='#424242')
t.insert(1.0,'申请时间')
t.pack(side=LEFT)

t1=Text(frm_1,width=25,height=1,fg='#424242')
t1.insert(1.0,'申请人编号')
t1.pack(side=LEFT)

t2=Text(frm_1,width=50,height=1,fg='#424242')
t2.insert(1.0,'症状概述')
t2.pack(side=LEFT)

t3=Text(frm_1,width=25,height=1,fg='#424242')
t3.insert(1.0,'是否接诊')
t3.pack(side=LEFT)

frm_1.pack(side=TOP,fill=BOTH)




result = selectInquiry(department)
def jiezhen1():
	acceptToDiagnose(result[0][0])
	root.withdraw()
	jiezheng.showjiezheng(root,result[0][0],result[0][1],result[0][2])
	print("{}号已接诊".format(result[0][0]))

def jiezhen2():
	acceptToDiagnose(result[1][0])
	root.withdraw()
	jiezheng.showjiezheng(root,result[1][0],result[1][1],result[1][2])
	print("{}号已接诊".format(result[1][0]))

def jiezhen3():
	acceptToDiagnose(result[2][0])
	root.withdraw()
	jiezheng.showjiezheng(root,result[2][0],result[2][1],result[2][2])
	print("{}号已接诊".format(result[2][0]))

def jiezhen4():
	acceptToDiagnose(result[3][0])
	root.withdraw()
	jiezheng.showjiezheng(root,result[3][0],result[3][1],result[3][2])
	print("{}号已接诊".format(result[3][0]))

def jiezhen5():
	acceptToDiagnose(result[4][0])
	root.withdraw()
	jiezheng.showjiezheng(root,result[4][0],result[4][1],result[4][2])
	print("{}号已接诊".format(result[4][0]))

frm_21=Frame(frm)
t=Text(frm_21,width=25,height=3,fg='#424242')
t.insert(1.0,result[0][1])
t.pack(side=LEFT)

t1=Text(frm_21,width=25,height=3,fg='#424242')
t1.insert(1.0,result[0][0])
t1.pack(side=LEFT)
t2=Text(frm_21,width=50,height=3,fg='#424242')
t2.insert(1.0,result[0][2])
t2.pack(side=LEFT)

t3 = Button(frm_21, width=25,height=1, text = '接诊',fg='#424242',bg='#e6ece9',command = jiezhen1)
# t3['values'] = fenlei    # 设置下拉列表的值
t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
# t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

frm_21.pack(side=TOP,fill=BOTH)

frm_22=Frame(frm)
t=Text(frm_22,width=25,height=3,fg='#424242')
t.insert(1.0,result[1][1])
t.pack(side=LEFT)

t1=Text(frm_22,width=25,height=3,fg='#424242')
t1.insert(1.0,result[1][0])
t1.pack(side=LEFT)
t2=Text(frm_22,width=50,height=3,fg='#424242')
t2.insert(1.0,result[1][2])
t2.pack(side=LEFT)

t3 = Button(frm_22, width=25,height=1, text = '接诊',fg='#424242',bg='#e6ece9',command = jiezhen2)
# t3['values'] = fenlei    # 设置下拉列表的值
t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
# t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

frm_22.pack(side=TOP,fill=BOTH)

frm_23=Frame(frm)
t=Text(frm_23,width=25,height=3,fg='#424242')
t.insert(1.0,result[2][1])
t.pack(side=LEFT)

t1=Text(frm_23,width=25,height=3,fg='#424242')
t1.insert(1.0,result[2][0])
t1.pack(side=LEFT)
t2=Text(frm_23,width=50,height=3,fg='#424242')
t2.insert(1.0,result[2][2])
t2.pack(side=LEFT)

t3 = Button(frm_23, width=25,height=1, text = '接诊',fg='#424242',bg='#e6ece9',command = jiezhen3)
# t3['values'] = fenlei    # 设置下拉列表的值
t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
# t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

frm_23.pack(side=TOP,fill=BOTH)

frm_24=Frame(frm)
t=Text(frm_24,width=25,height=3,fg='#424242')
t.insert(1.0,result[3][1])
t.pack(side=LEFT)

t1=Text(frm_24,width=25,height=3,fg='#424242')
t1.insert(1.0,result[3][0])
t1.pack(side=LEFT)
t2=Text(frm_24,width=50,height=3,fg='#424242')
t2.insert(1.0,result[3][2])
t2.pack(side=LEFT)

t3 = Button(frm_24, width=25,height=1, text = '接诊',fg='#424242',bg='#e6ece9',command = jiezhen4)
# t3['values'] = fenlei    # 设置下拉列表的值
t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
# t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

frm_24.pack(side=TOP,fill=BOTH)

frm_25=Frame(frm)
t=Text(frm_25,width=25,height=3,fg='#424242')
t.insert(1.0,result[4][1])
t.pack(side=LEFT)

t1=Text(frm_25,width=25,height=3,fg='#424242')
t1.insert(1.0,result[4][0])
t1.pack(side=LEFT)
t2=Text(frm_25,width=50,height=3,fg='#424242')
t2.insert(1.0,result[4][2])
t2.pack(side=LEFT)

t3 = Button(frm_25, width=25,height=1, text = '接诊',fg='#424242',bg='#e6ece9',command = jiezhen5)
# t3['values'] = fenlei    # 设置下拉列表的值
t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
# t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

frm_25.pack(side=TOP,fill=BOTH)

# frm_3=Frame(frm)
# t=Text(frm_3,width=25,height=3,fg='#424242')
# t.insert(1.0,'2018/5/29')
# t.pack(side=LEFT)

# t1=Text(frm_3,width=25,height=3,fg='#424242')
# t1.insert(1.0,'12139')
# t1.pack(side=LEFT)

# t2=Text(frm_3,width=50,height=3,fg='#424242')
# t2.insert(1.0,'咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕 \n,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕')
# t2.pack(side=LEFT)

# # number = StringVar()
# def jiezhen():
#     print('接诊')
# t3 = Button(frm_3, width=25,height=1, text = '接诊',command = jiezhen,bg='blue')
# # t3['values'] = fenlei    # 设置下拉列表的值
# t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
# # t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

# frm_3.pack(side=TOP,fill=BOTH)

def printWindow():
	print("换一批")

frm_4=Frame(frm)
t = Button(frm_4,text = '换一批',fg='#424242',bg='#e6ece9',command = printWindow)
t.pack()

frm_4.pack(side=TOP,fill=BOTH)

frm.pack(side=TOP,fill=BOTH)

root.mainloop()