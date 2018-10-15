from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

class showpic():
    def show(root):
        def resize(w, h, w_box, h_box, pil_image):      
          f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
          f2 = 1.0*h_box/h  
          factor = min([f1, f2])  
          width = int(w*factor)  
          height = int(h*factor)  
          return pil_image.resize((width, height), Image.ANTIALIAS)

        root3 = Toplevel()
        root3.title("doctor online system")
        root3.geometry('1000x1000')

        fenlei=('骨科','神经外科','胸外科','心血管外科',
        	'泌尿外科','烧伤科','整形科','普外科',
        	'小儿外科','消化内科','肾脏内科','心血管内科',
        	'呼吸内科','血液内科','内分泌科','风湿免疫科',
        	'变态反应/过敏反应科','感染/传染科','神经内科',
        	'肿瘤内科','耳鼻喉科','眼科','口腔科','神经科',
        	'皮肤科','疼痛科','妇产科','儿科学')

        canvas = Canvas(root3,width=1000,height=100,bg='#77ac98')
        """
        image = Image.open("title.jpg")
        im = ImageTk.PhotoImage(image)

        canvas.create_image(400,0,image=im)
        """
        canvas.create_text(100,55,text='私人医生',font=("Arial",24),fill='#e8f0eb')
        def printWindow():
            root.update()
            root.deiconify()
            root3.destroy()
        bt = Button(canvas,fg='#424242',bg='#e6ece9',text = '退出',command = printWindow)
        #修改button在canvas上的对齐方式
        canvas.create_window((950,20),window = bt,anchor = W)

        i=2
        def printwaiting():
            print('waitingnumber'+str(i))
        bt1 = Button(canvas,fg='#424242',bg='#e6ece9',text = '代办事项'+str(i),command = printwaiting,relief=GROOVE)
        #修改button在canvas上的对齐方式
        name="张三"
        gender="先生"
        canvas.create_text(930,90,text='欢迎您，'+name+gender,font=("Arial",12),fill='#e8f0eb')
        canvas.create_window((870,20),window = bt1,anchor = W)

        canvas.pack()

        canvas_down = Canvas(root3,width=150,height=650,bg='#e8f0eb')
        """
        image2 = Image.open("left.jpg")
        im2 = ImageTk.PhotoImage(image2)
        canvas_down.create_image(10,500,image=im2)
        """
        # def printWindow():
        #     print('查看历史记录')
        # bt2 = Button(fg='#424242',bg='#e6ece9',fg='#424242',bg='#e6ece9',canvas_down,text = '查看历史记录',command = printWindow,font=("Arial",16),bg='blue')
        # #修改button在canvas上的对齐方式
        # canvas_down.create_window((30,30),window = bt2,anchor = W)

        # def printWindow():
        #     print('查看该用户历史病例')
        # bt3 = Button(fg='#424242',bg='#e6ece9',fg='#424242',bg='#e6ece9',canvas_down,text = '查看该用户历史病例',command = printWindow,font=("Arial",16),bg='blue')
        # canvas_down.create_window((6,80),window = bt3,anchor = W)

        # def printpic():
        #     print('查看该用户提问信息')
        #     # root.showpic.show(root)
        #     # root3.destroy()
        # bt4 = Button(fg='#424242',bg='#e6ece9',fg='#424242',bg='#e6ece9',canvas_down,text = '查看该用户提问信息',command = printpic,font=("Arial",16),bg='blue')
        # canvas_down.create_window((6,130),window = bt4,anchor = W)

        # canvas_down.pack(side=LEFT,fill=BOTH)

        # def printhealth():
        #     print('查看用户饮食情况')
        # bt4 = Button(fg='#424242',bg='#e6ece9',fg='#424242',bg='#e6ece9',canvas_down,text = '查看用户健康数据',command = printhealth,font=("Arial",16),bg='blue')
        # canvas_down.create_window((15,180),window = bt4,anchor = W)

        canvas_down.pack(side=LEFT,fill=BOTH)


        frm = Frame(root3)

        t7=Label(frm,width=10,height=1,fg='#424242',font=('Arial',15),text='症状照片：')
        # t1.insert(1.0,'申请人编号：')
        t7.pack(side=LEFT)

        w_box=600
        h_box=600

        photo = Image.open("pic.png")#file：t图片路径
        w, h = photo.size 
        photo_resized = resize(w, h, w_box, h_box, photo)
        tk_image = ImageTk.PhotoImage(photo_resized) 
        t8 = Label(frm, image=tk_image, fg='#424242',width=w_box, height=h_box)
        t8.pack()

        frm.pack(side=TOP,fill=BOTH)

        root3.mainloop()



