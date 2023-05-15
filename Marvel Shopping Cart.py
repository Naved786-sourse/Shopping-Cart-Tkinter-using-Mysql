from tkinter import *
from PIL import ImageTk,Image
import PIL as f
import mysql.connector as sql
from tkinter import messagebox


root = Tk()
root.geometry("1350x1000")
root.title("Marvel Shopping Cart")
image_logo = ImageTk.PhotoImage(f.Image.open("marvel.png"))
heading = LabelFrame(root,fg="red",bd=2,bg="black", relief="groove")
heading.place(x=0,y=0,width=1350,height=105)
logo_label = Label(heading,image=image_logo)
logo_label.place(x=0,y=0)
text_label = Label(heading,text="Marvel Shopping Cart",font="arial 30 bold",bg="black",fg="red")
text_label.pack(side=TOP)

image_logo_larger = ImageTk.PhotoImage(f.Image.open("SpiderMan poster_1.png"))

CA_1 = ImageTk.PhotoImage(f.Image.open("captain_america_sheild.png"))
CA_2 = ImageTk.PhotoImage(f.Image.open("blue_sheild.png"))
CA_3 = ImageTk.PhotoImage(f.Image.open("caiptain_america_keychain.png"))
CA_4 = ImageTk.PhotoImage(f.Image.open("ca_tshirt_1.png"))
CA_5 = ImageTk.PhotoImage(f.Image.open("ca_tshirt_2.png"))
CA_6 = ImageTk.PhotoImage(f.Image.open("ca_tshirt_3.png"))
CA_7 = ImageTk.PhotoImage(f.Image.open("ca_shoes_1.png"))
CA_8 = ImageTk.PhotoImage(f.Image.open("ca_shoes_2.png"))
CA_9 = ImageTk.PhotoImage(f.Image.open("ca_shoes_3.png"))
CA_10 = ImageTk.PhotoImage(f.Image.open("captain_america.png"))

IM_1 = ImageTk.PhotoImage(f.Image.open("im_toy_1.png"))
IM_2 = ImageTk.PhotoImage(f.Image.open("im_toy_2.png"))
IM_3 = ImageTk.PhotoImage(f.Image.open("im_toy_3.png"))
IM_4 = ImageTk.PhotoImage(f.Image.open("im_shoes_1.png"))
IM_5 = ImageTk.PhotoImage(f.Image.open("im_shoes_2.png"))
IM_6 = ImageTk.PhotoImage(f.Image.open("im_shoes_3.png"))
IM_7 = ImageTk.PhotoImage(f.Image.open("im_shoes_4.png"))
IM_8 = ImageTk.PhotoImage(f.Image.open("im_tshirt_1.png"))
IM_9 = ImageTk.PhotoImage(f.Image.open("im_tshirt_2.png"))
IM_10 = ImageTk.PhotoImage(f.Image.open("im_tshirt_3.png"))

BW_1 = ImageTk.PhotoImage(f.Image.open("BW_1.png"))
BW_2 = ImageTk.PhotoImage(f.Image.open("BW_2.png"))
BW_3 = ImageTk.PhotoImage(f.Image.open("BW_3.png"))
BW_4 = ImageTk.PhotoImage(f.Image.open("BW_4.png"))
BW_5 = ImageTk.PhotoImage(f.Image.open("BW_5.png"))
BW_6 = ImageTk.PhotoImage(f.Image.open("BW_6.png"))
BW_7 = ImageTk.PhotoImage(f.Image.open("BW_7.png"))
BW_8 = ImageTk.PhotoImage(f.Image.open("BW_8.png"))
BW_9 = ImageTk.PhotoImage(f.Image.open("BW_9.png"))
BW_10 = ImageTk.PhotoImage(f.Image.open("BW_10.png"))


thor_1 = ImageTk.PhotoImage(f.Image.open("thor_1.png"))
thor_2 = ImageTk.PhotoImage(f.Image.open("thor_2.png"))
thor_3 = ImageTk.PhotoImage(f.Image.open("thor_3.png"))
thor_4 = ImageTk.PhotoImage(f.Image.open("thor_4.png"))
thor_5 = ImageTk.PhotoImage(f.Image.open("thor_5.png"))
thor_6 = ImageTk.PhotoImage(f.Image.open("thor_6.png"))
thor_7 = ImageTk.PhotoImage(f.Image.open("thor_7.png"))
thor_8 = ImageTk.PhotoImage(f.Image.open("thor_8.png"))
thor_9 = ImageTk.PhotoImage(f.Image.open("thor_9.png"))
thor_10 = ImageTk.PhotoImage(f.Image.open("thor_10.png"))

hulk_1 = ImageTk.PhotoImage(f.Image.open("hulk_1.png"))
hulk_2 = ImageTk.PhotoImage(f.Image.open("hulk_2.png"))
hulk_3 = ImageTk.PhotoImage(f.Image.open("hulk_3.png"))
hulk_4 = ImageTk.PhotoImage(f.Image.open("hulk_4.png"))
hulk_5 = ImageTk.PhotoImage(f.Image.open("hulk_5.png"))
hulk_6 = ImageTk.PhotoImage(f.Image.open("hulk_6.png"))
hulk_7 = ImageTk.PhotoImage(f.Image.open("hulk_7.png"))
hulk_8 = ImageTk.PhotoImage(f.Image.open("hulk_8.png"))
hulk_9 = ImageTk.PhotoImage(f.Image.open("hulk_9.png"))
hulk_10 = ImageTk.PhotoImage(f.Image.open("hulk_10.png"))



default_home = Label(root,text="Home Page",image=image_logo_larger)
default_home.place(x=0,y=105)

def tab1():
    def tab_CA():
        CA_Page = Label(root,bg="black",fg="red", font="Times_New_Roman 25")
        CA_Page.pack()

        def CA1():
            def CA1_Button():
                CA1_Full = Label(root,image=CA_1,bg="white")
                CA1_Full.place(x=3,y=108,width=1350,height=600)
            label_CA1 = Button(root,image=CA_1, bd=2, relief="groove",command=CA1_Button)
            label_CA1.place(x=3, y=108, width=235, height=250)
            Price_CA1 = Button(root,text="Rs-285")
            Price_CA1.place(x=3,y=360,width=235)

            def CA2_Button():
                CA2_Full = Label(root,image=CA_2,bg="white")
                CA2_Full.place(x=3,y=108,width=1350,height=600)
            label_CA2 = Button(root, image=CA_2, bd=2, relief="groove",command=CA2_Button)
            label_CA2.place(x=240, y=108, width=236, height=250)
            Price_CA2 = Button(root, text="Rs-285")
            Price_CA2.place(x=240, y=360, width=236)

            def CA3_Button():
                CA3_Full = Button(root,image=CA_3,bg="white")
                CA3_Full.place(x=3,y=108,width=1350,height=600)
            label_CA3 = Button(root, image=CA_3, bd=2, relief="groove",command=CA3_Button)
            label_CA3.place(x=474, y=108, width=236, height=250)
            Price_CA3 = Button(root, text="Rs-285")
            Price_CA3.place(x=474, y=360, width=236)


            def CA4_Button():
                CA4_Full = Button(root,image=CA_4,bg="white")
                CA4_Full.place(x=3,y=108,width=1350,height=600)
            label_CA4 = Button(root, image=CA_4, bd=2, relief="groove",command=CA4_Button)
            label_CA4.place(x=711, y=108, width=236, height=250)
            Price_CA4 = Button(root, text="Rs-285")
            Price_CA4.place(x=711, y=360, width=236)

            def CA5_Button():
                CA5_Full = Button(root,image=CA_5,bg="white")
                CA5_Full.place(x=3,y=108,width=1350,height=600)
            label_CA5 = Button(root, image=CA_5, bd=2, relief="groove",command=CA5_Button)
            label_CA5.place(x=949, y=108, width=236, height=250)
            Price_CA5 = Button(root, text="Rs-285")
            Price_CA5.place(x=949, y=360, width=236)

            def CA6_Button():
                CA6_Full = Button(root,image=CA_6,bg="white")
                CA6_Full.place(x=3,y=108,width=1350,height=600)
            label_CA6 = Button(root, image=CA_6, bd=2, relief="groove",command=CA6_Button)
            label_CA6.place(x=3, y=390, width=235, height=250)
            Price_CA6 = Button(root, text="Rs-285")
            Price_CA6.place(x=3, y=640, width=235)

            def CA7_Button():
                CA7_Full = Button(root,image=CA_7,bg="white")
                CA7_Full.place(x=3,y=108,width=1350,height=600)
            label_CA7 = Button(root, image=CA_7, bd=2, relief="groove",command=CA7_Button)
            label_CA7.place(x=240, y=390, width=236, height=250)
            Price_CA7 = Button(root, text="Rs-285")
            Price_CA7.place(x=240, y=640, width=236)

            def CA8_Button():
                CA8_Full = Button(root,image=CA_8,bg="white")
                CA8_Full.place(x=3,y=108,width=1350,height=600)
            label_CA8 = Button(root, image=CA_8, bd=2, relief="groove",command=CA8_Button)
            label_CA8.place(x=474, y=390, width=236, height=250)
            Price_CA8 = Button(root, text="Rs-285")
            Price_CA8.place(x=474, y=640, width=236)

            def CA9_Button():
                CA9_Full = Button(root,image=CA_9,bg="white")
                CA9_Full.place(x=3,y=108,width=1350,height=600)
            label_CA9 = Button(root, image=CA_9, bd=2, relief="groove",command=CA9_Button)
            label_CA9.place(x=711, y=390, width=236, height=250)
            Price_CA9 = Button(root, text="Rs-285")
            Price_CA9.place(x=711, y=640, width=236)

            def CA10_Button():
                CA10_Full = Button(root,image=CA_10,bg="white")
                CA10_Full.place(x=3,y=108,width=1350,height=600)
            label_CA10 = Button(root, image=CA_10, bd=2, relief="groove",command=CA10_Button)
            label_CA10.place(x=949, y=390, width=236, height=250)
            Price_CA10 = Button(root, text="Rs-285")
            Price_CA10.place(x=949, y=640, width=236)

        CA1()


    def tab_IM():
        IM_Page = Label(root, bg="black", fg="red", font="Times_New_Roman 25")
        IM_Page.pack()

        def IM1():
            def IM1_Button():
                IM1_Full = Label(root,image=IM_1,bg="white")
                IM1_Full.place(x=3,y=108,width=1350,height=600)
            label_IM1 = Button(root,image=IM_1, bd=2, relief="groove",command=IM1_Button)
            label_IM1.place(x=3, y=108, width=235, height=250)
            Price_IM1 = Button(root,text="Rs-285")
            Price_IM1.place(x=3,y=360,width=235)

            def IM2_Button():
                IM2_Full = Label(root, image=IM_2, bg="white")
                IM2_Full.place(x=3, y=108, width=1350, height=600)
            label_IM2 = Button(root, image=IM_2, bd=2, relief="groove", command=IM2_Button)
            label_IM2.place(x=240, y=108, width=236, height=250)
            Price_IM2 = Button(root, text="Rs-285")
            Price_IM2.place(x=240, y=360, width=236)

            def IM3_Button():
                IM3_Full = Button(root,image=IM_3,bg="white")
                IM3_Full.place(x=3,y=108,width=1350,height=600)
            label_IM3 = Button(root, image=IM_3, bd=2, relief="groove",command=IM3_Button)
            label_IM3.place(x=474, y=108, width=236, height=250)
            Price_IM3 = Button(root, text="Rs-285")
            Price_IM3.place(x=474, y=360, width=236)

            def IM4_Button():
                IM4_Full = Button(root,image=IM_4,bg="white")
                IM4_Full.place(x=3,y=108,width=1350,height=600)
            label_IM4 = Button(root, image=IM_4, bd=2, relief="groove",command=IM4_Button)
            label_IM4.place(x=711, y=108, width=236, height=250)
            Price_IM4 = Button(root, text="Rs-285")
            Price_IM4.place(x=711, y=360, width=236)

            def IM5_Button():
                IM5_Full = Button(root,image=IM_5,bg="white")
                IM5_Full.place(x=3,y=108,width=1350,height=600)
            label_IM5 = Button(root, image=IM_5, bd=2, relief="groove",command=IM5_Button)
            label_IM5.place(x=949, y=108, width=236, height=250)
            Price_IM5 = Button(root, text="Rs-285")
            Price_IM5.place(x=949, y=360, width=236)

            def IM6_Button():
                IM6_Full = Button(root,image=IM_6,bg="white")
                IM6_Full.place(x=3,y=108,width=1350,height=600)
            label_IM6 = Button(root, image=IM_6, bd=2, relief="groove",command=IM6_Button)
            label_IM6.place(x=3, y=390, width=235, height=250)
            Price_IM6 = Button(root, text="Rs-285")
            Price_IM6.place(x=3, y=640, width=235)

            def IM7_Button():
                IM7_Full = Button(root,image=IM_7,bg="white")
                IM7_Full.place(x=3,y=108,width=1350,height=600)
            label_IM7 = Button(root, image=IM_7, bd=2, relief="groove",command=IM7_Button)
            label_IM7.place(x=240, y=390, width=236, height=250)
            Price_IM7 = Button(root, text="Rs-285")
            Price_IM7.place(x=240, y=640, width=236)

            def IM8_Button():
                IM8_Full = Button(root,image=IM_8,bg="white")
                IM8_Full.place(x=3,y=108,width=1350,height=600)
            label_IM8 = Button(root, image=IM_8, bd=2, relief="groove",command=IM8_Button)
            label_IM8.place(x=474, y=390, width=236, height=250)
            Price_IM8 = Button(root, text="Rs-285")
            Price_IM8.place(x=474, y=640, width=236)

            def IM9_Button():
                IM9_Full = Button(root,image=IM_9,bg="white")
                IM9_Full.place(x=3,y=108,width=1350,height=600)
            label_IM9 = Button(root, image=IM_9, bd=2, relief="groove",command=IM9_Button)
            label_IM9.place(x=711, y=390, width=236, height=250)
            Price_IM9 = Button(root, text="Rs-285")
            Price_IM9.place(x=711, y=640, width=236)

            def IM10_Button():
                IM10_Full = Button(root,image=IM_10,bg="white")
                IM10_Full.place(x=3,y=108,width=1350,height=600)
            label_IM10 = Button(root, image=IM_10, bd=2, relief="groove",command=IM10_Button)
            label_IM10.place(x=949, y=390, width=236, height=250)
            Price_IM10 = Button(root, text="Rs-285")
            Price_IM10.place(x=949, y=640, width=236)
        IM1()

    def tab_BW():
        BW_Page = Label(root, bg="black", fg="red", font="Times_New_Roman 25")
        BW_Page.pack()

        def BW1():
            def BW1_Button():
                BW1_Full = Label(root,image=BW_1,bg="white")
                BW1_Full.place(x=3,y=108,width=1350,height=600)
            label_BW1 = Button(root,image=BW_1, bd=2, relief="groove",command=BW1_Button)
            label_BW1.place(x=3, y=108, width=235, height=250)
            Price_BW1 = Button(root,text="Rs-285")
            Price_BW1.place(x=3,y=360,width=235)

            def BW2_Button():
                BW2_Full = Label(root, image=BW_2, bg="white")
                BW2_Full.place(x=3, y=108, width=1350, height=600)
            label_BW2 = Button(root, image=BW_2, bd=2, relief="groove", command=BW2_Button)
            label_BW2.place(x=240, y=108, width=236, height=250)
            Price_BW2 = Button(root, text="Rs-285")
            Price_BW2.place(x=240, y=360, width=236)

            def BW3_Button():
                BW3_Full = Button(root,image=BW_3,bg="white")
                BW3_Full.place(x=3,y=108,width=1350,height=600)
            label_BW3 = Button(root, image=BW_3, bd=2, relief="groove",command=BW3_Button)
            label_BW3.place(x=474, y=108, width=236, height=250)
            Price_BW3 = Button(root, text="Rs-285")
            Price_BW3.place(x=474, y=360, width=236)

            def BW4_Button():
                BW4_Full = Button(root,image=BW_4,bg="white")
                BW4_Full.place(x=3,y=108,width=1350,height=600)
            label_BW4 = Button(root, image=BW_4, bd=2, relief="groove",command=BW4_Button)
            label_BW4.place(x=711, y=108, width=236, height=250)
            Price_BW4 = Button(root, text="Rs-285")
            Price_BW4.place(x=711, y=360, width=236)

            def BW5_Button():
                BW5_Full = Button(root,image=BW_5,bg="white")
                BW5_Full.place(x=3,y=108,width=1350,height=600)
            label_BW5 = Button(root, image=BW_5, bd=2, relief="groove",command=BW5_Button)
            label_BW5.place(x=949, y=108, width=236, height=250)
            Price_BW5 = Button(root, text="Rs-285")
            Price_BW5.place(x=949, y=360, width=236)

            def BW6_Button():
                BW6_Full = Button(root,image=BW_6,bg="white")
                BW6_Full.place(x=3,y=108,width=1350,height=600)
            label_BW6 = Button(root, image=BW_6, bd=2, relief="groove",command=BW6_Button)
            label_BW6.place(x=3, y=390, width=235, height=250)
            Price_BW6 = Button(root, text="Rs-285")
            Price_BW6.place(x=3, y=640, width=235)

            def BW7_Button():
                BW7_Full = Button(root,image=BW_7,bg="white")
                BW7_Full.place(x=3,y=108,width=1350,height=600)
            label_BW7 = Button(root, image=BW_7, bd=2, relief="groove",command=BW7_Button)
            label_BW7.place(x=240, y=390, width=236, height=250)
            Price_BW7 = Button(root, text="Rs-285")
            Price_BW7.place(x=240, y=640, width=236)

            def BW8_Button():
                BW8_Full = Button(root,image=BW_8,bg="white")
                BW8_Full.place(x=3,y=108,width=1350,height=600)
            label_BW8 = Button(root, image=BW_8, bd=2, relief="groove",command=BW8_Button)
            label_BW8.place(x=474, y=390, width=236, height=250)
            Price_BW8 = Button(root, text="Rs-285")
            Price_BW8.place(x=474, y=640, width=236)

            def BW9_Button():
                BW9_Full = Button(root,image=BW_9,bg="white")
                BW9_Full.place(x=3,y=108,width=1350,height=600)
            label_BW9 = Button(root, image=BW_9, bd=2, relief="groove",command=BW9_Button)
            label_BW9.place(x=711, y=390, width=236, height=250)
            Price_BW9 = Button(root, text="Rs-285")
            Price_BW9.place(x=711, y=640, width=236)

            def BW10_Button():
                BW10_Full = Button(root,image=BW_10,bg="white")
                BW10_Full.place(x=3,y=108,width=1350,height=600)
            label_BW10 = Button(root, image=BW_10, bd=2, relief="groove",command=BW10_Button)
            label_BW10.place(x=949, y=390, width=236, height=250)
            Price_BW10 = Button(root, text="Rs-285")
            Price_BW10.place(x=949, y=640, width=236)
        BW1()

    def tab_thor():
        thor_Page = Label(root, bg="black", fg="red", font="Times_New_Roman 25")
        thor_Page.pack()

        def thor1():
            def thor1_Button():
                thor1_Full = Label(root,image=thor_1,bg="white")
                thor1_Full.place(x=3,y=108,width=1350,height=600)
            label_thor1 = Button(root,image=thor_1, bd=2, relief="groove",command=thor1_Button)
            label_thor1.place(x=3, y=108, width=235, height=250)
            Price_thor1 = Button(root,text="Rs-285")
            Price_thor1.place(x=3,y=360,width=235)

            def thor2_Button():
                thor2_Full = Label(root, image=thor_2, bg="white")
                thor2_Full.place(x=3, y=108, width=1350, height=600)
            label_thor2 = Button(root, image=thor_2, bd=2, relief="groove", command=thor2_Button)
            label_thor2.place(x=240, y=108, width=236, height=250)
            Price_thor2 = Button(root, text="Rs-285")
            Price_thor2.place(x=240, y=360, width=236)

            def thor3_Button():
                thor3_Full = Button(root,image=thor_3,bg="white")
                thor3_Full.place(x=3,y=108,width=1350,height=600)
            label_thor3 = Button(root, image=thor_3, bd=2, relief="groove",command=thor3_Button)
            label_thor3.place(x=474, y=108, width=236, height=250)
            Price_thor3 = Button(root, text="Rs-285")
            Price_thor3.place(x=474, y=360, width=236)

            def thor4_Button():
                thor4_Full = Button(root,image=thor_4,bg="white")
                thor4_Full.place(x=3,y=108,width=1350,height=600)
            label_thor4 = Button(root, image=thor_4, bd=2, relief="groove",command=thor4_Button)
            label_thor4.place(x=711, y=108, width=236, height=250)
            Price_thor4 = Button(root, text="Rs-285")
            Price_thor4.place(x=711, y=360, width=236)

            def thor5_Button():
                thor5_Full = Button(root,image=thor_5,bg="white")
                thor5_Full.place(x=3,y=108,width=1350,height=600)
            label_thor5 = Button(root, image=thor_5, bd=2, relief="groove",command=thor5_Button)
            label_thor5.place(x=949, y=108, width=236, height=250)
            Price_thor5 = Button(root, text="Rs-285")
            Price_thor5.place(x=949, y=360, width=236)

            def thor6_Button():
                thor6_Full = Button(root,image=thor_6,bg="white")
                thor6_Full.place(x=3,y=108,width=1350,height=600)
            label_thor6 = Button(root, image=thor_6, bd=2, relief="groove",command=thor6_Button)
            label_thor6.place(x=3, y=390, width=235, height=250)
            Price_thor6 = Button(root, text="Rs-285")
            Price_thor6.place(x=3, y=640, width=235)

            def thor7_Button():
                thor7_Full = Button(root,image=thor_7,bg="white")
                thor7_Full.place(x=3,y=108,width=1350,height=600)
            label_thor7 = Button(root, image=thor_7, bd=2, relief="groove",command=thor7_Button)
            label_thor7.place(x=240, y=390, width=236, height=250)
            Price_thor7 = Button(root, text="Rs-285")
            Price_thor7.place(x=240, y=640, width=236)

            def thor8_Button():
                thor8_Full = Button(root,image=thor_8,bg="white")
                thor8_Full.place(x=3,y=108,width=1350,height=600)
            label_thor8 = Button(root, image=thor_8, bd=2, relief="groove",command=thor8_Button)
            label_thor8.place(x=474, y=390, width=236, height=250)
            Price_thor8 = Button(root, text="Rs-285")
            Price_thor8.place(x=474, y=640, width=236)

            def thor9_Button():
                thor9_Full = Button(root,image=thor_9,bg="white")
                thor9_Full.place(x=3,y=108,width=1350,height=600)
            label_thor9 = Button(root, image=thor_9, bd=2, relief="groove",command=thor9_Button)
            label_thor9.place(x=711, y=390, width=236, height=250)
            Price_thor9 = Button(root, text="Rs-285")
            Price_thor9.place(x=711, y=640, width=236)

            def thor10_Button():
                thor10_Full = Button(root,image=thor_10,bg="white")
                thor10_Full.place(x=3,y=108,width=1350,height=600)
            label_thor10 = Button(root, image=thor_10, bd=2, relief="groove",command=thor10_Button)
            label_thor10.place(x=949, y=390, width=236, height=250)
            Price_thor10 = Button(root, text="Rs-285")
            Price_thor10.place(x=949, y=640, width=236)
        thor1()

    def tab_hulk():
        hulk_Page = Label(root, bg="black", fg="red", font="Times_New_Roman 25")
        hulk_Page.pack()

        def hulk1():
            def hulk1_Button():
                hulk1_Full = Label(root,image=hulk_1,bg="white")
                hulk1_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk1 = Button(root,image=hulk_1, bd=2, relief="groove",command=hulk1_Button)
            label_hulk1.place(x=3, y=108, width=235, height=250)
            Price_hulk1 = Button(root,text="Rs-285")
            Price_hulk1.place(x=3,y=360,width=235)

            def hulk2_Button():
                hulk2_Full = Label(root, image=hulk_2, bg="white")
                hulk2_Full.place(x=3, y=108, width=1350, height=600)
            label_hulk2 = Button(root, image=hulk_2, bd=2, relief="groove", command=hulk2_Button)
            label_hulk2.place(x=240, y=108, width=236, height=250)
            Price_hulk2 = Button(root, text="Rs-285")
            Price_hulk2.place(x=240, y=360, width=236)

            def hulk3_Button():
                hulk3_Full = Button(root,image=hulk_3,bg="white")
                hulk3_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk3 = Button(root, image=hulk_3, bd=2, relief="groove",command=hulk3_Button)
            label_hulk3.place(x=474, y=108, width=236, height=250)
            Price_hulk3 = Button(root, text="Rs-285")
            Price_hulk3.place(x=474, y=360, width=236)

            def hulk4_Button():
                hulk4_Full = Button(root,image=hulk_4,bg="white")
                hulk4_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk4 = Button(root, image=hulk_4, bd=2, relief="groove",command=hulk4_Button)
            label_hulk4.place(x=711, y=108, width=236, height=250)
            Price_hulk4 = Button(root, text="Rs-285")
            Price_hulk4.place(x=711, y=360, width=236)

            def hulk5_Button():
                hulk5_Full = Button(root,image=hulk_5,bg="white")
                hulk5_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk5 = Button(root, image=hulk_5, bd=2, relief="groove",command=hulk5_Button)
            label_hulk5.place(x=949, y=108, width=236, height=250)
            Price_hulk5 = Button(root, text="Rs-285")
            Price_hulk5.place(x=949, y=360, width=236)

            def hulk6_Button():
                hulk6_Full = Button(root,image=hulk_6,bg="white")
                hulk6_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk6 = Button(root, image=hulk_6, bd=2, relief="groove",command=hulk6_Button)
            label_hulk6.place(x=3, y=390, width=235, height=250)
            Price_hulk6 = Button(root, text="Rs-285")
            Price_hulk6.place(x=3, y=640, width=235)

            def hulk7_Button():
                hulk7_Full = Button(root,image=hulk_7,bg="white")
                hulk7_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk7 = Button(root, image=hulk_7, bd=2, relief="groove",command=hulk7_Button)
            label_hulk7.place(x=240, y=390, width=236, height=250)
            Price_hulk7 = Button(root, text="Rs-285")
            Price_hulk7.place(x=240, y=640, width=236)

            def hulk8_Button():
                hulk8_Full = Button(root,image=hulk_8,bg="white")
                hulk8_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk8 = Button(root, image=hulk_8, bd=2, relief="groove",command=hulk8_Button)
            label_hulk8.place(x=474, y=390, width=236, height=250)
            Price_hulk8 = Button(root, text="Rs-285")
            Price_hulk8.place(x=474, y=640, width=236)

            def hulk9_Button():
                hulk9_Full = Button(root,image=hulk_9,bg="white")
                hulk9_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk9 = Button(root, image=hulk_9, bd=2, relief="groove",command=hulk9_Button)
            label_hulk9.place(x=711, y=390, width=236, height=250)
            Price_hulk9 = Button(root, text="Rs-285")
            Price_hulk9.place(x=711, y=640, width=236)

            def hulk10_Button():
                hulk10_Full = Button(root,image=hulk_10,bg="white")
                hulk10_Full.place(x=3,y=108,width=1350,height=600)
            label_hulk10 = Button(root, image=hulk_10, bd=2, relief="groove",command=hulk10_Button)
            label_hulk10.place(x=949, y=390, width=236, height=250)
            Price_hulk10 = Button(root, text="Rs-285")
            Price_hulk10.place(x=949, y=640, width=236)
        hulk1()








    CA_Button = Button(heading, text="Caiptain", command=tab_CA, bg="grey", fg="red", activebackground="blue")
    CA_Button.place(x=125, y=76,width=120,height=30)
    IM_Button = Button(heading, text="Iron Man", command=tab_IM, bg="grey", fg="red", activebackground="blue")
    IM_Button.place(x=247, y=76,width=120,height=30)
    BW_Button = Button(heading, text="Black Widow", command=tab_BW, bg="grey", fg="red", activebackground="blue")
    BW_Button.place(x=369, y=76,width=120,height=30)
    thor_Button = Button(heading, text="Thor", command=tab_thor, bg="grey", fg="red", activebackground="blue")
    thor_Button.place(x=491, y=76,width=120,height=30)
    hulk_Button = Button(heading, text="Hulk", command=tab_hulk, bg="grey", fg="red", activebackground="blue")
    hulk_Button.place(x=613, y=76,width=120,height=30)
def home():
    Home_Page = Label(root,text="Home Page",image=image_logo_larger)
    Home_Page.place(x=0,y=105)
Home_Button=Button(heading,text="Home",bg="grey",fg="red",activebackground="blue",command=home)
Home_Button.place(x=3,y=76,width=120,height=30)

global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
def signup():
    default_home.destroy()



    reg = Label(root, text="Create Account", fg="red", font=(None, 25)).place(x=400, y=140)
    firstname = Label(root, text="First Name",font="arial 15 bold").place(x=45, y=200)
    middlename = Label(root, text="Middle Name",font="arial 15 bold").place(x=30, y=280)
    lastname = Label(root, text="Last Name",font="arial 15 bold").place(x=55, y=360)
    mobile = Label(root, text="Mobile",font="arial 15 bold").place(x=55, y=440)

    gender = Label(root, text="Gender", font="arial 15 bold").place(x=600, y=200)
    email = Label(root, text="email", font="arial 15 bold").place(x=600, y=280)
    User = Label(root, text="User Name", font="arial 15 bold").place(x=570, y=360)
    password = Label(root, text="Create Password", font="arial 15 bold").place(x=510, y=440)

    e1 = Entry(root)
    e1.place(x=170, y=200,width=250,height=30)

    e2 = Entry(root)
    e2.place(x=170, y=280,width=250,height=30)

    e3 = Entry(root)
    e3.place(x=170, y=360,width=250,height=30)

    e4 = Entry(root)
    e4.place(x=170, y=440,width=250,height=30)

    e5 = Entry(root)
    e5.place(x=690, y=200,width=250,height=30)

    e6 = Entry(root)
    e6.place(x=690, y=280,width=250,height=30)

    e7 = Entry(root)
    e7.place(x=690, y=360,width=250,height=30)

    e8 = Entry(root)
    e8.place(x=690, y=440, width=250, height=30)

    db = sql.connect(host="localhost", user="root", password="naved786", database="")
    cursor = db.cursor()

    def create_table():
        try:
            cursor.execute("""CREATE TABLE Dummy(firstname VARCHAR(30),
                              middlename VARCHAR(30),
                              lastname VARCHAR(30),
                              gender VARCHAR(10),
                              mobile VARCHAR(10),
                              email VARCHAR(50),
                              user VARCHAR(50),
                              password VARCHAR(25))""")
        except:
            print("Table already created")

    def submit():
        sql = """INSERT INTO Dummy (firstname,lastname,gender,mobile,email,user,password)
                                    VALUE(%s,%s,%s,%s,%s,%s,%s)"""
        values = (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e5.get(), e6.get(), e7.get())
        cursor.execute(sql, values)
        db.commit()

    submit = Button(root, text="Submit", command=submit, bg="black", fg="white").place(x=470, y=550,width=120,height=30)

def login():
    default_home.destroy()
    global E1
    global E2

    username = Label(root, text="User Name", font="arial 15 bold").place(x=55, y=300)
    password = Label(root, text="Password", font="arial 15 bold").place(x=600, y=300)

    E1 = Entry(root)
    E1.place(x=170,y=300, width=250, height=30)
    E2 = Entry(root)
    E2.place(x=710,y=300, width=250, height=30)

    def login_command():
        mysqldb =sql.connect(host="localhost",user="root",password="naved786",database="mysql")
        mycursor = mysqldb.cursor()

        uname = e7.get()
        pswrd = e8.get()

        sql1 = "select * from Dummy where user = %s and password = %s"
        mycursor.execute(sql1,[(user),(password)])
        result = mycursor.fetchall()
        if result:
            messagebox.showinfo("Login Success")
            root.destroy()
        else:
            messagebox.showinfo(("Loging is not Success"))

    logIn = Button(root, text="login", command=login_command, bg="black", fg="white").place(x=470, y=550, width=120,
                                                                                       height=30)





Login_button = Button(heading,text="LOGIN",command=login,bg="red",fg="black")
Login_button.place(x=920,y=76,width=120,height=30)
signup_button = Button(heading,text="SIGN UP",command=signup,bg="red",fg="black")
signup_button.place(x=1043,y=76,width=120,height=30)





tab1()
root.mainloop()