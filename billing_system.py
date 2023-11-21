from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib

win=Tk()
win.geometry('1270x678')
win.title('Billing System')
win.iconbitmap('1489436625-billingdatadollarcurrency_81879.ico')

if not os.path.exists('bills'):
    os.mkdir('bills')

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')    

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number{billnumber} is saved successfully')
        billnumber=random.randint(500,1000)

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumber_entry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
                f.close()
                break
        else:
            messagebox.showerror('Error','Invalid Bill Number')
billnumber=random.randint(500,1000)

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login('jatin0063@gmail.com','xpem jyue ajcw gmsl')
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit
            messagebox.showinfo('Success','Bill Is Successfully Sent')
        except Exception as e:
            print(e)
            messagebox.showerror('Error','Something went Wrong')

    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        win1=Toplevel()
        win1.title('Send Gmail')
        win1.config(bg='grey20')
        win1.resizable(0,0)

        senderframe=LabelFrame(win1,text='SENDER',font=('arial',16,'bold'),border=6,bg='grey20',fg='white')
        senderframe.grid(row=0,column=0,padx=40,pady=20)

        senderlabel=Label(senderframe,text="Sender's Email",font=('arial',14,'bold'),bg='grey20',fg='white')
        senderlabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderframe,font=('arial',14,'bold'),border=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordlabel=Label(senderframe,text="Password",font=('arial',14,'bold'),bg='grey20',fg='white')
        passwordlabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderframe,font=('arial',14,'bold'),border=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientframe=LabelFrame(win1,text='RECIPIENT',font=('arial',16,'bold'),border=6,bg='grey20',fg='white')
        recipientframe.grid(row=1,column=0,padx=40,pady=20)

        recieverlabel=Label(recipientframe,text="E-mail Address",font=('arial',14,'bold'),bg='grey20',fg='white')
        recieverlabel.grid(row=0,column=0,padx=10,pady=8)

        recieverEntry=Entry(recipientframe,font=('arial',14,'bold'),border=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)

        messagelabel=Label(recipientframe,text="Message",font=('arial',14,'bold'),bg='grey20',fg='white')
        messagelabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(recipientframe,font=('arial',14,'bold'),border=2,relief=SUNKEN,width=45,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendbutton=Button(win1,text='SEND',font=('arial',14,'bold'),width=15,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)

        win1.mainloop()



def bill_area():
    if name_entry.get()=='' or phone_entry.get()=='':
        messagebox.showerror('Error','Customer Details Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error','No Products Selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Products are selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number:{billnumber}')
        textarea.insert(END,f'\nCustomer Name:{name_entry.get()}')
        textarea.insert(END,f'\nCustomer Phone Number:{phone_entry.get()}')
        textarea.insert(END,'\n==========================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')    
        textarea.insert(END,'\n==========================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'Bath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if DalEntry.get()!='0':
            textarea.insert(END,f'\nDal\t\t\t{DalEntry.get()}\t\t\t{Dalprice} Rs')    
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')    
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')    
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')    
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')    
        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')    
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nMountain Dew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')    
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')    
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')    
        if cocacolaEntry.get()!='0':
            textarea.insert(END,f'\nCoca-Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs')    
        textarea.insert(END,'\n----------------------------------------------------------')

        if cosmetictaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
        if drinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill\t\t\t\t{totalbill}')
        textarea.insert(END,'\n----------------------------------------------------------')
        save_bill()
         
def total():
    global soapprice,hairsprayprice,facecreamprice,hairgelprice,bodylotionprice,facewashprice
    global riceprice,Dalprice,oilprice,sugarprice,teaprice,wheatprice
    global maazaprice,frootiprice,dewprice,pepsiprice,spriteprice,cocacolaprice
    global totalbill

    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    riceprice=int(riceEntry.get())*30
    Dalprice=int(DalEntry.get())*100
    oilprice=int(oilEntry.get())*120
    sugarprice=int(sugarEntry.get())*50
    teaprice=int(teaEntry.get())*140
    wheatprice=int(wheatEntry.get())*80
 
    maazaprice=int(maazaEntry.get())*50
    frootiprice=int(frootiEntry.get())*20
    dewprice=int(dewEntry.get())*30
    pepsiprice=int(pepsiEntry.get())*20
    spriteprice=int(spriteEntry.get())*45
    cocacolaprice=int(cocacolaEntry.get())*90
    
    totaldrinksprice=maazaprice+frootiprice+dewprice+pepsiprice+spriteprice+cocacolaprice
    totalgroceryprice=riceprice+Dalprice+oilprice+sugarprice+teaprice+wheatprice
    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,str(totalcosmeticprice)+'Rs')
    cosmtictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmtictax)+'Rs')
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,str(totaldrinksprice)+'Rs')
    drinktax=totaldrinksprice*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,str(drinktax)+'Rs')
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+'Rs')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+'Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmtictax+grocerytax+drinktax

heading_label=Label(win,text='Retail Billing System',font=('times new roman',30,'bold'),bg='grey20',fg='gold',border=12,relief=GROOVE)
heading_label.pack(fill=X)

customer_detail_frame=LabelFrame(win,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',border=8,relief=GROOVE,bg='grey20')
customer_detail_frame.pack(fill=X)

namelabel=Label(customer_detail_frame,text='Name',font=('times new roman',15,'bold'),bg='grey20',fg='white')
namelabel.grid(row=0,column=0,padx=20)

name_entry=Entry(customer_detail_frame,font=('arial',15),border=7,width=18)
name_entry.grid(row=0,column=1,padx=8)

phonelabel=Label(customer_detail_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='grey20',fg='white')
phonelabel.grid(row=0,column=2,padx=20,pady=2)

phone_entry=Entry(customer_detail_frame,font=('arial',15),border=7,width=18)
phone_entry.grid(row=0,column=3,padx=8)

bill_numberlabel=Label(customer_detail_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='grey20',fg='white')
bill_numberlabel.grid(row=0,column=4,padx=20,pady=2)

billnumber_entry=Entry(customer_detail_frame,font=('arial',15),border=7,width=18)
billnumber_entry.grid(row=0,column=5,padx=8)

search_button=Button(customer_detail_frame,text='SEARCH',font=('arial',12,'bold'),border=7,width=10,command=search_bill)
search_button.grid(row=0,column=6,padx=20,pady=8)

product_frame=Frame(win)
product_frame.pack(fill=X)

cosmeticsframe=LabelFrame(product_frame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',border=8,relief=GROOVE,bg='grey20')
cosmeticsframe.grid(row=0,column=0)

bathsoaplabel=Label(cosmeticsframe,text='Bath Soap',font=('times new roman',15,'bold'),bg='grey20',fg='white')
bathsoaplabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,border=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamlabel=Label(cosmeticsframe,text='Face Cream',font=('times new roman',15,'bold'),bg='grey20',fg='white')
facecreamlabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,border=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashlabel=Label(cosmeticsframe,text='Face Wash',font=('times new roman',15,'bold'),bg='grey20',fg='white')
facewashlabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,border=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
facewashEntry.insert(0,0)

hairspraylabel=Label(cosmeticsframe,text='Hair Spray',font=('times new roman',15,'bold'),bg='grey20',fg='white')
hairspraylabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,border=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
hairsprayEntry.insert(0,0)

hairgellabel=Label(cosmeticsframe,text='Hair Gel',font=('times new roman',15,'bold'),bg='grey20',fg='white')
hairgellabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,border=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
hairgelEntry.insert(0,0)

bodylotionlabel=Label(cosmeticsframe,text='Body Lotion',font=('times new roman',15,'bold'),bg='grey20',fg='white')
bodylotionlabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,border=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
bodylotionEntry.insert(0,0)

groceryframe=LabelFrame(product_frame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',border=8,relief=GROOVE,bg='grey20')
groceryframe.grid(row=0,column=1)

ricelabel=Label(groceryframe,text='Rice',font=('times new roman',15,'bold'),bg='grey20',fg='white')
ricelabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,border=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
riceEntry.insert(0,0)

oillabel=Label(groceryframe,text='Oil',font=('times new roman',15,'bold'),bg='grey20',fg='white')
oillabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,border=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
oilEntry.insert(0,0)

Dallabel=Label(groceryframe,text='Daal',font=('times new roman',15,'bold'),bg='grey20',fg='white')
Dallabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

DalEntry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,border=5)
DalEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
DalEntry.insert(0,0)

wheatlabel=Label(groceryframe,text='Wheat',font=('times new roman',15,'bold'),bg='grey20',fg='white')
wheatlabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,border=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
wheatEntry.insert(0,0)

sugarlabel=Label(groceryframe,text='Sugar',font=('times new roman',15,'bold'),bg='grey20',fg='white')
sugarlabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,border=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
sugarEntry.insert(0,0)

tealabel=Label(groceryframe,text='Tea',font=('times new roman',15,'bold'),bg='grey20',fg='white')
tealabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,border=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
teaEntry.insert(0,0)

drinksframe=LabelFrame(product_frame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='gold',border=8,relief=GROOVE,bg='grey20')
drinksframe.grid(row=0,column=2)

maazalabel=Label(drinksframe,text='Maaza',font=('times new roman',15,'bold'),bg='grey20',fg='white')
maazalabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry=Entry(drinksframe,font=('times new roman',15,'bold'),width=10,border=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
maazaEntry.insert(0,0)

pepsilabel=Label(drinksframe,text='Pepsi',font=('times new roman',15,'bold'),bg='grey20',fg='white')
pepsilabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(drinksframe,font=('times new roman',15,'bold'),width=10,border=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
pepsiEntry.insert(0,0)

spritelabel=Label(drinksframe,text='Sprite',font=('times new roman',15,'bold'),bg='grey20',fg='white')
spritelabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinksframe,font=('times new roman',15,'bold'),width=10,border=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
spriteEntry.insert(0,0)

dewlabel=Label(drinksframe,text='Dew',font=('times new roman',15,'bold'),bg='grey20',fg='white')
dewlabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(drinksframe,font=('times new roman',15,'bold'),width=10,border=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
dewEntry.insert(0,0)

frootilabel=Label(drinksframe,text='Frooti',font=('times new roman',15,'bold'),bg='grey20',fg='white')
frootilabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinksframe,font=('times new roman',15,'bold'),width=10,border=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
frootiEntry.insert(0,0)

cocacolalabel=Label(drinksframe,text='Coca-Cola',font=('times new roman',15,'bold'),bg='grey20',fg='white')
cocacolalabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cocacolaEntry=Entry(drinksframe,font=('times new roman',15,'bold'),width=10,border=5)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
cocacolaEntry.insert(0,0)

billframe=Frame(product_frame,border=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billarealabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),border=7,relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=18,width=58,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuframe=LabelFrame(win,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',border=8,relief=GROOVE,bg='grey20')
billmenuframe.pack(fill=X)

cosmeticpricelabel=Label(billmenuframe,text='Cosmetic Price',font=('times new roman',13,'bold'),bg='grey20',fg='white')
cosmeticpricelabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuframe,font=('times new roman',13,'bold'),width=10,border=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10,sticky='w')

grocerypricelabel=Label(billmenuframe,text='Grocery Price',font=('times new roman',15,'bold'),bg='grey20',fg='white')
grocerypricelabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuframe,font=('times new roman',13,'bold'),width=10,border=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10,sticky='w')

drinkspricelabel=Label(billmenuframe,text='Cold Drink Price',font=('times new roman',13,'bold'),bg='grey20',fg='white')
drinkspricelabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

drinkspriceEntry=Entry(billmenuframe,font=('times new roman',13,'bold'),width=10,border=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10,sticky='w')

cosmetictaxlabel=Label(billmenuframe,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='grey20',fg='white')
cosmetictaxlabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuframe,font=('times new roman',13,'bold'),width=10,border=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10,sticky='w')

grocerytaxlabel=Label(billmenuframe,text='Grocery Tax',font=('times new roman',15,'bold'),bg='grey20',fg='white')
grocerytaxlabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuframe,font=('times new roman',13,'bold'),width=10,border=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10,sticky='w')

drinkstaxlabel=Label(billmenuframe,text='Cold Drink Tax',font=('times new roman',13,'bold'),bg='grey20',fg='white')
drinkstaxlabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

drinkstaxEntry=Entry(billmenuframe,font=('times new roman',13,'bold'),width=10,border=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10,sticky='w')

buttonframe=Frame(billmenuframe,border=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonframe,text='Total',font=('arial',16,'bold'),bg='grey20',fg='white',border=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(buttonframe,text='Bill',font=('arial',16,'bold'),bg='grey20',fg='white',border=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonframe,text='E-mail',font=('arial',16,'bold'),bg='grey20',fg='white',border=5,width=8,pady=10,command=send_email)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonframe,text='Print',font=('arial',16,'bold'),bg='grey20',fg='white',border=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonframe,text='Clear',font=('arial',16,'bold'),bg='grey20',fg='white',border=5,width=8,pady=10)
clearbutton.grid(row=0,column=4,pady=20,padx=5)


win.mainloop()