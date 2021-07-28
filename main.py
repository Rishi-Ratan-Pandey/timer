from tkinter import*
from tkinter.ttk import Spinbox,Label,Button
import datetime
from tkinter import messagebox
from ttkthemes import ThemedTk
root=ThemedTk(themebg=True)
root.set_theme('arc')
root.geometry("400x250")
now_time_sec=datetime.datetime.now().strftime('%S')
now_time_min=datetime.datetime.now().strftime('%M')
now_time_hr=datetime.datetime.now().strftime("%H")
sec_data=IntVar()
min_data=IntVar()
hr_data=IntVar()
countdown_data=IntVar()
countdown_data_1=IntVar()
countdown_data_2=IntVar()
def minus():
	global minus_this
	global minus_this1
	global minus_this2
	global id
	id=root.after(1000,minus)
	if minus_this<0:
		minus_this1-=1
		minus_this+=60
	if minus_this1<0:
		minus_this2-=1
		minus_this1+=60
	if minus_this==0 and minus_this1==0 and minus_this2==0:
		root.after_cancel(id)
		countdown_data.set('0')
		minus_this-=minus_this
		messagebox.showinfo('Alert!!','Time Up!')#add maiming option.
	countdown_data.set(minus_this)
	countdown_data_1.set(minus_this1)
	countdown_data_2.set(minus_this2)
	minus_this-=1
	

def start_countdown(sec,min,hr):
	global minus_this
	global minus_this1
	global minus_this2
	sec_spinbox.deiconify()
	min_spinbox.deiconify()
	hr_spinbox.deiconify()
	sec_label_indict.deiconify()
	min_label_indict.deiconify()
	hr_label_indict.deiconify()
	set_timer.deiconify()
	head.deiconify()

	a=Label(root,text=':',font=('Courier New',50))
	b=Label(root,text=':',font=('Courier New',50))
	sec_lab=Label(root,textvariable=countdown_data,text=sec,font=('Courier',25))
	sec_lab.place(x=230)
	countdown_data.set(sec)
	min_label=Label(root,textvariable=countdown_data_1,text=min,font=('Courier',25))
	min_label.place(x=125)
	countdown_data_1.set(min)
	hr_label=Label(root,textvariable=countdown_data_2,text=hr,font=('Courier',25))
	hr_label.place(x=15)
	countdown_data_2.set(hr)
	a.place(x=200,y=30)
	b.place(x=90,y=30)
	minus_this=sec
	minus_this1=min
	minus_this2=hr
	minus()
def set_timer_ye():
	if sec_data.get()==0 and min_data.get()==0 and hr_data.get()==0:
		messagebox.showinfo('Info','Please Add More Time.')
	else:
		messagebox.showinfo('Info','Timer Set Successfully')
		start_countdown(sec_data.get(),min_data.get(),hr_data.get())
head=Label(root,text='Timer',font=('Courier',30,'bold'))
head.place(x=125)
sec_label_indict=Label(root,text='Seconds:',font=('Courier',20,'bold'))
sec_label_indict.place(x=1,y=55)
sec_spinbox=Spinbox(root,state='readonly',textvariable=sec_data,from_=0,to=59,font=('Arial Rounded MT bold',20,'bold'),width=5)
sec_spinbox.place(x=1,y=95)
min_label_indict=Label(root,text='Minutes:',font=('Courier',20,'bold'))
min_label_indict.place(x=135,y=55)
min_spinbox=Spinbox(root,state='readonly',textvariable=min_data,from_=0,to=59,font=('Arial Rounded MT bold',20,'bold'),width=5)
min_spinbox.place(x=135,y=95)
hr_label_indict=Label(root,text='Hours:',font=('Courier',20,'bold'))
hr_label_indict.place(x=135+135,y=55)
hr_spinbox=Spinbox(root,state='readonly',textvariable=hr_data,from_=0,to=99,font=('Arial Rounded MT bold',20,'bold'),width=5)
hr_spinbox.place(x=135+135,y=95)
set_timer=Button(root,text='Set Timer',command=set_timer_ye)
set_timer.place(x=145,y=135)
mainloop()
# create a rewarding option.
# create a naming option.