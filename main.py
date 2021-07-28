from tkinter import*
from tkinter.ttk import Spinbox,Label,Button
from tkinter import messagebox
from ttkthemes import ThemedTk
root=ThemedTk(themebg=True)
root.set_theme('arc')
root.geometry("400x250")
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
		root.deiconify()
		root.after_cancel(id)
		countdown_data.set('00')
		minus_this-=minus_this
		messagebox.showinfo('Alert!!','Time Up!')
		head.place(x=125)
		sec_label_indict.place(x=1,y=55)
		sec_spinbox.place(x=1,y=95)
		min_label_indict.place(x=135,y=55)
		min_spinbox.place(x=135,y=95)
		hr_label_indict.place(x=135+135,y=55)
		hr_spinbox.place(x=135+135,y=95)
		set_timer.place(x=145,y=135)
		a.place(x=5454)
		b.place(x=3454)
		sec_label.place(y=6444)
		min_label.place(x=4544)
		hr_label.place(x=4589)
		root.geometry("400x250")		
	if minus_this<=9:
		countdown_data.set(f"0{minus_this}")
	else:
		countdown_data.set(f"{minus_this}")
	if minus_this1<=9:
		countdown_data_1.set(f"0{minus_this1}")
	else:
		countdown_data_1.set(f"{minus_this1}")
	if minus_this2<=9:
		countdown_data_2.set(f"0{minus_this2}")
	else:
		countdown_data_2.set(f"{minus_this2}")
	minus_this-=1
def start_countdown(sec,min,hr):
	global minus_this
	global minus_this1
	global minus_this2,a,b,sec_label,min_label,hr_label
	root.geometry('350x200')
	sec_spinbox.place(x=45444);min_spinbox.place(x=45444);hr_spinbox.place(x=45444);sec_label_indict.place(x=45444);min_label_indict.place(x=45444);hr_label_indict.place(x=45444);set_timer.place(x=45444);head.place(x=110)
	a=Label(root,text=':',font=('Courier New',40))
	b=Label(root,text=':',font=('Courier New',40))
	sec_label=Label(root,textvariable=countdown_data,text=sec,font=('Courier',50))
	sec_label.place(x=230,y=50)
	countdown_data.set(sec)
	min_label=Label(root,textvariable=countdown_data_1,text=min,font=('Courier',25+25))
	min_label.place(x=125,y=50)
	countdown_data_1.set(min)
	hr_label=Label(root,textvariable=countdown_data_2,text=hr,font=('Courier',25+25))
	hr_label.place(x=15,y=50)
	countdown_data_2.set(hr)
	a.place(x=200,y=50)
	b.place(x=90,y=50)
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
