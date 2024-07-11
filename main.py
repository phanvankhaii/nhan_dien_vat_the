import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
from keras.models import load_model


model = load_model('my_model.h5')

classes = { 1:'Giới hạn tốc độ (20km/h)',
            2:'Giới hạn tốc độ (30km/h)',      
            3:'Giới hạn tốc độ (50km/h)',       
            4:'Giới hạn tốc độ (60km/h)',      
            5:'Giới hạn tốc độ (70km/h)',    
            6:'Giới hạn tốc độ (80km/h)',      
            7:'Hết giới hạn tốc độ (80km/h)',     
            8:'Giới hạn tốc độ (100km/h)',    
            9:'Giới hạn tốc độ (120km/h)',     
           10:'Cấm vượt',   
           11:'Không được vượt xe có trọng tải trên 3,5 tấn',     
           12:'Giao nhau với đường không ưu tiên',     
           13:'Giao nhau với đường ưu tiên',    
           14:'Cảnh báo nguy hiểm',     
           15:'Stop',       
           16:'Đường cấm',       
           17:'Cấm xe > 3,5 tấn',       
           18:'Câm đi ngược chiều',       
           19:'BiểN nguy hiểm khác',     
           20:'Nguy hiểm khi rẽ trái',      
           21:'Nguy hiểm khi rẽ phải',   
           22:'Chỗ ngoặt nguy hiểm',      
           23:'Cảnh báo đường nhấp nhô',     
           24:'Cảnh báo đường trơn trượt',       
           25:'Đường hẹp bên phải',  
           26:'Đường đang thi công',    
           27:'Cảnh báo có đèn tín hiệu',      
           28:'Cảnh báo có người đi bộ',     
           29:'Cảnh báo có học sinh đi qua',     
           30:'Cảnh báo có xe đạp đi qua',       
           31:'Cảnh báo tuyết lở',
           32:'Cảnh báo thú hoang đi qua',      
           33:'Hết tất cả lệnh cấm',      
           34:'Rẽ phải phía trước',     
           35:'Rẽ trái phía trước',       
           36:'Đi thẳng',      
           37:'Đi thẳng hoặc rẽ phải',      
           38:'Đi thẳng hoặc rẽ trái',      
           39:'Hướng phải đi vòng sang phải',     
           40:'Hướng trái đi vòng sang trái',      
           41:'Nơi giao nhau chạy theo vòng xuyến',     
           42:'Hết đoạn đường cấm vượt',      
           43:'Hết đoạn đường cấm vượtvới xe trên 3.5 tấn' }
                 

top=tk.Tk()
top.geometry('800x600')
top.title('Nhận dạng biển báo giao thông ')
top.configure(background='#ffffff')

label=Label(top,background='#ffffff', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)

    pred_probabilities = model.predict(image)[0]
    pred = pred_probabilities.argmax(axis=-1)
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Nhận dạng",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#c71b20', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#c71b20', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Nhận dạng biển báo giao thông",pady=10, font=('arial',20,'bold'))
heading.configure(background='#ffffff',foreground='#364156')

heading1 = Label(top, text="Vui lòng upload ảnh bạn muốn nhận dạng",pady=10, font=('arial',20,'bold'))
heading1.configure(background='#ffffff',foreground='#364156')



heading.pack()
heading1.pack()

top.mainloop()
