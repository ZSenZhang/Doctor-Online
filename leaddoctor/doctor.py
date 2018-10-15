from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from sql_func import *

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

# image = Image.open("title3.jpg")
# im = ImageTk.PhotoImage(image)

# canvas.create_image(400,0,image=im)

canvas.create_text(100,55,text='导流医生系统',font=("Arial",24),fill='#e8f0eb')
def printWindow():
    print('quit')
bt = Button(canvas,text = '退出',command = printWindow,fg='#595959')
#修改button在canvas上的对齐方式
canvas.create_window((950,20),window = bt,anchor = W)

i=2
def printwaiting():
    print('waitingnumber'+str(i))
bt1 = Button(canvas,text = '代办事项'+str(i),fg='#595959',command = printwaiting,relief=GROOVE)
#修改button在canvas上的对齐方式
name="张三"
gender="先生"
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
bt2 = Button(canvas_down,text = '查看历史记录',command = printWindow,font=("Arial",20),fg='#424242',bg='#e6ece9')
#修改button在canvas上的对齐方式
canvas_down.create_window((15,30),window = bt2,anchor = W)

# result = selectAllNoClass()

def download():
	result = selectAllNoClass()
	frm_2=Frame(frm)
	t=Text(frm_2,width=25,height=3,fg='#424242',font=("Arial",15))
	t.insert(1.0,result[0][1])
	t.pack(side=LEFT)

	t1=Text(frm_2,width=25,height=3,fg='#424242',font=("Arial",15))
	t1.insert(1.0,str(result[0][0]))
	t1.pack(side=LEFT)

	t2=Text(frm_2,width=50,height=3,fg='#424242',font=("Arial",15))
	t2.insert(1.0,result[0][2])
	t2.pack(side=LEFT)

	number = StringVar()
	t31 = ttk.Combobox(frm_2, width=25,height=1, textvariable=number,font=("Arial",15))
	t31['values'] = fenlei    # 设置下拉列表的值
	t31.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
	t31.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

	frm_2.pack(side=TOP,fill=BOTH)

	frm_3=Frame(frm)
	t=Text(frm_3,width=25,height=3,fg='#424242',font=("Arial",15))
	t.insert(1.0,result[1][1])
	t.pack(side=LEFT)

	t1=Text(frm_3,width=25,height=3,fg='#424242',font=("Arial",15))
	t1.insert(1.0,str(result[1][0]))
	t1.pack(side=LEFT)

	t2=Text(frm_3,width=50,height=3,fg='#424242',font=("Arial",15))
	t2.insert(1.0,result[1][2])
	t2.pack(side=LEFT)

	number = StringVar()
	t32 = ttk.Combobox(frm_3, width=25,height=1, textvariable=number,font=("Arial",15))
	t32['values'] = fenlei    # 设置下拉列表的值
	t32.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
	t32.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

	frm_3.pack(side=TOP,fill=BOTH)

	frm_4=Frame(frm)
	t=Text(frm_4,width=25,height=3,fg='#424242',font=("Arial",15))
	t.insert(1.0,result[2][1])
	t.pack(side=LEFT)

	t1=Text(frm_4,width=25,height=3,fg='#424242',font=("Arial",15))
	t1.insert(1.0,str(result[2][0]))
	t1.pack(side=LEFT)

	t2=Text(frm_4,width=50,height=3,fg='#424242',font=("Arial",15))
	t2.insert(1.0,result[2][2])
	t2.pack(side=LEFT)

	number = StringVar()
	t33 = ttk.Combobox(frm_4, width=25,height=1, textvariable=number,font=("Arial",15))
	t33['values'] = fenlei    # 设置下拉列表的值
	t33.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
	t33.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

	frm_4.pack(side=TOP,fill=BOTH)

	frm_5=Frame(frm)
	t=Text(frm_5,width=25,height=3,fg='#424242')
	t.insert(1.0,result[3][1])
	t.pack(side=LEFT)

	t1=Text(frm_5,width=25,height=3,fg='#424242')
	t1.insert(1.0,str(result[3][0]))
	t1.pack(side=LEFT)

	t2=Text(frm_5,width=50,height=3,fg='#424242')
	t2.insert(1.0,result[3][2])
	t2.pack(side=LEFT)

	number = StringVar()
	t34 = ttk.Combobox(frm_5, width=25,height=1, textvariable=number)
	t34['values'] = fenlei    # 设置下拉列表的值
	t34.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
	t34.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

	frm_5.pack(side=TOP,fill=BOTH)

	frm_6=Frame(frm)
	t=Text(frm_6,width=25,height=3,fg='#424242',font=("Arial",15))
	t.insert(1.0,result[4][1])
	t.pack(side=LEFT)

	t1=Text(frm_6,width=25,height=3,fg='#424242')
	t1.insert(1.0,str(result[4][0]))
	t1.pack(side=LEFT)

	t2=Text(frm_6,width=50,height=3,fg='#424242')
	t2.insert(1.0,result[4][2])
	t2.pack(side=LEFT)

	number = StringVar()
	t35 = ttk.Combobox(frm_6, width=25,height=1, textvariable=number)
	t35['values'] = fenlei    # 设置下拉列表的值
	t35.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
	t35.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

	frm_6.pack(side=TOP,fill=BOTH)

	frm_7=Frame(frm)
	def submit():
		print('提交')
		department1 = t31.get()
		department2 = t32.get()
		department3 = t33.get()
		department4 = t34.get()
		department5 = t35.get()
		if department1 != "":
			decideDepartment(result[0][0],department1)
			print("commit 1")
		if department2 != "":
			decideDepartment(result[1][0],department2)
			print("commit 2")
		if department3 != "":
			decideDepartment(result[2][0],department3)
			print("commit 3")
		if department4 != "":
			decideDepartment(result[3][0],department4)
			print("commit 4")
		if department5 != "":
			decideDepartment(result[4][0],department5)
			print("commit 5")


		frm_2.pack_forget()
		frm_3.pack_forget()
		frm_4.pack_forget()
		frm_5.pack_forget()
		frm_6.pack_forget()
		frm_7.pack_forget()

	t = Button(frm_7,text = '提交',command = submit,bg='#f9faf8',fg='#595959')
	t.pack()

	frm_7.pack(side=TOP,fill=BOTH)

bt3 = Button(canvas_down,text = '查看未完成任务',command = download,font=("Arial",20),bg='#f9faf8',fg='#424242')
canvas_down.create_window((6,80),window = bt3,anchor = W)

canvas_down.pack(side=LEFT,fill=BOTH)

frm = Frame(root)
frm_1=Frame(frm)
t=Text(frm_1,width=25,height=1,fg='#424242',font=("Arial",15))
t.insert(1.0,'申请时间')
t.pack(side=LEFT)

t1=Text(frm_1,width=25,height=1,fg='#424242',font=("Arial",15))
t1.insert(1.0,'申请人编号')
t1.pack(side=LEFT)

t2=Text(frm_1,width=50,height=1,fg='#424242',font=("Arial",15))
t2.insert(1.0,'症状')
t2.pack(side=LEFT)

t3=Text(frm_1,width=25,height=1,fg='#424242',font=("Arial",15))
t3.insert(1.0,'导流单位')
t3.pack(side=LEFT)

frm_1.pack(side=TOP,fill=BOTH)

frm.pack(side=TOP,fill=BOTH)

root.mainloop()
