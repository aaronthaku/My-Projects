from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import math,random
import time
import os
import datetime
class BURGER_HOUSE:
    def __init__(self):
    #main window
        self.window = Tk()
        self.window.configure(bg="black")
        self.window.geometry("1000x800+100+50")
        self.window.title("Restaurant Billing System Admin Login ")
        self.window.resizable(False,False)
        
        self.Frame0=Frame(self.window,bg="#d44942" ,bd=20,relief=GROOVE)
        self.Frame0.place(x=300,y=150,width=395,height=450)
        
        Label(self.Frame0,text="",bg="#d44942").grid(row=0,column=0)
        Label(self.Frame0,text="Admin Login",font=("stoneage Bt",30,"bold"),bg="#d44942").grid(row=0)
        Label(self.Frame0,text="",bg="#d44942").grid(row=1)
        
        self.username_verify = StringVar()
        self.password_verify = StringVar()
        
        Label(self.Frame0,text="",bg="#d44942").grid(row=3)
        Label(self.Frame0, text = "Username :",font=("times new roman",20,"bold"),bg ="#d44942" ).grid(row=3,column=0)
        self.username_entry1 = Entry(self.Frame0, textvariable = self.username_verify,width= 20,font="arial 15",bd=7,relief=SUNKEN)
        self.username_entry1.grid(row=4)
       
        Label(self.Frame0, text = "",bg="#d44942" ).grid(row=5)
        Label(self.Frame0,text = "Password :",font=("times new roman",20,"bold"),bg="#d44942").grid(row=6,column=0) 
        self.password_entry1 = Entry(self.Frame0, textvariable = self.password_verify,width= 20,show="*",font="arial 15",bd=7,relief=SUNKEN)
        self.password_entry1.grid(row=7)  

        Label(self.Frame0,text="",bg="#d44942").grid(row=8,column=0)
        Label(self.Frame0, text = "",bg="#d44942" ).grid(row=10)
        Button(self.Frame0, text = "Login", font="arial 15",bd=7,width=13,command = self.login_verify).grid(row=11,column=0,sticky="w")
        Button(self.Frame0, text = "Register",font="arial 15",bd=7,width=13, command = self.register).grid(row=11,columnspan=1,sticky="e")
       
        Label(self.Frame0,text="",bg="#d44942").grid(row=12,column=3)
        localtime=time.asctime(time.localtime(time.time()))
        lblInfo=Label(self.Frame0,font=('arial',20,'bold'),text=localtime,bg="#d44942" ,bd=10,anchor='w').grid(row=13)
        Label(self.Frame0, text = "",bg="#d44942" ).grid(row=14, column=0,columnspan=3)
        
        self.window.mainloop()
    
    #registring window
    def register(self):
        self.window1 = Toplevel(self.window)
        self.window1.title("register")
        self.window1.geometry("600x300+100+50")
        self.window1.configure(bg="#d44942")        
        
        self.username = StringVar()
        self.password = StringVar()
        
        Label(self.window1, text = "Please enter details below",font=("stoneage Bt",30,"bold"),bg="#d44942" ).pack()
        Label(self.window1, text = "",bg="#d44942").pack()
        Label(self.window1, text = "Username * ",font=("times new roman",20,"bold"),bg="#d44942" ).pack()

        username_entry = Entry(self.window1, textvariable = self.username,width= 20,font="arial 15",bd=7,relief=SUNKEN)
        username_entry.pack()
        Label(self.window1, text = "Password * ",font=("times new roman",20,"bold"),bg="#d44942" ).pack()
        password_entry =  Entry(self.window1, textvariable = self.password,width= 20,font="arial 15",bd=7,relief=SUNKEN)
        password_entry.pack()
        Label(self.window1, text = "",bg="#d44942" ).pack()
        Button(self.window1, text = "Register",font=("areial",15),width = 13,bd=7,command = self.register_user).pack()
         
    def register_user(self):
        username_information = self.username.get()
        password_information = self.password.get()
        if username_information == ""and password_information == "":
            try:
                raise ZeroDivisionError
          
            except ZeroDivisionError:
              messagebox.showerror("error","Enter Username and Password")
              self.window1.destroy()
        
        else:
            file=open(username_information, "w")
            file.write(username_information+"\n")
            file.write(password_information)
            file.close()
            messagebox.showinfo("message","Username and Password is sucessfully registered!") 
            self.window1.destroy()
            
    def login_verify(self):
        self.username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        self.username_entry1.delete(0, END)
        self.password_entry1.delete(0, END)
        
        list_of_files = os.listdir()
        if self.username1 in list_of_files:
            file1 = open(self.username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
              self.secondscreen()
            else:
              messagebox.showerror("Password Error", "Please enter correct Password ! Incorrect Password")         

        else:
            messagebox.showerror("User Not Found", "User Not Found")

    def secondscreen(self):
        self.root1=Toplevel(self.window) 
        self.root1.geometry("1650x950")
        self.root1.title("Restaurant Billing System")
        bg_color="#d44942"
        title =Label(self.root1,text="THE    BURGER    HOUSE",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",35,"bold"),pady=2).pack(fill=X)

#======================Variables=================================
   #=========Beverages=============
        self.cappaccino=IntVar()
        self.latte=IntVar()
        self.americano=IntVar()
        self.moccha=IntVar()
        self.espresso=IntVar()
        self.mineral=IntVar()
        self.diet=IntVar()
#=============Burger and Pizza==========
        self.chicken_burger=IntVar()
        self.ham_burger=IntVar()
        self.veg_burger=IntVar()
        self.special_burger=IntVar()
        self.buff_pizza=IntVar()
        self.chicken_pizza=IntVar()
        self.cheese_pizza=IntVar()
#=========Mo:Mo and Chowmein===========
        self.veg_chowmein=IntVar()
        self.buff_chowmein=IntVar()
        self.chicken_chowmein=IntVar()
        self.buff_momo=IntVar()
        self.chicken_momo=IntVar()
        self.veg_momo=IntVar()
        self.c_momo=IntVar()
#==========Product total price=============
        self.beverages_price=StringVar()
        self.burger_price=StringVar()
        self.momoandchowmein_price=StringVar()
        self.total_price=StringVar()
#============customers Details==================
        self.cusname=StringVar()
        self.cusphn=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()
#========Customer Detail Frame==============
        Frame1=LabelFrame(self.root1,bd=10,relief=GROOVE,text="Customer Detail",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        Frame1.place(x=0,y=80,relwidth=1)        

        Cusname_lbl=Label(Frame1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        Cusname_txt=Entry(Frame1,width=15,textvariable=self.cusname,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5)

        Cusphn_lbl=Label(Frame1,text="Contact No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        Cusphn_txt=Entry(Frame1,width=10,textvariable=self.cusphn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5)

    
#==================Beverage===============
        Frame2=LabelFrame(self.root1,bd=12,relief=GROOVE,text="Beverages",font=("times new roman",15,"bold"),pady=2,fg="gold",bg="Black")
        Frame2.place(x=10,y=180,width=330,height=460) 

        cappaccino_lbl=Label(Frame2,text="Cappaccino",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=0,column=0,padx=5,pady=5,sticky="w")
        cappaccino_txt=Entry(Frame2,width=10,textvariable=self.cappaccino,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10)

        latte_lbl=Label(Frame2,text="Cafe Latte",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=1,column=0,padx=5,pady=5,sticky="w")
        latte_txt=Entry(Frame2,width=10,textvariable=self.latte,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10)
        
        americano_lbl=Label(Frame2,text="Cafe Americano",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=2,column=0,padx=5,pady=5,sticky="w")
        americano_txt=Entry(Frame2,width=10,textvariable=self.americano,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10)
                
        moccha_lbl=Label(Frame2,text="Cafe Moccha",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=3,column=0,padx=5,pady=5,sticky="w")
        moccha_txt=Entry(Frame2,width=10,textvariable=self.moccha,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10)
        
        espresso_lbl=Label(Frame2,text="Espresso Solo",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=4,column=0,padx=5,pady=5,sticky="w")
        espresso_txt=Entry(Frame2,width=10,textvariable=self.espresso,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10)
       
        mineral_lbl=Label(Frame2,text="Mineral Water",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=6,column=0,padx=5,pady=5,sticky="w")
        mineral_txt=Entry(Frame2,width=10,textvariable=self.mineral,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=6,column=1,pady=10)
        
        diet_lbl=Label(Frame2,text="Diet COke/Pepsi",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=7,column=0,padx=5,pady=5,sticky="w")
        diet_txt=Entry(Frame2,width=10,textvariable=self.diet,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=7,column=1,pady=10)
        
        #==============Burger ad pizza===========
        
        Frame3=LabelFrame(self.root1,bd=12,relief=GROOVE,text="Burger and Pizza",font=("times new roman",15,"bold"),pady=2,fg="gold",bg="Black")
        Frame3.place(x=345,y=180,width=350,height=460) 

        ccb_lbl=Label(Frame3,text="C.Chicken Burger",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=0,column=0,padx=5,pady=5,sticky="w")
        ccb_txt=Entry(Frame3,width=10,textvariable=self.chicken_burger,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10)

        hamb_lbl=Label(Frame3,text="Ham Burger",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=1,column=0,padx=5,pady=5,sticky="w")
        hamb_txt=Entry(Frame3,width=10,textvariable=self.ham_burger,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10)
        
        veg_lbl=Label(Frame3,text="Veg Burger",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=2,column=0,padx=5,pady=5,sticky="w")
        veg_txt=Entry(Frame3,width=10,textvariable=self.veg_burger,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10)
                
        mix_lbl=Label(Frame3,text="Our Special Burger",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=3,column=0,padx=5,pady=5,sticky="w")
        mix_txt=Entry(Frame3,width=10,textvariable=self.special_burger,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10)
        
        buffpizza_lbl=Label(Frame3,text="Buff Pizza",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=4,column=0,padx=5,pady=5,sticky="w")
        buffpizza_txt=Entry(Frame3,width=10,textvariable=self.buff_pizza,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10)
       
        chickenpizza_lbl=Label(Frame3,text="Chicken Pizza",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=5,column=0,padx=5,pady=5,sticky="w")
        chickenpizza_txt=Entry(Frame3,width=10,textvariable=self.chicken_pizza,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=5,column=1,pady=10)
        
        cheesepizza_lbl=Label(Frame3,text="Cheese Pizza",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=6,column=0,padx=5,pady=5,sticky="w")
        cheesepizza_txt=Entry(Frame3,width=10,textvariable=self.cheese_pizza,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=6,column=1,pady=10)
        
     #=============Mo:Mo and  chowmein==========================
        Frame4=LabelFrame(self.root1,bd=12,relief=GROOVE,text="Mo:Mo & Chowmein",font=("times new roman",15,"bold"),pady=2,fg="gold",bg="Black")
        Frame4.place(x=700,y=180,width=350,height=460) 

        chickenmomo_lbl=Label(Frame4,text="Chicken Mo:Mo",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=0,column=0,padx=5,pady=5,sticky="w")
        chickenmomo_txt=Entry(Frame4,width=10,textvariable=self.chicken_momo,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10)

        buffmomo_lbl=Label(Frame4,text="Buff Mo:Mo",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=1,column=0,padx=5,pady=5,sticky="w")
        buffmomo_txt=Entry(Frame4,width=10,textvariable=self.buff_momo,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10)
        
        vegmomo_lbl=Label(Frame4,text="Veg Mo:Mo",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=2,column=0,padx=5,pady=5,sticky="w")
        vegmomo_txt=Entry(Frame4,width=10,textvariable=self.veg_momo,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10)
                
        chickenchowmein_lbl=Label(Frame4,text="Chicken Chowmein",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=3,column=0,padx=5,pady=5,sticky="w")
        chickenchowmein_txt=Entry(Frame4,width=10,textvariable=self.chicken_chowmein,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10)
        
        buffchowmein_lbl=Label(Frame4,text="Buff Chowmein",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=4,column=0,padx=5,pady=5,sticky="w")
        buffchowmein_txt=Entry(Frame4,width=10,textvariable=self.buff_chowmein,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10)
       
        vegchowmein_lbl=Label(Frame4,text="Veg Chowmein",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=5,column=0,padx=5,pady=5,sticky="w")
        vegchowmein_txt=Entry(Frame4,width=10,textvariable=self.veg_chowmein,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=5,column=1,pady=10)
        
        cmomo_lbl=Label(Frame4,text="Buff/Chicken C ",font=("times new roman",16,"bold"),bg="black",fg="#ffff00").grid(row=6,column=0,padx=5,pady=5,sticky="w")
        cmomo_txt=Entry(Frame4,width=10,textvariable=self.c_momo,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=6,column=1,pady=10)
        
#==================Bill Part==============================================

        Frame5=LabelFrame(self.root1,bd=12,relief=GROOVE,text="Restaurant Billing Area",font=("times new roman",15,"bold"),pady=2,fg="gold",bg=bg_color)
        Frame5.place(x=1055,y=180,width=465,height=470)       
        scrol_y=Scrollbar(Frame5,orient=VERTICAL)
        self.txtarea=Text(Frame5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

#================================Buttons=============================
        Frame6=LabelFrame(self.root1,bd=12,relief=GROOVE,text="Order Billing",font=("times new roman",15,"bold"),pady=2,fg="gold",bg=bg_color)
        Frame6.place(x=0,y=645,relwidth=1,height=145) 
        
        o1=Label(Frame6,text="Total Beverages Price",fg="white",bg=bg_color,font=("times new roman",13,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        o1_txt=Entry(Frame6,width=10,textvariable=self.beverages_price,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=0,pady=2)
        
        o2=Label(Frame6,text="Total Burger and Pizza Price",fg="white",bg=bg_color,font=("times new roman",13,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        o2_txt=Entry(Frame6,width=10,textvariable=self.burger_price,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=0,pady=2)
        
        o3=Label(Frame6,text="Total Mo:Mo & Chowmein Price",fg="white",bg=bg_color,font=("times new roman",13,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        o3_txt=Entry(Frame6,width=10,textvariable=self.momoandchowmein_price,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=0,pady=2)
        
        vatbp=Label(Frame6,text="Total Price",fg="white",bg=bg_color,font=("times new roman",13,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        vatbp_txt=Entry(Frame6,width=10,textvariable=self.total_price,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=0,pady=2)
         
#+=============================button Frame========================

        Frame7=Frame(Frame6,bd=6,relief=GROOVE)
        Frame7.place(x=750,width=705,height=90)

        tbtn=Button(Frame7,command=self.total,text="Total",bg="black",fg="white",bd=6,pady=10,width=12,font=("times new roman",15,"bold")).grid(row=0,column=1,padx=5,pady=5)
        billbtn=Button(Frame7,text="Generate Bill",command=self.rbilling_a,bg="black",fg="white",bd=6,pady=10,width=12,font=("times new roman",15,"bold")).grid(row=0,column=2,padx=5,pady=5)
        cbtn=Button(Frame7,text="Clear",command=self.clear,bg="black",fg="white",bd=6,pady=10,width=12,font=("times new roman",15,"bold")).grid(row=0,column=3,padx=5,pady=5)
        exitbtn=Button(Frame7,text="Exit",command=self.exit,bg="black",fg="white",bd=6,pady=10,width=12,font=("times new roman",15,"bold")).grid(row=0,column=4,padx=5,pady=5)
        
        self.wcnote_bill()

    def total(self):
        self.b_cappaccino_p=self.cappaccino.get()*120
        self.b_latte_p=self.latte.get()*150
        self.b_americano_p=self.americano.get()*120
        self.b_moccha_p=self.moccha.get()*180
        self.b_mineral_p=self.mineral.get()*40
        self.b_diet_p=self.diet.get()*85
        self.b_espresso_p=self.espresso.get()*160

        self.total_beverages_price=float(
                                        self.b_cappaccino_p +
                                        self.b_latte_p +
                                        self.b_americano_p +
                                        self.b_moccha_p +
                                        self.b_mineral_p +
                                        self.b_diet_p +
                                        self.b_espresso_p
                                        )
        self.beverages_price.set("Rs. "+str(self.total_beverages_price))
        
        self.bp_chicken_burger_p=self.chicken_burger.get()*210
        self.bp_ham_burger_p=self.ham_burger.get()*165
        self.bp_veg_burger_p=self.veg_burger.get()*145
        self.bp_special_burger_p=self.special_burger.get()*280
        self.bp_buff_pizza_p=self.buff_pizza.get()*360
        self.bp_chicken_pizza_p=self.chicken_pizza.get()*320
        self.bp_cheese_pizza_p=self.cheese_pizza.get()*290
        
        self.total_burger_price=float(
                                        self.bp_chicken_burger_p +
                                        self.bp_ham_burger_p +
                                        self.bp_veg_burger_p +
                                        self.bp_special_burger_p +
                                        self.bp_buff_pizza_p+
                                        self.bp_chicken_pizza_p +
                                        self.bp_cheese_pizza_p
                                      )
        self.burger_price.set("Rs. "+str(self.total_burger_price))                                   
      
        self.mc_veg_chowmein_p=self.veg_chowmein.get()*155
        self.mc_buff_chowmein_p=self.buff_chowmein.get()*160
        self.mc_chicken_chowmein_p=self.chicken_chowmein.get()*175
        self.mc_buff_momo_p=self.buff_momo.get()*145
        self.mc_chicken_momo_p=self.chicken_momo.get()*160
        self.mc_veg_momo_p=self.veg_momo.get()*125
        self.mc_c_momo_p=self.c_momo.get()*200
       
        self.total_momoandchowmein_price=float(
                                        self.mc_veg_chowmein_p +
                                        self.mc_buff_chowmein_p +
                                        self.mc_chicken_chowmein_p +
                                        self.mc_buff_momo_p +
                                        self.mc_chicken_momo_p +
                                        self.mc_veg_momo_p +
                                        self.mc_c_momo_p
                                    )
        self.momoandchowmein_price.set("Rs. "+str(self.total_momoandchowmein_price)) 

        self.wholetotal_bill = float(
                                    self.total_beverages_price +
                                    self.total_burger_price +
                                    self.total_momoandchowmein_price 
                                    
                                    )
        
        self.total_price.set(float(self.wholetotal_bill))
                                   
 #==========================================================================================================================================     
             
    def wcnote_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\tWELCOME TO THE BURGER HOUSE BILLING SYSTEM\n\n")

        self.txtarea.insert(END,f'\n Bill Number : {self.bill_no.get()}')
        self.txtarea.insert(END,f"\n Customer Name:{self.cusname.get()}")
        self.txtarea.insert(END,f"\n Contact Number:{self.cusphn.get()}\n")
        self.txtarea.insert(END,f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
        self.txtarea.insert(END,f"\nProduct\t\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
    def rbilling_a(self):
        if self.cusname.get()==""or self.cusphn.get()=="":
            messagebox.showerror("Error Found","You must enter Customer details.")
        elif self.beverages_price.get()=="Rs. 0.0" and self.burger_price.get()=="Rs. 0.0" and self.momoandchowmein_price.get()=="Rs. 0.0":
            messagebox.showerror("Error Found","No any food item has been selected.")
        else:
            self.wcnote_bill()             
   #===============Beverages=================    
       
        if self.cappaccino.get()!=0:
            self.txtarea.insert(END,f"\n\nCappaccino\t\t\t{self.cappaccino.get()}\t\t{self.b_cappaccino_p}")
                                     
        if self.latte.get()!=0:
            self.txtarea.insert(END,f"\n\nCafe Latte\t\t\t{self.latte.get()}\t\t{self.b_latte_p}")

        if self.americano.get()!=0:
            self.txtarea.insert(END,f"\n\nCafe Americano\t\t\t{self.americano.get()}\t\t{self.b_americano_p}")
        if self.moccha.get()!=0:
           self.txtarea.insert(END,f"\n\nCafe Moccha\t\t\t{self.moccha.get()}\t\t{self.b_moccha_p}")
       
        if self.mineral.get()!=0:
           self.txtarea.insert(END,f"\n\nMineral Water\t\t\t{self.mineral.get()}\t\t{self.b_mineral_p}")
       
        if self.diet.get()!=0:
            self.txtarea.insert(END,f"\n\nDiet Coke/Pepsi\t\t\t{self.diet.get()}\t\t{self.b_diet_p}")
       
        if self.espresso.get()!=0:
            self.txtarea.insert(END,f"\n\nEspresso\t\t\t{self.espresso.get()}\t\t{self.b_espresso_p}")

#======================MoMO and chowmein==============
        if self.veg_chowmein.get()!=0:
            self.txtarea.insert(END,f"\n\nVeg Chowmein\t\t\t{self.veg_chowmein.get()}\t\t{self.mc_veg_chowmein_p}")
                                    
        if self.chicken_chowmein.get()!=0:
            self.txtarea.insert(END,f"\n\nChicken Chowmein\t\t\t{self.chicken_chowmein.get()}\t\t{self.mc_chicken_chowmein_p}")

        if self.buff_chowmein.get()!=0:
            self.txtarea.insert(END,f"\n\nBuff Chowmein\t\t\t{self.buff_chowmein.get()}\t\t{self.mc_buff_chowmein_p}")

        if self.buff_momo.get()!=0:
            self.txtarea.insert(END,f"\n\nBuff Mo:Mo\t\t\t{self.buff_momo.get()}\t\t{self.mc_buff_momo_p}")
        
        if self.c_momo.get()!=0:
            self.txtarea.insert(END,f"\n\nC.Mo:Mo\t\t\t{self.c_momo.get()}\t\t{self.mc_c_momo_p}")
       
        if self.chicken_momo.get()!=0:
            self.txtarea.insert(END,f"\n\nChicken Mo:Mo\t\t\t{self.chicken_momo.get()}\t\t{self.mc_chicken_momo_p}")
       
        if self.veg_momo.get()!=0:
            self.txtarea.insert(END,f"\n\nVeg Mo:Mo\t\t\t{self.veg_momo.get()}\t\t{self.mc_veg_momo_p}")
        
       
        #======================Burger and Pizza==============
        if self.chicken_burger.get()!=0:
            self.txtarea.insert(END,f"\n\nCrunchyChicken Burger\t\t\t{self.chicken_burger.get()}\t\t{self.bp_chicken_burger_p}")
                                    
        if self.ham_burger.get()!=0:
            self.txtarea.insert(END,f"\n\nHam Burger\t\t\t{self.ham_burger.get()}\t\t{self.bp_ham_burger_p}")

        if self.veg_burger.get()!=0:
            self.txtarea.insert(END,f"\n\nVeg BUrger\t\t\t{self.veg_burger.get()}\t\t{self.bp_veg_burger_p}")

        if self.special_burger.get()!=0:
            self.txtarea.insert(END,f"\n\nOur Special Burger\t\t\t{self.special_burger.get()}\t\t{self.bp_special_burger_p}")
       
        if self.cheese_pizza.get()!=0:
           self.txtarea.insert(END,f"\n\nCheese Pizza\t\t\t{self.cheese_pizza.get()}\t\t{self.bp_cheese_pizza_p}")
        
        if self.chicken_pizza.get()!=0:
            self.txtarea.insert(END,f"\n\nChicken Pizza\t\t\t{self.chicken_pizza.get()}\t\t{self.bp_cheese_pizza_p}")
       
        if self.buff_pizza.get()!=0:
            self.txtarea.insert(END,f"\n\nBuff Pizza\t\t\t{self.buff_pizza.get()}\t\t{self.bp_buff_pizza_p}")
        
        self.txtarea.insert(END,f"\n\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
        
        if self.total_price.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n\nTotal Price\t\t\t\t\t{self.total_price.get()}")
        
        self.txtarea.insert(END,f"\n\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
        
        self.txtarea.insert(END,f"\n\nTotal Bill :\t\t\t\t\tRs. {float(self.wholetotal_bill)}")
        self.txtarea.insert(END,f"\n\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
        
        self.txtarea.insert(END,f"\n\n\n\n\n --------Thanks for visiting our Restaurant!--------")
        self.txtarea.insert(END,f"\n --------------Please visit again!!!----------------")
    
    def clear(self):
        op=messagebox.askyesno("Clear","Are you sure you want to Clear?")
        if op>0:

            #=========Beverages=============
            self.cappaccino.set(0)
            self.latte.set(0)
            self.americano.set(0)
            self.moccha.set(0)
            self.espresso.set(0)
            self.mineral.set(0)
            self.diet.set(0)
    #=============Burger and Pizza==========
            self.chicken_burger.set(0)
            self.ham_burger.set(0)
            self.veg_burger.set(0)
            self.special_burger.set(0)
            self.buff_pizza.set(0)
            self.chicken_pizza.set(0)
            self.cheese_pizza.set(0)
    #=========Mo:Mo and Chowmein===========
            self.veg_chowmein.set(0)
            self.buff_chowmein.set(0)
            self.chicken_chowmein.set(0)
            self.buff_momo.set(0)
            self.chicken_momo.set(0)
            self.veg_momo.set(0)
            self.c_momo.set(0)
    #==========Product total price=============
            self.beverages_price.set("")
            self.burger_price.set("")
            self.momoandchowmein_price.set("")
    #============customers Details==================
            self.cusname.set("")
            self.cusphn.set("")
        
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.wcnote_bill()

    def exit(self):
        op=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if op>0:
            self.root1.destroy()

obj=  BURGER_HOUSE()
