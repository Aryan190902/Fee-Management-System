from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Student():
    def __init__(self, root):
        self.root = root
        self.root.title("Fee Management System")
        self.root.geometry("1576x900")

        # All Variables
        self.name_var = StringVar()
        self.date_var = StringVar()
        self.instru_var = StringVar()
        self.amount_var = StringVar()

        self.type_var = StringVar()
        self.search_var = StringVar()

        name = Label(self.root, text='Fee Management System',
         font=('Courier New', 40, 'bold'), bg='cyan',
          fg='white', borderwidth=2, relief='solid')
        name.pack(side=TOP, fill=X)
        # ---------------- To fill details ----------------
        fillDetails = Frame(self.root, borderwidth=2, relief='solid', bg='red')
        fillDetails.place(x=10, y=75, width=400, height=715)
        # Title
        fillTitle = Label(fillDetails, text = "Details", font=('Courier New', 25, 'bold'))
        fillTitle.grid(row=0, columnspan=2, padx=125)
        # Name
        name_label = Label(fillDetails, text="Name: ",
        font=('Courier New', 20, 'bold'), bg='red', fg='white', pady=20)
        name_label.grid(row=1, column=0, sticky='w')
        name_entry = Entry(fillDetails, width=15, textvariable=self.name_var, 
         font=('Courier New', 15, 'bold'), borderwidth=2, relief='solid')
        name_entry.grid(row=1, column=1, sticky='w')

        # Date
        date_label = Label(fillDetails, text='Date of Fee \nSubmission: ',
        bg='red', fg='white', font=('Courier New', 15, 'bold'))
        date_label.grid(row=2, column=0, sticky='w')
        date_entry = Entry(fillDetails, width=15, textvariable = self.date_var,
         font=('Courier New', 15, 'bold'), borderwidth=2, relief='solid')
        date_entry.grid(row=2, column=1, sticky='w', pady= 40)

        # Amount
        fee_label = Label(fillDetails, text='Amount: ₹', bg='red',
         fg='white', font=('Courier New', 15, 'bold'))
        fee_label.grid(row=3, column=0, sticky='w')
        fee_entry = Entry(fillDetails, width=15,textvariable=self.amount_var,
         font=('Courier New', 15, 'bold'), borderwidth=2, relief='solid')
        fee_entry.grid(row=3, column=1, sticky='w', pady=40)

        # Instrument
        intru_label= Label(fillDetails, text='Instrument: ', bg='red',
         fg='white', font=('Courier New', 15, 'bold'))
        intru_label.grid(row=4, column=0, sticky='w')
        intru_entry = ttk.Combobox(fillDetails, textvariable=self.instru_var, font=('Courier New', 15, 'bold'),
         width=15, state='readonly')
        intru_entry['values'] = ('Guitar', 'Drum', 'Synthesizer', 'Vocal', 'Octapad',
         'Harmonium', 'Others')
        intru_entry.grid(row=4, column=1, sticky='w', pady=40)

        # ------------- Buttons -----------------
        btn_frame = Frame(fillDetails, bg='red')
        btn_frame.place(x=10, y= 475, width=375, height=60) 
        # Add
        Addbtn = Button(btn_frame, text='Add', 
         width=6, font=('Courier New', 15, 'bold'),
        bg='cyan', fg='white', command=self.register)
        Addbtn.grid(row=0, column=0, sticky='w', padx=5, pady=10)
        #Clear
        clearbtn = Button(btn_frame, text='Clear', width=6, font=('Courier New', 15, 'bold'),
        bg='cyan', fg='white', command=self.clear)
        clearbtn.grid(row=0, column=1, sticky='w', padx=5, pady=10)
        # Update
        updatebtn = Button(btn_frame, text='Update', 
        width=6, font=('Courier New', 15, 'bold'),
        bg='cyan', fg='white', command=self.update)
        updatebtn.grid(row=0, column=2, sticky='w', padx=5, pady=10)
        #Delete
        deletebtn = Button(btn_frame, text='Delete', 
         width=6, font=('Courier New', 15, 'bold'),
        bg='cyan', fg='white', command=self.delete)
        deletebtn.grid(row=0, column=3, sticky='w', padx=5, pady=10)
 
        # ---------------- To show the stored Data --------------
        showDetails = Frame(self.root, borderwidth=2, relief='solid', bg='red')
        showDetails.place(x=420, y=75, width=1100, height=715)

        type_search = Label(showDetails, text='Search By: ', bg='red',
         fg='white', font=('Courier New', 20, 'bold'))
        type_search.grid(row=0, column=0, sticky='w')
        type_search_box = ttk.Combobox(showDetails, textvariable=self.type_var, font=('Courier New', 15, 'bold'),
         width=15, state='readonly')
        type_search_box['values'] = ('Name', 'Date', 'Instrument')
        type_search_box.grid(row=0, column=1, sticky='w')

        search_label = Label(showDetails, text='Search: ', bg='red',
         fg='white', font=('Courier New', 20, 'bold'))
        search_label.grid(row=1, column=0, sticky='w', pady=15, padx= 10)
        search_entry = Entry(showDetails, width=25,
         font=('Courier New', 20, 'bold'), borderwidth=2, relief='solid', textvariable=self.search_var)
        search_entry.grid(row=1, column=1, sticky='w')
        searchBtn = Button(showDetails, text='Search',
         font=('Courier New', 15, 'bold'), borderwidth=2, relief='solid', command=self.type_data)
        searchBtn.grid(row=1, column=2, padx= 10)
        showBtn = Button(showDetails, text='Show All',
         font=('Courier New', 15, 'bold'), borderwidth=2, relief='solid', command=self.fetch_data)
        showBtn.grid(row=1, column=3, padx= 10)

        # ------------- Table ---------------
        table_frame = Frame(showDetails, width=1070, height=550, borderwidth=2, relief='solid')
        table_frame.place(x=10, y= 125)

        scrollX = Scrollbar(table_frame, orient=HORIZONTAL)
        scrollY = Scrollbar(table_frame, orient=VERTICAL)

        self.details = ttk.Treeview(table_frame, columns=('Name', 'Submission Date',
         'Instrument', 'Amount'), xscrollcommand= scrollX.set,
          yscrollcommand= scrollY.set)

        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.details.xview)
        scrollY.config(command=self.details.yview)

        self.details.heading('Name', text='Name')
        self.details.heading('Submission Date', text='Submission Date')
        self.details.heading('Instrument', text='Instrument')
        self.details.heading('Amount', text='Amount')
        self.details['show'] = 'headings'
        self.details.column('Name', width=300)
        self.details.column('Submission Date', width=200)
        self.details.column('Instrument', width=300)
        self.details.column('Amount', width=200)
        self.details.pack(fill=BOTH, expand=1)
        self.details.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()
      
    def register(self):
      con = pymysql.connect(host='localhost', user='root', password='', database='fms')
      cur=con.cursor()
      cur.execute("insert into fees values(%s, %s, %s, %s)", (self.name_var.get(),
                                                                  self.date_var.get(),
                                                                  self.instru_var.get(),
                                                                  self.amount_var.get()
                                                                  ))
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()
    
    def fetch_data(self):
      con = pymysql.connect(host='localhost', user='root', password='', database='fms')
      cur=con.cursor()
      cur.execute("select * from fees")
      rows= cur.fetchall()
      if len(rows) != 0:
        self.details.delete(*self.details.get_children())
        for row in rows:
          self.details.insert('', END, values=row)
        con.commit()
      con.close()

    def clear(self):
      self.name_var.set('')
      self.date_var.set('')
      self.amount_var.set('')
      self.instru_var.set('')

    def get_cursor(self, event):
      cursor_row = self.details.focus()
      content = self.details.item(cursor_row)
      row = content['values']
      self.name_var.set(row[0])
      self.date_var.set(row[1])
      self.instru_var.set(row[2])
      self.amount_var.set(row[3])
      

    def update(self):
      con = pymysql.connect(host='localhost', user='root', password='', database='fms')
      cur=con.cursor()
      cur.execute("update fees set Name=%s, Date=%s,Instrument=%s,Amount=%s where Name=%s", (self.name_var.get(),
                                                                  self.date_var.get(),
                                                                  self.instru_var.get(),
                                                                  self.amount_var.get(),
                                                                  self.name_var.get()
                                                                  ))
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()

    def delete(self):
      con = pymysql.connect(host='localhost', user='root', password='', database='fms')
      cur=con.cursor()
      cur.execute("delete from fees where name=%s", self.name_var.get())
      con.commit()
      con.close()
      self.fetch_data()
      self.clear()

    def type_data(self):
      con = pymysql.connect(host='localhost', user='root', password='', database='fms')
      cur=con.cursor()
      cur.execute("select * from fees where " + str(self.type_var.get()) + " LIKE '%"
       + str(self.search_var.get()) + "%'")
      rows= cur.fetchall()
      if len(rows) != 0:
        self.details.delete(*self.details.get_children())
        for row in rows:
          self.details.insert('', END, values=row)
        con.commit()
      con.close()
      self.search_var.set("")

root = Tk()
ob = Student(root)
root.mainloop()