from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from sql_func import *


class jiezheng:
	def showjiezheng(root,innum,intime,symptom):
		root2 = Toplevel()
		root2.title("doctor online system")
		root2.geometry('1000x1000')

		fenlei=('骨科','神经外科','胸外科','心血管外科',
			'泌尿外科','烧伤科','整形科','普外科',
			'小儿外科','消化内科','肾脏内科','心血管内科',
			'呼吸内科','血液内科','内分泌科','风湿免疫科',
			'变态反应/过敏反应科','感染/传染科','神经内科',
			'肿瘤内科','耳鼻喉科','眼科','口腔科','神经科',
			'皮肤科','疼痛科','妇产科','儿科学')

		canvas = Canvas(root2,width=1000,height=100,bg='#77ac98')
		"""
		image = Image.open("title.jpg")
		im = ImageTk.PhotoImage(image)

		canvas.create_image(400,0,image=im)
		"""
		canvas.create_text(100,55,text='骨科',font=("Arial",24),fill='#e8f0eb')
		def printWindow():
			root.update()
			root.deiconify()
			root2.destroy()
		bt = Button(canvas,text = '返回',fg='#424242',bg='#e6ece9',command = printWindow)
		#修改button在canvas上的对齐方式
		canvas.create_window((950,20),window = bt,anchor = W)

		i=2
		def printwaiting():
		    print('waitingnumber'+str(i))
		bt1 = Button(canvas,text = '代办事项'+str(i),fg='#424242',bg='#e6ece9',command = printwaiting,relief=GROOVE)
		#修改button在canvas上的对齐方式
		name="张三"
		gender="先生"
		canvas.create_text(930,90,text='欢迎您，'+name+gender,font=("Arial",12),fill='#e8f0eb')
		canvas.create_window((870,20),window = bt1,anchor = W)

		canvas.pack()

		canvas_down = Canvas(root2,width=150,height=650,bg='#e6ece9')
		"""
		image2 = Image.open("left.jpg")
		im2 = ImageTk.PhotoImage(image2)
		canvas_down.create_image(10,500,image=im2)
		"""
		def printWindow():
		    print('查看历史记录')
		bt2 = Button(canvas_down,text = '查看历史记录',fg='#424242',bg='#e6ece9',command = printWindow,font=("Arial",16))
		#修改button在canvas上的对齐方式
		canvas_down.create_window((30,30),window = bt2,anchor = W)

		def printWindow():
		    print('查看该用户历史病例')
		bt3 = Button(canvas_down,text = '查看该用户历史病例',fg='#424242',bg='#e6ece9',command = printWindow,font=("Arial",16))
		canvas_down.create_window((6,80),window = bt3,anchor = W)

		def printpic():
		    print('查看症状图片')
		bt4 = Button(canvas_down,text = '查看症状图片',fg='#424242',bg='#e6ece9',command = printpic,font=("Arial",16))
		canvas_down.create_window((30,130),window = bt4,anchor = W)

		canvas_down.pack(side=LEFT,fill=BOTH)

		frm = Frame(root2)
		frm_1=Frame(frm)
		t=Label(frm_1,text='申请时间：',fg='#424242',width=10,height=1,font=('Arial',15))
		# t.tag_config('t',underline=True)
		# t.insert(5.0,'申请时间：')
		t.pack(side=LEFT)

		t4=Text(frm_1,width=10,height=1,fg='#424242',font=('Arial',15))
		t4.tag_config('t4',underline=True)
		t4.insert(1.0,intime,'t4')
		t4.pack(side=LEFT)

		t1=Label(frm_1,width=10,height=1,fg='#424242',font=('Arial',15),text='申请人编号：')
		# t1.insert(1.0,'申请人编号：')
		t1.pack(side=LEFT)

		t5=Text(frm_1,width=8,height=1,fg='#424242',font=('Arial',15))
		t5.tag_config('t5',foreground='black',underline=True)
		t5.insert(1.0,innum,'t5')
		t5.pack(side=LEFT)

		t2=Label(frm_1,width=6,height=1,fg='#424242',font=('Arial',15),text='性别：')
		# t2.insert(1.0,'性别：')
		t2.pack(side=LEFT)

		t3=Text(frm_1,width=6,height=1,fg='#424242',font=('Arial',15))
		t3.tag_config('t3',foreground='black',underline=True)
		t3.insert(1.0,'男','t3')
		t3.pack(side=LEFT)

		t6=Label(frm_1,width=6,height=1,fg='#424242',font=('Arial',15),text='年龄：')
		# t6.insert(1.0,'年龄：')
		t6.pack(side=LEFT)

		age=20

		t7=Text(frm_1,width=8,height=1,fg='#424242',font=('Arial',15))
		t7.tag_config('t7',foreground='black',underline=True)
		t7.insert(1.0,str(age)+'岁','t7')
		t7.pack(side=LEFT)

		t8=Text(frm_1,width=6,height=1,fg='#424242',font=('Arial',15))
		t8.insert(1.0,'科别：')
		t8.pack(side=LEFT)

		t9=Text(frm_1,width=4,height=1,fg='#424242',font=('Arial',15))
		t9.tag_config('t3',foreground='black',underline=True)
		t9.insert(1.0,'骨科','t3')
		t9.pack(side=LEFT)

		frm_1.pack(side=TOP,fill=BOTH)

		frm_2=Frame(frm)
		t=Label(frm_2,width=10,height=1,fg='#424242',font=('Arial',15),text='症状：')
		# t.insert(1.0,'症状:')
		t.pack(side=LEFT)

		# t1=Text(frm_2,width=25,height=3)
		# t1.insert(1.0,'12138')
		# t1.pack(side=LEFT)

		t2=Text(frm_2,height=3,font=('Arial',15),fg='#424242')
		t2.tag_config('t2',foreground='black',underline=True)
		t2.insert(1.0,symptom,'t2')
		t2.pack(side=LEFT)

		# number = StringVar()
		# t3 = ttk.Combobox(frm_2, width=25,height=1, textvariable=number)
		# t3['values'] = fenlei    # 设置下拉列表的值
		# t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
		# t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

		frm_2.pack(side=TOP,fill=BOTH)

		frm_3=Frame(frm)
		t=Label(frm_3,width=10,height=1,font=('Arial',15),text='过敏物：',fg='#424242')
		t.pack(side=LEFT)

		guomingshi='青霉素过敏'
		guomingshiheight=(len(guomingshi)/15)+1

		t1=Text(frm_3,width=15,height=guomingshiheight,font=('Arial',15),fg='#424242')
		# text = Entry(top, borderwidth = 3)
		t1.tag_config('t1',foreground='black',underline=True)
		t1.insert(1.0,guomingshi,'t1')
		t1.pack(side=LEFT)

		t2=Label(frm_3,width=10,height=1,font=('Arial',15),text='既往手术：',fg='#424242')
		t2.pack(side=LEFT)

		shoushushi='无'
		shoushushiheight=(len(shoushushi)/15)+1

		t3=Text(frm_3,height=shoushushiheight,width=15,font=('Arial',15),fg='#424242')
		t3.tag_config('t3',foreground='black',underline=True)
		t3.insert(1.0,'无','t3')
		t3.pack(side=LEFT)

		t4=Label(frm_3,width=20,height=1,font=('Arial',15),text='月经情况（女性患者）：',fg='#424242')
		t4.pack(side=LEFT)

		t5=Text(frm_3,height=2,width=15,font=('Arial',15),fg='#424242')
		t5.tag_config('t5',foreground='black',underline=True)
		t5.insert(1.0,'','t5')
		t5.pack(side=LEFT)

		frm_3.pack(side=TOP,fill=BOTH)

		# frm_7=Frame(frm)

		# t=Label(frm_7,width=20,height=1,text='查看症状图片：',font=('Arial',15))
		# t.pack(side=LEFT)

		# def printpic():
		#     print('查看症状图片')
		# t1 = Button(frm_7,text = '查看图片',command = printpic,font=("Arial",16),bg='blue')
		# t1.pack(side=LEFT)

		# frm_7.pack(side=TOP,fill=BOTH)


		frm_4=Frame(frm)
		t=Label(frm_4,width=8,height=1,text='医生诊断：',font=('Arial',15),fg='#424242')
		t.pack(side=LEFT)

		# t1=Entry(frm_4,width=75,font=('Arial',15),borderwidth=2)
		# t1.pack()

		class advice:
			frm_add=Frame(frm_4)
			t3=Entry(frm_add,width=80,font=('Arial',15),borderwidth=3)

		def addline():
			advice.t3.pack()
			advice.frm_add.pack()
		t2 = Button(frm_4,text = '添加医嘱',fg='#424242',bg='#e6ece9',command = addline)
		t2.pack(side=RIGHT)

		frm_4.pack(side=TOP,fill=BOTH)

		frm_5=Frame(frm)
		# t=Label(frm_5,width=10,height=1,font=('Arial',15),text='标签：')
		# t.pack(side=LEFT)
		t=Label(frm_5,width=12,height=1,font=('Arial',15),fg='#424242',text='')
		t.pack(side=LEFT)

		t1=Label(frm_5,width=18,height=1,font=('Arial',15),fg='#424242',text='推荐药物')
		t1.pack(side=LEFT)

		t2=Label(frm_5,width=29,height=1,font=('Arial',15),fg='#424242',text='药物编号')
		t2.pack(side=LEFT)

		t3=Label(frm_5,width=20,height=1,font=('Arial',15),fg='#424242',text='服用方法')
		t3.pack(side=LEFT)

		frm_5.pack(side=TOP,fill=BOTH)

		frm_6=Frame(frm)

		t6=Label(frm_6,width=12,height=1,font=('Arial',15),fg='#424242',text='药品：')
		t6.pack(side=LEFT)

		class advice_yaowu:
			entry_list = []

		def addyaowu():
			frm_add=Frame(frm_6)
			# t3=Label(frm_6,w)
			# t1=Label(frm_6,width=20,height=1,font=('Arial',15),text='推荐药物：')
			# t1.pack(side=TOP)
			# t4=Label(frm_add,width=12,height=1,font=('Arial',15),text='')
			# t4.pack(side=LEFT)

			t=Entry(frm_add,width=20,font=('Arial',15),borderwidth=3)
			t.pack(side=LEFT)

			t1=Entry(frm_add,width=20,font=('Arial',15),borderwidth=3)
			t1.pack(side=LEFT)

			t2=Entry(frm_add,width=30,font=('Arial',15),borderwidth=3)
			t2.pack(side=LEFT)

			frm_add.pack()

			advice_yaowu.entry_list.append([t,t1,t2])

		    # t4=Label(frm_4,width=20,height=1,font=('Arial',15),text='')
		    # t4.pack()

		t3 = Button(frm_6,text = '添加药物',fg='#424242',bg='#e6ece9',command = addyaowu)
		t3.pack(side=RIGHT)

		frm_6.pack(side=TOP,fill=BOTH)

		frm_10=Frame(frm)
		def commitAdvice():
			diagnose = advice.t3.get()
			writeDiagnose(innum,diagnose)

			for drug_item in advice_yaowu.entry_list:
				drugname = drug_item[0].get()
				usingmethod = drug_item[2].get()
				decideDrugs(innum,drugname,usingmethod)

			setDoneToTrue(innum)
			print('提交成功')
		t = Button(frm_10,text = '提交',fg='#424242',bg='#e6ece9',command = commitAdvice)
		t.pack()

		frm_10.pack(side=TOP,fill=BOTH)

		frm.pack(side=TOP,fill=BOTH)

		root2.mainloop()