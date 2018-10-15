from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib
from numpy import arange, sin, pi
from showpic import showpic
from sql_func import *
# import private_doctor


class history():
	def show(root,patient_name):

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

		startmonth=('1','2','3','4','5','6','7','8','9','10','11','12')
		startday=('1','2','3','4','5','6','7','8','9','10',
			'11','12','13','14','15','16','17','18','19','20',
			'21','22','23','24','25','26','27','28','29','30','31')
		endmonth=('1','2','3','4','5','6','7','8','9','10','11','12')
		endday=('1','2','3','4','5','6','7','8','9','10',
			'11','12','13','14','15','16','17','18','19','20',
			'21','22','23','24','25','26','27','28','29','30','31')


		canvas = Canvas(root2,width=1000,height=100,bg='#77ac98')
		# image = Image.open("title.jpg")
		# im = ImageTk.PhotoImage(image)

		# canvas.create_image(400,0,image=im)
		canvas.create_text(100,55,text='私人医生',font=("Arial",24),fill='#e8f0eb')
		def quit():
			root.update()
			root.deiconify()
			root2.destroy()
		bt = Button(canvas,fg='#424242',bg='#e6ece9',text = '退出',command = quit)
		#修改button在canvas上的对齐方式
		canvas.create_window((950,20),window = bt,anchor = W)

		i=2
		def printwaiting():
		    print('waitingnumber'+str(i))
		bt1 = Button(canvas,fg='#424242',bg='#e6ece9',text = '代办事项'+str(i),command = printwaiting,relief=GROOVE)
		#修改button在canvas上的对齐方式
		name = "张三"
		gender="先生"
		canvas.create_text(930,90,text='欢迎您，'+name+gender,font=("Arial",12),fill='#e8f0eb')
		canvas.create_window((870,20),window = bt1,anchor = W)

		canvas.pack()

		canvas_down = Canvas(root2,width=150,height=650,bg='#e8f0eb')
		"""
		image2 = Image.open("left.jpg")
		im2 = ImageTk.PhotoImage(image2)
		canvas_down.create_image(10,500,image=im2)
		"""
		# def printWindow():
		#     print('查看历史记录')
		# bt2 = Button(canvas_down,text = '查看历史记录',command = printWindow,font=("Arial",16),bg='blue')
		# #修改button在canvas上的对齐方式
		# canvas_down.create_window((30,30),window = bt2,anchor = W)

		# def printproblem():
		#     print('查看该用户历史病例')
		# bt3 = Button(canvas_down,text = '查看该用户提问信息',command = printproblem,font=("Arial",16),bg='blue')
		# canvas_down.create_window((6,80),window = bt3,anchor = W)

		# def printpic():
		# 	showpic.show(root)
		# 	root2.withdraw()
		# bt4 = Button(canvas_down,text = '查看症状图片',command = printpic,font=("Arial",16),bg='blue')
		# canvas_down.create_window((30,130),window = bt4,anchor = W)

		# canvas_down.pack(side=LEFT,fill=BOTH)

		# def printhealth():
		#     print('查看用户提问信息')
		# bt4 = Button(canvas_down,text = '查看用户健康数据',command = printhealth,font=("Arial",16),bg='blue')
		# canvas_down.create_window((15,180),window = bt4,anchor = W)

		canvas_down.pack(side=LEFT,fill=BOTH)


		frm=Frame(root2)
		frm_1=Frame(frm)
		frm_2=Frame(frm)
		startmonthnumber = StringVar()
		startdaynumber=StringVar()
		endmonthnumber=StringVar()
		enddaynumber=StringVar()
		t9=Label(frm_1,fg='#424242',width=10,height=1,font=('Arial',15),text='查看日期：')
		# t1.insert(1.0,'申请人编号：')
		t9.pack(side=LEFT)

		t = ttk.Combobox(frm_1,width=3,height=1, textvariable=startmonthnumber)
		t['values'] = startmonth    # 设置下拉列表的值
		t.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
		t.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

		t5=Label(frm_1,fg='#424242',width=3,height=1,font=('Arial',15),text='月')
		# t1.insert(1.0,'申请人编号：')
		t5.pack(side=LEFT)

		t1 = ttk.Combobox(frm_1,width=3,height=1, textvariable=startdaynumber)
		t1['values'] = startday    # 设置下拉列表的值
		t1.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
		t1.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

		t6=Label(frm_1,fg='#424242',width=3,height=1,font=('Arial',15),text='日')
		# t1.insert(1.0,'申请人编号：')
		t6.pack(side=LEFT)

		t2=Label(frm_1,fg='#424242',width=2,height=1,font=('Arial',15),text='-')
		# t1.insert(1.0,'申请人编号：')
		t2.pack(side=LEFT)

		t3 = ttk.Combobox(frm_1,width=3,height=1, textvariable=endmonthnumber)
		t3['values'] = endmonth    # 设置下拉列表的值
		t3.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
		t3.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

		t7=Label(frm_1,fg='#424242',width=3,height=1,font=('Arial',15),text='月')
		# t1.insert(1.0,'申请人编号：')
		t7.pack(side=LEFT)

		t4 = ttk.Combobox(frm_1,width=3,height=1, textvariable=enddaynumber)
		t4['values'] = endday    # 设置下拉列表的值
		t4.pack(side=LEFT)      # 设置其在界面中出现的位置  column代表列   row 代表行
		t4.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

		t8=Label(frm_1,fg='#424242',width=3,height=1,font=('Arial',15),text='日')
		# t1.insert(1.0,'申请人编号：')
		t8.pack(side=LEFT)

		def showdiet():
			frm_whole=Frame(frm_2)

			result = selectUserHistory(patient_name)

			for data in result:
				t=Label(frm_whole,fg='#424242',font=('Arial',15),text=data[1])
				t.pack(side=TOP,fill=BOTH)

				frm_add=Frame(frm_whole)
				t1=Label(frm_add,fg='#424242',width=10,height=1,font=('Arial',15),text='症状：')
				t1.pack(side=LEFT)
				t2=Text(frm_add,fg='#424242',height=3,font=('Arial',15))
				t2.tag_config('t2',foreground='black',underline=True)
				t2.insert(1.0,data[2],'t2')
				t2.pack(side=LEFT)

				frm_add.pack(side=TOP,fill=BOTH)


				frm_add2=Frame(frm_whole)

				t2=Label(frm_add2,fg='#424242',width=10,height=1,font=('Arial',15),text='用药：')
				t2.pack(side=LEFT)

				# t3=Label(frm_add,width=30,height=1,font=('Arial',15),text='晚餐')
				# t3.pack(side=LEFT)

				


				# t1=Label(frm_add2,width=30,height=1,font=('Arial',15),text='馄饨，包子')
				# t1.pack(side=LEFT)
				drugs = data[5]
				t3=Text(frm_add2,height=1,fg='#424242',font=('Arial',15))
				t3.tag_config('t2',foreground='black',underline=True)
				t3.insert(1.0,'，'.join(drugs),'t3')
				t3.pack(side=LEFT)
				# t3=Label(frm_add2,width=70,height=1,font=('Arial',15),text='阿莫西林，三九感冒灵')
				# t3.pack(side=LEFT)

				# t3=Label(frm_add2,width=30,height=1,font=('Arial',15),text='面条，牛肉')
				# t3.pack(side=LEFT)
				

				frm_add2.pack(side=TOP,fill=BOTH)

			

			frm_button=Frame(frm_whole)


			t2=Label(frm_button,fg='#424242',width=10,height=1,font=('Arial',15),text='病症图片：')
			t2.pack(side=LEFT)

			def showpic():
				print("showpic")
			t10 = Button(frm_button,fg='#424242',bg='#e6ece9',text = '查看',command = showpic,font=('Arial',15))
			t10.pack(side=LEFT)

			frm_button.pack(side=TOP,fill=BOTH)


			t=Label(frm_whole,fg='#424242',font=('Arial',15),text='2018/3/2')
			t.pack(side=TOP,fill=BOTH)

			frm_add3=Frame(frm_whole)
			t1=Label(frm_add3,fg='#424242',width=10,height=1,font=('Arial',15),text='症状：')
			t1.pack(side=LEFT)

			t2=Text(frm_add3,height=3,fg='#424242',font=('Arial',15))
			t2.tag_config('t2',foreground='black',underline=True)
			t2.insert(1.0,'咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕,咳嗽，喉咙疼痛，流鼻涕','t2')
			t2.pack(side=LEFT)

			frm_add3.pack(side=TOP,fill=BOTH)


			frm_add4=Frame(frm_whole)

			t2=Label(frm_add4,width=10,height=1,fg='#424242',font=('Arial',15),text='用药：')
			t2.pack(side=LEFT)

			# t3=Label(frm_add,width=30,height=1,fg='#424242',font=('Arial',15),text='晚餐')
			# t3.pack(side=LEFT)

			


			# t1=Label(frm_add2,width=30,height=1,fg='#424242',font=('Arial',15),text='馄饨，包子')
			# t1.pack(side=LEFT)

			t3=Text(frm_add4,fg='#424242',height=1,font=('Arial',15))
			t3.tag_config('t2',foreground='black',underline=True)
			t3.insert(1.0,'阿莫西林，三九感冒灵','t3')
			t3.pack(side=LEFT)
			# t3=Label(frm_add2,width=70,height=1,fg='#424242',font=('Arial',15),text='阿莫西林，三九感冒灵')
			# t3.pack(side=LEFT)

			# t3=Label(frm_add2,width=30,height=1,fg='#424242',font=('Arial',15),text='面条，牛肉')
			# t3.pack(side=LEFT)
			

			frm_add4.pack(side=TOP,fill=BOTH)

			frm_button1=Frame(frm_whole)


			t2=Label(frm_button1,fg='#424242',width=10,height=1,font=('Arial',15),text='病症图片：')
			t2.pack(side=LEFT)

			def showpic():
				print("showpic")
			t10 = Button(frm_button1,fg='#424242',bg='#e6ece9',text = '查看',command = showpic,font=('Arial',15))
			t10.pack(side=LEFT)

			frm_button1.pack(side=TOP,fill=BOTH)
			

			frm_whole.pack(side=TOP,fill=BOTH)
		t10 = Button(frm_1,fg='#424242',bg='#e6ece9',text = '查看',command = showdiet,font=('Arial',15))
		t10.pack(side=LEFT)

		frm_1.pack(side=TOP,fill=BOTH)
		frm_2.pack(side=TOP,fill=BOTH)


		frm.pack(side=TOP,fill=BOTH)


		root2.mainloop()