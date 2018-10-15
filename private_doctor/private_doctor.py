from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from health import health
from history import history
from showpic import showpic
from sql_func import *
import MySQLdb

# =============================================

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

canvas.create_image(400,0,image=im)
"""
canvas.create_text(100,55,text='私人医生',font=("Arial",24),fill='#e8f0eb')
def printWindow():
    print('quit')
bt = Button(canvas,text = '退出',command = printWindow,fg='#424242',bg='#e6ece9')
#修改button在canvas上的对齐方式
canvas.create_window((950,20),window = bt,anchor = W)

innum = 4

db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
cursor = db.cursor()

cursor.execute('''SELECT TIME,USERNAME,SYMPTOM FROM INQUIRY WHERE INNUM = {}'''.format(innum))
result = cursor.fetchall()
intime = result[0][0]
patient_name = result[0][1]
symptom = result[0][2]

cursor.close()
db.close()


i = 2
def printwaiting():
    print('waitingnumber'+str(i))
bt1 = Button(canvas,text = '代办事项'+str(i),fg='#424242',bg='#e6ece9',command = printwaiting,relief=GROOVE)
#修改button在canvas上的对齐方式
name="张三"
# patient_name="陈金坤"
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
	print('查看该用户历史病例')
bt2 = Button(canvas_down,text = '查看历史记录',command = printWindow,font=("Arial",16),fg='#424242',bg='#e6ece9')
#修改button在canvas上的对齐方式
canvas_down.create_window((30,30),window = bt2,anchor = W)

def showhistory():
	root.withdraw()
	history.show(root,patient_name)
bt3 = Button(canvas_down,text = '查看该用户历史病例',command = showhistory,font=("Arial",16),fg='#424242',bg='#e6ece9')
canvas_down.create_window((6,80),window = bt3,anchor = W)

def showpicture():
    root.withdraw()
    showpic.show(root)
bt4 = Button(canvas_down,text = '查看症状图片',command = showpicture,font=("Arial",16),fg='#424242',bg='#e6ece9')
canvas_down.create_window((30,130),window = bt4,anchor = W)

canvas_down.pack(side=LEFT,fill=BOTH)

def showhealth():
	root.withdraw()
	health.show(root)
bt4 = Button(canvas_down,text = '查看用户健康数据',command = showhealth,font=("Arial",16),fg='#424242',bg='#e6ece9')
canvas_down.create_window((15,180),window = bt4,anchor = W)

canvas_down.pack(side=LEFT,fill=BOTH)

frm = Frame(root)
frm_1=Frame(frm)
t=Label(frm_1,text='申请时间：',width=10,height=1,font=('Arial',15),fg='#424242')

# t.tag_config('t',underline=True)
# t.insert(5.0,'申请时间：')
t.pack(side=LEFT)

t4=Text(frm_1,width=10,height=1,font=('Arial',15),fg='#424242')
t4.tag_config('t4',underline=True)
t4.insert(1.0,intime,'t4')
t4.pack(side=LEFT)

t1=Label(frm_1,width=10,height=1,font=('Arial',15),fg='#424242',text='申请人姓名：')
# t1.insert(1.0,'申请人编号：')
t1.pack(side=LEFT)

t5=Text(frm_1,width=8,height=1,font=('Arial',15),fg='#424242')
t5.tag_config('t5',foreground='#424242',underline=True)
t5.insert(1.0,patient_name,'t5')
t5.pack(side=LEFT)

t2=Label(frm_1,width=6,height=1,font=('Arial',15),fg='#424242',text='性别：')
# t2.insert(1.0,'性别：')
t2.pack(side=LEFT)

t3=Text(frm_1,width=6,height=1,fg='#424242',font=('Arial',15))
t3.tag_config('t3',foreground='#424242',underline=True)
t3.insert(1.0,'男','t3')
t3.pack(side=LEFT)

t6=Label(frm_1,width=6,height=1,fg='#424242',font=('Arial',15),text='年龄：')
# t6.insert(1.0,'年龄：')
t6.pack(side=LEFT)

age=20

t7=Text(frm_1,width=8,height=1,fg='#424242',font=('Arial',15))
t7.tag_config('t7',foreground='#424242',underline=True)
t7.insert(1.0,str(age)+'岁','t7')
t7.pack(side=LEFT)

t8=Text(frm_1,width=10,height=1,fg='#424242',font=('Arial',15))
t8.insert(1.0,'健康状况：')
t8.pack(side=LEFT)

t9=Text(frm_1,width=4,height=1,fg='#424242',font=('Arial',15))
t9.tag_config('t3',foreground='#424242',underline=True)
t9.insert(1.0,'良好','t3')
t9.pack(side=LEFT)

frm_1.pack(side=TOP,fill=BOTH)

frm_8=Frame(frm)
t=Label(frm_8,width=10,height=1,fg='#424242',font=('Arial',15),text='面对的疑惑：')
# t.insert(1.0,'症状:')
t.pack(side=LEFT)

# t1=Text(frm_2,width=25,height=3)
# t1.insert(1.0,'12138')
# t1.pack(side=LEFT)

t2=Text(frm_8,height=3,fg='#424242',font=('Arial',15))
t2.tag_config('t2',foreground='#424242',underline=True)
t2.insert(1.0,'无','t2')
t2.pack(side=LEFT)

# number = StringVar()
# t3 = ttk.Combobox(frm_2, width=25,height=1, textvariable=number)
# t3['values'] = fenlei    # 设置下拉列表的值
# t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
# t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

frm_8.pack(side=TOP,fill=BOTH)

frm_2=Frame(frm)
t=Label(frm_2,width=10,height=1,fg='#424242',font=('Arial',15),text='症状：')
# t.insert(1.0,'症状:')
t.pack(side=LEFT)

# t1=Text(frm_2,width=25,height=3)
# t1.insert(1.0,'12138')
# t1.pack(side=LEFT)

t2=Text(frm_2,height=1,fg='#424242',font=('Arial',15))
t2.tag_config('t2',foreground='#424242',underline=True)
t2.insert(1.0,symptom,'t2')
t2.pack(side=LEFT)

# number = StringVar()
# t3 = ttk.Combobox(frm_2, width=25,height=1, textvariable=number)
# t3['values'] = fenlei    # 设置下拉列表的值
# t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
# t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

frm_2.pack(side=TOP,fill=BOTH)

frm_3=Frame(frm)
t=Label(frm_3,width=10,height=1,fg='#424242',font=('Arial',15),text='过敏物：')
t.pack(side=LEFT)

guomingshi='青霉素过敏'
guomingshiheight=(len(guomingshi)/15)+1

t1=Text(frm_3,width=15,height=guomingshiheight,fg='#424242',font=('Arial',15))
# text = Entry(top, borderwidth = 3)
t1.tag_config('t1',foreground='#424242',underline=True)
t1.insert(1.0,guomingshi,'t1')
t1.pack(side=LEFT)

t2=Label(frm_3,width=10,height=1,fg='#424242',font=('Arial',15),text='既往手术：')
t2.pack(side=LEFT)

shoushushi='无'
shoushushiheight=(len(shoushushi)/15)+1

t3=Text(frm_3,height=shoushushiheight,width=15,fg='#424242',font=('Arial',15))
t3.tag_config('t3',foreground='#424242',underline=True)
t3.insert(1.0,'无','t3')
t3.pack(side=LEFT)

t4=Label(frm_3,width=20,height=1,fg='#424242',font=('Arial',15),text='月经情况（女性客户）：')
t4.pack(side=LEFT)

t5=Text(frm_3,height=2,width=15,fg='#424242',font=('Arial',15))
t5.tag_config('t5',foreground='#424242',underline=True)
t5.insert(1.0,'','t5')
t5.pack(side=LEFT)

frm_3.pack(side=TOP,fill=BOTH)

# frm_7=Frame(frm)

# t=Lable(frm_7,width=20,height=1,text='查看症状图片：',font=('Arial',15))
# t.pack(side=LEFT)

# def printpic():
#     print('查看症状图片')
# t1 = Button(frm_7,text = '查看图片',command = printpic,font=("Arial",16),bg='#f9faf8')
# t1.pack(side=LEFT)

# frm_7.pack(side=TOP,fill=BOTH)

frm_4=Frame(frm)
t=Label(frm_4,width=8,height=1,fg='#424242',text='医生建议：',font=('Arial',15))
t.pack(side=LEFT)

class advice:
	frm_add=Frame(frm_4)
	t3=Entry(frm_add,width=80,fg='#424242',font=('Arial',15),borderwidth=3)

# t1=Entry(frm_4,width=75,font=('Arial',15),borderwidth=2)
# t1.pack()

def addline():
	advice.t3.pack()
	advice.frm_add.pack()
t2 = Button(frm_4,text = '添加医嘱',fg='#424242',command = addline,bg='#e6ece9')
t2.pack(side=RIGHT)

frm_4.pack(side=TOP,fill=BOTH)

frm_9=Frame(frm)
t=Label(frm_9,width=8,height=1,fg='#424242',text='饮食建议：',font=('Arial',15))
t.pack(side=LEFT)

class advice_meal:
	frm_add1=Frame(frm_9)
	t2=Label(frm_add1,width=8,fg='#424242',height=1,text='早餐：',font=('Arial',15))

	t31=Entry(frm_add1,width=50,fg='#424242',font=('Arial',15),borderwidth=3)

	frm_add2=Frame(frm_9)
	t21=Label(frm_add2,width=8,height=1,fg='#424242',text='中餐：',font=('Arial',15))

	t32=Entry(frm_add2,width=50,fg='#424242',font=('Arial',15),borderwidth=3)

	frm_add3=Frame(frm_9)
	t22=Label(frm_add3,width=8,fg='#424242',height=1,text='晚餐：',font=('Arial',15))

	t33=Entry(frm_add3,width=50,fg='#424242',font=('Arial',15),borderwidth=3)

# t1=Entry(frm_4,width=75,font=('Arial',15),borderwidth=2)
# t1.pack()

def addline():
	advice_meal.t2.pack(side=LEFT)

	
	advice_meal.t31.pack()
	advice_meal.frm_add1.pack()

	advice_meal.t21.pack(side=LEFT)

	advice_meal.t32.pack()
	advice_meal.frm_add2.pack()

	
	advice_meal.t22.pack(side=LEFT)

	advice_meal.t33.pack()
	advice_meal.frm_add3.pack()

t2 = Button(frm_9,text = '添加饮食建议',fg='#424242',command = addline,bg='#f9faf8')
t2.pack(side=RIGHT)

frm_9.pack(side=TOP,fill=BOTH)


frm_5=Frame(frm)
# t=Lable(frm_5,width=10,height=1,font=('Arial',15),text='标签：')
# t.pack(side=LEFT)
t=Label(frm_5,width=12,height=1,fg='#424242',font=('Arial',15),text='')
t.pack(side=LEFT)

t1=Label(frm_5,width=18,height=1,fg='#424242',font=('Arial',15),text='推荐药物')
t1.pack(side=LEFT)

t2=Label(frm_5,width=29,height=1,fg='#424242',font=('Arial',15),text='药物编号')
t2.pack(side=LEFT)

t3=Label(frm_5,width=20,height=1,fg='#424242',font=('Arial',15),text='服用方法')
t3.pack(side=LEFT)

frm_5.pack(side=TOP,fill=BOTH)

frm_6=Frame(frm)

t6=Label(frm_6,width=12,height=1,fg='#424242',font=('Arial',15),text='药品：')
t6.pack(side=LEFT)

class advice_yaowu:
	entry_list = []

def addyaowu():
	frm_add=Frame(frm_6)
	# t3=Lable(frm_6,w)
	# t1=Lable(frm_6,width=20,height=1,font=('Arial',15),text='推荐药物：')
	# t1.pack(side=TOP)
	# t4=Lable(frm_add,width=12,height=1,font=('Arial',15),text='')
	# t4.pack(side=LEFT)

	t=Entry(frm_add,width=20,fg='#424242',font=('Arial',15),borderwidth=3)
	t.pack(side=LEFT)

	t1=Entry(frm_add,width=20,fg='#424242',font=('Arial',15),borderwidth=3)
	t1.pack(side=LEFT)

	t2=Entry(frm_add,width=30,fg='#424242',font=('Arial',15),borderwidth=3)
	t2.pack(side=LEFT)

	frm_add.pack()

	advice_yaowu.entry_list.append([t,t1,t2])

    # t4=Lable(frm_4,width=20,height=1,font=('Arial',15),text='')
    # t4.pack()

t3 = Button(frm_6,text = '添加药物',command = addyaowu,fg='#424242',bg='#e6ece9')
t3.pack(side=RIGHT)

frm_6.pack(side=TOP,fill=BOTH)

frm_10=Frame(frm)
def commitAdvice():
	diagnose = advice.t3.get()
	breakfast = advice_meal.t31.get()
	lunch = advice_meal.t32.get()
	dinner = advice_meal.t33.get()
	writeDiagnose(innum,diagnose)
	decideFood(innum,breakfast,lunch,dinner)

	for drug_item in advice_yaowu.entry_list:
		drugname = drug_item[0].get()
		usingmethod = drug_item[2].get()
		decideDrugs(innum,drugname,usingmethod)

	setDoneToTrue(innum)

	print('提交成功')
t = Button(frm_10,text = '提交',command = commitAdvice)
t.pack()

frm_10.pack(side=TOP,fill=BOTH)

frm.pack(side=TOP,fill=BOTH)

root.mainloop()