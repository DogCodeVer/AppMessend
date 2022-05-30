from tkinter import *
from ShiftEncode import *


class App():
    def sendMsg(self):

        self.msg = Frame(self.bg_msg, bg='#272928')
        self.msg.pack()
        msg_text = Label(self.msg,
                         text=self.ent_msg.get(),
                         bg='#383A39',
                         font=15,
                         fg='#E4E6E5',
                         padx=0.1,
                         pady=0.1,
                         border='5')
        msg_text.pack()


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
        self.root.geometry("1200x666")

        self.bg_msg = Frame(self.root, bg='#272928')
        self.bg_msg.pack()
        self.bg_msg.place(height=600, width=350, x=5, y=5)

        self.ent_msg = Entry(self.bg_msg, bg="#383A39", borderwidth=0, fg='#E4E6E5',font=12)
        self.ent_msg.pack()
        self.ent_msg.place(bordermode="ignore", width=280, height=35, x=5, y=560)

        self.btn_msg = Button(self.bg_msg, text="Send", bg="#E4E6E5", borderwidth=0, fg='#383A39', command=self.sendMsg)
        self.btn_msg.pack()
        self.btn_msg.place(bordermode="ignore", width=55, height=35, x=290, y=560)

        self.setting = Frame(self.root)
        self.setting.pack()
        self.setting.place(x=400, y=5)

        self.txt_sum = Label(self.setting, text="Выбрать сумматоры")
        self.txt_sum.grid(column=0, row=0)

        self.s1 = IntVar()
        self.s2 = IntVar()
        self.s3 = IntVar()

        self.check1 = Checkbutton(self.setting, variable=self.s1, onvalue="1", offvalue="0")
        self.check2 = Checkbutton(self.setting, variable=self.s2, onvalue="2", offvalue="0")
        self.check3 = Checkbutton(self.setting, variable=self.s3, onvalue="3", offvalue="0")

        self.check1.grid(column=1, row=0)
        self.check2.grid(column=2, row=0)
        self.check3.grid(column=3, row=0)

        self.btn_sum = Button(self.setting, text="Добавить", command=lambda: (self.addSum(self.s1, self.s2, self.s3)))
        self.btn_sum.grid(row=1)

        self.summators = Label(self.setting, text="Сумматоры:{}".format(self.s))
        self.summators.grid(row=2)

        self.encoded=Label(self.setting,text="Закодированое сообщение:")
        self.encoded.grid(row=3)

        self.decoded=Label(self.setting,text="Декодированое сообщение:")
        self.decoded.grid(row=4)


app = App()
app.root.mainloop()