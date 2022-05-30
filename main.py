from tkinter import *
from ShiftEncode import *


class App():
    def sendMsg(self):
        msg_text = Label(self.msg,
                         text=self.ent_msg.get(),
                         bg='#383A39',
                         font=15,
                         fg='#E4E6E5',
                         padx=0.1,
                         pady=0.1,
                         border='5')
        msg_text.pack()
        msg_text.place()


        codded=encode(self.ent_msg.get(), self.s)

        # with open("log.txt", "a") as self.file:
        #     self.file.write(self.ent_msg.get() + " " + encode(codded) + '\n')

        self.encoded.configure(text="Закодированое сообщение:"+encode(self.ent_msg.get(), self.s))
        self.decoded.configure(text="Декодированое сообщение:"+decode(codded,self.s))

    def addSum(self, s1, s2, s3):
        s_num = (str(s1.get()) + str(s2.get()) + str(s3.get())).replace('0', '')

        if len(s_num) < 2:
            return 0

        self.s.append(s_num)
        res = self.s

        self.summators.configure(text="Сумматоры:{}".format(res))



    def __init__(self):
        self.s = []

        self.root = Tk()
        self.root.title("Messenger")
        self.root.geometry("360x610")

        self.bg_msg = Frame(self.root, bg='#272928')
        self.bg_msg.pack()
        self.bg_msg.place(height=600, width=350, x=5, y=5)

        self.ent_msg = Entry(self.bg_msg, bg="#383A39", borderwidth=0, fg='#E4E6E5',font=12)
        self.ent_msg.pack()
        self.ent_msg.place(bordermode="ignore", width=280, height=35, x=5, y=560)

        self.btn_msg = Button(self.bg_msg, text="Send", bg="#E4E6E5", borderwidth=0, fg='#383A39', command=self.sendMsg)
        self.btn_msg.pack()
        self.btn_msg.place(bordermode="ignore", width=55, height=35, x=290, y=560)

        self.setting = Frame(self.bg_msg,bg='#272928')
        self.setting.pack()
        self.setting.place(height=140, width=350)

        self.txt_sum = Label(self.setting, text="Выбрать сумматоры",bg='#272928',fg='#E4E6E5')
        self.txt_sum.pack(side='left')

        self.s1 = IntVar()
        self.s2 = IntVar()
        self.s3 = IntVar()

        self.check1 = Checkbutton(self.setting, variable=self.s1, onvalue="1", offvalue="0",bg='#272928')
        self.check2 = Checkbutton(self.setting, variable=self.s2, onvalue="2", offvalue="0",bg='#272928')
        self.check3 = Checkbutton(self.setting, variable=self.s3, onvalue="3", offvalue="0",bg='#272928')

        self.check1.pack(side="left")
        self.check2.pack(side="left")
        self.check3.pack(side="left")

        self.btn_sum = Button(self.setting, text="Добавить", command=lambda: (self.addSum(self.s1, self.s2, self.s3)))
        self.btn_sum.pack(side='left')

        self.summators = Label(self.setting, text="Сумматоры:{}".format(self.s),bg='#272928',fg='#E4E6E5')
        self.summators.pack()
        self.summators.place(x=0,y=0)

        self.encoded=Label(self.setting,text="Закодированое сообщение:",bg='#272928',fg='#E4E6E5')
        self.encoded.pack()
        self.encoded.place(y=20)


        self.decoded=Label(self.setting,text="Декодированое сообщение:",bg='#272928',fg='#E4E6E5')
        self.decoded.pack()
        self.decoded.place(y=40)

        self.msg = Frame(self.bg_msg, bg='#272928')
        self.msg.pack()
        self.msg.place(x=5,y=100)

app = App()
app.root.mainloop()