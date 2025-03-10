import pandas
filename = None
column_names = []
get_names = []
df = {}
validation = None
def creation_window(root_window,box,xpos,ypos,buton,text):
    global filename
    global validation
    columns_wanted = None

    def check_columns_wanted(column,root_window,box,xpos,ypos,text):
        global list
        global validation
        result = column.get()
        #set_var = result
        try:
            result = int(result)
            if result<= 9:
                for i in range(0,result):
                    entry = box(root_window,width=50)
                    entry.place(x=xpos,y=ypos+30)
                    lab = text(root_window,text="column "+ str(i+1))
                    lab.place(x=xpos-70,y=ypos+30)
                    column_names.append(entry)
                    ypos+=30
            else:
                if validation:
                    validation.destroy()
                    validation = text(root_window,text="insert a valid number from 1-9")
                    validation.place(x=xpos+120,y=ypos-30)
                else:
                    validation = text(root_window,text="insert a valid number from 1-9")
                    validation.place(x=xpos+120,y=ypos-30)
        except:
            if validation:
                validation.destroy()
                validation = text(root_window,text="insert a valid number from 1-9")
                validation.place(x=xpos+120,y=ypos-30)
            else:
                validation.destroy()
                validation = text(root_window,text="insert a valid number from 1-9")
                validation.place(x=xpos+120,y=ypos-30)
            # label = text(root_window,text="insert a valid number from 1-9")
            # label.place(x=xpos+120,y=ypos-30)
        #result = int(column)

        # if int(result)< 9:
        #     for i in range(0,int(result)):
        #         entry = box(root_window,width=50)
        #         entry.place(x=xpos,y=ypos+30)
        #         lab = text(root_window,text="column "+ str(i+1))
        #         lab.place(x=xpos-70,y=ypos+30)
        #         column_names.append(entry)
        #         ypos+=30
        # else:
        #     if validation:
        #         validation.destroy()
        #         validation = text(root_window,text="insert a valid number from 1-9")
        #         validation.place(x=xpos+120,y=ypos-30)




    children = root_window.winfo_children()
    if children:
        for i in children:
            i.destroy()
    
    filename = box(root_window,width=50)
    filename.place(x=xpos,y=ypos)
    label = text(root_window,text="File name")
    label.place(x=xpos-70,y=ypos)
    ypos+=30

    column_wanted_box = box(root_window,width=10)
    column_wanted_box.place(x=xpos+40,y=ypos)

    button = buton(root_window,text="click",command=lambda:check_columns_wanted(column_wanted_box,columns_wanted,box,xpos,ypos,text))
    button.place(x=xpos,y=ypos)

    create_button = buton(root_window,text = "Create",command=create_csv)
    create_button.config(font=["Arial",20,"bold"],fg="red")
    create_button.place(x=xpos,y=400)
    ypos+=30

def create_csv():
    global df
    for i in column_names:
        result = i.get()
        get_names.append(result)
    
    for i in get_names:
        df[i] = ""

    data = pandas.DataFrame(df,index=[0])

    open(filename.get(),"w")
    data.to_csv(filename.get(),index=False)
    

    




