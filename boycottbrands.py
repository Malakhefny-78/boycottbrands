from tkinter import *

# Function to load boycott brands from the file
def boycott_brands_function():
        with open(r'C:\Users\malak\Desktop\Boycott Brands.txt', 'r') as file:
            brands = file.read()
            return brands
    
# Function to check if the company is on the boycott list
def check_boycott():
    company_name = entry1.get().capitalize()
    if company_name in boycott_brands.split('\n'):
        result_lable.config(text=f"{company_name} is on the boycott list.")
    else:
        result_lable.config(text=f"{company_name} is not on the boycott list.")
    entry1.delete(0, END)

#add company to list
def add_company():
    company_name = entry2.get().capitalize()
    with open(r'C:\Users\malak\Desktop\Boycott Brands.txt', 'a') as file:
        file.write(company_name + '\n')
    global boycott_brands
    boycott_brands += company_name + '\n'
    result_lable.config(text=f"{company_name} has been added to the boycott list.")
    entry2.delete(0, END)

# Load the boycott brands from the file
boycott_brands = boycott_brands_function()

# Create the main window
window = Tk()
window.geometry('1000x500')
window.title("Boycott Brands Checker")
window.configure(bg='sky blue')

# Create and place the Result Label
label1 = Label(window, text="Company name:",font=('sansserif',20),bg='sky blue', fg='navy blue')  
label1.place(x=350,y=100)

# Create and place the Entry 
entry1 = Entry(window, font=('sansserif',20) ,fg='maroon',bg='snow2')  
entry1.place(x=300,y=150)

# Create and place the Check Button
check_button =Button(window, text="Check Boycott Status", command=check_boycott,bg='lavender')  
check_button.place(x=390,y=200)

# Create and place the Label for adding a new company to the boycott list
label2 = Label(window, text="Company to add:",font=('sansserif',20),bg='sky blue', fg='navy blue')  
label2.place(x=330,y=250)

# Create and place the Entry for adding a new company to the boycott list
entry2 = Entry(window,font=('sansserif',20) ,fg='maroon',bg='snow2')  
entry2.place(x=300,y=300)

# Create and place the Button to add a new company to the boycott list
add_button = Button(window, text="Add Company to Boycott List", command=add_company, bg='lavender')
add_button.place(x=350,y=350)

#create and place the result for output
result_lable=Label(window, text="Result",font=('sansserif',20),bg='sky blue', fg='navy blue')
result_lable.place(x=200,y=400)

# Run the application
window.mainloop()