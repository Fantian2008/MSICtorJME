#Version 1.0a - 11 . 30 . 2022
#
#Copyright (C) 2022 -2032 Zilin Ding
#email: DZL20081110@163.com
#QQ:2302368576
from tkinter import *
import tkinter.messagebox as tm
from math import *
from fractions import Fraction
import numpy as np
import sympy as sy
import statistics as st
import sys

sys.setrecursionlimit(100000)

def main():

    root = Tk()
    root.config(bg = 'white')
    root.title("MSICtorJME多功能计算器(初中教育版) Version 1.0a_主页")

    frame = Frame(root)
    frame.config(bg = 'white')
    frame.pack(side=TOP,fill=Y,anchor='center')

    class AppWindows:

        def mathindex_page(self):

            root2 = Toplevel(root)
            root2.config(bg='white')
            root2.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_功能页")

            frame2 = Frame(root2)
            frame2.config(bg='white')
            frame2.pack(side=TOP, fill=Y, anchor='center')

            def decmath_page():

                class Decnum_math:

                    def __init__(self, dan, fan):
                        self.dan = dan
                        self.fan = fan

                    def farc(self):
                        f = str(u1_1.get())
                        self.fan = Fraction(f)
                        self.fan = str(self.fan)
                        d1_1.set(str(self.fan))

                    def add(self):
                        f = float(u1_1.get())
                        s = float(m1_1.get())
                        self.dan = (f + s)
                        self.dan = str(self.dan)
                        d1_1.set(str(self.dan))

                    def sub(self):
                        f = float(u1_1.get())
                        s = float(m1_1.get())
                        self.dan = (f - s)
                        d1_1.set(str(self.dan))

                    def mul(self):
                        f = float(u1_1.get())
                        s = float(m1_1.get())
                        self.dan = (f * s)
                        self.dan = round(self.dan, 16)
                        d1_1.set(str(self.dan))

                    def div(self):
                        f = float(u1_1.get())
                        s = float(m1_1.get())
                        self.dan = (f / s)
                        self.dan = round(self.dan, 16)
                        d1_1.set(str(self.dan))

                    def mpow(self):
                        f = float(u1_1.get())
                        s = float(m1_1.get())
                        self.dan = (f ** s)
                        self.dan = round(self.dan, 16)
                        d1_1.set(str(self.dan))

                    def rad(self):
                        f = float(u1_1.get())
                        s = float(m1_1.get())
                        self.dan = (f ** (1 / s))
                        self.dan = round(self.dan, 16)
                        d1_1.set(str(self.dan))

                    def thelog(self):
                        f = float(u1_1.get())
                        s = float(m1_1.get())
                        self.dan = log(s,f)
                        self.dan = round(self.dan, 16)
                        d1_1.set(str(self.dan))

                    def delall(self):
                        u1_1.set("")
                        m1_1.set("")
                        d1_1.set("")
                        self.fan = Fraction(0,1)
                        self.dan = 0.0
                    

                def __quitdecmathpage__():
                    root2_1.destroy()


                u1_1 = StringVar()
                m1_1 = StringVar()
                d1_1 = StringVar()
                decmath = Decnum_math(0.0,Fraction(0,1))

                root2_1 = Toplevel(root2)
                root2_1.config(bg='white')
                root2_1.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_小数计算器")

                frame2_1 = Frame(root2_1)
                frame2_1.config(bg='white')
                frame2_1.pack(side=TOP, fill=Y, anchor='center')

                lab1 = Label(frame2_1, font=('微软雅黑', 15), text="MSICtor JME 小数计算器", anchor='center')
                lab1.config(fg='blue', bg='white')
                lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                lab2 = Label(frame2_1, font=('微软雅黑', 10), text="上式/底数/被开方数:")
                lab2.config(bg='white')
                lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)

                lab11 = Label(frame2_1, font=('微软雅黑', 5), text="")
                lab11.config(bg='white')
                lab11.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                lab3 = Label(frame2_1, font=('微软雅黑', 10), text="下式/指数/真数/次方根数:")
                lab3.config(bg='white')
                lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                lab22 = Label(frame2_1, font=('微软雅黑', 5), text="")
                lab22.config(bg='white')
                lab22.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                lab4 = Label(frame2_1, font=('微软雅黑', 10), text="计算结果:")
                lab4.config(bg='white')
                lab4.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                lab33 = Label(frame2_1, font=('微软雅黑', 10), text="")
                lab33.config(bg='white')
                lab33.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                lab5 = Label(frame2_1, font=('微软雅黑', 8),
                             text="*注:1.使用“小数转分数”功能时,请把要转换的小数写在“上式/底数/被开方数”中。\n2.使用“log”时,在“上式/底数/被开方数:”里填写底数,在“下式/指数/真数/次方根数:”中填写真数。\n3.输入的数据必须为小数(格式为:整数部分.(英文点)小数部分),必须使用英文输入法!\n4.输入时数据后面不能有空格。\n5.计算结果仅保留小数点后16位。")
                lab5.config(bg='white')
                lab5.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                lab6 = Label(root2_1, font=('微软雅黑', 7),
                             text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                lab6.config(bg='white')
                lab6.pack(anchor='se', padx=5, pady=5)

                ent1 = Entry(frame2_1, textvariable=u1_1)
                ent1.grid(row=1, column=1, sticky='ew', columnspan=1)

                ent2 = Entry(frame2_1, textvariable=m1_1)
                ent2.grid(row=3, column=1, sticky='ew', columnspan=1)

                ent3 = Entry(frame2_1, textvariable=d1_1)
                ent3.grid(row=5, column=1, sticky='ew', columnspan=1)

                button1 = Button(frame2_1, text="  +  ", command=decmath.add)
                button1.config(bg='white')
                button1.grid(row=1, column=2, padx=5, pady=5)

                button2 = Button(frame2_1, text="  -  ", command=decmath.sub)
                button2.config(bg='white')
                button2.grid(row=2, column=2, padx=5, pady=5)

                button3 = Button(frame2_1, text="  *  ", command=decmath.mul)
                button3.config(bg='white')
                button3.grid(row=3, column=2, padx=5, pady=5)

                button4 = Button(frame2_1, text="  /  ", command=decmath.div)
                button4.config(bg='white')
                button4.grid(row=4, column=2, padx=5, pady=5)

                button5 = Button(frame2_1, text="幂运算", command=decmath.mpow)
                button5.config(bg='white')
                button5.grid(row=5, column=2, padx=5, pady=5)

                button6 = Button(frame2_1, text="根式运算", command=decmath.rad)
                button6.config(bg='white')
                button6.grid(row=1, column=3, padx=5, pady=5)

                button11 = Button(frame2_1, text="小数转分数", command=decmath.farc)
                button11.config(bg='white')
                button11.grid(row=3, column=3, padx=5, pady=5)

                button7 = Button(frame2_1, text="  log  ", command=decmath.thelog)
                button7.config(bg='white')
                button7.grid(row=2, column=3, padx=5, pady=5)
                
                button10 = Button(frame2_1, text="   C   ", command=decmath.delall)
                button10.config(bg='white')
                button10.grid(row=4, column=3, padx=5, pady=5)
                
                button12 = Button(frame2_1, text="返回功能页", command=__quitdecmathpage__)
                button12.config(bg='white')
                button12.grid(row=5, column=3, padx=5, pady=5)

                root2_1.update_idletasks()

                x = (root2_1.winfo_screenwidth() - root2_1.winfo_reqwidth()) / 2
                y = (root2_1.winfo_screenheight() - root2_1.winfo_reqheight()) / 2
                root2_1.geometry("+%d+%d" % (x, y))

                root2_1.mainloop()

            def farcmath_page():

                class Farcnum_math:

                    def __init__(self, fan,dan):
                        self.fan = fan
                        self.dan = dan

                    def dec(self):
                        f = str(u1_2.get())
                        self.fan = Fraction(f)
                        self.dan = float(self.fan)
                        d1_2.set(str(self.dan))

                    def fadd(self):
                        f = Fraction(str(u1_2.get()))
                        s = Fraction(str(m1_2.get()))
                        self.fan = Fraction(f + s)
                        d1_2.set(str(self.fan))

                    def fsub(self):
                        f = Fraction(str(u1_2.get()))
                        s = Fraction(str(m1_2.get()))
                        self.fan = Fraction(f - s)
                        d1_2.set(str(self.fan))

                    def fmul(self):
                        f = Fraction(str(u1_2.get()))
                        s = Fraction(str(m1_2.get()))
                        self.fan = Fraction(f * s)
                        d1_2.set(str(self.fan))

                    def fdiv(self):
                        f = Fraction(str(u1_2.get()))
                        s = Fraction(str(m1_2.get()))
                        self.fan = Fraction(f / s)
                        d1_2.set(str(self.fan))

                    def fpow(self):
                        f = Fraction(str(u1_2.get()))
                        s = Fraction(str(m1_2.get()))
                        self.fan = Fraction(f ** s)
                        d1_2.set(str(self.fan))

                    def frad(self):
                        f = Fraction(str(u1_2.get()))
                        s = Fraction(str(m1_2.get()))
                        self.fan = Fraction(f ** (1 / s))
                        self.dan = float(self.fan)
                        self.dan = round(self.dan,16)
                        an = "小数:%s,分数:%s"%(str(self.dan),str(self.fan))
                        d1_2.set(str(an))

                    def thelog(self):
                        f = Fraction(str(u1_2.get()))
                        s = Fraction(str(m1_2.get()))
                        self.fan = Fraction(log(s,f))
                        d1_2.set(str(self.fan))

                    def delall(self):
                        u1_2.set("")
                        m1_2.set("")
                        d1_2.set("")
                        self.fan = Fraction(0,1)
                        self.dan = 0.0

                def __quitfarcmathpage__():
                    root2_2.destroy()

                u1_2 = StringVar()
                m1_2 = StringVar()
                d1_2 = StringVar()
                farcmath = Farcnum_math(Fraction(0, 1), 0.0)

                root2_2 = Toplevel(root2)
                root2_2.config(bg='white')
                root2_2.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_分数计算器")

                frame2_2 = Frame(root2_2)
                frame2_2.config(bg='white')
                frame2_2.pack(side=TOP, fill=Y, anchor='center')

                lab1 = Label(frame2_2, font=('微软雅黑', 15), text="MSICtor JME 分数计算器", anchor='center')
                lab1.config(fg='blue', bg='white')
                lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                lab2 = Label(frame2_2, font=('微软雅黑', 10), text="上式/底数/被开方数:")
                lab2.config(bg='white')
                lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)

                lab11 = Label(frame2_2, font=('微软雅黑', 5), text="")
                lab11.config(bg='white')
                lab11.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                lab3 = Label(frame2_2, font=('微软雅黑', 10), text="下式/指数/真数/次方根数:")
                lab3.config(bg='white')
                lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                lab22 = Label(frame2_2, font=('微软雅黑', 5), text="")
                lab22.config(bg='white')
                lab22.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                lab4 = Label(frame2_2, font=('微软雅黑', 10), text="计算结果:")
                lab4.config(bg='white')
                lab4.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                lab33 = Label(frame2_2, font=('微软雅黑', 10), text="")
                lab33.config(bg='white')
                lab33.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                lab5 = Label(frame2_2, font=('微软雅黑', 8),
                             text="*注:1.使用“分数转小数”功能时,请把要转换的分数写在“上式/底数/被开方数”中。\n2.使用“log”时,在“上式/底数/被开方数:”里填写底数,在“下式/指数/真数/次方根数:”中填写真数。\n3.输入必须为分数(格式为:分子/分母),必须使用英文输入法!\n4.输入时数据后面不能有空格。")
                lab5.config(bg='white')
                lab5.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                lab6 = Label(root2_2, font=('微软雅黑', 7),
                             text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                lab6.config(bg='white')
                lab6.pack(anchor='se', padx=5, pady=5)

                ent1 = Entry(frame2_2, textvariable=u1_2)
                ent1.grid(row=1, column=1, sticky='ew', columnspan=1)

                ent2 = Entry(frame2_2, textvariable=m1_2)
                ent2.grid(row=3, column=1, sticky='ew', columnspan=1)

                ent3 = Entry(frame2_2, textvariable=d1_2)
                ent3.grid(row=5, column=1, sticky='ew', columnspan=1)

                button1 = Button(frame2_2, text="  +  ", command=farcmath.fadd)
                button1.config(bg='white')
                button1.grid(row=1, column=2, padx=5, pady=5)

                button2 = Button(frame2_2, text="  -  ", command=farcmath.fsub)
                button2.config(bg='white')
                button2.grid(row=2, column=2, padx=5, pady=5)

                button3 = Button(frame2_2, text="  *  ", command=farcmath.fmul)
                button3.config(bg='white')
                button3.grid(row=3, column=2, padx=5, pady=5)

                button4 = Button(frame2_2, text="  /  ", command=farcmath.fdiv)
                button4.config(bg='white')
                button4.grid(row=4, column=2, padx=5, pady=5)

                button5 = Button(frame2_2, text="幂运算", command=farcmath.fpow)
                button5.config(bg='white')
                button5.grid(row=5, column=2, padx=5, pady=5)

                button6 = Button(frame2_2, text="根式运算", command=farcmath.frad)
                button6.config(bg='white')
                button6.grid(row=1, column=3, padx=5, pady=5)

                button11 = Button(frame2_2, text="分数转小数", command=farcmath.dec)
                button11.config(bg='white')
                button11.grid(row=3, column=3, padx=5, pady=5)

                button7 = Button(frame2_2, text="  log  ", command=farcmath.thelog)
                button7.config(bg='white')
                button7.grid(row=2, column=3, padx=5, pady=5)

                button10 = Button(frame2_2, text="   C   ", command=farcmath.delall)
                button10.config(bg='white')
                button10.grid(row=4, column=3, padx=5, pady=5)

                button12 = Button(frame2_2, text="返回功能页", command=__quitfarcmathpage__)
                button12.config(bg='white')
                button12.grid(row=5, column=3, padx=5, pady=5)

                root2_2.update_idletasks()

                x = (root2_2.winfo_screenwidth() - root2_2.winfo_reqwidth()) / 2
                y = (root2_2.winfo_screenheight() - root2_2.winfo_reqheight()) / 2
                root2_2.geometry("+%d+%d" % (x, y))

                root2_2.mainloop()

            def numbertheory_page():

                class Numbertheory_math:

                    def __init__(self, fan):
                        self.fan = fan

                    def theceil(self):
                        f = Fraction(str(u1_15.get()))
                        self.fan = Fraction(ceil(f))
                        d1_15.set(str(self.fan))

                    def thefloor(self):
                        f = Fraction(str(u1_15.get()))
                        self.fan = Fraction(floor(f))
                        d1_15.set(str(self.fan))

                    def thefabs(self):
                        f = Fraction(str(u1_15.get()))
                        self.fan = Fraction(fabs(f))
                        d1_15.set(str(self.fan))

                    def thegcd(self):
                        f = int(str(u1_15.get()))
                        s = int(str(m1_15.get()))
                        self.fan = int(gcd(f,s))
                        d1_15.set(str(self.fan))

                    def thelcm(self):
                        f = int(str(u1_15.get()))
                        s = int(str(m1_15.get()))
                        self.fan = int(lcm(f,s))
                        d1_15.set(str(self.fan))

                    def theprime(self):
                        num = int(u1_15.get())
                        if num == 1:
                            d1_15.set("1非质数(素数),非合数")
                        else:
                            for i in range(2, num):
                                if num % i == 0:
                                    d1_15.set("{} 非质数 ".format(num))
                                    break
                            else:
                                d1_15.set("{} 为质数 ".format(num))

                    def delall(self):
                        u1_15.set("")
                        m1_15.set("")
                        d1_15.set("")
                        self.fan = Fraction(0, 1)
                        self.dan = 0.0

                def __quitnumthemathpage__():
                    root2_15.destroy()

                u1_15 = StringVar()
                m1_15 = StringVar()
                d1_15 = StringVar()
                numtheory = Numbertheory_math(Fraction(0, 1))

                root2_15 = Toplevel(root2)
                root2_15.config(bg='white')
                root2_15.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_数论计算器")

                frame2_15 = Frame(root2_15)
                frame2_15.config(bg='white')
                frame2_15.pack(side=TOP, fill=Y, anchor='center')

                lab1 = Label(frame2_15, font=('微软雅黑', 15), text="MSICtor JME 数论计算器", anchor='center')
                lab1.config(fg='blue', bg='white')
                lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                lab2 = Label(frame2_15, font=('微软雅黑', 10), text="数a:")
                lab2.config(bg='white')
                lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)

                lab11 = Label(frame2_15, font=('微软雅黑', 5), text="")
                lab11.config(bg='white')
                lab11.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                lab3 = Label(frame2_15, font=('微软雅黑', 10), text="数b:")
                lab3.config(bg='white')
                lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                lab22 = Label(frame2_15, font=('微软雅黑', 5), text="")
                lab22.config(bg='white')
                lab22.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                lab4 = Label(frame2_15, font=('微软雅黑', 10), text="计算结果:")
                lab4.config(bg='white')
                lab4.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                lab33 = Label(frame2_15, font=('微软雅黑', 10), text="")
                lab33.config(bg='white')
                lab33.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                lab5 = Label(frame2_15, font=('微软雅黑', 8),
                             text="*注:1.使用取整,绝对值功能时,请把要计算的数写在“数a”中。\n2.使用最大公约数,最小公倍数时,请把要计算的数写在“数a”和“数b”中。\n3.输入的数据可为小数或分数(公约数,公倍数,质数判断只能输入整数),\n分数格式为:分子/分母,必须使用英文输入法!\n4.计算结果仅为分数。\n5.使用质数判断时请把数据写在“数a”中。")
                lab5.config(bg='white')
                lab5.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                lab6 = Label(root2_15, font=('微软雅黑', 7),
                             text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                lab6.config(bg='white')
                lab6.pack(anchor='se', padx=5, pady=5)

                ent1 = Entry(frame2_15, textvariable=u1_15)
                ent1.grid(row=1, column=1, sticky='ew', columnspan=1)

                ent2 = Entry(frame2_15, textvariable=m1_15)
                ent2.grid(row=3, column=1, sticky='ew', columnspan=1)

                ent3 = Entry(frame2_15, textvariable=d1_15)
                ent3.grid(row=5, column=1, sticky='ew', columnspan=1)

                button1 = Button(frame2_15, text="向上取整", command=numtheory.theceil)
                button1.config(bg='white')
                button1.grid(row=1, column=2, padx=5, pady=5)

                button2 = Button(frame2_15, text="向下取整", command=numtheory.thefloor)
                button2.config(bg='white')
                button2.grid(row=2, column=2, padx=5, pady=5)

                button3 = Button(frame2_15, text="绝对值", command=numtheory.thefabs)
                button3.config(bg='white')
                button3.grid(row=3, column=2, padx=5, pady=5)

                button4 = Button(frame2_15, text="最大公约数", command=numtheory.thegcd)
                button4.config(bg='white')
                button4.grid(row=4, column=2, padx=5, pady=5)

                button5 = Button(frame2_15, text="最小公倍数", command=numtheory.thelcm)
                button5.config(bg='white')
                button5.grid(row=5, column=2, padx=5, pady=5)

                button6 = Button(frame2_15, text="质数判断", command=numtheory.theprime)
                button6.config(bg='white')
                button6.grid(row=1, column=3, padx=5, pady=5)

                button10 = Button(frame2_15, text="   C   ", command=numtheory.delall)
                button10.config(bg='white')
                button10.grid(row=2, column=3, padx=5, pady=5)

                button12 = Button(frame2_15, text="返回功能页", command=__quitnumthemathpage__)
                button12.config(bg='white')
                button12.grid(row=3, column=3, padx=5, pady=5)

                root2_15.update_idletasks()

                x = (root2_15.winfo_screenwidth() - root2_15.winfo_reqwidth()) / 2
                y = (root2_15.winfo_screenheight() - root2_15.winfo_reqheight()) / 2
                root2_15.geometry("+%d+%d" % (x, y))

                root2_15.mainloop()



            class Equmath_pages:

                def any_equ_page(self):

                    def any_threeoneteam():
                        x = sy.Symbol('x')
                        y = sy.Symbol('y')
                        z = sy.Symbol('z')
                        expr1 = str(u1_5.get())
                        expr1 = expr1.replace("=","-(") + ")"
                        expr2 = str(m1_5.get())
                        expr2 = expr2.replace("=", "-(") + ")"
                        expr3 = str(u1_5_1.get())
                        expr3 = expr3.replace("=", "-(") + ")"
                        r1 = sy.solve([expr1,expr2,expr3], [x,y,z])
                        r1 = str(r1)
                        r1 = r1.replace("{", "")
                        r1 = r1.replace("}", "")
                        r1 = r1.replace(":", "=")
                        if r1 == "[]":
                            d1_5.set("无解")
                        else:
                            d1_5.set(r1)


                    def any_twooneteam():
                        x = sy.Symbol('x')
                        y = sy.Symbol('y')
                        expr1 = str(u1_5.get())
                        expr2 = str(m1_5.get())
                        expr1 = expr1.replace("=", "-(") + ")"
                        expr2 = expr2.replace("=", "-(") + ")"
                        r1 = sy.solve([expr1,expr2], [x,y])
                        r1 = str(r1)
                        r1 = r1.replace("{","")
                        r1 = r1.replace("}","")
                        r1 = r1.replace(":","=")
                        if r1 == "[]":
                            d1_5.set("无解")
                        else:
                            d1_5.set(r1)

                    def any_oneone():
                        x = sy.Symbol('x')
                        expr1 = str(u1_5.get())
                        expr1 = expr1.replace("=", "-(") + ")"
                        r1 = sy.solve(expr1, [x])
                        r1 = str(r1)
                        r1 = r1.replace("[", "x=")
                        r1 = r1.replace("]", "")
                        d1_5.set(r1)

                    def any_onetwo():
                        x = sy.Symbol('x')
                        expr1 = str(u1_5.get())
                        expr1 = expr1.replace("=", "-(") + ")"
                        r1 = sy.solve(expr1, [x])
                        r1 = str(r1)
                        r1 = r1.replace("[", "x=")
                        r1 = r1.replace("]", "")
                        d1_5.set(r1)

                    def delall():
                        u1_5.set("")
                        m1_5.set("")
                        u1_5_1.set("")
                        d1_5.set("")

                    def __quitequcmathpage__():
                        root2_5.destroy()

                    u1_5 = StringVar()
                    u1_5_1 = StringVar()
                    d1_5 = StringVar()
                    m1_5 = StringVar()

                    root2_5 = Toplevel(root2)
                    root2_5.config(bg='white')
                    root2_5.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_自定义解方程/方程组")

                    frame2_5 = Frame(root2_5)
                    frame2_5.config(bg='white')
                    frame2_5.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_5, font=('微软雅黑', 15), text="MSICtor JME 自定义解方程/方程组", anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_5, font=('微软雅黑', 10), text=" 方程式（关于未知数x,y,z) : 自定义(输入时注意事项见“*注”) ")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_5, font=('微软雅黑', 10), text="一式:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_5, font=('微软雅黑', 10), text="二式:")
                    lab3.config(bg='white')
                    lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab4 = Label(frame2_5, font=('微软雅黑', 10), text="三式:")
                    lab4.config(bg='white')
                    lab4.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_5, font=('微软雅黑', 10), text="该方程/方程组的解:")
                    lab5.config(bg='white')
                    lab5.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_5, font=('微软雅黑', 8),
                                 text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:(分子/分母)。\n2.本计算器支持根式运算,表示平方根用“(符号sqrt(被开方数))”。\n3.输入时按顺序输入方程式,必须使用英文输入法。\n4.输入未知数系数时,未知数和系数之间用乘或除号连接。")
                    lab6.config(bg='white')
                    lab6.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_5, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_5, textvariable=u1_5)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_5, textvariable=m1_5)
                    ent2.grid(row=3, column=1, sticky='ew', columnspan=1)

                    ent3 = Entry(frame2_5, textvariable=u1_5_1)
                    ent3.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_5, textvariable=d1_5)
                    ent4.grid(row=5, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_5, text="一元一次方程", command=any_oneone)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button2 = Button(frame2_5, text="二元一次方程组", command=any_twooneteam)
                    button2.config(bg='white')
                    button2.grid(row=3, column=2, padx=5, pady=5)

                    button3 = Button(frame2_5, text="三元一次方程组", command=any_threeoneteam)
                    button3.config(bg='white')
                    button3.grid(row=4, column=2, padx=5, pady=5)

                    button4 = Button(frame2_5, text="一元二次方程", command=any_onetwo)
                    button4.config(bg='white')
                    button4.grid(row=5, column=2, padx=5, pady=5)

                    button10 = Button(frame2_5, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=6, column=2, padx=5, pady=5)

                    button12 = Button(frame2_5, text="返回功能页", command=__quitequcmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=7, column=2, padx=5, pady=5)

                    root2_5.update_idletasks()

                    x = (root2_5.winfo_screenwidth() - root2_5.winfo_reqwidth()) / 2
                    y = (root2_5.winfo_screenheight() - root2_5.winfo_reqheight()) / 2
                    root2_5.geometry("+%d+%d" % (x, y))

                    root2_5.mainloop()

                def f_tilequ_page(self):

                    def f_tilequ():
                        a = Fraction(str(u1_4.get()))
                        b = Fraction(str(m1_4.get()))
                        c = Fraction(str(u1_4_1.get()))
                        d = Fraction(str(m1_4_1.get()))
                        e = Fraction(str(u1_4_2.get()))
                        f = Fraction(str(m1_4_2.get()))
                        g = Fraction(str(u1_4_3.get()))
                        h = Fraction(str(m1_4_3.get()))
                        if a == e and b == f and d - c == h - g:
                            d1_4.set("无数解")
                            pass
                        elif a == e and b == f and d - c != h - g:
                            d1_4.set("无解")
                            pass
                        else:
                            l1 = d * e - a * h - c * e + a * g
                            l2 = b * e - a * f
                            y = l1 / l2
                            x = (h - f * y - g) / e
                            fan1 = Fraction(x)
                            fan2 = Fraction(y)
                            dan1 = float(fan1)
                            dan2 = float(fan2)
                            d1_4.set("小数解:x=%f,y=%f;分数解:x=%s,y=%s" % (dan1, dan2, str(fan1), str(fan2)))
                            dan = 0.0
                            fan = Fraction(0, 1)

                    def delall():
                        u1_4.set("")
                        m1_4.set("")
                        u1_4_1.set("")
                        m1_4_1.set("")
                        u1_4_2.set("")
                        m1_4_2.set("")
                        u1_4_3.set("")
                        m1_4_3.set("")
                        d1_4.set("")

                    def __quitequcmathpage__():
                        root2_4.destroy()

                    u1_4 = StringVar()
                    m1_4 = StringVar()
                    u1_4_1 = StringVar()
                    m1_4_1 = StringVar()
                    u1_4_2 = StringVar()
                    m1_4_2 = StringVar()
                    u1_4_3 = StringVar()
                    m1_4_3 = StringVar()
                    d1_4 = StringVar()

                    root2_4 = Toplevel(root2)
                    root2_4.config(bg='white')
                    root2_4.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_解二元一次方程")

                    frame2_4 = Frame(root2_4)
                    frame2_4.config(bg='white')
                    frame2_4.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_4, font=('微软雅黑', 15), text="MSICtor JME 解二元一次方程组", anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_4, font=('微软雅黑', 10), text=" 方程式（关于未知数x,y) : 一式: a*x +b*y + c = d , 二式: e*x + f*y + g = h ")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_4, font=('微软雅黑', 10), text="一式未知数x的系数a的值:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_4, font=('微软雅黑', 10), text="一式未知数y的系数b的值:")
                    lab3.config(bg='white')
                    lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab4 = Label(frame2_4, font=('微软雅黑', 10), text="一式常数c的值:")
                    lab4.config(bg='white')
                    lab4.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_4, font=('微软雅黑', 10), text="一式常数d的值:")
                    lab5.config(bg='white')
                    lab5.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_4, font=('微软雅黑', 10), text="二式未知数x的系数e的值:")
                    lab6.config(bg='white')
                    lab6.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(frame2_4, font=('微软雅黑', 10), text="二式未知数y的系数f的值:")
                    lab7.config(bg='white')
                    lab7.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                    lab8 = Label(frame2_4, font=('微软雅黑', 10), text="二式常数g的值:")
                    lab8.config(bg='white')
                    lab8.grid(row=8, column=0, padx=5, pady=5, sticky=W)

                    lab9 = Label(frame2_4, font=('微软雅黑', 10), text="二式常数h的值:")
                    lab9.config(bg='white')
                    lab9.grid(row=9, column=0, padx=5, pady=5, sticky=W)

                    lab10 = Label(frame2_4, font=('微软雅黑', 10), text="该方程组的解:")
                    lab10.config(bg='white')
                    lab10.grid(row=10, column=0, padx=5, pady=5, sticky=W)

                    lab11 = Label(frame2_4, font=('微软雅黑', 8),
                                 text="*注:1.本计算器用于易于化简但难于计算的方程请把方程组,也可以用于计算两条一次函数交点。\n2.请把方程化到最简再解,化简格式为:ax+by+c=d,ex+fy+g=h。\n3.输入可为分数或小数(格式见小数和分数计算器下方),\n最后会得到小数解和分数解,必须使用英文输入法。\n4.本计算器不支持根式运算。\n5.输入时数据后面不能有空格。")
                    lab11.config(bg='white')
                    lab11.grid(row=11, column=0, padx=5, pady=5, sticky=W)

                    lab12 = Label(root2_4, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab12.config(bg='white')
                    lab12.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_4, textvariable=u1_4)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_4, textvariable=m1_4)
                    ent2.grid(row=3, column=1, sticky='ew', columnspan=1)

                    ent3 = Entry(frame2_4, textvariable=u1_4_1)
                    ent3.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_4, textvariable=m1_4_1)
                    ent4.grid(row=5, column=1, sticky='ew', columnspan=1)

                    ent5 = Entry(frame2_4, textvariable=u1_4_2)
                    ent5.grid(row=6, column=1, sticky='ew', columnspan=1)

                    ent6 = Entry(frame2_4, textvariable=m1_4_2)
                    ent6.grid(row=7, column=1, sticky='ew', columnspan=1)

                    ent7 = Entry(frame2_4, textvariable=u1_4_3)
                    ent7.grid(row=8, column=1, sticky='ew', columnspan=1)

                    ent8 = Entry(frame2_4, textvariable=m1_4_3)
                    ent8.grid(row=9, column=1, sticky='ew', columnspan=1)

                    ent9 = Entry(frame2_4, textvariable=d1_4)
                    ent9.grid(row=10, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_4, text=" 计算 ", command=f_tilequ)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button10 = Button(frame2_4, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=3, column=2, padx=5, pady=5)

                    button12 = Button(frame2_4, text="返回功能页", command=__quitequcmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=4, column=2, padx=5, pady=5)

                    root2_4.update_idletasks()

                    x = (root2_4.winfo_screenwidth() - root2_4.winfo_reqwidth()) / 2
                    y = (root2_4.winfo_screenheight() - root2_4.winfo_reqheight()) / 2
                    root2_4.geometry("+%d+%d" % (x, y))

                    root2_4.mainloop()


                def f_ulequ_page(self):

                    def f_ulequ():
                        a = Fraction(str(u1_3.get()))
                        b = Fraction(str(m1_3.get()))
                        c = Fraction(str(u1_3_1.get()))
                        fan = Fraction((c-b)/a)
                        dan = float(fan)
                        d1_3.set("小数解:x=%f,分数解:x=%s"%(dan,str(fan)))
                        dan = 0.0
                        fan = Fraction(0,1)

                    def delall():
                        u1_3.set("")
                        m1_3.set("")
                        u1_3_1.set("")
                        d1_3.set("")

                    def __quitequcmathpage__():
                        root2_3.destroy()

                    u1_3 = StringVar()
                    m1_3 = StringVar()
                    u1_3_1 = StringVar()
                    d1_3 = StringVar()

                    root2_3 = Toplevel(root2)
                    root2_3.config(bg='white')
                    root2_3.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_解一元一次方程")

                    frame2_3 = Frame(root2_3)
                    frame2_3.config(bg='white')
                    frame2_3.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_3, font=('微软雅黑', 15), text="MSICtor JME 解一元一次方程", anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_3, font=('微软雅黑', 10), text=" 方程式（关于未知数x) : a*x + b = c ")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_3, font=('微软雅黑', 10), text="未知数x的系数a的值:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_3, font=('微软雅黑', 10), text="常数b的值:")
                    lab3.config(bg='white')
                    lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab4 = Label(frame2_3, font=('微软雅黑', 10), text="常数c的值:")
                    lab4.config(bg='white')
                    lab4.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_3, font=('微软雅黑', 10), text="该方程的解:")
                    lab5.config(bg='white')
                    lab5.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_3, font=('微软雅黑', 8),
                                 text="*注:1.本计算器用于易于化简但难于计算的方程。\n2.请把方程化到最简再解,化简格式为:ax+b=c。\n3.输入可为分数或小数(格式见小数和分数计算器下方),\n最后会得到小数解和分数解,必须使用英文输入法。\n4.本计算器不支持根式运算。\n5.输入时数据后面不能有空格。")
                    lab6.config(bg='white')
                    lab6.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_3, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_3, textvariable=u1_3)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_3, textvariable=m1_3)
                    ent2.grid(row=3, column=1, sticky='ew', columnspan=1)

                    ent3 = Entry(frame2_3, textvariable=u1_3_1)
                    ent3.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_3, textvariable=d1_3)
                    ent4.grid(row=5, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_3, text=" 计算 ", command=f_ulequ)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button10 = Button(frame2_3, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=3, column=2, padx=5, pady=5)

                    button12 = Button(frame2_3, text="返回功能页", command=__quitequcmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=4, column=2, padx=5, pady=5)

                    root2_3.update_idletasks()

                    x = (root2_3.winfo_screenwidth() - root2_3.winfo_reqwidth()) / 2
                    y = (root2_3.winfo_screenheight() - root2_3.winfo_reqheight()) / 2
                    root2_3.geometry("+%d+%d" % (x, y))

                    root2_3.mainloop()

            def statistics_page():

                class Statistics:

                    def ari_mean(self):
                        info = str(u1_11.get())
                        lst = info.split(" ")
                        lst = list(map(float, lst))
                        n = "算数平均数:{}"
                        an = n.format(st.mean(lst))
                        d1_11.set(an)

                    def wei_mean(self):
                        info1 = str(u1_11.get())
                        info2 = str(m1_11.get())
                        lst1 = info1.split(" ")
                        lst1 = list(map(float, lst1))
                        lst2 = info2.split(" ")
                        lst2 = list(map(float, lst2))
                        c1 = len(lst1)
                        count = 0
                        meannum = 0.0
                        n = 0.0

                        def sumall(lst1, lst2, c1, count, meannum, n):
                            if count == c1:
                                an = meannum / n
                                d1_11.set("加权平均数:%f" % an)
                            else:
                                meannum += lst1[count] * lst2[count]
                                n += lst2[count]
                                count += 1
                                sumall(lst1, lst2, c1, count, meannum, n)

                        sumall(lst1, lst2, c1, count, meannum, n)

                    def themedian(self):
                        info = str(u1_11.get())
                        lst = info.split(" ")
                        lst = list(map(float, lst))
                        n = "中位数:{}"
                        an = n.format(np.median(lst))
                        d1_11.set(an)

                    def themode(self):
                        info = str(u1_11.get())
                        lst = info.split(" ")
                        lst = list(map(float, lst))
                        n = "众数:{}"
                        an = n.format(st.mode(lst))
                        d1_11.set(an)

                    def variance(self):
                        info = str(u1_11.get())
                        lst = info.split(" ")
                        lst = list(map(float, lst))
                        n = "方差:{}"
                        an = n.format(np.var(lst))
                        d1_11.set(an)

                    def std(self):
                        info = str(u1_11.get())
                        lst = info.split(" ")
                        lst = list(map(float, lst))
                        n = "标准差:{}"
                        an = n.format(np.std(lst))
                        d1_11.set(an)

                    def foandla(self):
                        info = str(u1_11.get())
                        lst = info.split(" ")
                        lst.sort()
                        lst = list(map(float, lst))
                        n = "极差:{}"
                        an = n.format(np.ptp(lst))
                        d1_11.set(str(an))

                    def thedev(self):
                        info = str(u1_11.get())
                        lst = info.split(" ")
                        lst = list(map(float, lst))
                        count = 0
                        n = len(lst)
                        dev = 0.0
                        u = np.mean(lst)
                        def sumall(n, count, dev, u):
                            if count == n:
                                d1_11.set("离差:%f" % dev)
                            else:
                                g = (float(lst[count]) - u) ** 2
                                dev += g ** (1 / 2)
                                count += 1
                                sumall(n, count, dev, u)

                        sumall(n, count, dev, u)

                    def ssdev(self):
                        info = str(u1_11.get())
                        lst = info.split(" ")
                        lst = list(map(float, lst))
                        count = 0
                        n = len(lst)
                        dev = 0.0
                        u = np.mean(lst)
                        def sumall(n, count, dev, u):
                            if count == n:
                                d1_11.set("离差平方和:%f" % dev)
                            else:
                                g = (float(lst[count]) - u) ** 2
                                dev += g
                                count += 1
                                sumall(n, count, dev, u)

                        sumall(n, count, dev, u)


                def delall():
                    u1_11.set("")
                    d1_11.set("")

                def __quitestamathpage__():
                    root2_11.destroy()

                u1_11 = StringVar()
                m1_11 = StringVar()
                d1_11 = StringVar()
                stati = Statistics()

                root2_11 = Toplevel(root2)
                root2_11.config(bg='white')
                root2_11.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_数据统计计算器")

                frame2_11 = Frame(root2_11)
                frame2_11.config(bg='white')
                frame2_11.pack(side=TOP, fill=Y, anchor='center')

                lab1 = Label(frame2_11, font=('微软雅黑', 15), text="MSICtor JME 数据统计计算器", anchor='center')
                lab1.config(fg='blue', bg='white')
                lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                lab8 = Label(frame2_11, font=('微软雅黑', 10), text=" 数据组(输入格式见“*注”) : x1,x2,x3,...,xn ")
                lab8.config(bg='white')
                lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                lab2 = Label(frame2_11, font=('微软雅黑', 10), text="输入的数据组:")
                lab2.config(bg='white')
                lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                lab3 = Label(frame2_11, font=('微软雅黑', 10), text="权重:")
                lab3.config(bg='white')
                lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                lab4 = Label(frame2_11, font=('微软雅黑', 10), text="计算结果:")
                lab4.config(bg='white')
                lab4.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                lab5 = Label(frame2_11, font=('微软雅黑', 10), text="")
                lab5.config(bg='white')
                lab5.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                lab6 = Label(frame2_11, font=('微软雅黑', 8),
                             text="*注:1.输入数据组和权重时,每个数据之间用空格隔开。\n2.本计算器仅支持小数数组。\n3.求解众数时,如果没有众数,则会输出数据组里的第一个数据。\n4.本计算器不支持根式运算。\n5.输入时数据组和权重最后一个数据后面不能有空格,必须使用英文输入法。")
                lab6.config(bg='white')
                lab6.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                lab7 = Label(root2_11, font=('微软雅黑', 7),
                             text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                lab7.config(bg='white')
                lab7.pack(anchor='se', padx=5, pady=5)

                ent1 = Entry(frame2_11, textvariable=u1_11)
                ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                ent2 = Entry(frame2_11, textvariable=m1_11)
                ent2.grid(row=3, column=1, sticky='ew', columnspan=1)

                ent4 = Entry(frame2_11, textvariable=d1_11)
                ent4.grid(row=4, column=1, sticky='ew', columnspan=1)

                button1 = Button(frame2_11, text="算术平均数", command=stati.ari_mean)
                button1.config(bg='white')
                button1.grid(row=2, column=2, padx=5, pady=5)

                button2 = Button(frame2_11, text="加权平均数", command=stati.wei_mean)
                button2.config(bg='white')
                button2.grid(row=3, column=2, padx=5, pady=5)

                button3 = Button(frame2_11, text=" 中位数 ", command=stati.themedian)
                button3.config(bg='white')
                button3.grid(row=4, column=2, padx=5, pady=5)

                button4 = Button(frame2_11, text="  众数  ", command=stati.themode)
                button4.config(bg='white')
                button4.grid(row=5, column=2, padx=5, pady=5)

                button5 = Button(frame2_11, text="  方差  ", command=stati.variance)
                button5.config(bg='white')
                button5.grid(row=6, column=2, padx=5, pady=5)

                button6 = Button(frame2_11, text=" 标准差 ", command=stati.std)
                button6.config(bg='white')
                button6.grid(row=2, column=3, padx=5, pady=5)

                button7 = Button(frame2_11, text="  离差  ", command=stati.thedev)
                button7.config(bg='white')
                button7.grid(row=3, column=3, padx=5, pady=5)

                button8 = Button(frame2_11, text="离差平方和", command=stati.ssdev)
                button8.config(bg='white')
                button8.grid(row=4, column=3, padx=5, pady=5)

                button10 = Button(frame2_11, text="   C   ", command=delall)
                button10.config(bg='white')
                button10.grid(row=5, column=3, padx=5, pady=5)

                button12 = Button(frame2_11, text="返回功能页", command=__quitestamathpage__)
                button12.config(bg='white')
                button12.grid(row=6, column=3, padx=5, pady=5)

                root2_11.update_idletasks()

                x = (root2_11.winfo_screenwidth() - root2_11.winfo_reqwidth()) / 2
                y = (root2_11.winfo_screenheight() - root2_11.winfo_reqheight()) / 2
                root2_11.geometry("+%d+%d" % (x, y))

                root2_11.mainloop()

            def inequality_page():

                def any_oneoneteam():
                    x = sy.Symbol('x')
                    expr1 = str(u1_6.get())
                    expr2 = str(m1_6.get())
                    r1 = sy.solve([expr1, expr2], [x])
                    r1 = str(r1)
                    if r1 == "False":
                        d1_6.set("无解")
                    else:
                        d1_6.set(r1)

                def any_oneone():
                    x = sy.Symbol('x')
                    expr1 = str(u1_6.get())
                    r1 = sy.solve(expr1, [x])
                    r1 = str(r1)
                    d1_6.set(r1)

                def delall():
                    u1_6.set("")
                    m1_6.set("")
                    d1_6.set("")

                def __quitinequcmathpage__():
                    root2_6.destroy()

                u1_6 = StringVar()
                d1_6 = StringVar()
                m1_6 = StringVar()

                root2_6 = Toplevel(root2)
                root2_6.config(bg='white')
                root2_6.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_解一元一次不等式/不等式组")

                frame2_6 = Frame(root2_6)
                frame2_6.config(bg='white')
                frame2_6.pack(side=TOP, fill=Y, anchor='center')

                lab1 = Label(frame2_6, font=('微软雅黑', 15), text="MSICtor JME 解一元一次不等式/不等式组", anchor='center')
                lab1.config(fg='blue', bg='white')
                lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                lab8 = Label(frame2_6, font=('微软雅黑', 10),
                             text=" 不等式（关于未知数x) : 自定义(输入时注意事项见“*注”) ")
                lab8.config(bg='white')
                lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                lab2 = Label(frame2_6, font=('微软雅黑', 10), text="一式:")
                lab2.config(bg='white')
                lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                lab22 = Label(frame2_6, font=('微软雅黑', 10), text="")
                lab22.config(bg='white')
                lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                lab3 = Label(frame2_6, font=('微软雅黑', 10), text="二式:")
                lab3.config(bg='white')
                lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                lab33 = Label(frame2_6, font=('微软雅黑', 10), text="")
                lab33.config(bg='white')
                lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                lab5 = Label(frame2_6, font=('微软雅黑', 10), text="该不等式/不等式组的解集:")
                lab5.config(bg='white')
                lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                lab6 = Label(frame2_6, font=('微软雅黑', 8),
                             text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:(分子/分母)。\n2.输入时按顺序输入不等式,必须使用英文输入法。\n3.每个不等式的不等号方向必须相同。\n4.输入未知数系数时,未知数和系数之间用乘或除号连接。")
                lab6.config(bg='white')
                lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                lab7 = Label(root2_6, font=('微软雅黑', 7),
                             text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                lab7.config(bg='white')
                lab7.pack(anchor='se', padx=5, pady=5)

                ent1 = Entry(frame2_6, textvariable=u1_6)
                ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                ent2 = Entry(frame2_6, textvariable=m1_6)
                ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                ent4 = Entry(frame2_6, textvariable=d1_6)
                ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                button1 = Button(frame2_6, text="一元一次不等式", command=any_oneone)
                button1.config(bg='white')
                button1.grid(row=2, column=2, padx=5, pady=5)

                button2 = Button(frame2_6, text="一元一次不等式组", command=any_oneoneteam)
                button2.config(bg='white')
                button2.grid(row=3, column=2, padx=5, pady=5)

                button10 = Button(frame2_6, text="   C   ", command=delall)
                button10.config(bg='white')
                button10.grid(row=4, column=2, padx=5, pady=5)

                button12 = Button(frame2_6, text="返回功能页", command=__quitinequcmathpage__)
                button12.config(bg='white')
                button12.grid(row=5, column=2, padx=5, pady=5)

                root2_6.update_idletasks()

                x = (root2_6.winfo_screenwidth() - root2_6.winfo_reqwidth()) / 2
                y = (root2_6.winfo_screenheight() - root2_6.winfo_reqheight()) / 2
                root2_6.geometry("+%d+%d" % (x, y))

                root2_6.mainloop()

            class Function_pages:

                def aepf_page(self):

                    def aepf():
                        info1 = str(u1_7.get())
                        info2 = str(m1_7.get())
                        info1 = info1.replace("(", "")
                        info2 = info2.replace("(", "")
                        info1 = info1.replace(")", "")
                        info2 = info2.replace(")", "")
                        lst1 = info1.split(",")
                        lst2 = info2.split(",")
                        x1 = lst1[0]
                        x2 = lst2[0]
                        y1 = lst1[1]
                        y2 = lst2[1]
                        k = sy.Symbol('k')
                        b = sy.Symbol('b')
                        solvestr1 = (y1 + "=" + "k*" + x1 + "+b")
                        solvestr2 = (y2 + "=" + "k*" + x2 + "+b")
                        solvestr1 = solvestr1.replace("=", "-(") + ")"
                        solvestr2 = solvestr2.replace("=", "-(") + ")"
                        r1 = sy.solve([solvestr1, solvestr2], [k, b])
                        dct = dict(r1)
                        l = []
                        for v in dct.values():
                            l.append(v)
                        n1 = str(l[0])
                        n2 = str(l[1])
                        p1 = ""
                        if n2 == "0":
                            p1 = "y="+n1+"*x"
                        else:
                            p1 = "y="+n1+"*x+("+n2+")"
                        d1_7.set(p1)

                    def delall():
                        u1_7.set("")
                        m1_7.set("")
                        d1_7.set("")

                    def __quitaepfmathpage__():
                        root2_7.destroy()

                    u1_7 = StringVar()
                    d1_7 = StringVar()
                    m1_7 = StringVar()

                    root2_7 = Toplevel(root2)
                    root2_7.config(bg='white')
                    root2_7.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_求一次函数解析式")

                    frame2_7 = Frame(root2_7)
                    frame2_7.config(bg='white')
                    frame2_7.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_7, font=('微软雅黑', 15), text="MSICtor JME 求一次函数解析式",
                                 anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_7, font=('微软雅黑', 10),
                                 text=" 一次函数直线AB（y是关于x的函数) : \ny=斜率k*x+截距b(k!=0)(输入时注意事项见“*注”) ")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_7, font=('微软雅黑', 10), text="点A:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab22 = Label(frame2_7, font=('微软雅黑', 10), text="")
                    lab22.config(bg='white')
                    lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_7, font=('微软雅黑', 10), text="点B:")
                    lab3.config(bg='white')
                    lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab33 = Label(frame2_7, font=('微软雅黑', 10), text="")
                    lab33.config(bg='white')
                    lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_7, font=('微软雅黑', 10), text="该一次函数的解析式:")
                    lab5.config(bg='white')
                    lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_7, font=('微软雅黑', 8),
                                 text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:分子/分母。\n2.输入点的格式为:(横坐标,纵坐标),必须使用英文输入法。\n3.每个字符之间不能有空格。")
                    lab6.config(bg='white')
                    lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_7, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_7, textvariable=u1_7)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_7, textvariable=m1_7)
                    ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_7, textvariable=d1_7)
                    ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_7, text="  计算  ", command=aepf)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button10 = Button(frame2_7, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=3, column=2, padx=5, pady=5)

                    button12 = Button(frame2_7, text="返回功能页", command=__quitaepfmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=4, column=2, padx=5, pady=5)

                    root2_7.update_idletasks()

                    x = (root2_7.winfo_screenwidth() - root2_7.winfo_reqwidth()) / 2
                    y = (root2_7.winfo_screenheight() - root2_7.winfo_reqheight()) / 2
                    root2_7.geometry("+%d+%d" % (x, y))

                    root2_7.mainloop()

                def cppf_page(self):

                    def xcppf():
                        info1 = str(u1_8.get())
                        info2 = str(m1_8.get())
                        info1 = info1.replace("x", info2)
                        info1 = info1.replace("=", "-(") + ")"
                        y = sy.Symbol('y')
                        r1 = sy.solve(info1, [y])
                        r1 = list(r1)
                        t = str(r1[0])
                        an = "(" + info2 + "," + t + ")"
                        d1_8.set(an)

                    def ycppf():
                        info1 = str(u1_8.get())
                        info2 = str(m1_8.get())
                        info1 = info1.replace("y", info2)
                        info1 = info1.replace("=", "-(") + ")"
                        x = sy.Symbol('x')
                        r1 = sy.solve(info1, [x])
                        r1 = list(r1)
                        t = str(r1[0])
                        an = "(" + t + "," + info2 + ")"
                        d1_8.set(an)

                    def delall():
                        u1_8.set("")
                        m1_8.set("")
                        d1_8.set("")

                    def __quitcppfmathpage__():
                        root2_8.destroy()

                    u1_8 = StringVar()
                    d1_8 = StringVar()
                    m1_8 = StringVar()

                    root2_8 = Toplevel(root2)
                    root2_8.config(bg='white')
                    root2_8.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_求一次函数上点的坐标")

                    frame2_8 = Frame(root2_8)
                    frame2_8.config(bg='white')
                    frame2_8.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_8, font=('微软雅黑', 15), text="MSICtor JME 求一次函数上点的坐标",
                                 anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_8, font=('微软雅黑', 10),
                                 text=" 一次函数直线AB（y是关于x的函数) : \ny=斜率k*x+截距b(k!=0)(输入时注意事项见“*注”) ")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_8, font=('微软雅黑', 10), text="这个一次函数的解析式:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab22 = Label(frame2_8, font=('微软雅黑', 10), text="")
                    lab22.config(bg='white')
                    lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_8, font=('微软雅黑', 10), text="这个点的横坐标/纵坐标:")
                    lab3.config(bg='white')
                    lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab33 = Label(frame2_8, font=('微软雅黑', 10), text="")
                    lab33.config(bg='white')
                    lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_8, font=('微软雅黑', 10), text="计算结果,这个点的坐标:")
                    lab5.config(bg='white')
                    lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_8, font=('微软雅黑', 8),
                                 text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:(分子/分母)。\n2.必须使用英文输入法。")
                    lab6.config(bg='white')
                    lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_8, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_8, textvariable=u1_8)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_8, textvariable=m1_8)
                    ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_8, textvariable=d1_8)
                    ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_8, text="输入横坐标", command=xcppf)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button2 = Button(frame2_8, text="输入纵坐标", command=ycppf)
                    button2.config(bg='white')
                    button2.grid(row=3, column=2, padx=5, pady=5)

                    button10 = Button(frame2_8, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=4, column=2, padx=5, pady=5)

                    button12 = Button(frame2_8, text="返回功能页", command=__quitcppfmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=5, column=2, padx=5, pady=5)

                    root2_8.update_idletasks()

                    x = (root2_8.winfo_screenwidth() - root2_8.winfo_reqwidth()) / 2
                    y = (root2_8.winfo_screenheight() - root2_8.winfo_reqheight()) / 2
                    root2_8.geometry("+%d+%d" % (x, y))

                    root2_8.mainloop()

                def tppf_page(self):

                    def tppf():
                        info1 = str(u1_9.get())
                        info2 = str(m1_9.get())
                        x = sy.Symbol('x')
                        y = sy.Symbol('y')
                        expr1 = info1.replace("=", "-(") + ")"
                        expr2 = info2.replace("=", "-(") + ")"
                        r1 = sy.solve([expr1, expr2], [x, y])
                        if r1 == []:
                            d1_9.set("两直线平行")
                        else:
                            r1 = dict(r1)
                            l = []
                            for v in r1.values():
                                l.append(v)
                            n1 = str(l[0])
                            n2 = str(l[1])
                            an = "(" + n1 + "," + n2 + ")"
                            d1_9.set(an)

                    def delall():
                        u1_9.set("")
                        m1_9.set("")
                        d1_9.set("")

                    def __quittppfmathpage__():
                        root2_9.destroy()

                    u1_9 = StringVar()
                    d1_9 = StringVar()
                    m1_9 = StringVar()

                    root2_9 = Toplevel(root2)
                    root2_9.config(bg='white')
                    root2_9.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_求一次函数交点")

                    frame2_9 = Frame(root2_9)
                    frame2_9.config(bg='white')
                    frame2_9.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_9, font=('微软雅黑', 15), text="MSICtor JME 求一次函数交点坐标",
                                 anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_9, font=('微软雅黑', 10),
                                 text=" 一次函数l1 : y1=斜率k1*x+截距b1(k!=0) , 直线l2 : 自定义 \n (输入时注意事项见“*注”) ")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_9, font=('微软雅黑', 10), text="一次函数l1解析式:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab22 = Label(frame2_9, font=('微软雅黑', 10), text="")
                    lab22.config(bg='white')
                    lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_9, font=('微软雅黑', 10), text="直线l2解析式:")
                    lab3.config(bg='white')
                    lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab33 = Label(frame2_9, font=('微软雅黑', 10), text="")
                    lab33.config(bg='white')
                    lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_9, font=('微软雅黑', 10), text="计算结果,交点坐标:")
                    lab5.config(bg='white')
                    lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_9, font=('微软雅黑', 8),
                                 text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:(分子/分母)。\n2.必须使用英文输入法。\n3.直线l2可为函数,也可为直线。")
                    lab6.config(bg='white')
                    lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_9, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_9, textvariable=u1_9)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_9, textvariable=m1_9)
                    ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_9, textvariable=d1_9)
                    ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_9, text="  计算  ", command=tppf)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button10 = Button(frame2_9, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=3, column=2, padx=5, pady=5)

                    button12 = Button(frame2_9, text="返回功能页", command=__quittppfmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=4, column=2, padx=5, pady=5)

                    root2_9.update_idletasks()

                    x = (root2_9.winfo_screenwidth() - root2_9.winfo_reqwidth()) / 2
                    y = (root2_9.winfo_screenheight() - root2_9.winfo_reqheight()) / 2
                    root2_9.geometry("+%d+%d" % (x, y))

                    root2_9.mainloop()

                def tvpf_page(self):

                    def tvpf():
                        info1 = str(u1_10.get())
                        info2 = str(m1_10.get())
                        info2 = info2.replace("(", "")
                        info2 = info2.replace(")", "")
                        lst = info2.split(",")
                        k = str(info1)
                        b = sy.Symbol('b')
                        x = str(lst[0])
                        y = str(lst[1])
                        solvestr = y + "=" + "-" + k + "*" + x + "+" + "b"
                        solvestr = solvestr.replace("=","-(") + ")"
                        an = sy.solve(solvestr,[b])
                        an = str(an)
                        an = an.replace("[","")
                        an = an.replace("]", "")
                        e = "y" + "=" + "-" + k + "*x+(" + an + ")"
                        d1_10.set(e)

                    def delall():
                        u1_10.set("")
                        m1_10.set("")
                        d1_10.set("")

                    def __quittvpfmathpage__():
                        root2_10.destroy()

                    u1_10 = StringVar()
                    d1_10 = StringVar()
                    m1_10 = StringVar()

                    root2_10 = Toplevel(root2)
                    root2_10.config(bg='white')
                    root2_10.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_求相垂直一次函数的解析式")

                    frame2_10 = Frame(root2_10)
                    frame2_10.config(bg='white')
                    frame2_10.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_10, font=('微软雅黑', 15), text="MSICtor JME 求相垂直一次函数的解析式",
                                 anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_10, font=('微软雅黑', 10),
                                 text=" 一次函数l1 : y1=斜率k1*x+截距b1(k!=0) , \n 一次函数l2 : y2=-斜率k1*x+截距b2(k!=0) \n (输入时注意事项见“*注”) ")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_10, font=('微软雅黑', 10), text="一次函数l1的斜率k1:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab22 = Label(frame2_10, font=('微软雅黑', 10), text="")
                    lab22.config(bg='white')
                    lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_10, font=('微软雅黑', 10), text="一次函数l2所过点的坐标:")
                    lab3.config(bg='white')
                    lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab33 = Label(frame2_10, font=('微软雅黑', 10), text="")
                    lab33.config(bg='white')
                    lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_10, font=('微软雅黑', 10), text="一次函数l2的解析式:")
                    lab5.config(bg='white')
                    lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_10, font=('微软雅黑', 8),
                                 text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:(分子/分母)。\n2.必须使用英文输入法。\n3.输入点的坐标的格式为(横坐标,纵坐标)。")
                    lab6.config(bg='white')
                    lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_10, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_10, textvariable=u1_10)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_10, textvariable=m1_10)
                    ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_10, textvariable=d1_10)
                    ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_10, text="  计算  ", command=tvpf)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button10 = Button(frame2_10, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=3, column=2, padx=5, pady=5)

                    button12 = Button(frame2_10, text="返回功能页", command=__quittvpfmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=4, column=2, padx=5, pady=5)

                    root2_10.update_idletasks()

                    x = (root2_10.winfo_screenwidth() - root2_10.winfo_reqwidth()) / 2
                    y = (root2_10.winfo_screenheight() - root2_10.winfo_reqheight()) / 2
                    root2_10.geometry("+%d+%d" % (x, y))

                    root2_10.mainloop()

            class Geometry_pages:

                def tpd_page(self):

                    def tpd():
                        info1 = str(u1_12.get())
                        info2 = str(m1_12.get())
                        info1 = info1.replace("(", "")
                        info2 = info2.replace("(", "")
                        info1 = info1.replace(")", "")
                        info2 = info2.replace(")", "")
                        lst1 = info1.split(",")
                        lst2 = info2.split(",")
                        x1 = Fraction(str(lst1[0]))
                        x2 = Fraction(str(lst2[0]))
                        y1 = Fraction(str(lst1[1]))
                        y2 = Fraction(str(lst2[1]))
                        an1 = ( x1 - x2 ) ** 2 +( y1 - y2 ) ** 2
                        an2 = sqrt(an1)
                        anw = ""
                        if an2%1 != 0 :
                            anw = "sqrt(" + str(an1) + ")"
                        else:
                            anw = an2
                        d1_12.set(anw)

                    def delall():
                        u1_12.set("")
                        m1_12.set("")
                        d1_12.set("")

                    def __quittpdmathpage__():
                        root2_12.destroy()

                    u1_12 = StringVar()
                    d1_12 = StringVar()
                    m1_12 = StringVar()

                    root2_12 = Toplevel(root2)
                    root2_12.config(bg='white')
                    root2_12.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_两点间距离公式")

                    frame2_12 = Frame(root2_12)
                    frame2_12.config(bg='white')
                    frame2_12.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_12, font=('微软雅黑', 15), text="MSICtor JME 两点间距离公式",
                                 anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_12, font=('微软雅黑', 10),
                                 text=" 点A : (a,b) ; 点B : (m,n) \n 两点间距离公式 : sqrt[(x1-x2)**2+(y1-y2)**2]")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_12, font=('微软雅黑', 10), text="点A坐标:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab22 = Label(frame2_12, font=('微软雅黑', 10), text="")
                    lab22.config(bg='white')
                    lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_12, font=('微软雅黑', 10), text="点B坐标:")
                    lab3.config(bg='white')
                    lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab33 = Label(frame2_12, font=('微软雅黑', 10), text="")
                    lab33.config(bg='white')
                    lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_12, font=('微软雅黑', 10), text="两点间距离:")
                    lab5.config(bg='white')
                    lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_12, font=('微软雅黑', 8),
                                 text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:分子/分母。\n2.必须使用英文输入法。\n3.输入点的坐标的格式为(横坐标,纵坐标)。\n4.输出里的sqrt意为平方根,在此用来表示根号。")
                    lab6.config(bg='white')
                    lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_12, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_12, textvariable=u1_12)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_12, textvariable=m1_12)
                    ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_12, textvariable=d1_12)
                    ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_12, text="  计算  ", command=tpd)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button10 = Button(frame2_12, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=3, column=2, padx=5, pady=5)

                    button12 = Button(frame2_12, text="返回功能页", command=__quittpdmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=4, column=2, padx=5, pady=5)

                    root2_12.update_idletasks()

                    x = (root2_12.winfo_screenwidth() - root2_12.winfo_reqwidth()) / 2
                    y = (root2_12.winfo_screenheight() - root2_12.winfo_reqheight()) / 2
                    root2_12.geometry("+%d+%d" % (x, y))

                    root2_12.mainloop()

                def gryfun_page(self):

                    class Gryfun:

                        def __init__(self, fan):
                            self.fan = fan

                        def thecos(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = cos(f)
                            d1_14.set(str(self.fan))

                        def thesin(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = sin(f)
                            d1_14.set(str(self.fan))

                        def thetan(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = tan(f)
                            d1_14.set(str(self.fan))

                        def theacos(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = acos(f)
                            d1_14.set(str(self.fan))

                        def theasin(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = asin(f)
                            d1_14.set(str(self.fan))

                        def theatan(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = atan(f)
                            d1_14.set(str(self.fan))

                        def theacosh(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = acos(f)
                            d1_14.set(str(self.fan))

                        def theasinh(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = asin(f)
                            d1_14.set(str(self.fan))
                        def theatanh(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = atan(f)
                            d1_14.set(str(self.fan))

                        def thecosh(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = acos(f)
                            d1_14.set(str(self.fan))

                        def thesinh(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = asin(f)
                            d1_14.set(str(self.fan))

                        def thetanh(self):
                            f = Fraction(str(u1_14.get()))
                            self.fan = atan(f)
                            d1_14.set(str(self.fan))

                        def delall(self):
                            u1_14.set("")
                            d1_14.set("")
                            self.fan = Fraction(0,1)

                    def __quitgfmathpage__():
                        root2_14.destroy()

                    u1_14 = StringVar()
                    d1_14 = StringVar()
                    gry = Gryfun(Fraction(0,1))

                    root2_14 = Toplevel(root2)
                    root2_14.config(bg='white')
                    root2_14.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_几何函数计算器")

                    frame2_14 = Frame(root2_14)
                    frame2_14.config(bg='white')
                    frame2_14.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_14, font=('微软雅黑', 15), text="MSICtor JME 几何函数计算器",
                                 anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_14, font=('微软雅黑', 10), text="弧度:")
                    lab2.config(bg='white')
                    lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)

                    lab22 = Label(frame2_14, font=('微软雅黑', 10), text="")
                    lab22.config(bg='white')
                    lab22.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_14, font=('微软雅黑', 10), text="计算结果:")
                    lab3.config(bg='white')
                    lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab33 = Label(frame2_14, font=('微软雅黑', 10), text="")
                    lab33.config(bg='white')
                    lab33.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_14, font=('微软雅黑', 8),
                                 text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:分子/分母。\n2.必须使用英文输入法。\n3.在使用反三角函数时输入的值应为-1到1之间。\n4.输出的值全部为小数。")
                    lab6.config(bg='white')
                    lab6.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_14, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_14, textvariable=u1_14)
                    ent1.grid(row=1, column=1, sticky='ew', columnspan=1)


                    ent4 = Entry(frame2_14, textvariable=d1_14)
                    ent4.grid(row=3, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_14, text="  正弦  ", command=gry.thesin)
                    button1.config(bg='white')
                    button1.grid(row=1, column=2, padx=5, pady=5)

                    button2 = Button(frame2_14, text="  余弦  ", command=gry.thecos)
                    button2.config(bg='white')
                    button2.grid(row=2, column=2, padx=5, pady=5)

                    button3 = Button(frame2_14, text="  正切  ", command=gry.thetan)
                    button3.config(bg='white')
                    button3.grid(row=3, column=2, padx=5, pady=5)

                    button4 = Button(frame2_14, text=" 反正弦 ", command=gry.theasin)
                    button4.config(bg='white')
                    button4.grid(row=4, column=2, padx=5, pady=5)

                    button5 = Button(frame2_14, text=" 反余弦 ", command=gry.theacos)
                    button5.config(bg='white')
                    button5.grid(row=5, column=2, padx=5, pady=5)

                    button6 = Button(frame2_14, text=" 反正切 ", command=gry.theatan)
                    button6.config(bg='white')
                    button6.grid(row=1, column=3, padx=5, pady=5)

                    button7 = Button(frame2_14, text="双曲正弦", command=gry.thesinh)
                    button7.config(bg='white')
                    button7.grid(row=2, column=3, padx=5, pady=5)

                    button8 = Button(frame2_14, text="双曲余弦", command=gry.thecosh)
                    button8.config(bg='white')
                    button8.grid(row=3, column=3, padx=5, pady=5)

                    button9 = Button(frame2_14, text="双曲正切", command=gry.thetanh)
                    button9.config(bg='white')
                    button9.grid(row=4, column=3, padx=5, pady=5)

                    button11 = Button(frame2_14, text="反双曲正弦", command=gry.theasinh)
                    button11.config(bg='white')
                    button11.grid(row=5, column=3, padx=5, pady=5)

                    button13 = Button(frame2_14, text="反双曲余弦", command=gry.theacosh)
                    button13.config(bg='white')
                    button13.grid(row=1, column=4, padx=5, pady=5)

                    button14 = Button(frame2_14, text="反双曲正切", command=gry.theatanh)
                    button14.config(bg='white')
                    button14.grid(row=2, column=4, padx=5, pady=5)

                    button10 = Button(frame2_14, text="   C   ", command=gry.delall)
                    button10.config(bg='white')
                    button10.grid(row=3, column=4, padx=5, pady=5)

                    button12 = Button(frame2_14, text="返回功能页", command=__quitgfmathpage__)
                    button12.config(bg='white')
                    button12.grid(row=4, column=4, padx=5, pady=5)

                    root2_14.update_idletasks()

                    x = (root2_14.winfo_screenwidth() - root2_14.winfo_reqwidth()) / 2
                    y = (root2_14.winfo_screenheight() - root2_14.winfo_reqheight()) / 2
                    root2_14.geometry("+%d+%d" % (x, y))

                    root2_14.mainloop()

                def mpmi_page(self):

                    def mpmi():
                        info1 = str(u1_13.get())
                        info2 = str(m1_13.get())
                        info1 = info1.replace("(", "")
                        info2 = info2.replace("(", "")
                        info1 = info1.replace(")", "")
                        info2 = info2.replace(")", "")
                        lst1 = info1.split(",")
                        lst2 = info2.split(",")
                        x1 = Fraction(str(lst1[0]))
                        x2 = Fraction(str(lst2[0]))
                        y1 = Fraction(str(lst1[1]))
                        y2 = Fraction(str(lst2[1]))
                        an = [str( ( x1 + x2 ) / 2 ),str( ( y1 + y2 ) / 2 )]
                        anw = "(" + an[0] + "," + an[1] + ")"
                        d1_13.set(anw)
                    def delall():
                        u1_13.set("")
                        m1_13.set("")
                        d1_13.set("")

                    def __quitmpmimathpage__():
                        root2_13.destroy()

                    u1_13 = StringVar()
                    d1_13 = StringVar()
                    m1_13 = StringVar()

                    root2_13 = Toplevel(root2)
                    root2_13.config(bg='white')
                    root2_13.title("MSICtorJME多功能计算器(初中教育版)_数学计算器_中点坐标公式")

                    frame2_13 = Frame(root2_13)
                    frame2_13.config(bg='white')
                    frame2_13.pack(side=TOP, fill=Y, anchor='center')

                    lab1 = Label(frame2_13, font=('微软雅黑', 15), text="MSICtor JME 中点坐标公式",
                                 anchor='center')
                    lab1.config(fg='blue', bg='white')
                    lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab8 = Label(frame2_13, font=('微软雅黑', 10),
                                 text=" 点A : (a,b) ; 点B : (m,n) \n 中点坐标公式 : ((x1+x2)/2,(y1+y2)/2)")
                    lab8.config(bg='white')
                    lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                    lab2 = Label(frame2_13, font=('微软雅黑', 10), text="点A坐标:")
                    lab2.config(bg='white')
                    lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab22 = Label(frame2_13, font=('微软雅黑', 10), text="")
                    lab22.config(bg='white')
                    lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab3 = Label(frame2_13, font=('微软雅黑', 10), text="点B坐标:")
                    lab3.config(bg='white')
                    lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab33 = Label(frame2_13, font=('微软雅黑', 10), text="")
                    lab33.config(bg='white')
                    lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    lab5 = Label(frame2_13, font=('微软雅黑', 10), text="中点坐标:")
                    lab5.config(bg='white')
                    lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                    lab6 = Label(frame2_13, font=('微软雅黑', 8),
                                 text="*注:1.本计算器支持小数,分数运算;输入分数时请按照此格式:分子/分母。\n2.必须使用英文输入法。\n3.输入点的坐标的格式为(横坐标,纵坐标)。")
                    lab6.config(bg='white')
                    lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                    lab7 = Label(root2_13, font=('微软雅黑', 7),
                                 text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab7.config(bg='white')
                    lab7.pack(anchor='se', padx=5, pady=5)

                    ent1 = Entry(frame2_13, textvariable=u1_13)
                    ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                    ent2 = Entry(frame2_13, textvariable=m1_13)
                    ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                    ent4 = Entry(frame2_13, textvariable=d1_13)
                    ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                    button1 = Button(frame2_13, text="  计算  ", command=mpmi)
                    button1.config(bg='white')
                    button1.grid(row=2, column=2, padx=5, pady=5)

                    button10 = Button(frame2_13, text="   C   ", command=delall)
                    button10.config(bg='white')
                    button10.grid(row=3, column=2, padx=5, pady=5)

                    button12 = Button(frame2_13, text="返回功能页", command=__quitmpmimathpage__)
                    button12.config(bg='white')
                    button12.grid(row=4, column=2, padx=5, pady=5)

                    root2_13.update_idletasks()

                    x = (root2_13.winfo_screenwidth() - root2_13.winfo_reqwidth()) / 2
                    y = (root2_13.winfo_screenheight() - root2_13.winfo_reqheight()) / 2
                    root2_13.geometry("+%d+%d" % (x, y))

                    root2_13.mainloop()

                

            def __quitmathindexpage__():
                info = tm.askquestion('提示','你确定要返回首页吗?\n这会关掉数学计算器所有已经打开的功能页!')
                if info == 'yes':
                    root2.destroy()
                else:
                    pass

            equ_pages = Equmath_pages()
            fun_pages = Function_pages()
            gry_pages = Geometry_pages()

            lab2_0 = Label(frame2, font=('微软雅黑', 15), text="MSICtor JME 数学计算器", anchor='center')
            lab2_0.config(fg='blue', bg='white')
            lab2_0.grid(row=0, columnspan=2, padx=5, pady=5, sticky="n")

            lab2_1 = Label(frame2, font=('微软雅黑', 10), text="四则运算:")
            lab2_1.config(bg='white')
            lab2_1.grid(row=1, column=0, padx=5, pady=5, sticky=W)

            lab2_2 = Label(frame2, font=('微软雅黑', 10), text="方程和方程组:")
            lab2_2.config(bg='white')
            lab2_2.grid(row=3, column=0, padx=5, pady=5, sticky=W)

            lab2_3 = Label(frame2, font=('微软雅黑', 10), text="函数:")
            lab2_3.config(bg='white')
            lab2_3.grid(row=7, column=0, padx=5, pady=5, sticky=W)

            lab2_4 = Label(frame2, font=('微软雅黑', 10), text="数据统计:")
            lab2_4.config(bg='white')
            lab2_4.grid(row=9, column=0, padx=5, pady=5, sticky=W)

            lab2_5 = Label(frame2, font=('微软雅黑', 10), text="几何:")
            lab2_5.config(bg='white')
            lab2_5.grid(row=11, column=0, padx=5, pady=5, sticky=W)

            lab2_6 = Label(frame2, font=('微软雅黑', 10), text="不等式和不等式组:")
            lab2_6.config(bg='white')
            lab2_6.grid(row=5, column=0, padx=5, pady=5, sticky=W)

            button2_0 = Button(frame2, text="小数计算器", command=decmath_page)
            button2_0.config(bg='white')
            button2_0.grid(row=2, column=0, padx=5, pady=5)

            button2_1 = Button(frame2, text="分数计算器", command=farcmath_page)
            button2_1.config(bg='white')
            button2_1.grid(row=2, column=1, padx=5, pady=5)

            button2_2 = Button(frame2, text="解一元一次方程", command=equ_pages.f_ulequ_page)
            button2_2.config(bg='white')
            button2_2.grid(row=4, column=0, padx=5, pady=5)

            button2_3 = Button(frame2, text="解二元一次方程组", command=equ_pages.f_tilequ_page)
            button2_3.config(bg='white')
            button2_3.grid(row=4, column=1, padx=5, pady=5)

            button2_4 = Button(frame2, text="自定义解方程/方程组", command=equ_pages.any_equ_page)
            button2_4.config(bg='white')
            button2_4.grid(row=4, column=2, padx=5, pady=5)

            button2_5 = Button(frame2, text="解一元一次\n不等式/不等式组", command=inequality_page)
            button2_5.config(bg='white')
            button2_5.grid(row=6, column=0, padx=5, pady=5)

            button2_6 = Button(frame2, text="求一次函数解析式", command=fun_pages.aepf_page)
            button2_6.config(bg='white')
            button2_6.grid(row=8, column=0, padx=5, pady=5)

            button2_7 = Button(frame2, text="平面直角坐标系\n两点间距离公式", command=gry_pages.tpd_page)
            button2_7.config(bg='white')
            button2_7.grid(row=12, column=0, padx=5, pady=5)

            button2_9 = Button(frame2, text="求一次函数上点的坐标", command=fun_pages.cppf_page)
            button2_9.config(bg='white')
            button2_9.grid(row=8, column=1, padx=5, pady=5)

            button2_10 = Button(frame2, text="求相垂直一次函数的解析式", command=fun_pages.tvpf_page)
            button2_10.config(bg='white')
            button2_10.grid(row=8, column=3, padx=5, pady=5)

            button2_11 = Button(frame2, text="求一次函数交点坐标", command=fun_pages.tppf_page)
            button2_11.config(bg='white')
            button2_11.grid(row=8, column=2, padx=5, pady=5)

            button2_12 = Button(frame2, text="数据统计计算器", command=statistics_page)
            button2_12.config(bg='white')
            button2_12.grid(row=10, column=0, padx=5, pady=5)

            button2_13 = Button(frame2, text="平面直角坐标系\n中点坐标公式", command=gry_pages.mpmi_page)
            button2_13.config(bg='white')
            button2_13.grid(row=12, column=1, padx=5, pady=5)

            button2_14 = Button(frame2, text="几何函数计算器", command=gry_pages.gryfun_page)
            button2_14.config(bg='white')
            button2_14.grid(row=12, column=2, padx=5, pady=5)

            button2_15 = Button(frame2, text="数论计算器", command=numbertheory_page)
            button2_15.config(bg='white')
            button2_15.grid(row=2, column=2, padx=5, pady=5)

            button2_q = Button(root2, text="返回首页", command=__quitmathindexpage__)
            button2_q.config(bg='white')
            button2_q.pack(anchor='se', padx=5, pady=5)

            lab2_6 = Label(root2, font=('微软雅黑', 7),
                           text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
            lab2_6.config(bg='white')
            lab2_6.pack(anchor='se', padx=5, pady=5)


            root2.update_idletasks()

            x = (root2.winfo_screenwidth() - root2.winfo_reqwidth()) / 2
            y = (root2.winfo_screenheight() - root2.winfo_reqheight()) / 2
            root2.geometry("+%d+%d" % (x, y))

            root2.mainloop()

        def snindex_page(self):

            root3 = Toplevel(root)
            root3.config(bg='white')
            root3.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_功能页")

            frame3 = Frame(root3)
            frame3.config(bg='white')
            frame3.pack(side=TOP, fill=Y, anchor='center')

            class SN_pages:

                def phyindexpage(self):

                    def v_page():

                        def v1():

                            f = float(u4_1.get())
                            s = float(m4_1.get())
                            an = f/s
                            d4_1.set("v="+str(an))

                        def v2():

                            f = float(u4_1.get())
                            s = float(m4_1.get())
                            an = f/s
                            d4_1.set("t="+str(an))

                        def v3():

                            f = float(u4_1.get())
                            s = float(m4_1.get())
                            an = f*s
                            d4_1.set("s="+str(an))

                        def delall():
                            u4_1.set("")
                            m4_1.set("")
                            d4_1.set("")

                        def __quitvsnpage__():
                            root4_1.destroy()

                        u4_1 = StringVar()
                        d4_1 = StringVar()
                        m4_1 = StringVar()

                        root4_1 = Toplevel(root4)
                        root4_1.config(bg='white')
                        root4_1.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_物理计算器_速度公式")

                        frame4_1 = Frame(root4_1)
                        frame4_1.config(bg='white')
                        frame4_1.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame4_1, font=('微软雅黑', 15), text="MSICtor JME 速度公式",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame4_1, font=('微软雅黑', 10),
                                     text=" v = s / t ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame4_1, font=('微软雅黑', 10), text="数a:")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame4_1, font=('微软雅黑', 10), text="")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame4_1, font=('微软雅黑', 10), text="数b:")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame4_1, font=('微软雅黑', 10), text="")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame4_1, font=('微软雅黑', 10), text="计算结果:")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame4_1, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。\n3.公式第二个数为a,第三个数为b。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root4_1, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame4_1, textvariable=u4_1)
                        ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                        ent2 = Entry(frame4_1, textvariable=m4_1)
                        ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame4_1, textvariable=d4_1)
                        ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame4_1, text="v=s/t", command=v1)
                        button1.config(bg='white')
                        button1.grid(row=2, column=2, padx=5, pady=5)

                        button2 = Button(frame4_1, text="t=s/v", command=v2)
                        button2.config(bg='white')
                        button2.grid(row=3, column=2, padx=5, pady=5)

                        button3 = Button(frame4_1, text="s=v*t", command=v3)
                        button3.config(bg='white')
                        button3.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame4_1, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame4_1, text="返回功能页", command=__quitvsnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root4_1.update_idletasks()

                        x = (root4_1.winfo_screenwidth() - root4_1.winfo_reqwidth()) / 2
                        y = (root4_1.winfo_screenheight() - root4_1.winfo_reqheight()) / 2
                        root4_1.geometry("+%d+%d" % (x, y))

                        root4_1.mainloop()

                    def p_page():

                        def p1():

                            f = float(u4_2.get())
                            s = float(m4_2.get())
                            an = f/s
                            d4_2.set("ρ="+str(an))

                        def p2():

                            f = float(u4_2.get())
                            s = float(m4_2.get())
                            an = f/s
                            d4_2.set("V="+str(an))

                        def p3():

                            f = float(u4_2.get())
                            s = float(m4_2.get())
                            an = f*s
                            d4_2.set("m="+str(an))

                        def delall():
                            u4_2.set("")
                            m4_2.set("")
                            d4_2.set("")

                        def __quitpsnpage__():
                            root4_2.destroy()

                        u4_2 = StringVar()
                        d4_2 = StringVar()
                        m4_2 = StringVar()

                        root4_2 = Toplevel(root4)
                        root4_2.config(bg='white')
                        root4_2.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_物理计算器_密度公式")

                        frame4_2 = Frame(root4_2)
                        frame4_2.config(bg='white')
                        frame4_2.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame4_2, font=('微软雅黑', 15), text="MSICtor JME 密度公式",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame4_2, font=('微软雅黑', 10),
                                     text=" ρ = m / V ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame4_2, font=('微软雅黑', 10), text="数a:")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame4_2, font=('微软雅黑', 10), text="")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame4_2, font=('微软雅黑', 10), text="数b:")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame4_2, font=('微软雅黑', 10), text="")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame4_2, font=('微软雅黑', 10), text="计算结果:")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame4_2, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。\n3.公式第二个数为a,第三个数为b。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root4_2, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame4_2, textvariable=u4_2)
                        ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                        ent2 = Entry(frame4_2, textvariable=m4_2)
                        ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame4_2, textvariable=d4_2)
                        ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame4_2, text="ρ=m/V", command=p1)
                        button1.config(bg='white')
                        button1.grid(row=2, column=2, padx=5, pady=5)

                        button2 = Button(frame4_2, text="V=m/ρ", command=p2)
                        button2.config(bg='white')
                        button2.grid(row=3, column=2, padx=5, pady=5)

                        button3 = Button(frame4_2, text="m=V*ρ", command=p3)
                        button3.config(bg='white')
                        button3.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame4_2, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame4_2, text="返回功能页", command=__quitpsnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root4_2.update_idletasks()

                        x = (root4_2.winfo_screenwidth() - root4_2.winfo_reqwidth()) / 2
                        y = (root4_2.winfo_screenheight() - root4_2.winfo_reqheight()) / 2
                        root4_2.geometry("+%d+%d" % (x, y))

                        root4_2.mainloop()

                    def g_page():

                        def g1():

                            f = float(u4_3.get())
                            an = f * 9.8
                            d4_3.set("G="+str(an))

                        def g2():

                            f = float(u4_3.get())
                            an = f / 9.8
                            d4_3.set("m="+str(an))

                        def delall():
                            u4_3.set("")
                            d4_3.set("")

                        def __quitgsnpage__():
                            root4_3.destroy()

                        u4_3 = StringVar()
                        d4_3 = StringVar()

                        root4_3 = Toplevel(root4)
                        root4_3.config(bg='white')
                        root4_3.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_物理计算器_重力公式")

                        frame4_3 = Frame(root4_3)
                        frame4_3.config(bg='white')
                        frame4_3.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame4_3, font=('微软雅黑', 15), text="MSICtor JME 重力公式",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame4_3, font=('微软雅黑', 10),
                                     text=" G = m * g ( g = 9.8N/kg ) ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame4_3, font=('微软雅黑', 10), text="")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame4_3, font=('微软雅黑', 10), text="数a(kg或N):")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame4_3, font=('微软雅黑', 10), text="")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame4_3, font=('微软雅黑', 10), text="计算结果:")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame4_3, font=('微软雅黑', 10), text="")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame4_3, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root4_3, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame4_3, textvariable=u4_3)
                        ent1.grid(row=3, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame4_3, textvariable=d4_3)
                        ent4.grid(row=5, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame4_3, text="G=mg", command=g1)
                        button1.config(bg='white')
                        button1.grid(row=3, column=2, padx=5, pady=5)

                        button2 = Button(frame4_3, text="m=G/g", command=g2)
                        button2.config(bg='white')
                        button2.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame4_3, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame4_3, text="返回功能页", command=__quitgsnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root4_3.update_idletasks()

                        x = (root4_3.winfo_screenwidth() - root4_3.winfo_reqwidth()) / 2
                        y = (root4_3.winfo_screenheight() - root4_3.winfo_reqheight()) / 2
                        root4_3.geometry("+%d+%d" % (x, y))

                        root4_3.mainloop()

                    def pa_page():

                        def pa1():
                            f = float(u4_4.get())
                            s = float(m4_4.get())
                            an = f / s
                            d4_4.set("p=" + str(an))

                        def pa2():
                            f = float(u4_4.get())
                            s = float(m4_4.get())
                            an = f / s
                            d4_4.set("S=" + str(an))

                        def pa3():
                            f = float(u4_4.get())
                            s = float(m4_4.get())
                            an = f * s
                            d4_4.set("F=" + str(an))

                        def delall():
                            u4_4.set("")
                            m4_4.set("")
                            d4_4.set("")

                        def __quitpasnpage__():
                            root4_4.destroy()

                        u4_4 = StringVar()
                        d4_4 = StringVar()
                        m4_4 = StringVar()

                        root4_4 = Toplevel(root4)
                        root4_4.config(bg='white')
                        root4_4.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_物理计算器_压强公式")

                        frame4_4 = Frame(root4_4)
                        frame4_4.config(bg='white')
                        frame4_4.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame4_4, font=('微软雅黑', 15), text="MSICtor JME 压强公式",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame4_4, font=('微软雅黑', 10),
                                     text=" p = F / S ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame4_4, font=('微软雅黑', 10), text="数a:")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame4_4, font=('微软雅黑', 10), text="")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame4_4, font=('微软雅黑', 10), text="数b:")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame4_4, font=('微软雅黑', 10), text="")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame4_4, font=('微软雅黑', 10), text="计算结果:")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame4_4, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。\n3.公式第二个数为a,第三个数为b。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root4_4, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame4_4, textvariable=u4_4)
                        ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                        ent2 = Entry(frame4_4, textvariable=m4_4)
                        ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame4_4, textvariable=d4_4)
                        ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame4_4, text="p=F/S", command=pa1)
                        button1.config(bg='white')
                        button1.grid(row=2, column=2, padx=5, pady=5)

                        button2 = Button(frame4_4, text="S=F/p", command=pa2)
                        button2.config(bg='white')
                        button2.grid(row=3, column=2, padx=5, pady=5)

                        button3 = Button(frame4_4, text="F=S*p", command=pa3)
                        button3.config(bg='white')
                        button3.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame4_4, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame4_4, text="返回功能页", command=__quitpasnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root4_4.update_idletasks()

                        x = (root4_4.winfo_screenwidth() - root4_4.winfo_reqwidth()) / 2
                        y = (root4_4.winfo_screenheight() - root4_4.winfo_reqheight()) / 2
                        root4_4.geometry("+%d+%d" % (x, y))

                        root4_4.mainloop()

                    def wt_page():

                        def wt1():
                            f = float(u4_5.get())
                            s = float(m4_5.get())
                            an = f / s
                            d4_5.set("P="+str(an))

                        def wt2():
                            f = float(u4_5.get())
                            s = float(m4_5.get())
                            an = f / s
                            d4_5.set("t="+str(an))

                        def wt3():
                            f = float(u4_5.get())
                            s = float(m4_5.get())
                            an = f * s
                            d4_5.set("W="+str(an))

                        def delall():
                            u4_5.set("")
                            m4_5.set("")
                            d4_5.set("")

                        def __quitwtsnpage__():
                            root4_5.destroy()

                        u4_5 = StringVar()
                        d4_5 = StringVar()
                        m4_5 = StringVar()

                        root4_5 = Toplevel(root4)
                        root4_5.config(bg='white')
                        root4_5.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_物理计算器_功率公式")

                        frame4_5 = Frame(root4_5)
                        frame4_5.config(bg='white')
                        frame4_5.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame4_5, font=('微软雅黑', 15), text="MSICtor JME 功率公式",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame4_5, font=('微软雅黑', 10),
                                     text=" P = W / t ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame4_5, font=('微软雅黑', 10), text="数a:")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame4_5, font=('微软雅黑', 10), text="")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame4_5, font=('微软雅黑', 10), text="数b:")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame4_5, font=('微软雅黑', 10), text="")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame4_5, font=('微软雅黑', 10), text="计算结果:")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame4_5, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。\n3.公式第二个数为a,第三个数为b。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root4_5, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame4_5, textvariable=u4_5)
                        ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                        ent2 = Entry(frame4_5, textvariable=m4_5)
                        ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame4_5, textvariable=d4_5)
                        ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame4_5, text="P=W/t", command=wt1)
                        button1.config(bg='white')
                        button1.grid(row=2, column=2, padx=5, pady=5)

                        button2 = Button(frame4_5, text="t=W/P", command=wt2)
                        button2.config(bg='white')
                        button2.grid(row=3, column=2, padx=5, pady=5)

                        button3 = Button(frame4_5, text="W=P*t", command=wt3)
                        button3.config(bg='white')
                        button3.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame4_5, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame4_5, text="返回功能页", command=__quitwtsnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root4_5.update_idletasks()

                        x = (root4_5.winfo_screenwidth() - root4_5.winfo_reqwidth()) / 2
                        y = (root4_5.winfo_screenheight() - root4_5.winfo_reqheight()) / 2
                        root4_5.geometry("+%d+%d" % (x, y))

                        root4_5.mainloop()

                    def w_page():

                        def w1():
                            f = float(u4_6.get())
                            s = float(m4_6.get())
                            an = f * s
                            d4_6.set("W="+str(an))

                        def w2():
                            f = float(u4_6.get())
                            s = float(m4_6.get())
                            an = f / s
                            d4_6.set("F="+str(an))

                        def w3():
                            f = float(u4_6.get())
                            s = float(m4_6.get())
                            an = f / s
                            d4_6.set("s="+str(an))

                        def delall():
                            u4_6.set("")
                            m4_6.set("")
                            d4_6.set("")

                        def __quitwsnpage__():
                            root4_6.destroy()

                        u4_6 = StringVar()
                        d4_6 = StringVar()
                        m4_6 = StringVar()

                        root4_6 = Toplevel(root4)
                        root4_6.config(bg='white')
                        root4_6.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_物理计算器_功的计算")

                        frame4_6 = Frame(root4_6)
                        frame4_6.config(bg='white')
                        frame4_6.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame4_6, font=('微软雅黑', 15), text="MSICtor JME 功的计算",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame4_6, font=('微软雅黑', 10),
                                     text=" W = F * s ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame4_6, font=('微软雅黑', 10), text="数a:")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame4_6, font=('微软雅黑', 10), text="")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame4_6, font=('微软雅黑', 10), text="数b:")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame4_6, font=('微软雅黑', 10), text="")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame4_6, font=('微软雅黑', 10), text="计算结果:")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame4_6, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。\n3.公式第二个数为a,第三个数为b。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root4_6, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame4_6, textvariable=u4_6)
                        ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                        ent2 = Entry(frame4_6, textvariable=m4_6)
                        ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame4_6, textvariable=d4_6)
                        ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame4_6, text="W=F*s", command=w1)
                        button1.config(bg='white')
                        button1.grid(row=2, column=2, padx=5, pady=5)

                        button2 = Button(frame4_6, text="F=W/s", command=w2)
                        button2.config(bg='white')
                        button2.grid(row=3, column=2, padx=5, pady=5)

                        button3 = Button(frame4_6, text="s=W/F", command=w3)
                        button3.config(bg='white')
                        button3.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame4_6, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame4_6, text="返回功能页", command=__quitwsnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root4_6.update_idletasks()

                        x = (root4_6.winfo_screenwidth() - root4_6.winfo_reqwidth()) / 2
                        y = (root4_6.winfo_screenheight() - root4_6.winfo_reqheight()) / 2
                        root4_6.geometry("+%d+%d" % (x, y))

                        root4_6.mainloop()

                    def u_page():

                        def u1():
                            f = float(u4_7.get())
                            s = float(m4_7.get())
                            an = f + s
                            d4_7.set("U▲="+str(an))

                        def u2():
                            f = float(u4_7.get())
                            s = float(m4_7.get())
                            an = f - s
                            d4_7.set("W="+str(an))

                        def u3():
                            f = float(u4_7.get())
                            s = float(m4_7.get())
                            an = f - s
                            d4_7.set("Q="+str(an))

                        def delall():
                            u4_7.set("")
                            m4_7.set("")
                            d4_7.set("")

                        def __quitwsnpage__():
                            root4_7.destroy()

                        u4_7 = StringVar()
                        d4_7 = StringVar()
                        m4_7 = StringVar()

                        root4_7 = Toplevel(root4)
                        root4_7.config(bg='white')
                        root4_7.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_物理计算器_热力学第一定律")

                        frame4_7 = Frame(root4_7)
                        frame4_7.config(bg='white')
                        frame4_7.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame4_7, font=('微软雅黑', 15), text="MSICtor JME 热力学第一定律",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame4_7, font=('微软雅黑', 10),
                                     text=" U▲化学热能 = Q环境较换热 + W环境交换功 ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame4_7, font=('微软雅黑', 10), text="数a:")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame4_7, font=('微软雅黑', 10), text="")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame4_7, font=('微软雅黑', 10), text="数b:")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame4_7, font=('微软雅黑', 10), text="")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame4_7, font=('微软雅黑', 10), text="计算结果:")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame4_7, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。\n3.公式第二个数为a,第三个数为b。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root4_7, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame4_7, textvariable=u4_7)
                        ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                        ent2 = Entry(frame4_7, textvariable=m4_7)
                        ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame4_7, textvariable=d4_7)
                        ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame4_7, text="U▲=Q+W", command=u1)
                        button1.config(bg='white')
                        button1.grid(row=2, column=2, padx=5, pady=5)

                        button2 = Button(frame4_7, text="W=U▲-Q", command=u2)
                        button2.config(bg='white')
                        button2.grid(row=3, column=2, padx=5, pady=5)

                        button3 = Button(frame4_7, text="Q=U▲-W", command=u3)
                        button3.config(bg='white')
                        button3.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame4_7, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame4_7, text="返回功能页", command=__quitwsnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root4_7.update_idletasks()

                        x = (root4_7.winfo_screenwidth() - root4_7.winfo_reqwidth()) / 2
                        y = (root4_7.winfo_screenheight() - root4_7.winfo_reqheight()) / 2
                        root4_7.geometry("+%d+%d" % (x, y))

                        root4_7.mainloop()

                    def __quitphyindexpage__():
                        info = tm.askquestion('提示', '你确定要返回首页吗?\n这会关掉物理计算器所有已经打开的功能页!')
                        if info == 'yes':
                            root4.destroy()
                        else:
                            pass

                    root4 = Toplevel(root3)
                    root4.config(bg='white')
                    root4.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_物理计算器_功能页")

                    frame4 = Frame(root4)
                    frame4.config(bg='white')
                    frame4.pack(side=TOP, fill=Y, anchor='center')

                    lab4_0 = Label(frame4, font=('微软雅黑', 15), text="MSICtor JME 物理计算器", anchor='center')
                    lab4_0.config(fg='darkblue', bg='white')
                    lab4_0.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab4_1 = Label(frame4, font=('微软雅黑', 10), text="物体的性质:")
                    lab4_1.config(bg='white')
                    lab4_1.grid(row=1, column=0, padx=5, pady=5, sticky=W)

                    lab4_2 = Label(frame4, font=('微软雅黑', 10), text="力学:")
                    lab4_2.config(bg='white')
                    lab4_2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                    lab4_3 = Label(frame4, font=('微软雅黑', 10), text="压强:")
                    lab4_3.config(bg='white')
                    lab4_3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    lab4_4 = Label(frame4, font=('微软雅黑', 10), text="功:")
                    lab4_4.config(bg='white')
                    lab4_4.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                    lab4_5 = Label(frame4, font=('微软雅黑', 10), text="热力学:")
                    lab4_5.config(bg='white')
                    lab4_5.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                    button4_q = Button(root4, text="返回首页", command=__quitphyindexpage__)
                    button4_q.config(bg='white')
                    button4_q.pack(anchor='se', padx=5, pady=5)

                    lab4_5 = Label(root4, font=('微软雅黑', 7),
                                   text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab4_5.config(bg='white')
                    lab4_5.pack(anchor='se', padx=5, pady=5)

                    button4_0 = Button(frame4, text="速度公式", command=v_page)
                    button4_0.config(bg='white')
                    button4_0.grid(row=1, column=1, padx=5, pady=5, sticky=N)

                    button4_1 = Button(frame4, text="密度公式", command=p_page)
                    button4_1.config(bg='white')
                    button4_1.grid(row=1, column=2, padx=5, pady=5, sticky=N)

                    button4_2 = Button(frame4, text="重力公式", command=g_page)
                    button4_2.config(bg='white')
                    button4_2.grid(row=2, column=1, padx=5, pady=5, sticky=N)

                    button4_3 = Button(frame4, text="压强公式", command=pa_page)
                    button4_3.config(bg='white')
                    button4_3.grid(row=3, column=1, padx=5, pady=5, sticky=N)

                    button4_4 = Button(frame4, text="功率公式", command=wt_page)
                    button4_4.config(bg='white')
                    button4_4.grid(row=4, column=1, padx=5, pady=5, sticky=N)

                    button4_5 = Button(frame4, text="功的计算", command=w_page)
                    button4_5.config(bg='white')
                    button4_5.grid(row=4, column=2, padx=5, pady=5, sticky=N)

                    button4_6 = Button(frame4, text="热力学第一定律", command=u_page)
                    button4_6.config(bg='white')
                    button4_6.grid(row=5, column=1, padx=5, pady=5, sticky=N)

                    root4.update_idletasks()

                    x = (root4.winfo_screenwidth() - root4.winfo_reqwidth()) / 2
                    y = (root4.winfo_screenheight() - root4.winfo_reqheight()) / 2
                    root4.geometry("+%d+%d" % (x, y))

                    root4.mainloop()

                def chmindexpage(self):

                    def sol_page():

                        def sol1():

                            f = float(u5_2.get())
                            s = float(m5_2.get())
                            an = f/s
                            an = an * 100
                            d5_2.set("溶质质量分数=" + str(an) + "%" )

                        def sol2():

                            f = str(u5_2.get())
                            s = str(m5_2.get())
                            f = f.replace("%", "/100")
                            s = s.replace("%", "/100")
                            f = eval(f)
                            s = eval(s)
                            f = float(f)
                            s = float(s)
                            an = f/s
                            d5_2.set("溶液质量="+str(an))

                        def sol3():

                            f = str(u5_2.get())
                            s = str(m5_2.get())
                            f = f.replace("%","/100")
                            s = s.replace("%","/100")
                            f = eval(f)
                            s = eval(s)
                            f = float(f)
                            s = float(s)
                            an = f * s
                            d5_2.set("溶质质量="+str(an))

                        def delall():
                            u5_2.set("")
                            m5_2.set("")
                            d5_2.set("")

                        def __quitsolsnpage__():
                            root5_2.destroy()

                        u5_2 = StringVar()
                        d5_2 = StringVar()
                        m5_2 = StringVar()

                        root5_2 = Toplevel(root5)
                        root5_2.config(bg='white')
                        root5_2.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_化学计算器_溶质质量分数")

                        frame5_2 = Frame(root5_2)
                        frame5_2.config(bg='white')
                        frame5_2.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame5_2, font=('微软雅黑', 15), text="MSICtor JME 溶质质量分数",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame5_2, font=('微软雅黑', 10),
                                     text=" 溶质质量分数 = 溶质质量 / 溶液质量 * 100 % ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame5_2, font=('微软雅黑', 10), text="数a:")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame5_2, font=('微软雅黑', 10), text="")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame5_2, font=('微软雅黑', 10), text="数b:")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame5_2, font=('微软雅黑', 10), text="")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame5_2, font=('微软雅黑', 10), text="计算结果:")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame5_2, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。\n3.原公式第二个数为a,第三个数为b。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root5_2, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame5_2, textvariable=u5_2)
                        ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                        ent2 = Entry(frame5_2, textvariable=m5_2)
                        ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame5_2, textvariable=d5_2)
                        ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame5_2, text="溶质质量分数=溶质质量/溶液质量*100 %", command=sol1)
                        button1.config(bg='white')
                        button1.grid(row=2, column=2, padx=5, pady=5)

                        button2 = Button(frame5_2, text="溶液质量=溶质质量/溶质质量分数", command=sol2)
                        button2.config(bg='white')
                        button2.grid(row=3, column=2, padx=5, pady=5)

                        button3 = Button(frame5_2, text="溶质质量=溶液质量*溶质质量分数", command=sol3)
                        button3.config(bg='white')
                        button3.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame5_2, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame5_2, text="返回功能页", command=__quitsolsnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root5_2.update_idletasks()

                        x = (root5_2.winfo_screenwidth() - root5_2.winfo_reqwidth()) / 2
                        y = (root5_2.winfo_screenheight() - root5_2.winfo_reqheight()) / 2
                        root5_2.geometry("+%d+%d" % (x, y))

                        root5_2.mainloop()

                    def mol_page():

                        def mol1():

                            f = float(u5_1.get())
                            s = float(m5_1.get())
                            an = f/s
                            d5_1.set("n="+str(an))

                        def mol2():

                            f = float(u5_1.get())
                            s = float(m5_1.get())
                            an = f/s
                            d5_1.set("M或NA="+str(an))

                        def mol3():

                            f = float(u5_1.get())
                            s = float(m5_1.get())
                            an = f*s
                            d5_1.set("m或N="+str(an))

                        def delall():
                            u5_1.set("")
                            m5_1.set("")
                            d5_1.set("")

                        def __quitmolsnpage__():
                            root5_1.destroy()

                        u5_1 = StringVar()
                        d5_1 = StringVar()
                        m5_1 = StringVar()

                        root5_1 = Toplevel(root5)
                        root5_1.config(bg='white')
                        root5_1.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_化学计算器_物质的量")

                        frame5_1 = Frame(root5_1)
                        frame5_1.config(bg='white')
                        frame5_1.pack(side=TOP, fill=Y, anchor='center')

                        lab1 = Label(frame5_1, font=('微软雅黑', 15), text="MSICtor JME 物质的量",
                                     anchor='center')
                        lab1.config(fg='blue', bg='white')
                        lab1.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                        lab8 = Label(frame5_1, font=('微软雅黑', 10),
                                     text=" n物质的量(mol) = m物质的质量(g)  / M物质的摩尔质量(g/mol) \n n物质的量(mol) = N粒子数  / NA阿伏伽德罗常量 ")
                        lab8.config(bg='white')
                        lab8.grid(row=1, column=0, padx=5, pady=5, sticky=N)

                        lab2 = Label(frame5_1, font=('微软雅黑', 10), text="数a:")
                        lab2.config(bg='white')
                        lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)

                        lab22 = Label(frame5_1, font=('微软雅黑', 10), text="")
                        lab22.config(bg='white')
                        lab22.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                        lab3 = Label(frame5_1, font=('微软雅黑', 10), text="数b:")
                        lab3.config(bg='white')
                        lab3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

                        lab33 = Label(frame5_1, font=('微软雅黑', 10), text="")
                        lab33.config(bg='white')
                        lab33.grid(row=5, column=0, padx=5, pady=5, sticky=W)

                        lab5 = Label(frame5_1, font=('微软雅黑', 10), text="计算结果:")
                        lab5.config(bg='white')
                        lab5.grid(row=6, column=0, padx=5, pady=5, sticky=W)

                        lab6 = Label(frame5_1, font=('微软雅黑', 8),
                                     text="*注:1.本计算器仅支持小数。\n2.输入时必须使用英文输入法。\n3.原公式第二个数为a,第三个数为b。")
                        lab6.config(bg='white')
                        lab6.grid(row=7, column=0, padx=5, pady=5, sticky=W)

                        lab7 = Label(root5_1, font=('微软雅黑', 7),
                                     text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                        lab7.config(bg='white')
                        lab7.pack(anchor='se', padx=5, pady=5)

                        ent1 = Entry(frame5_1, textvariable=u5_1)
                        ent1.grid(row=2, column=1, sticky='ew', columnspan=1)

                        ent2 = Entry(frame5_1, textvariable=m5_1)
                        ent2.grid(row=4, column=1, sticky='ew', columnspan=1)

                        ent4 = Entry(frame5_1, textvariable=d5_1)
                        ent4.grid(row=6, column=1, sticky='ew', columnspan=1)

                        button1 = Button(frame5_1, text="n=m/M(n=N/NA)", command=mol1)
                        button1.config(bg='white')
                        button1.grid(row=2, column=2, padx=5, pady=5)

                        button2 = Button(frame5_1, text="M=m/n(NA=N/n)", command=mol2)
                        button2.config(bg='white')
                        button2.grid(row=3, column=2, padx=5, pady=5)

                        button3 = Button(frame5_1, text="m=M*n(N=NA*n)", command=mol3)
                        button3.config(bg='white')
                        button3.grid(row=4, column=2, padx=5, pady=5)

                        button10 = Button(frame5_1, text="   C   ", command=delall)
                        button10.config(bg='white')
                        button10.grid(row=5, column=2, padx=5, pady=5)

                        button12 = Button(frame5_1, text="返回功能页", command=__quitmolsnpage__)
                        button12.config(bg='white')
                        button12.grid(row=6, column=2, padx=5, pady=5)

                        root5_1.update_idletasks()

                        x = (root5_1.winfo_screenwidth() - root5_1.winfo_reqwidth()) / 2
                        y = (root5_1.winfo_screenheight() - root5_1.winfo_reqheight()) / 2
                        root5_1.geometry("+%d+%d" % (x, y))

                        root5_1.mainloop()

                    def __quitchmindexpage__():
                        info = tm.askquestion('提示', '你确定要返回首页吗?\n这会关掉化学计算器所有已经打开的功能页!')
                        if info == 'yes':
                            root5.destroy()
                        else:
                            pass

                    root5 = Toplevel(root3)
                    root5.config(bg='white')
                    root5.title("MSICtorJME多功能计算器(初中教育版)_科学计算器_化学计算器_功能页")

                    frame5 = Frame(root5)
                    frame5.config(bg='white')
                    frame5.pack(side=TOP, fill=Y, anchor='center')

                    lab5_0 = Label(frame5, font=('微软雅黑', 15), text="MSICtor JME 化学计算器", anchor='center')
                    lab5_0.config(fg='darkblue', bg='white')
                    lab5_0.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

                    lab5_1 = Label(frame5, font=('微软雅黑', 10), text="物质的量:")
                    lab5_1.config(bg='white')
                    lab5_1.grid(row=1, column=0, padx=5, pady=5, sticky=W)

                    lab5_2 = Label(frame5, font=('微软雅黑', 10), text="溶液:")
                    lab5_2.config(bg='white')
                    lab5_2.grid(row=3, column=0, padx=5, pady=5, sticky=W)

                    button5_q = Button(root5, text="返回首页", command=__quitchmindexpage__)
                    button5_q.config(bg='white')
                    button5_q.pack(anchor='se', padx=5, pady=5)

                    lab5_6 = Label(root5, font=('微软雅黑', 7),
                                   text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
                    lab5_6.config(bg='white')
                    lab5_6.pack(anchor='se', padx=5, pady=5)

                    button5_0 = Button(frame5, text="物质的量", command=mol_page)
                    button5_0.config(bg='white')
                    button5_0.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky=N)

                    button5_1 = Button(frame5, text="溶质质量分数", command=sol_page)
                    button5_1.config(bg='white')
                    button5_1.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky=N)

                    root5.update_idletasks()

                    x = (root5.winfo_screenwidth() - root5.winfo_reqwidth()) / 2
                    y = (root5.winfo_screenheight() - root5.winfo_reqheight()) / 2
                    root5.geometry("+%d+%d" % (x, y))

                    root5.mainloop()

            def __quitsnindexpage__():
                info = tm.askquestion('提示','你确定要返回首页吗?\n这会关掉科学计算器所有已经打开的功能页!')
                if info == 'yes':
                    root3.destroy()
                else:
                    pass

            snp = SN_pages()

            lab3_0 = Label(frame3, font=('微软雅黑', 15), text="MSICtor JME 科学计算器", anchor='center')
            lab3_0.config(fg='darkblue', bg='white')
            lab3_0.grid(row=0, columnspan=2, padx=5, pady=5, sticky=N)

            lab3_1 = Label(frame3, font=('微软雅黑', 10), text="物理计算器:")
            lab3_1.config(fg='navy',bg='white')
            lab3_1.grid(row=1, column=0, padx=5, pady=5, sticky=W)

            lab3_2 = Label(frame3, font=('微软雅黑', 10), text="化学计算器:")
            lab3_2.config(fg='gold',bg='white')
            lab3_2.grid(row=3, column=0, padx=5, pady=5, sticky=W)

            button3_q = Button(root3, text="返回首页", command=__quitsnindexpage__)
            button3_q.config(bg='white')
            button3_q.pack(anchor='se', padx=5, pady=5)

            lab3_6 = Label(root3, font=('微软雅黑', 7),
                           text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
            lab3_6.config(bg='white')
            lab3_6.pack(anchor='se', padx=5, pady=5)

            button3_0 = Button(frame3, text="物理计算器", command=snp.phyindexpage)
            button3_0.config(fg='navy')
            button3_0.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky=N)

            button3_1 = Button(frame3, text="化学计算器", command=snp.chmindexpage)
            button3_1.config(fg='gold')
            button3_1.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky=N)

            root3.update_idletasks()

            x = (root3.winfo_screenwidth() - root3.winfo_reqwidth()) / 2
            y = (root3.winfo_screenheight() - root3.winfo_reqheight()) / 2
            root3.geometry("+%d+%d" % (x, y))

            root3.mainloop()



        def __quit__(a):
            info=tm.askquestion('提示','你确定要退出吗?\n这会关掉计算器所有已经打开的功能页!')
            if info == 'yes':
                sys.exit(0)
            else:
                pass
            

    appwin =AppWindows()


    lab1_0 = Label(frame,font=('微软雅黑',20), text="")
    lab1_0.config(bg = 'white')
    lab1_0.grid(row=0, column=0, padx=5, pady=5, sticky=N)

    lab1_1 = Label(frame,font=('微软雅黑',20), text="")
    lab1_1.config(bg = 'white')
    lab1_1.grid(row=1, column=0, padx=5, pady=5, sticky=N)

    lab1_2 = Label(frame,font=('微软雅黑',40), text="      Welcome欢迎使用      ")
    lab1_2.config(fg = 'orange',bg = 'white')
    lab1_2.grid(row=2, column=0, padx=5, pady=5, sticky=N)

    lab1_3 = Label(frame,font=('微软雅黑',20), text="MSICtor MJE\n多功能集成计算器(初中教育版)")
    lab1_3.config(fg = 'yellow',bg = 'white')
    lab1_3.grid(row=3, column=0, padx=5, pady=5,sticky=N)

    lab1_4 = Label(frame,font=('微软雅黑',20), text="")
    lab1_4.config(bg = 'white')
    lab1_4.grid(row=4, column=0, padx=5, pady=5, sticky=N)

    lab1_5 = Label(frame,font=('微软雅黑',20), text="")
    lab1_5.config(bg = 'white')
    lab1_5.grid(row=5, column=0, padx=5, pady=5, sticky=N)

    lab1_7 = Label(frame,font=('微软雅黑',20), text="")
    lab1_7.config(bg = 'white')
    lab1_7.grid(row=6, column=0, padx=5, pady=5, sticky=N)

    lab1_6 = Label(root, font=('微软雅黑', 7),text="Version 1.0a - 11 . 30 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
    lab1_6.config(bg = 'white')
    lab1_6.pack(anchor='se', padx=5, pady=5)

    button1 = Button(frame, text="数学计算器", command=appwin.mathindex_page)
    button1.config(fg = 'blue')
    button1.grid(row=4, column=0,padx=200,pady=20,sticky=NW)

    button2 = Button(frame, text="科学计算器", command=appwin.snindex_page)
    button2.config(fg = 'darkblue')
    button2.grid(row=4, column=0,padx=200,pady=20,sticky=N)

    button3 = Button(frame, text="退出计算器", command=appwin.__quit__)
    button3.grid(row=4, column=0,padx=200,pady=20,sticky=NE)

    root.update_idletasks()

    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))

    root.mainloop()



if __name__ == "__main__":

    main()









