

# Dictionary

mydict = {'alphabet':['a-apple', 'b-bee', 'c-cat', 'd-dog', 'e-egg', 'f-fish', 'g-giraffe', 'h-horse', 'i-ice-cream', 'j-jump'
, 'k-king', 'l-lion', 'm-mushroom', 'n-nurse', 'o-ox', 'p-panda', 'q-queen', 'r-rabbit', 's-snake', 't-tiger', 'u-umbrella'
, 'v-van', 'w-whale', 'x-x-ray', 'y-yak', 'z-zebra']
,'month': ['january','February','March','April','May','June','July','August','September','October','November','December']
,'day' : ['sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
,'animal' : ['bee', 'bird', 'bug', 'butterfly', 'cat', 'chick', 'cow', 'crocodile', 'dog', 'duck', 'fox', 'frog', 'giraffe', 'goat', 'hippo', 'kangaroo', 'lion'
, 'monkey', 'owl', 'panda', 'porcupine', 'rhino','sheep', 'snake', 'tiger', 'worn', 'zebra']
,'vegetables' : ['bell-pepper','broccoli','carrot','chili','corn','cucumber','eggplant','garlic','kale','onion','parsley','potato','pumpkin','radish','tomato']
,'occupations' : ['doctor','engineer','fireman','gardener','merchant','model','musician','nurse','painter','photographer','pilot','police','postman','saleman','scientist','singer','soldier','sportsman','student','teacher','horse-riding']
,'place':['bank', 'church', 'hospital', 'hotel', 'house', 'library', 'market', 'museum', 'place', 'police-station', 'post-office', 'restaurant', 'school', 'temple']
, 'weather':['cloudy', 'cold', 'cool', 'fine', 'foggy', 'hot', 'rainbow', 'rainy', 'snow', 'storm', 'sunny', 'weather', 'windy']
,'colour' : ['black', 'blue', 'brown', 'colour', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow']
,'sport' : ['badminton', 'baseball', 'basketball', 'bowling', 'boxing', 'cycling', 'football', 'golf', 'horse riding', 'rugby', 'swimming', 'tabletennis', 'tennis', 'volleyball']
,'vehicle' : ['airplane', 'bicycle', 'bus', 'car', 'helicopter', 'motorcycle', 'ship', 'taxi', 'train', 'truck', 'van', 'Vehicles']
,'body' : ['arm', 'cheek', 'chin', 'ear', 'eyebrow', 'face', 'foot', 'hair', 'hand', 'leg', 'mount', 'neck', 'shoulder', 'tongue', 'tooth']
,'clothing':['belt', 'bikini', 'boots', 'canvas-shoes', 'cap', 'coat', 'dress', 'flip-flops', 'glasses', 'hat', 'high-heel', 'jacket', 'jeans', 'necktie', 'shirt', 'shorts', 'skirt', 'slacks', 'socks', 'suit', 'swimsuit', 't-shirt', 'trousers', 'tuxedo', 'vest']
,'food' : ['french-fries', 'fried-chicken', 'fried-egg', 'fried-rice', 'green-curry','hamburger', 'hot-dog', 'noodle', 'omelet'
, 'papaya-salad','pizza', 'porridge', 'salad', 'salmon', 'sanwich', 'spaghetti','steak', 'sushi', 'thai-fried-noodles', 'tom-yum-kung']}

# List
randoms= ['vegetables','occupations','animal','colour','sport','vehicle','body','food','clothing']
catagory = ['alphabet','day','month','animal','body','clothing','colour','food','occupations','place','sport','vehicle','vegetables','weather']
lst_sort = ['alphabet','day','month']

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random 
import time 
import win32com.client as wincl
i=0

def speech (text):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Rate == -2
    time.sleep(1)
    speak.Speak(text)
    print(text)
    
def image_slide():
    global g
    global temp
    global i
    global ch
    
    if i < ch: 
        try:
            img = Image.open(f'image\\flashcard\\{temp[i]}.jpg')
        except:
            te = temp[i].replace('-','_')
            img = Image.open(f'image\\flashcard\\{te}.jpg')
        width, height = img.size
        #sc = resize_img (width, height)
        img = img.resize((450, 450), Image.ANTIALIAS)
        #img = img.resize((int(width * sc), int(height * sc)))
        photo = ImageTk.PhotoImage(img)
        fimg = Frame(center, bg='black', width=450, height=450, padx=20, pady=20)
        fimg.grid(row=0, column=1, sticky="nsew")            
        panel = Label(fimg,image = photo)
        #panel.pack_forget()                   
        panel.pack()
        panel.image = photo         
        vo = temp[i].replace('_','-')
        speech(vo)
        #print(vo)
        #print(i)
        i += 1       
        panel.after(1500, image_slide)
    else:
        i=0
        img = Image.open(f'image\\end.jpg')
        img = img.resize((450, 450), Image.ANTIALIAS)
        fimg = Frame(center, bg='black', width=450, height=450, padx=20, pady=20)
        fimg.grid(row=0, column=1, sticky="nsew")
        photo = ImageTk.PhotoImage(img)
        panel = Label(fimg,image = photo)
        panel.image = photo            
        panel.pack()
    def start_click(e):
    global g
    global temp
    global ch
    global i
    i = 0
    g  = (e.widget["text"]).lower()
    speech (g)
    temp = mydict[f'{g}']  
    
    if g != 'day':
        if g != 'month':
            if g != 'alphabet':
                random.shuffle(temp)        
    ch = len(mydict[f'{g}'])    
    i = 0        
    image_slide()
   
  def auto_click(e):
    global temp
    global ch
    i=0
    g  = (e.widget["text"]).lower()
    speech (g)
    temp=[]
    if g =='random':
        for b in range(len(randoms)):
            a = randoms[b]
            temp.extend(mydict[f'{a}'])
        random.shuffle(temp)
    else:
        for c in range(len(catagory)):
            a = catagory[c]
            temp.extend(mydict[f'{a}'])
    ch = len(temp)
    i = 0
    image_slide()   
  
  root = tk.Tk ()
root.title('English for Kids')
root.geometry('790x680+200+50')
speech('Hello Phupha')
center = Frame(root, bg='black', width=50, height=40, padx=0, pady=0)
center.grid(row=1, sticky="nsew")
butt = Frame(root, bg='red', width=50, height=100, padx=0, pady=0)
butt.grid(row=2, sticky="nsew")
ctr_left = Frame(center, bg='white', width=215, height=420, padx=0, pady=50)
fimg = Frame(center, bg='black', width=450, height=450, padx=20, pady=20)
ctr_right = Frame(center, bg='white', width=215, height=420, padx=0, pady=50)
ctr_left.grid(row=0, column=0, sticky="nsew")
fimg.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="nsew") 
f1 = Frame(root, bg='red', width=50, height=40, padx=20, pady=20)
f1.grid(row=0, column=0, sticky="nsew") 

lbl2 = Label(f1,text="English for Kids",font = ('Helvetica', 30,'bold'),width=15, bg='red',fg='white')
lbl2.pack( padx=5,pady=5)
img = Image.open(f'image\\robot.jpg')
img = img.resize((450, 450), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)       
panel = Label(fimg,image = photo)
panel.image = photo            
panel.pack()

img = Image.open(f'image\\button\\autoplay.jpg')
img = img.resize((140,45), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img) 
a = Button(ctr_right, image= photo, text='AutoPlay', borderwidth=0 )
a.image = photo  
a.pack( padx=3,pady=1)
a.bind('<Button-1>', auto_click)

for i in range(0,7):
    ca = catagory[i].capitalize()
    print( catagory[i])
    img2 = Image.open(f'image\\button\\{catagory[i]}.jpg')
    img2 = img2.resize((140,45), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img2) 
   # w = Button(ctr_right, image=p1_shapes[i], text=shapes[i], borderwidth=0)
    c = Button(ctr_right, image = photo, text=(ca), borderwidth=0  )    
    c.image = photo
    c.pack(padx=3,pady=1) 
    c.bind('<Button-1>', start_click)

img1 = Image.open(f'image\\button\\random.jpg')
img1 = img1.resize((140,45), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(img1)    
b = Button(ctr_left, image= photo1, text='Random', borderwidth=0)
b.image = photo1 
b.pack(padx=3,pady=1)
b.bind('<Button-1>', auto_click)

for i in range(8,14):
    ca = catagory[i].capitalize()
    print( catagory[i])
    img3 = Image.open(f'image\\button\\{catagory[i]}.jpg')
    img3 = img3.resize((140,45), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img3) 
    d = Button(ctr_left, image = photo, text=(ca), borderwidth=0  )    
    d.image = photo
    d.pack(padx=3, pady=1) 
    d.bind('<Button-1>', start_click)
root.mainloop()
