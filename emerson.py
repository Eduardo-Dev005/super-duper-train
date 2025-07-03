import customtkinter as ctk

telaP = ctk.CTk()
telaP.title("Dados")
telaP.geometry("300x400")
telaP.resizable(False, False)
telaP._set_appearance_mode("light")

telaP.grid_columnconfigure(0, weight=0)
telaP.grid_columnconfigure(6, weight=0)

telaP.grid_rowconfigure(0, weight = 1)
telaP.grid_rowconfigure(1, weight = 1)
telaP.grid_rowconfigure(2, weight = 1)
telaP.grid_rowconfigure(3, weight = 1)
telaP.grid_rowconfigure(4, weight = 1)
telaP.grid_rowconfigure(5, weight = 1)
telaP.grid_rowconfigure(6, weight = 1)
telaP.grid_rowconfigure(7, weight = 1)
telaP.grid_rowconfigure(8, weight = 1)
telaP.grid_rowconfigure(9, weight = 1)
telaP.grid_rowconfigure(10, weight = 1)

b1 = ctk.CTkButton(
    telaP,
    text = "d4", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b1.grid(row = 8, 
        column = 1,
        padx = 10,
        sticky = "s"
        )

b2 =  ctk.CTkButton(
    telaP,
    text = "d6", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b2.grid(
    row = 8, 
    column = 2,
    padx = 10,
    sticky = "s"
    )

b3 =  ctk.CTkButton(
    telaP,
    text = "d8", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b3.grid(
    row = 8, 
    column = 3,
    padx = 10,
    sticky = "s"
    )

b4 =  ctk.CTkButton(
    telaP,
    text = "d10", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b4.grid(
    row = 9, 
    column = 1,
    padx = 10,  
    )

b5 =  ctk.CTkButton(
    telaP,
    text = "d12", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b5.grid(
    row = 9, 
    column = 2,
    padx = 10,  
    )

b6=  ctk.CTkButton(
    telaP,
    text = "d20", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b6.grid(
    row = 9, 
    column = 3,
    padx = 10,  
    )

b7 = ctk.CTkButton(
    telaP,
    text = "-", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b7.grid(
    row = 10, 
    column = 1,
    padx = 10,  
    sticky ="N"
    )

b8 = ctk.CTkButton(
    telaP,
    text = "d20", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b8.grid(
    row = 10, 
    column = 2,
    padx = 10,  
    sticky ="N"
    )

b9 = ctk.CTkButton(
    telaP,
    text = "+", 
    fg_color= "#000000", 
    text_color= "#ffffff",
    height= 30,
    width= 80
    )

b9.grid(
    row = 10, 
    column = 3,
    padx = 10,  
    sticky ="N"
    )
telaP.mainloop()