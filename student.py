from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognisation_system")
        #FIRST IMAGE
        img=Image.open(r"C:\Users\rampi\Desktop\FACE RECGNISATION\college_image\edu.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        #=======variable=====
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semister=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_radio1=StringVar()
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        #SECOND IMAGE
        img1=Image.open(r"C:\Users\rampi\Desktop\FACE RECGNISATION\college_image\gp.JFIF")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #THIRD IMAGE
        img2=Image.open(r"C:\Users\rampi\Desktop\FACE RECGNISATION\college_image\pg.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2 )
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        
        #bg image
        img3=Image.open(r"C:\Users\rampi\Desktop\FACE RECGNISATION\college_image\k.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3 )
        bg_img.place(x=0,y=130,width=1530,height=710) 
        
        
        title_lbl=Label(bg_img,text="STUDENTS MANAGEMENT SYSTEM",font=('time new roman',35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        #Left side lable frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=780,height=580)
        
        img_left=Image.open(r"C:\Users\rampi\Desktop\FACE RECGNISATION\college_image\std.jpg")
        img_left=img_left.resize((400,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=400,height=130)
        
        img_left1=Image.open(r"C:\Users\rampi\Desktop\FACE RECGNISATION\college_image\edu.jpg")
        img_left1=img_left1.resize((400,130),Image.ANTIALIAS)
        self.photoimg_left1=ImageTk.PhotoImage(img_left1)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left1)
        f_lbl.place(x=400,y=0,width=400,height=130)
        
        #current Course information
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Informatoin",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=120,width=770,height=120)
        
        
        #Department
        dep_lable=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Math","Statistic")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_lable=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=10)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","B.sc","ITI","BE","M.Sc.","PHD")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W )
        
        #Year
        year_lable=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=10)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W )
        
        
        #Semister
        sem_lable=Label(current_course_frame,text="Semister",font=("times new roman",12,"bold"),bg="white")
        sem_lable.grid(row=1,column=2,padx=10)
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semister,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select_sem","Semster_l","Semister_ll")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W )
        
        #Class_Student_information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Informatoin",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=240,width=770,height=300)
        
        
        #StudentId Entry
        studentId_lable=Label(class_student_frame,text='Student_id:',font=("times new roman",13,"bold"),bg="white")
        studentId_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Student Name
        studentname_lable=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentname_lable.grid(row=0,column=2,padx=10,pady=5 ,sticky=W)
        
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        #Class Division
        student_div_lable=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        student_div_lable.grid(row=1,column=0,padx=10,pady=5 ,sticky=W)
        
        student_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        student_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #Roll No.
        student_rollno_lable=Label(class_student_frame,text="Roll No.:",font=("times new roman",13,"bold"),bg="white")
        student_rollno_lable.grid(row=1,column=2,padx=10,pady=5 ,sticky=W)
        
        student_rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        student_rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #Gender
        student_gender_lable=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        student_gender_lable.grid(row=2,column=0,padx=10,pady=5 ,sticky=W)
        
        student_gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        student_gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #Email
        student_email_lable=Label(class_student_frame,text="EmailId:",font=("times new roman",13,"bold"),bg="white")
        student_email_lable.grid(row=2,column=2,padx=10,pady=5 ,sticky=W)
        
        student_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        student_email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #DOB
        student_dob_lable=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        student_dob_lable.grid(row=3,column=0,padx=10,pady=5 ,sticky=W)
        
        student_dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        student_dob_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #Phone No.
        student_phone_lable=Label(class_student_frame,text="Mobile No.:",font=("times new roman",13,"bold"),bg="white")
        student_phone_lable.grid(row=3,column=2,padx=10,pady=5 ,sticky=W)
        
        student_phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        student_phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
        #Address
        student_add_lable=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        student_add_lable.grid(row=4,column=0,padx=10,pady=5 ,sticky=W)
        
        student_add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        student_add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="Take a photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No a photo sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #Buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=763,height=40)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)
        
        update_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)
        
        
        delete_btn=Button(btn_frame,text="Delete",width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)
        
        
        reaset_btn=Button(btn_frame,text="Reset",width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reaset_btn.grid(row=0,column=4)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=763,height=35)
        
        
        take_photo_btn=Button(btn_frame1,text="Take photo sample",width=40,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        
        update_photo_btn=Button(btn_frame1,text="Update photo",width=40,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        #Right side lable frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=830,y=10,width=660,height=580)
        
        #Right Image
        img_right=Image.open(r"C:\Users\rampi\Desktop\FACE RECGNISATION\college_image\n.jpg")
        img_right=img_right.resize((650,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=650,height=130)
    
        search_student_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search Students",font=("times new roman",12,"bold"))
        search_student_frame.place(x=5,y=125,width=645,height=113)
        
        search_lable=Label(search_student_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        
        search_combo=ttk.Combobox(search_student_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W )
        
        
        
        search_entry=ttk.Entry(search_student_frame,width=11,font=("times new roman",16,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        search_btn=Button(search_student_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
        
        showall_btn=Button(search_student_frame,text="Show_all",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)
        
        #=====table Frame=======
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=210,width=642,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","photo","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
    
     # ================Function Declearation====================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==" " or self.va_std_id.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user= "root" , password="ram123", autocommit=True,database='face_recgnization',auth_plugin = 'mysql_native_password'
                )
                
                    
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semister.get(),
                                                                                                        self.va_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_radio1.get()
                                                                        
                                                                                                        
                                                                                                                                  ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success","Student record has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()           