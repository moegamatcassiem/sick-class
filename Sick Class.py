from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Sick Class")
frame = Frame(root)

SickID = Label(root, text="SicknessCode")
SickID.pack(side=LEFT)
SickID.place(x=20, y=20)

sick_entry = Entry(root, bd=1)
sick_entry.pack(side=RIGHT)
sick_entry.place(x=300, y=20)

DurationOfTreatment = Label(root, text="DurationOfTreatment")
DurationOfTreatment.pack(side=LEFT)
DurationOfTreatment.place(x=20, y=80)

weeks_monthly = Label(root, text="Weekly/Months")
weeks_monthly.pack(side=RIGHT)
weeks_monthly.place(x=380, y=80)

due_entry = Entry(root, bd=1, width=8)
due_entry.pack(side=RIGHT)
due_entry.place(x=300, y=80)

MDoctorsID = Label(root, text="DoctorsPracticeNumber")
MDoctorsID.pack(side=LEFT)
MDoctorsID.place(x=20, y=150)

doc_entry = Entry(root, bd=1)
doc_entry.pack(side=RIGHT)
doc_entry.place(x=300, y=150)

scan_fee = Label(root, text="Scan/Consultation Fee")
scan_fee.pack(side=LEFT)
scan_fee.place(x=20, y=190)

scan_entry = Entry(root, bd=1)
scan_entry.pack(side=RIGHT)
scan_entry.place(x=301, y=190)


amount_paid = Label(root)
amount_paid.pack(side=LEFT)
amount_paid.place(x=20, y=260)

var = StringVar()

class Sick():
    def sickness(self):
        self.SickID = SickID
        self.DurationOfTreatment = DurationOfTreatment
        self.DoctorsID = MDoctorsID
        self.medcancer = 400
        self.medinflu = 350.50

def sickness():
    if var.get() == "Cancer":
        if int(scan_entry.get()) > 600:
            messagebox.showinfo("Message", "Sorry we cannot treat you")
        elif int(scan_entry.get()) < 600:
           cancer_answer = int(scan_entry.get()) + 400
           amount_paid.config(text="AmountPaidForTreatment: " + str(cancer_answer))

    if var.get() == "Influenza": # Calculating Influenza
        if int(scan_entry.get()) >= 600:
            influ_answer = 350.50 + int(scan_entry.get())
            amount_paid.config(text="AmountPaidForTreatment: " + str(influ_answer))
        elif int(scan_entry.get()) < 600:
            influ_answer = 350.50 + int(scan_entry.get())
            discount = (influ_answer * (2/100)) + influ_answer
            messagebox.showinfo("Message", "2% discount")
            amount_paid.config(text="Amount Paid For Treatment: " + str(discount))




radio_btn1=Radiobutton(root, text="Cancer", variable=var, value="Cancer")
radio_btn1.pack(side=LEFT)
radio_btn1.place(x=20, y=220)

radio_btn2 = Radiobutton(root, text="Influenza", variable=var, value="Influenza")
radio_btn2.pack(side=LEFT)
radio_btn2.place(x=20, y=240)

cal_btn = Button(root, text="Calculate", command=sickness)
cal_btn.pack(side=LEFT)
cal_btn.place(x=20, y=300)

def clear_all():
    sick_entry.delete(0, END)
    due_entry.delete(0, END)
    doc_entry.delete(0, END)
    scan_entry.delete(0, END)

clear_btn=Button(root, text="Clear", command=clear_all)
clear_btn.pack(side=RIGHT)
clear_btn.place(x=300, y=300)



root.mainloop()