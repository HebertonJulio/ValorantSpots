import customtkinter as ctk         # Interface        
from tkinter import *
from tkvideo import tkvideo
from PIL import Image, ImageTk            # Imagens


# ---- AGENTES -------
#   Sage - Pixel  -
#   Sova - Pixel -
#   Viper - Pixel -
#   Cypher - Pixel -
#   Killjoy - Pixel -
#   Fade - Pixel -
#   Deadlock - Pixel
#   Vyse - Pixel
#   Kayo - Pixel
# -------------------
# ------ MAPAS ------

#   Bind    #
#   Ascent  #
#   Sunset  #
#   Lotus   
#   Haven   #
#   Split   #


# Variaveis Globais
size_window = "1920x1080"
tamanho_video = (450,550)

# Imagens dos mapas
def imagens_mapas():
     global Bind_Final_Image, Ascent_Final_Image, Sunset_Final_Image, Lotus_Final_Image, Haven_Final_Image, Split_Final_Image 
     tamanho_imagem_mapa = (300,300)

     Bind_ImageMap = Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Image_Maps\Bind_Image.jpg")
     Bind_Final_Image = ctk.CTkImage(Bind_ImageMap, size=tamanho_imagem_mapa)

     Ascent_ImageMap = Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Image_Maps\Ascent_Image.jpg")
     Ascent_Final_Image = ctk.CTkImage(Ascent_ImageMap, size=tamanho_imagem_mapa)

     Sunset_ImageMap = Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Image_Maps\Sunset_Image.jpg") 
     Sunset_Final_Image = ctk.CTkImage(Sunset_ImageMap, size=tamanho_imagem_mapa)

     Lotus_ImageMap = Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Image_Maps\Lotus_Image.jpg") 
     Lotus_Final_Image = ctk.CTkImage(Lotus_ImageMap, size=tamanho_imagem_mapa)

     Haven_ImageMap = Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Image_Maps\Haven_Image.jpg") 
     Haven_Final_Image = ctk.CTkImage(Haven_ImageMap, size=tamanho_imagem_mapa)

     Split_ImageMap = Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Image_Maps\Split_Image.png")
     Split_Final_Image = ctk.CTkImage(Split_ImageMap, size=tamanho_imagem_mapa)


def adicionar_plano_de_fundo(PrincipalWindow, caminho_imagem):
    PrincipalWindow.state("zoomed")
    plano_de_fundo = Image.open(caminho_imagem)
    ctk_imagem = ctk.CTkImage(light_image=plano_de_fundo, dark_image=plano_de_fundo, size=(1920,1080))
    label_fundo = ctk.CTkLabel(PrincipalWindow, image=ctk_imagem)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
    label_fundo.image = ctk_imagem


# Icone do software


# Icones Size (55,66)

tamanho_icone = (120,130)

icone_sage = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\sage.png"), size=tamanho_icone)
icone_sova = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\sova.png"), size=tamanho_icone)
icone_viper = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\viper.png"), size=tamanho_icone)
icone_cypher = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\cypher.png"), size=tamanho_icone)
icone_killjoy = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\killjoy.png"), size=tamanho_icone)
icone_fade = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\fade.png"), size=tamanho_icone)
icone_deadlock = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\deadlock.png"), size=tamanho_icone)
icone_vyse = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\vyse.png"), size=tamanho_icone)
icone_kayo = ctk.CTkImage(light_image=Image.open(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icons\kayo.png"), size=tamanho_icone)

 ######################## Funcoes Agentes  ###################################


######### SAGE ###########  SAGE ######################## SAGE ###########  SAGE ###############

def Pixel_Sage():
    global Sage_Window
    Sage_Window = ctk.CTkToplevel(PrincipalWindow)  # Create a Window
    Sage_Window.geometry(size_window)     # Size Window
    Sage_Window.title("Pixel's Sage")   # Title Window
    PrincipalWindow.withdraw()      # Esconde a janela principal
    Sage_Window.state("zoomed") 
    Sage_Window.protocol("WM_DELETE_WINDOW", close_window)    # Fecha a janela principal caso o usuario clique no X
    Button_Voltar_Principal = ctk.CTkButton(Sage_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sage_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    #adicionar_plano_de_fundo(Sage_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    Sage_Spots_Text = ctk.CTkLabel(Sage_Window, text=("Sage | Spots Maps"), font=("Arial", 16, "bold"))
    Sage_Spots_Text.pack(pady=(40, 0))


    # LISTA DE MAPAS | SAGE
    # Frame para agrupar os botoes 


    button_frame = ctk.CTkFrame(Sage_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Sage_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Sage_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sage_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Sage_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Sage_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sage_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Sage_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Sage_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sage_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Sage_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Sage_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sage_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Sage_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Sage_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sage_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Sage_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Sage_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sage_Split.grid(row=1, column=2, padx=10, pady=10)



def Pixel_Sage_Bind():
    Sage_Bind_Window = ctk.CTkToplevel(Sage_Window)
    Sage_Bind_Window.geometry(size_window)
    Sage_Bind_Window.title("Sage | Bind")
    Sage_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sage_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sage_Window.withdraw()
    Sage_Bind_Window.state("zoomed")    # MAXIMIZA A JANELA
    Sage_Bind_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    #adicionar_plano_de_fundo(Sage_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")   
    # VIDEOS SPOTS
    
    label1_sage_bind = Label(Sage_Bind_Window)
    label1_sage_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sage_Maps/Sage_Bind/SAGE_1_BIND.mp4", label1_sage_bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_sage_bind = Label(Sage_Bind_Window)
    label2_sage_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Bind\SAGE_2_BIND.mp4", label2_sage_bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_sage_bind = Label(Sage_Bind_Window)
    label3_sage_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Bind\SAGE_3_BIND.mp4", label3_sage_bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_sage_bind = Label(Sage_Bind_Window)
    label4_sage_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Bind\SAGE_4_BIND.mp4", label4_sage_bind, loop=1, size=tamanho_video)
    player_04.play()

def Pixel_Sage_Ascent():
    Sage_Ascent_Window = ctk.CTkToplevel(Sage_Window)
    Sage_Ascent_Window.geometry(size_window)
    Sage_Ascent_Window.title("Sage | Ascent")
    Sage_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sage_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sage_Window.withdraw()
    Sage_Ascent_Window.state("zoomed")    # MAXIMIZA A JANELA
    Sage_Ascent_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    #adicionar_plano_de_fundo(Sage_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOTS

    label1_sage_Ascent = Label(Sage_Ascent_Window)
    label1_sage_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sage_Maps/Sage_Ascent/SAGE_1_Ascent.mp4", label1_sage_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_sage_Ascent = Label(Sage_Ascent_Window)
    label2_sage_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Ascent\SAGE_2_Ascent.mp4", label2_sage_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_sage_Ascent = Label(Sage_Ascent_Window)
    label3_sage_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Ascent\SAGE_3_Ascent.mp4", label3_sage_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_sage_Ascent = Label(Sage_Ascent_Window)
    label4_sage_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Ascent\SAGE_4_Ascent.mp4", label4_sage_Ascent, loop=1, size=tamanho_video)
    player_04.play()

def Pixel_Sage_Sunset():
    Sage_Sunset_Window = ctk.CTkToplevel(Sage_Window)
    Sage_Sunset_Window.geometry(size_window)
    Sage_Sunset_Window.title("Sage | Sunset")
    Sage_Sunset_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sage_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sage_Window.withdraw()
    Sage_Sunset_Window.state("zoomed")    # MAXIMIZA A JANELA
    Sage_Sunset_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    #adicionar_plano_de_fundo(Sage_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    # VIDEOS SPOTS
    label1_sage_Sunset = Label(Sage_Sunset_Window)
    label1_sage_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sage_Maps/Sage_Sunset/SAGE_1_Sunset.mp4", label1_sage_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_sage_Sunset = Label(Sage_Sunset_Window)
    label2_sage_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Sunset\SAGE_2_Sunset.mp4", label2_sage_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_sage_Sunset = Label(Sage_Sunset_Window)
    label3_sage_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Sunset\SAGE_3_Sunset.mp4", label3_sage_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_sage_Sunset = Label(Sage_Sunset_Window)
    label4_sage_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Sunset\SAGE_4_Sunset.mp4", label4_sage_Sunset, loop=1, size=tamanho_video)
    player_04.play()
    
def Pixel_Sage_Lotus():
    Sage_Lotus_Window = ctk.CTkToplevel(Sage_Window)
    Sage_Lotus_Window.geometry(size_window)
    Sage_Lotus_Window.title("Sage | Lotus")
    Sage_Lotus_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sage_Lotus_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sage_Window.withdraw()
    Sage_Lotus_Window.state("zoomed")    # MAXIMIZA A JANELA    
    Sage_Lotus_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    #adicionar_plano_de_fundo(Sage_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    # VIDEOS SPOTS
    label1_sage_Lotus = Label(Sage_Lotus_Window)
    label1_sage_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sage_Maps/Sage_Lotus/SAGE_1_Lotus.mp4", label1_sage_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_sage_Lotus = Label(Sage_Lotus_Window)
    label2_sage_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Lotus\SAGE_2_Lotus.mp4", label2_sage_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_sage_Lotus = Label(Sage_Lotus_Window)
    label3_sage_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Lotus\SAGE_3_Lotus.mp4", label3_sage_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_sage_Lotus = Label(Sage_Lotus_Window)
    label4_sage_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Lotus\SAGE_4_Lotus.mp4", label4_sage_Lotus, loop=1, size=tamanho_video)
    player_04.play()
    
def Pixel_Sage_Haven():
    Sage_Haven_Window = ctk.CTkToplevel(Sage_Window)
    Sage_Haven_Window.geometry(size_window)
    Sage_Haven_Window.title("Sage | Haven")
    Sage_Haven_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sage_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sage_Window.withdraw()
    Sage_Haven_Window.state("zoomed")    # MAXIMIZA A JANELA
    Sage_Haven_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    #adicionar_plano_de_fundo(Sage_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    # VIDEOS SPOTS
    label1_sage_Haven = Label(Sage_Haven_Window)
    label1_sage_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sage_Maps/Sage_Haven/SAGE_1_Haven.mp4", label1_sage_Haven, loop=1, size=tamanho_video)
    player_01.play()

    label2_sage_Haven = Label(Sage_Haven_Window)
    label2_sage_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Haven\SAGE_2_Haven.mp4", label2_sage_Haven, loop=1, size=tamanho_video)
    player_02.play()

    label3_sage_Haven = Label(Sage_Haven_Window)
    label3_sage_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Haven\SAGE_3_Haven.mp4", label3_sage_Haven, loop=1, size=tamanho_video)
    player_03.play()

    label4_sage_Haven = Label(Sage_Haven_Window)
    label4_sage_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Haven\SAGE_4_Haven.mp4", label4_sage_Haven, loop=1, size=tamanho_video)
    player_04.play()
    
def Pixel_Sage_Split():
    Sage_Split_Window = ctk.CTkToplevel(Sage_Window)
    Sage_Split_Window.geometry(size_window)
    Sage_Split_Window.title("Sage | Split")
    Sage_Split_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sage_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sage_Window.withdraw()
    Sage_Split_Window.state("zoomed")    # MAXIMIZA A JANELA
    Sage_Split_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    #adicionar_plano_de_fundo(Sage_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    # VIDEOS SPOTS
    label1_sage_Split = Label(Sage_Split_Window)
    label1_sage_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sage_Maps/Sage_Split/SAGE_1_Split.mp4", label1_sage_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_sage_Split = Label(Sage_Split_Window)
    label2_sage_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Split\SAGE_2_Split.mp4", label2_sage_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_sage_Split = Label(Sage_Split_Window)
    label3_sage_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Split\SAGE_3_Split.mp4", label3_sage_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_sage_Split = Label(Sage_Split_Window)
    label4_sage_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sage_Maps\Sage_Split\SAGE_4_Split.mp4", label4_sage_Split, loop=1, size=tamanho_video)
    player_04.play()
    



###### SOVA ######### SOVA ####### SOVA ####### SOVA ####### SOVA #######
def Pixel_Sova():
    global Sova_Window
    Sova_Window = ctk.CTkToplevel(PrincipalWindow)
    Sova_Window.geometry(size_window)
    Sova_Window.title("Pixel's Sova")
    PrincipalWindow.withdraw()
    Sova_Window.state("zoomed")
    Sova_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sova_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    #adicionar_plano_de_fundo(Sova_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    Sova_Spots_Text = ctk.CTkLabel(Sova_Window, text=("Sova | Spots Maps"), font=("Arial", 16, "bold"))
    Sova_Spots_Text.pack(pady=(20, 0))

    # LISTA DE MAPAS | SOVA


    # BIND
    button_frame = ctk.CTkFrame(Sova_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Sova_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Sova_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sova_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Sova_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Sova_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sova_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Sova_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Sova_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sova_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Sova_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Sova_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sova_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Sova_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Sova_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sova_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Sova_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Sova_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Sova_Split.grid(row=1, column=2, padx=10, pady=10)



def Pixel_Sova_Bind():
    Sova_Bind_Window = ctk.CTkToplevel(Sova_Window)
    Sova_Bind_Window.geometry(size_window)
    Sova_Bind_Window.title("Sova | Bind")
    Sova_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sova_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sova_Window.withdraw()
    Sova_Bind_Window.state("zoomed") 
    #adicionar_plano_de_fundo(Sova_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOTS
    label1_Sova_bind = Label(Sova_Bind_Window)
    label1_Sova_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sova_Maps/Sova_Bind/Sova_1_BIND.mp4", label1_Sova_bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_Sova_bind = Label(Sova_Bind_Window)
    label2_Sova_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Bind\Sova_2_BIND.mp4", label2_Sova_bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_Sova_bind = Label(Sova_Bind_Window)
    label3_Sova_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Bind\Sova_3_BIND.mp4", label3_Sova_bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_Sova_bind = Label(Sova_Bind_Window)
    label4_Sova_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Bind\Sova_4_BIND.mp4", label4_Sova_bind, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Sova_Ascent():
    Sova_Ascent_Window = ctk.CTkToplevel(Sova_Window)
    Sova_Ascent_Window.geometry(size_window)
    Sova_Ascent_Window.title("Sova | Ascent")
    Sova_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sova_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sova_Window.withdraw()
    Sova_Ascent_Window.state("zoomed") 
    #adicionar_plano_de_fundo(Sova_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOTS
    label1_Sova_Ascent = Label(Sova_Ascent_Window)
    label1_Sova_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sova_Maps/Sova_Ascent/Sova_1_Ascent.mp4", label1_Sova_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_Sova_Ascent = Label(Sova_Ascent_Window)
    label2_Sova_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Ascent\Sova_2_Ascent.mp4", label2_Sova_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_Sova_Ascent = Label(Sova_Ascent_Window)
    label3_Sova_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Ascent\Sova_3_Ascent.mp4", label3_Sova_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_Sova_Ascent = Label(Sova_Ascent_Window)
    label4_Sova_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Ascent\Sova_4_Ascent.mp4", label4_Sova_Ascent, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Sova_Sunset():
    Sova_Sunset_Window = ctk.CTkToplevel(Sova_Window)
    Sova_Sunset_Window.geometry(size_window)
    Sova_Sunset_Window.title("Sova | Sunset")
    Sova_Sunset_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sova_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sova_Window.withdraw()
    Sova_Sunset_Window.state("zoomed") 
    #adicionar_plano_de_fundo(Sova_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOTS

    label1_Sova_Sunset = Label(Sova_Sunset_Window)
    label1_Sova_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sova_Maps/Sova_Sunset/Sova_1_Sunset.mp4", label1_Sova_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_Sova_Sunset = Label(Sova_Sunset_Window)
    label2_Sova_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Sunset\Sova_2_Sunset.mp4", label2_Sova_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_Sova_Sunset = Label(Sova_Sunset_Window)
    label3_Sova_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Sunset\Sova_3_Sunset.mp4", label3_Sova_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_Sova_Sunset = Label(Sova_Sunset_Window)
    label4_Sova_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Sunset\Sova_4_Sunset.mp4", label4_Sova_Sunset, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Sova_Lotus():
    Sova_Lotus_Window = ctk.CTkToplevel(Sova_Window)
    Sova_Lotus_Window.geometry(size_window)
    Sova_Lotus_Window.title("Sova | Lotus")
    Sova_Lotus_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sova_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sova_Window.withdraw()
    Sova_Lotus_Window.state("zoomed") 
    #adicionar_plano_de_fundo(Sova_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOTS

    label1_Sova_Lotus = Label(Sova_Lotus_Window)
    label1_Sova_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sova_Maps/Sova_Lotus/Sova_1_Lotus.mp4", label1_Sova_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_Sova_Lotus = Label(Sova_Lotus_Window)
    label2_Sova_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Lotus\Sova_2_Lotus.mp4", label2_Sova_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_Sova_Lotus = Label(Sova_Lotus_Window)
    label3_Sova_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Lotus\Sova_3_Lotus.mp4", label3_Sova_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_Sova_Lotus = Label(Sova_Lotus_Window)
    label4_Sova_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Lotus\Sova_4_Lotus.mp4", label4_Sova_Lotus, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Sova_Haven():
    Sova_Haven_Window = ctk.CTkToplevel(Sova_Window)
    Sova_Haven_Window.geometry(size_window)
    Sova_Haven_Window.title("Sova | Haven")
    Sova_Haven_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sova_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sova_Window.withdraw()
    Sova_Haven_Window.state("zoomed") 
    #adicionar_plano_de_fundo(Sova_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOTS
    label1_Sova_Haven = Label(Sova_Haven_Window)
    label1_Sova_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sova_Maps/Sova_Haven/Sova_1_Haven.mp4", label1_Sova_Haven, loop=1, size=tamanho_video)
    player_01.play()

    label2_Sova_Haven = Label(Sova_Haven_Window)
    label2_Sova_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Haven\Sova_2_Haven.mp4", label2_Sova_Haven, loop=1, size=tamanho_video)
    player_02.play()

    label3_Sova_Haven = Label(Sova_Haven_Window)
    label3_Sova_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Haven\Sova_3_Haven.mp4", label3_Sova_Haven, loop=1, size=tamanho_video)
    player_03.play()

    label4_Sova_Haven = Label(Sova_Haven_Window)
    label4_Sova_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Haven\Sova_4_Haven.mp4", label4_Sova_Haven, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Sova_Split():
    Sova_Split_Window = ctk.CTkToplevel(Sova_Window)
    Sova_Split_Window.geometry(size_window)
    Sova_Split_Window.title("Sova | Split")
    Sova_Split_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Sova_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Sova_Window.withdraw()
    Sova_Split_Window.state("zoomed") 
    #adicionar_plano_de_fundo(Sova_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOTS

    label1_Sova_Split = Label(Sova_Split_Window)
    label1_Sova_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Sova_Maps/Sova_Split/Sova_1_Split.mp4", label1_Sova_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_Sova_Split = Label(Sova_Split_Window)
    label2_Sova_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Split\Sova_2_Split.mp4", label2_Sova_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_Sova_Split = Label(Sova_Split_Window)
    label3_Sova_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Split\Sova_3_Split.mp4", label3_Sova_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_Sova_Split = Label(Sova_Split_Window)
    label4_Sova_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Sova_Maps\Sova_Split\Sova_4_Split.mp4", label4_Sova_Split, loop=1, size=tamanho_video)
    player_04.play()


####### VIPER ####### VIPER ####### VIPER ######### VIPER ####### VIPER #####

def Pixel_Viper():
    global Viper_Window
    Viper_Window = ctk.CTkToplevel(PrincipalWindow)
    Viper_Window.geometry(size_window)
    Viper_Window.title("Pixel's Viper")
    PrincipalWindow.withdraw()
    Viper_Window.state("zoomed")
    Viper_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Viper_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    #adicionar_plano_de_fundo(Viper_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    Viper_Spots_Text = ctk.CTkLabel(Viper_Window, text="Viper | Spots Maps", font=("Arial", 16, "bold"))
    Viper_Spots_Text.pack(pady=(20,0))

    # LISTA DE MAPAS | VIPER
    # BIND
    button_frame = ctk.CTkFrame(Viper_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Viper_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Viper_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Viper_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Viper_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Viper_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Viper_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Viper_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Viper_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Viper_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Viper_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Viper_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Viper_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Viper_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Viper_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Viper_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Viper_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Viper_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Viper_Split.grid(row=1, column=2, padx=10, pady=10)



def Pixel_Viper_Bind():
    Viper_Bind_Window = ctk.CTkToplevel(Viper_Window)
    Viper_Bind_Window.geometry(size_window)
    Viper_Bind_Window.title("Viper | Bind")
    Viper_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Viper_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Viper_Window.withdraw()
    Viper_Bind_Window.state("zoomed")
    #adicionar_plano_de_fundo(Viper_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")    
    # VIDEOS SPOT
    label1_Viper_bind = Label(Viper_Bind_Window)
    label1_Viper_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Viper_Maps/Viper_Bind/Viper_1_BIND.mp4", label1_Viper_bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_Viper_bind = Label(Viper_Bind_Window)
    label2_Viper_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Bind\Viper_2_BIND.mp4", label2_Viper_bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_Viper_bind = Label(Viper_Bind_Window)
    label3_Viper_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Bind\Viper_3_BIND.mp4", label3_Viper_bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_Viper_bind = Label(Viper_Bind_Window)
    label4_Viper_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Bind\Viper_4_BIND.mp4", label4_Viper_bind, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Viper_Ascent():
    Viper_Ascent_Window = ctk.CTkToplevel(Viper_Window)
    Viper_Ascent_Window.geometry(size_window)
    Viper_Ascent_Window.title("Viper | Ascent")
    Viper_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Viper_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Viper_Window.withdraw()
    Viper_Ascent_Window.state("zoomed")
    #adicionar_plano_de_fundo(Viper_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Viper_Ascent = Label(Viper_Ascent_Window)
    label1_Viper_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Viper_Maps/Viper_Ascent/Viper_1_Ascent.mp4", label1_Viper_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_Viper_Ascent = Label(Viper_Ascent_Window)
    label2_Viper_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Ascent\Viper_2_Ascent.mp4", label2_Viper_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_Viper_Ascent = Label(Viper_Ascent_Window)
    label3_Viper_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Ascent\Viper_3_Ascent.mp4", label3_Viper_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_Viper_Ascent = Label(Viper_Ascent_Window)
    label4_Viper_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Ascent\Viper_4_Ascent.mp4", label4_Viper_Ascent, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Viper_Sunset():
    Viper_Sunset_Window = ctk.CTkToplevel(Viper_Window)
    Viper_Sunset_Window.geometry(size_window)
    Viper_Sunset_Window.title("Viper | Sunset")
    Viper_Sunset_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Viper_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Viper_Window.withdraw()
    Viper_Sunset_Window.state("zoomed")
    #adicionar_plano_de_fundo(Viper_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Viper_Sunset = Label(Viper_Sunset_Window)
    label1_Viper_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Viper_Maps/Viper_Sunset/Viper_1_Sunset.mp4", label1_Viper_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_Viper_Sunset = Label(Viper_Sunset_Window)
    label2_Viper_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Sunset\Viper_2_Sunset.mp4", label2_Viper_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_Viper_Sunset = Label(Viper_Sunset_Window)
    label3_Viper_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Sunset\Viper_3_Sunset.mp4", label3_Viper_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_Viper_Sunset = Label(Viper_Sunset_Window)
    label4_Viper_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Sunset\Viper_4_Sunset.mp4", label4_Viper_Sunset, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Viper_Lotus():
    Viper_Lotus_Window = ctk.CTkToplevel(Viper_Window)
    Viper_Lotus_Window.geometry(size_window)
    Viper_Lotus_Window.title("Viper | Lotus")
    Viper_Lotus_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Viper_Lotus_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Viper_Window.withdraw()
    Viper_Lotus_Window.state("zoomed")
    #adicionar_plano_de_fundo(Viper_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Viper_Lotus = Label(Viper_Lotus_Window)
    label1_Viper_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Viper_Maps/Viper_Lotus/Viper_1_Lotus.mp4", label1_Viper_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_Viper_Lotus = Label(Viper_Lotus_Window)
    label2_Viper_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Lotus\Viper_2_Lotus.mp4", label2_Viper_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_Viper_Lotus = Label(Viper_Lotus_Window)
    label3_Viper_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Lotus\Viper_3_Lotus.mp4", label3_Viper_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_Viper_Lotus = Label(Viper_Lotus_Window)
    label4_Viper_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Lotus\Viper_4_Lotus.mp4", label4_Viper_Lotus, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Viper_Haven():
    Viper_Haven_Window = ctk.CTkToplevel(Viper_Window)
    Viper_Haven_Window.geometry(size_window)
    Viper_Haven_Window.title("Viper | Haven")
    Viper_Haven_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Viper_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Viper_Window.withdraw()
    Viper_Haven_Window.state("zoomed")
    #adicionar_plano_de_fundo(Viper_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Viper_Haven = Label(Viper_Haven_Window)
    label1_Viper_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Viper_Maps/Viper_Haven/Viper_1_Haven.mp4", label1_Viper_Haven, loop=1, size=tamanho_video)
    player_01.play()

    label2_Viper_Haven = Label(Viper_Haven_Window)
    label2_Viper_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Haven\Viper_2_Haven.mp4", label2_Viper_Haven, loop=1, size=tamanho_video)
    player_02.play()

    label3_Viper_Haven = Label(Viper_Haven_Window)
    label3_Viper_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Haven\Viper_3_Haven.mp4", label3_Viper_Haven, loop=1, size=tamanho_video)
    player_03.play()

    label4_Viper_Haven = Label(Viper_Haven_Window)
    label4_Viper_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Haven\Viper_4_Haven.mp4", label4_Viper_Haven, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Viper_Split():
    Viper_Split_Window = ctk.CTkToplevel(Viper_Window)
    Viper_Split_Window.geometry(size_window)
    Viper_Split_Window.title("Viper | Split")
    Viper_Split_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Viper_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Viper_Window.withdraw()
    Viper_Split_Window.state("zoomed")
    #adicionar_plano_de_fundo(Viper_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Viper_Split = Label(Viper_Split_Window)
    label1_Viper_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Viper_Maps/Viper_Split/Viper_1_Split.mp4", label1_Viper_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_Viper_Split = Label(Viper_Split_Window)
    label2_Viper_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Split\Viper_2_Split.mp4", label2_Viper_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_Viper_Split = Label(Viper_Split_Window)
    label3_Viper_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Split\Viper_3_Split.mp4", label3_Viper_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_Viper_Split = Label(Viper_Split_Window)
    label4_Viper_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Viper_Maps\Viper_Split\Viper_4_Split.mp4", label4_Viper_Split, loop=1, size=tamanho_video)
    player_04.play()



##### CYPHER ##### CYPHER ###### CYPHER ###### CYPHER ###### CYPHER ###### CYPHER ######
def Pixel_Cypher():
    global Cypher_Window
    Cypher_Window = ctk.CTkToplevel(PrincipalWindow)
    Cypher_Window.geometry(size_window)
    Cypher_Window.title("Cypher Spots")
    PrincipalWindow.withdraw()
    Cypher_Window.state("zoomed")
    Cypher_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Cypher_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    #adicionar_plano_de_fundo(Cypher_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    # Comeco da Janela Cypher
    Cypher_Spots_Text = ctk.CTkLabel(Cypher_Window, text="Cypher | Spots Maps", font=("Arial", 16, "bold"))
    Cypher_Spots_Text.pack(pady=(20,0))

    # LISTA DE MAPAS | CYPHER
    # BIND
    button_frame = ctk.CTkFrame(Cypher_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Cypher_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Cypher_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Cypher_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Cypher_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Cypher_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Cypher_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Cypher_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Cypher_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Cypher_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Cypher_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Cypher_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Cypher_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Cypher_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Cypher_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Cypher_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Cypher_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Cypher_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Cypher_Split.grid(row=1, column=2, padx=10, pady=10)




def Pixel_Cypher_Bind():
    Cypher_Bind_Window = ctk.CTkToplevel(Cypher_Window)
    Cypher_Bind_Window.geometry(size_window)
    Cypher_Bind_Window.title("Cypher | Bind")
    Cypher_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Cypher_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Cypher_Window.withdraw()
    Cypher_Bind_Window.state("zoomed")
    #adicionar_plano_de_fundo(Cypher_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Cypher_bind = Label(Cypher_Bind_Window)
    label1_Cypher_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Cypher_Maps/Cypher_Bind/Cypher_1_BIND.mp4", label1_Cypher_bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_Cypher_bind = Label(Cypher_Bind_Window)
    label2_Cypher_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Bind\Cypher_2_BIND.mp4", label2_Cypher_bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_Cypher_bind = Label(Cypher_Bind_Window)
    label3_Cypher_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Bind\Cypher_3_BIND.mp4", label3_Cypher_bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_Cypher_bind = Label(Cypher_Bind_Window)
    label4_Cypher_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Bind\Cypher_4_BIND.mp4", label4_Cypher_bind, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Cypher_Ascent():
    Cypher_Ascent_Window = ctk.CTkToplevel(Cypher_Window)
    Cypher_Ascent_Window.geometry(size_window)
    Cypher_Ascent_Window.title("Cypher | Ascent")
    Cypher_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Cypher_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Cypher_Window.withdraw()
    Cypher_Ascent_Window.state("zoomed")
    #adicionar_plano_de_fundo(Cypher_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")   
    # VIDEOS SPOT
    label1_Cypher_Ascent = Label(Cypher_Ascent_Window)
    label1_Cypher_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Cypher_Maps/Cypher_Ascent/Cypher_1_Ascent.mp4", label1_Cypher_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_Cypher_Ascent = Label(Cypher_Ascent_Window)
    label2_Cypher_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Ascent\Cypher_2_Ascent.mp4", label2_Cypher_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_Cypher_Ascent = Label(Cypher_Ascent_Window)
    label3_Cypher_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Ascent\Cypher_3_Ascent.mp4", label3_Cypher_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_Cypher_Ascent = Label(Cypher_Ascent_Window)
    label4_Cypher_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Ascent\Cypher_4_Ascent.mp4", label4_Cypher_Ascent, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Cypher_Sunset():
    Cypher_Sunset_Window = ctk.CTkToplevel(Cypher_Window)
    Cypher_Sunset_Window.geometry(size_window)
    Cypher_Sunset_Window.title("Cypher | Sunset")
    Cypher_Sunset_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Cypher_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Cypher_Window.withdraw()
    Cypher_Sunset_Window.state("zoomed")
    #adicionar_plano_de_fundo(Cypher_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Cypher_Sunset = Label(Cypher_Sunset_Window)
    label1_Cypher_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Cypher_Maps/Cypher_Sunset/Cypher_1_Sunset.mp4", label1_Cypher_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_Cypher_Sunset = Label(Cypher_Sunset_Window)
    label2_Cypher_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Sunset\Cypher_2_Sunset.mp4", label2_Cypher_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_Cypher_Sunset = Label(Cypher_Sunset_Window)
    label3_Cypher_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Sunset\Cypher_3_Sunset.mp4", label3_Cypher_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_Cypher_Sunset = Label(Cypher_Sunset_Window)
    label4_Cypher_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Sunset\Cypher_4_Sunset.mp4", label4_Cypher_Sunset, loop=1, size=tamanho_video)
    player_04.play()

def Pixel_Cypher_Lotus():
    Cypher_Lotus_Window = ctk.CTkToplevel(Cypher_Window)
    Cypher_Lotus_Window.geometry(size_window)
    Cypher_Lotus_Window.title("Cypher | Lotus")
    Cypher_Lotus_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Cypher_Lotus_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Cypher_Window.withdraw()
    Cypher_Lotus_Window.state("zoomed")
    #adicionar_plano_de_fundo(Cypher_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Cypher_Lotus = Label(Cypher_Lotus_Window)
    label1_Cypher_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Cypher_Maps/Cypher_Lotus/Cypher_1_Lotus.mp4", label1_Cypher_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_Cypher_Lotus = Label(Cypher_Lotus_Window)
    label2_Cypher_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Lotus\Cypher_2_Lotus.mp4", label2_Cypher_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_Cypher_Lotus = Label(Cypher_Lotus_Window)
    label3_Cypher_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Lotus\Cypher_3_Lotus.mp4", label3_Cypher_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_Cypher_Lotus = Label(Cypher_Lotus_Window)
    label4_Cypher_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Lotus\Cypher_4_Lotus.mp4", label4_Cypher_Lotus, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Cypher_Haven():
    Cypher_Haven_Window = ctk.CTkToplevel(Cypher_Window)
    Cypher_Haven_Window.geometry(size_window)
    Cypher_Haven_Window.title("Cypher | Haven")
    Cypher_Haven_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Cypher_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Cypher_Window.withdraw()
    Cypher_Haven_Window.state("zoomed")
    #adicionar_plano_de_fundo(Cypher_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Cypher_Haven = Label(Cypher_Haven_Window)
    label1_Cypher_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Cypher_Maps/Cypher_Haven/Cypher_1_Haven.mp4", label1_Cypher_Haven, loop=1, size=tamanho_video)
    player_01.play()

    label2_Cypher_Haven = Label(Cypher_Haven_Window)
    label2_Cypher_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Haven\Cypher_2_Haven.mp4", label2_Cypher_Haven, loop=1, size=tamanho_video)
    player_02.play()

    label3_Cypher_Haven = Label(Cypher_Haven_Window)
    label3_Cypher_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Haven\Cypher_3_Haven.mp4", label3_Cypher_Haven, loop=1, size=tamanho_video)
    player_03.play()

    label4_Cypher_Haven = Label(Cypher_Haven_Window)
    label4_Cypher_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Haven\Cypher_4_Haven.mp4", label4_Cypher_Haven, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Cypher_Split():
    Cypher_Split_Window = ctk.CTkToplevel(Cypher_Window)
    Cypher_Split_Window.geometry(size_window)
    Cypher_Split_Window.title("Cypher | Split")
    Cypher_Split_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Cypher_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Cypher_Window.withdraw()
    Cypher_Split_Window.state("zoomed")
    #adicionar_plano_de_fundo(Cypher_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Cypher_Split = Label(Cypher_Split_Window)
    label1_Cypher_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Cypher_Maps/Cypher_Split/Cypher_1_Split.mp4", label1_Cypher_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_Cypher_Split = Label(Cypher_Split_Window)
    label2_Cypher_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Split\Cypher_2_Split.mp4", label2_Cypher_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_Cypher_Split = Label(Cypher_Split_Window)
    label3_Cypher_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Split\Cypher_3_Split.mp4", label3_Cypher_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_Cypher_Split = Label(Cypher_Split_Window)
    label4_Cypher_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Cypher_Maps\Cypher_Split\Cypher_4_Split.mp4", label4_Cypher_Split, loop=1, size=tamanho_video)
    player_04.play()



########  KILLJOY ####### KILLJOY ######### KILLJOY ######## KILLJOY ######## KILLJOY ########
def Pixel_Killjoy():
    global Killjoy_Window
    Killjoy_Window = ctk.CTkToplevel(PrincipalWindow)
    Killjoy_Window.geometry(size_window)
    Killjoy_Window.title("Killjoy Spots")
    Killjoy_Window.protocol("WM_DELETE_WINDOW", close_window)
    PrincipalWindow.withdraw()
    Killjoy_Window.state("zoomed")
    Button_Voltar_Principal = ctk.CTkButton(Killjoy_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    #adicionar_plano_de_fundo(Killjoy_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")


    # Comeco da Janela Killjoy
    Killjoy_Spots_Text = ctk.CTkLabel(Killjoy_Window, text="Killjoy | Spots Maps", font=("Arial", 16, "bold"))
    Killjoy_Spots_Text.pack(pady=(20,0))

    # LISTA DE MAPAS | Killjoy
    # BIND
    button_frame = ctk.CTkFrame(Killjoy_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Killjoy_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Killjoy_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Killjoy_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Killjoy_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Killjoy_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Killjoy_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Killjoy_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Killjoy_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Killjoy_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Killjoy_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Killjoy_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Killjoy_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Killjoy_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Killjoy_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Killjoy_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Killjoy_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Killjoy_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Killjoy_Split.grid(row=1, column=2, padx=10, pady=10)



def Pixel_Killjoy_Bind():
    Killjoy_Bind_Window = ctk.CTkToplevel(Killjoy_Window)
    Killjoy_Bind_Window.geometry(size_window)
    Killjoy_Bind_Window.title("Killjoy | Bind")
    Killjoy_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Killjoy_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Killjoy_Window.withdraw()
    Killjoy_Bind_Window.state("zoomed")
    #adicionar_plano_de_fundo(Killjoy_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Killjoy_bind = Label(Killjoy_Bind_Window)
    label1_Killjoy_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Killjoy_Maps/Killjoy_Bind/Killjoy_1_BIND.mp4", label1_Killjoy_bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_Killjoy_bind = Label(Killjoy_Bind_Window)
    label2_Killjoy_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Bind\Killjoy_2_BIND.mp4", label2_Killjoy_bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_Killjoy_bind = Label(Killjoy_Bind_Window)
    label3_Killjoy_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Bind\Killjoy_3_BIND.mp4", label3_Killjoy_bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_Killjoy_bind = Label(Killjoy_Bind_Window)
    label4_Killjoy_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Bind\Killjoy_4_BIND.mp4", label4_Killjoy_bind, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Killjoy_Ascent():
    Killjoy_Ascent_Window = ctk.CTkToplevel(Killjoy_Window)
    Killjoy_Ascent_Window.geometry(size_window)
    Killjoy_Ascent_Window.title("Killjoy | Ascent")
    Killjoy_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Killjoy_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Killjoy_Window.withdraw()
    Killjoy_Ascent_Window.state("zoomed")
    #adicionar_plano_de_fundo(Killjoy_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Killjoy_Ascent = Label(Killjoy_Ascent_Window)
    label1_Killjoy_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Killjoy_Maps/Killjoy_Ascent/Killjoy_1_Ascent.mp4", label1_Killjoy_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_Killjoy_Ascent = Label(Killjoy_Ascent_Window)
    label2_Killjoy_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Ascent\Killjoy_2_Ascent.mp4", label2_Killjoy_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_Killjoy_Ascent = Label(Killjoy_Ascent_Window)
    label3_Killjoy_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Ascent\Killjoy_3_Ascent.mp4", label3_Killjoy_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_Killjoy_Ascent = Label(Killjoy_Ascent_Window)
    label4_Killjoy_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Ascent\Killjoy_4_Ascent.mp4", label4_Killjoy_Ascent, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Killjoy_Sunset():
    Killjoy_Sunset_Window = ctk.CTkToplevel(Killjoy_Window)
    Killjoy_Sunset_Window.geometry(size_window)
    Killjoy_Sunset_Window.title("Killjoy | Sunset")
    Killjoy_Sunset_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Killjoy_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Killjoy_Window.withdraw()
    Killjoy_Sunset_Window.state("zoomed")
    #adicionar_plano_de_fundo(Killjoy_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    # VIDEOS SPOT
    label1_Killjoy_Sunset = Label(Killjoy_Sunset_Window)
    label1_Killjoy_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Killjoy_Maps/Killjoy_Sunset/Killjoy_1_Sunset.mp4", label1_Killjoy_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_Killjoy_Sunset = Label(Killjoy_Sunset_Window)
    label2_Killjoy_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Sunset\Killjoy_2_Sunset.mp4", label2_Killjoy_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_Killjoy_Sunset = Label(Killjoy_Sunset_Window)
    label3_Killjoy_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Sunset\Killjoy_3_Sunset.mp4", label3_Killjoy_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_Killjoy_Sunset = Label(Killjoy_Sunset_Window)
    label4_Killjoy_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Sunset\Killjoy_4_Sunset.mp4", label4_Killjoy_Sunset, loop=1, size=tamanho_video)
    player_04.play()




def Pixel_Killjoy_Lotus():
    Killjoy_Lotus_Window = ctk.CTkToplevel(Killjoy_Window)
    Killjoy_Lotus_Window.geometry(size_window)
    Killjoy_Lotus_Window.title("Killjoy | Lotus")
    Killjoy_Lotus_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Killjoy_Lotus_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Killjoy_Window.withdraw()
    Killjoy_Lotus_Window.state("zoomed")
    #adicionar_plano_de_fundo(Killjoy_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Killjoy_Lotus = Label(Killjoy_Lotus_Window)
    label1_Killjoy_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Killjoy_Maps/Killjoy_Lotus/Killjoy_1_Lotus.mp4", label1_Killjoy_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_Killjoy_Lotus = Label(Killjoy_Lotus_Window)
    label2_Killjoy_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Lotus\Killjoy_2_Lotus.mp4", label2_Killjoy_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_Killjoy_Lotus = Label(Killjoy_Lotus_Window)
    label3_Killjoy_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Lotus\Killjoy_3_Lotus.mp4", label3_Killjoy_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_Killjoy_Lotus = Label(Killjoy_Lotus_Window)
    label4_Killjoy_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Lotus\Killjoy_4_Lotus.mp4", label4_Killjoy_Lotus, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Killjoy_Haven():
    Killjoy_Haven_Window = ctk.CTkToplevel(Killjoy_Window)
    Killjoy_Haven_Window.geometry(size_window)
    Killjoy_Haven_Window.title("Killjoy | Haven")
    Killjoy_Haven_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Killjoy_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Killjoy_Window.withdraw()
    Killjoy_Haven_Window.state("zoomed")
    #adicionar_plano_de_fundo(Killjoy_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Killjoy_Haven = Label(Killjoy_Haven_Window)
    label1_Killjoy_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Killjoy_Maps/Killjoy_Haven/Killjoy_1_Haven.mp4", label1_Killjoy_Haven, loop=1, size=tamanho_video)
    player_01.play()

    label2_Killjoy_Haven = Label(Killjoy_Haven_Window)
    label2_Killjoy_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Haven\Killjoy_2_Haven.mp4", label2_Killjoy_Haven, loop=1, size=tamanho_video)
    player_02.play()

    label3_Killjoy_Haven = Label(Killjoy_Haven_Window)
    label3_Killjoy_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Haven\Killjoy_3_Haven.mp4", label3_Killjoy_Haven, loop=1, size=tamanho_video)
    player_03.play()

    label4_Killjoy_Haven = Label(Killjoy_Haven_Window)
    label4_Killjoy_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Haven\Killjoy_4_Haven.mp4", label4_Killjoy_Haven, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Killjoy_Split():
    Killjoy_Split_Window = ctk.CTkToplevel(Killjoy_Window)
    Killjoy_Split_Window.geometry(size_window)
    Killjoy_Split_Window.title("Killjoy | Split")
    Killjoy_Split_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Killjoy_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Killjoy_Window.withdraw()
    Killjoy_Split_Window.state("zoomed")
    #adicionar_plano_de_fundo(Killjoy_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Killjoy_Split = Label(Killjoy_Split_Window)
    label1_Killjoy_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Killjoy_Maps/Killjoy_Split/Killjoy_1_Split.mp4", label1_Killjoy_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_Killjoy_Split = Label(Killjoy_Split_Window)
    label2_Killjoy_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Split\Killjoy_2_Split.mp4", label2_Killjoy_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_Killjoy_Split = Label(Killjoy_Split_Window)
    label3_Killjoy_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Split\Killjoy_3_Split.mp4", label3_Killjoy_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_Killjoy_Split = Label(Killjoy_Split_Window)
    label4_Killjoy_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Killjoy_Maps\Killjoy_Split\Killjoy_4_Split.mp4", label4_Killjoy_Split, loop=1, size=tamanho_video)
    player_04.play()


######## FADE ####### FADE ######### FADE ######## FADE ######## FADE ########
def Pixel_Fade():
    global Fade_Window
    Fade_Window = ctk.CTkToplevel(PrincipalWindow)
    Fade_Window.geometry(size_window)
    Fade_Window.title("Fade Spots")
    Fade_Window.protocol("WM_DELETE_WINDOW", close_window)
    PrincipalWindow.withdraw()
    Fade_Window.state("zoomed")
    Button_Voltar_Principal = ctk.CTkButton(Fade_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    #adicionar_plano_de_fundo(Fade_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")


    # Comeco da Janela Fade
    Fade_Spots_Text = ctk.CTkLabel(Fade_Window, text="Fade | Spots Maps", font=("Arial", 16, "bold"))
    Fade_Spots_Text.pack(pady=(20,0))

    # LISTA DE MAPAS | FADE
     # Lotus
    button_frame = ctk.CTkFrame(Fade_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Fade_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Fade_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Fade_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Fade_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Fade_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Fade_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Fade_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Fade_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Fade_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Fade_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Fade_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Fade_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Fade_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Fade_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Fade_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Fade_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Fade_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Fade_Split.grid(row=1, column=2, padx=10, pady=10)




def Pixel_Fade_Bind():
    Fade_Bind_Window = ctk.CTkToplevel(Fade_Window)
    Fade_Bind_Window.geometry(size_window)
    Fade_Bind_Window.title("Fade | Bind")
    Fade_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Fade_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Fade_Window.withdraw()
    Fade_Bind_Window.state("zoomed")
    #adicionar_plano_de_fundo(Fade_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Fade_bind = Label(Fade_Bind_Window)
    label1_Fade_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Fade_Maps/Fade_Bind/Fade_1_BIND.mp4", label1_Fade_bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_Fade_bind = Label(Fade_Bind_Window)
    label2_Fade_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Bind\Fade_2_BIND.mp4", label2_Fade_bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_Fade_bind = Label(Fade_Bind_Window)
    label3_Fade_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Bind\Fade_3_BIND.mp4", label3_Fade_bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_Fade_bind = Label(Fade_Bind_Window)
    label4_Fade_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Bind\Fade_4_BIND.mp4", label4_Fade_bind, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Fade_Ascent():
    Fade_Ascent_Window = ctk.CTkToplevel(Fade_Window)
    Fade_Ascent_Window.geometry(size_window)
    Fade_Ascent_Window.title("Fade | Ascent")
    Fade_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Fade_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Fade_Window.withdraw()
    Fade_Ascent_Window.state("zoomed")
    #adicionar_plano_de_fundo(Fade_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Fade_Ascent = Label(Fade_Ascent_Window)
    label1_Fade_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Fade_Maps/Fade_Ascent/Fade_1_Ascent.mp4", label1_Fade_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_Fade_Ascent = Label(Fade_Ascent_Window)
    label2_Fade_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Ascent\Fade_2_Ascent.mp4", label2_Fade_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_Fade_Ascent = Label(Fade_Ascent_Window)
    label3_Fade_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Ascent\Fade_3_Ascent.mp4", label3_Fade_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_Fade_Ascent = Label(Fade_Ascent_Window)
    label4_Fade_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Ascent\Fade_4_Ascent.mp4", label4_Fade_Ascent, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Fade_Sunset():
    Fade_Sunset_Window = ctk.CTkToplevel(Fade_Window)
    Fade_Sunset_Window.geometry(size_window)
    Fade_Sunset_Window.title("Fade | Sunset")
    Fade_Sunset_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Fade_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Fade_Window.withdraw()
    Fade_Sunset_Window.state("zoomed")
    #adicionar_plano_de_fundo(Fade_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Fade_Sunset = Label(Fade_Sunset_Window)
    label1_Fade_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Fade_Maps/Fade_Sunset/Fade_1_Sunset.mp4", label1_Fade_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_Fade_Sunset = Label(Fade_Sunset_Window)
    label2_Fade_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Sunset\Fade_2_Sunset.mp4", label2_Fade_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_Fade_Sunset = Label(Fade_Sunset_Window)
    label3_Fade_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Sunset\Fade_3_Sunset.mp4", label3_Fade_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_Fade_Sunset = Label(Fade_Sunset_Window)
    label4_Fade_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Sunset\Fade_4_Sunset.mp4", label4_Fade_Sunset, loop=1, size=tamanho_video)
    player_04.play()




def Pixel_Fade_Lotus():
    Fade_Lotus_Window = ctk.CTkToplevel(Fade_Window)
    Fade_Lotus_Window.geometry(size_window)
    Fade_Lotus_Window.title("Fade | Lotus")
    Fade_Lotus_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Fade_Lotus_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Fade_Window.withdraw()
    Fade_Lotus_Window.state("zoomed")
    #adicionar_plano_de_fundo(Fade_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Fade_Lotus = Label(Fade_Lotus_Window)
    label1_Fade_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Fade_Maps/Fade_Lotus/Fade_1_Lotus.mp4", label1_Fade_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_Fade_Lotus = Label(Fade_Lotus_Window)
    label2_Fade_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Lotus\Fade_2_Lotus.mp4", label2_Fade_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_Fade_Lotus = Label(Fade_Lotus_Window)
    label3_Fade_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Lotus\Fade_3_Lotus.mp4", label3_Fade_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_Fade_Lotus = Label(Fade_Lotus_Window)
    label4_Fade_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Lotus\Fade_4_Lotus.mp4", label4_Fade_Lotus, loop=1, size=tamanho_video)
    player_04.play()




def Pixel_Fade_Haven():
    Fade_Haven_Window = ctk.CTkToplevel(Fade_Window)
    Fade_Haven_Window.geometry(size_window)
    Fade_Haven_Window.title("Fade | Haven")
    Fade_Haven_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Fade_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Fade_Window.withdraw()
    Fade_Haven_Window.state("zoomed")
    #adicionar_plano_de_fundo(Fade_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Fade_Haven = Label(Fade_Haven_Window)
    label1_Fade_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Fade_Maps/Fade_Haven/Fade_1_Haven.mp4", label1_Fade_Haven, loop=1, size=tamanho_video)
    player_01.play()

    label2_Fade_Haven = Label(Fade_Haven_Window)
    label2_Fade_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Haven\Fade_2_Haven.mp4", label2_Fade_Haven, loop=1, size=tamanho_video)
    player_02.play()

    label3_Fade_Haven = Label(Fade_Haven_Window)
    label3_Fade_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Haven\Fade_3_Haven.mp4", label3_Fade_Haven, loop=1, size=tamanho_video)
    player_03.play()

    label4_Fade_Haven = Label(Fade_Haven_Window)
    label4_Fade_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Haven\Fade_4_Haven.mp4", label4_Fade_Haven, loop=1, size=tamanho_video)
    player_04.play()




def Pixel_Fade_Split():
    Fade_Split_Window = ctk.CTkToplevel(Fade_Window)
    Fade_Split_Window.geometry(size_window)
    Fade_Split_Window.title("Fade | Split")
    Fade_Split_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Fade_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Fade_Window.withdraw()
    Fade_Split_Window.state("zoomed")
    #adicionar_plano_de_fundo(Fade_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Fade_Split = Label(Fade_Split_Window)
    label1_Fade_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Fade_Maps/Fade_Split/Fade_1_Split.mp4", label1_Fade_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_Fade_Split = Label(Fade_Split_Window)
    label2_Fade_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Split\Fade_2_Split.mp4", label2_Fade_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_Fade_Split = Label(Fade_Split_Window)
    label3_Fade_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Split\Fade_3_Split.mp4", label3_Fade_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_Fade_Split = Label(Fade_Split_Window)
    label4_Fade_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Fade_Maps\Fade_Split\Fade_4_Split.mp4", label4_Fade_Split, loop=1, size=tamanho_video)
    player_04.play()







######## DEADLOCK ####### DEADLOCK ######### DEADLOCK ######## DEADLOCK ######## DEADLOCK ########
def Pixel_Deadlock():
    global Deadlock_Window
    Deadlock_Window = ctk.CTkToplevel(PrincipalWindow)
    Deadlock_Window.geometry(size_window)
    Deadlock_Window.title("Deadlock Spots")
    Deadlock_Window.protocol("WM_DELETE_WINDOW", close_window)
    PrincipalWindow.withdraw()
    Deadlock_Window.state("zoomed")
    Button_Voltar_Principal = ctk.CTkButton(Deadlock_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    #adicionar_plano_de_fundo(Deadlock_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")


    # Comeco da Janela Deadlock
    Deadlock_Spots_Text = ctk.CTkLabel(Deadlock_Window, text="Deadlock | Spots Maps", font=("Arial", 16, "bold"))
    Deadlock_Spots_Text.pack(pady=(20,0))

    # LISTA DE MAPAS | Deadlock
    button_frame = ctk.CTkFrame(Deadlock_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Deadlock_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Deadlock_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Deadlock_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Deadlock_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Deadlock_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Deadlock_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Deadlock_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Deadlock_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Deadlock_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Deadlock_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Deadlock_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Deadlock_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Deadlock_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Deadlock_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Deadlock_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Deadlock_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Deadlock_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Deadlock_Split.grid(row=1, column=2, padx=10, pady=10)




def Pixel_Deadlock_Bind():
    Deadlock_Bind_Window = ctk.CTkToplevel(Deadlock_Window)
    Deadlock_Bind_Window.geometry(size_window)
    Deadlock_Bind_Window.title("Deadlock | Bind")
    Deadlock_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Deadlock_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Deadlock_Window.withdraw()
    Deadlock_Bind_Window.state("zoomed")
    #adicionar_plano_de_fundo(Deadlock_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Deadlock_bind = Label(Deadlock_Bind_Window)
    label1_Deadlock_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Deadlock_Maps/Deadlock_Bind/Deadlock_1_BIND.mp4", label1_Deadlock_bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_Deadlock_bind = Label(Deadlock_Bind_Window)
    label2_Deadlock_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Bind\Deadlock_2_BIND.mp4", label2_Deadlock_bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_Deadlock_bind = Label(Deadlock_Bind_Window)
    label3_Deadlock_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Bind\Deadlock_3_BIND.mp4", label3_Deadlock_bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_Deadlock_bind = Label(Deadlock_Bind_Window)
    label4_Deadlock_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Bind\Deadlock_4_BIND.mp4", label4_Deadlock_bind, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Deadlock_Ascent():
    Deadlock_Ascent_Window = ctk.CTkToplevel(Deadlock_Window)
    Deadlock_Ascent_Window.geometry(size_window)
    Deadlock_Ascent_Window.title("Deadlock | Ascent")
    Deadlock_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Deadlock_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Deadlock_Window.withdraw()
    Deadlock_Ascent_Window.state("zoomed")
    #adicionar_plano_de_fundo(Deadlock_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Deadlock_Ascent = Label(Deadlock_Ascent_Window)
    label1_Deadlock_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Deadlock_Maps/Deadlock_Ascent/Deadlock_1_Ascent.mp4", label1_Deadlock_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_Deadlock_Ascent = Label(Deadlock_Ascent_Window)
    label2_Deadlock_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Ascent\Deadlock_2_Ascent.mp4", label2_Deadlock_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_Deadlock_Ascent = Label(Deadlock_Ascent_Window)
    label3_Deadlock_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Ascent\Deadlock_3_Ascent.mp4", label3_Deadlock_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_Deadlock_Ascent = Label(Deadlock_Ascent_Window)
    label4_Deadlock_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Ascent\Deadlock_4_Ascent.mp4", label4_Deadlock_Ascent, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Deadlock_Sunset():
    Deadlock_Sunset_Window = ctk.CTkToplevel(Deadlock_Window)
    Deadlock_Sunset_Window.geometry(size_window)
    Deadlock_Sunset_Window.title("Deadlock | Sunset")
    Deadlock_Sunset_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Deadlock_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Deadlock_Window.withdraw()
    Deadlock_Sunset_Window.state("zoomed")
    #adicionar_plano_de_fundo(Deadlock_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Deadlock_Sunset = Label(Deadlock_Sunset_Window)
    label1_Deadlock_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Deadlock_Maps/Deadlock_Sunset/Deadlock_1_Sunset.mp4", label1_Deadlock_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_Deadlock_Sunset = Label(Deadlock_Sunset_Window)
    label2_Deadlock_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Sunset\Deadlock_2_Sunset.mp4", label2_Deadlock_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_Deadlock_Sunset = Label(Deadlock_Sunset_Window)
    label3_Deadlock_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Sunset\Deadlock_3_Sunset.mp4", label3_Deadlock_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_Deadlock_Sunset = Label(Deadlock_Sunset_Window)
    label4_Deadlock_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Deadlock_Maps\Deadlock_Sunset\Deadlock_4_Sunset.mp4", label4_Deadlock_Sunset, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Deadlock_Lotus():
    Deadlock_Lotus_Window = ctk.CTkToplevel(Deadlock_Window)
    Deadlock_Lotus_Window.geometry(size_window)
    Deadlock_Lotus_Window.title("Deadlock | Lotus")
    Deadlock_Lotus_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Deadlock_Lotus_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Deadlock_Window.withdraw()
    Deadlock_Lotus_Window.state("zoomed")
    #adicionar_plano_de_fundo(Deadlock_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Deadlock_Lotus = Label(Deadlock_Lotus_Window)
    label1_Deadlock_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Deadlock_Maps/Deadlock_Lotus/Deadlock_1_Lotus.mp4", label1_Deadlock_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_Deadlock_Lotus = Label(Deadlock_Lotus_Window)
    label2_Deadlock_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Lotus\Deadlock_2_Lotus.mp4", label2_Deadlock_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_Deadlock_Lotus = Label(Deadlock_Lotus_Window)
    label3_Deadlock_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Lotus\Deadlock_3_Lotus.mp4", label3_Deadlock_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_Deadlock_Lotus = Label(Deadlock_Lotus_Window)
    label4_Deadlock_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Lotus\Deadlock_4_Lotus.mp4", label4_Deadlock_Lotus, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Deadlock_Haven():
    Deadlock_Haven_Window = ctk.CTkToplevel(Deadlock_Window)
    Deadlock_Haven_Window.geometry(size_window)
    Deadlock_Haven_Window.title("Deadlock | Haven")
    Deadlock_Haven_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Deadlock_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Deadlock_Window.withdraw()
    Deadlock_Haven_Window.state("zoomed")
    #adicionar_plano_de_fundo(Deadlock_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Deadlock_Haven = Label(Deadlock_Haven_Window)
    label1_Deadlock_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Deadlock_Maps/Deadlock_Haven/Deadlock_1_Haven.mp4", label1_Deadlock_Haven, loop=1, size=tamanho_video)
    player_01.play()

    label2_Deadlock_Haven = Label(Deadlock_Haven_Window)
    label2_Deadlock_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Haven\Deadlock_2_Haven.mp4", label2_Deadlock_Haven, loop=1, size=tamanho_video)
    player_02.play()

    label3_Deadlock_Haven = Label(Deadlock_Haven_Window)
    label3_Deadlock_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Haven\Deadlock_3_Haven.mp4", label3_Deadlock_Haven, loop=1, size=tamanho_video)
    player_03.play()

    label4_Deadlock_Haven = Label(Deadlock_Haven_Window)
    label4_Deadlock_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Haven\Deadlock_4_Haven.mp4", label4_Deadlock_Haven, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Deadlock_Split():
    Deadlock_Split_Window = ctk.CTkToplevel(Deadlock_Window)
    Deadlock_Split_Window.geometry(size_window)
    Deadlock_Split_Window.title("Deadlock | Split")
    Deadlock_Split_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Deadlock_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Deadlock_Window.withdraw()
    Deadlock_Split_Window.state("zoomed")
    #adicionar_plano_de_fundo(Deadlock_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Deadlock_Split = Label(Deadlock_Split_Window)
    label1_Deadlock_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Deadlock_Maps/Deadlock_Split/Deadlock_1_Split.mp4", label1_Deadlock_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_Deadlock_Split = Label(Deadlock_Split_Window)
    label2_Deadlock_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Split\Deadlock_2_Split.mp4", label2_Deadlock_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_Deadlock_Split = Label(Deadlock_Split_Window)
    label3_Deadlock_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Split\Deadlock_3_Split.mp4", label3_Deadlock_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_Deadlock_Split = Label(Deadlock_Split_Window)
    label4_Deadlock_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Deadlock_Maps\Deadlock_Split\Deadlock_4_Split.mp4", label4_Deadlock_Split, loop=1, size=tamanho_video)
    player_04.play()
    



######## VYSE ####### VYSE ######### VYSE ######## VYSE ######## VYSE ########
def Pixel_Vyse():
    global Vyse_Window
    Vyse_Window = ctk.CTkToplevel(PrincipalWindow)
    Vyse_Window.geometry(size_window)
    Vyse_Window.title("Vyse Spots")
    Vyse_Window.protocol("WM_DELETE_WINDOW", close_window)
    PrincipalWindow.withdraw()
    Vyse_Window.state("zoomed")
    Button_Voltar_Principal = ctk.CTkButton(Vyse_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    #adicionar_plano_de_fundo(Vyse_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")



    # Comeco Janela Vyse
    Vyse_Spots_Text = ctk.CTkLabel(Vyse_Window, text="Vyse | Spots Maps", font=("Arial", 16 , "bold"))
    Vyse_Spots_Text.pack(pady=(20,0))

    # LISTA DE MAPAS | VYSE
    button_frame = ctk.CTkFrame(Vyse_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Vyse_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Vyse_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Vyse_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Vyse_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Vyse_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Vyse_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Vyse_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Vyse_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Vyse_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Vyse_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Vyse_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Vyse_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Vyse_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Vyse_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Vyse_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Vyse_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Vyse_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Vyse_Split.grid(row=1, column=2, padx=10, pady=10)




def Pixel_Vyse_Bind():
    Vyse_Bind_Window = ctk.CTkToplevel(Vyse_Window)
    Vyse_Bind_Window.geometry(size_window)
    Vyse_Bind_Window.title("Vyse | Bind")
    Vyse_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Vyse_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Vyse_Window.withdraw()
    Vyse_Bind_Window.state("zoomed")
    #adicionar_plano_de_fundo(Vyse_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Vyse_bind = Label(Vyse_Bind_Window)
    label1_Vyse_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Vyse_Maps/Vyse_Bind/Vyse_1_BIND.mp4", label1_Vyse_bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_Vyse_bind = Label(Vyse_Bind_Window)
    label2_Vyse_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Vyse_Maps\Vyse_Bind\Vyse_2_BIND.mp4", label2_Vyse_bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_Vyse_bind = Label(Vyse_Bind_Window)
    label3_Vyse_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Vyse_Maps\Vyse_Bind\Vyse_3_BIND.mp4", label3_Vyse_bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_Vyse_bind = Label(Vyse_Bind_Window)
    label4_Vyse_bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Vyse_Maps\Vyse_Bind\Vyse_4_BIND.mp4", label4_Vyse_bind, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Vyse_Ascent():
    Vyse_Ascent_Window = ctk.CTkToplevel(Vyse_Window)
    Vyse_Ascent_Window.geometry(size_window)
    Vyse_Ascent_Window.title("Vyse | Ascent")
    Vyse_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Vyse_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Vyse_Window.withdraw()
    Vyse_Ascent_Window.state("zoomed")
    #adicionar_plano_de_fundo(Vyse_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Vyse_Ascent = Label(Vyse_Ascent_Window)
    label1_Vyse_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Vyse_Maps/Vyse_Ascent/Vyse_1_Ascent.mp4", label1_Vyse_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_Vyse_Ascent = Label(Vyse_Ascent_Window)
    label2_Vyse_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Ascent\Vyse_2_Ascent.mp4", label2_Vyse_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_Vyse_Ascent = Label(Vyse_Ascent_Window)
    label3_Vyse_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Ascent\Vyse_3_Ascent.mp4", label3_Vyse_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_Vyse_Ascent = Label(Vyse_Ascent_Window)
    label4_Vyse_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Ascent\Vyse_4_Ascent.mp4", label4_Vyse_Ascent, loop=1, size=tamanho_video)
    player_04.play()




def Pixel_Vyse_Sunset():
    Vyse_Sunset_Window = ctk.CTkToplevel(Vyse_Window)
    Vyse_Sunset_Window.geometry(size_window)
    Vyse_Sunset_Window.title("Vyse | Sunset")
    Vyse_Sunset_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Vyse_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Vyse_Window.withdraw()
    Vyse_Sunset_Window.state("zoomed")
    #adicionar_plano_de_fundo(Vyse_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Vyse_Sunset = Label(Vyse_Sunset_Window)
    label1_Vyse_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Vyse_Maps/Vyse_Sunset/Vyse_1_Sunset.mp4", label1_Vyse_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_Vyse_Sunset = Label(Vyse_Sunset_Window)
    label2_Vyse_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Sunset\Vyse_2_Sunset.mp4", label2_Vyse_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_Vyse_Sunset = Label(Vyse_Sunset_Window)
    label3_Vyse_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Sunset\Vyse_3_Sunset.mp4", label3_Vyse_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_Vyse_Sunset = Label(Vyse_Sunset_Window)
    label4_Vyse_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Sunset\Vyse_4_Sunset.mp4", label4_Vyse_Sunset, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Vyse_Lotus():
    Vyse_Lotus_Window = ctk.CTkToplevel(Vyse_Window)
    Vyse_Lotus_Window.geometry(size_window)
    Vyse_Lotus_Window.title("Vyse | Lotus")
    Vyse_Lotus_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Vyse_Lotus_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Vyse_Window.withdraw()
    Vyse_Lotus_Window.state("zoomed")
    #adicionar_plano_de_fundo(Vyse_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Vyse_Lotus = Label(Vyse_Lotus_Window)
    label1_Vyse_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Vyse_Maps/Vyse_Lotus/Vyse_1_Lotus.mp4", label1_Vyse_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_Vyse_Lotus = Label(Vyse_Lotus_Window)
    label2_Vyse_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Lotus\Vyse_2_Lotus.mp4", label2_Vyse_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_Vyse_Lotus = Label(Vyse_Lotus_Window)
    label3_Vyse_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Lotus\Vyse_3_Lotus.mp4", label3_Vyse_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_Vyse_Lotus = Label(Vyse_Lotus_Window)
    label4_Vyse_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Lotus\Vyse_4_Lotus.mp4", label4_Vyse_Lotus, loop=1, size=tamanho_video)
    player_04.play()




def Pixel_Vyse_Haven():
    Vyse_Haven_Window = ctk.CTkToplevel(Vyse_Window)
    Vyse_Haven_Window.geometry(size_window)
    Vyse_Haven_Window.title("Vyse | Haven")
    Vyse_Haven_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Vyse_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Vyse_Window.withdraw()
    Vyse_Haven_Window.state("zoomed")
    #adicionar_plano_de_fundo(Vyse_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Vyse_Haven = Label(Vyse_Haven_Window)
    label1_Vyse_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Vyse_Maps/Vyse_Haven/Vyse_1_Haven.mp4", label1_Vyse_Haven, loop=1, size=tamanho_video)
    player_01.play()

    label2_Vyse_Haven = Label(Vyse_Haven_Window)
    label2_Vyse_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Haven\Vyse_2_Haven.mp4", label2_Vyse_Haven, loop=1, size=tamanho_video)
    player_02.play()

    label3_Vyse_Haven = Label(Vyse_Haven_Window)
    label3_Vyse_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Haven\Vyse_3_Haven.mp4", label3_Vyse_Haven, loop=1, size=tamanho_video)
    player_03.play()

    label4_Vyse_Haven = Label(Vyse_Haven_Window)
    label4_Vyse_Haven.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Haven\Vyse_4_Haven.mp4", label4_Vyse_Haven, loop=1, size=tamanho_video)
    player_04.play()




def Pixel_Vyse_Split():
    Vyse_Split_Window = ctk.CTkToplevel(Vyse_Window)
    Vyse_Split_Window.geometry(size_window)
    Vyse_Split_Window.title("Vyse | Split")
    Vyse_Split_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Vyse_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Vyse_Window.withdraw()
    Vyse_Split_Window.state("zoomed")
    #adicionar_plano_de_fundo(Vyse_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Vyse_Split = Label(Vyse_Split_Window)
    label1_Vyse_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Vyse_Maps/Vyse_Split/Vyse_1_Split.mp4", label1_Vyse_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_Vyse_Split = Label(Vyse_Split_Window)
    label2_Vyse_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Split\Vyse_2_Split.mp4", label2_Vyse_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_Vyse_Split = Label(Vyse_Split_Window)
    label3_Vyse_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Split\Vyse_3_Split.mp4", label3_Vyse_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_Vyse_Split = Label(Vyse_Split_Window)
    label4_Vyse_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents Maps\Vyse_Maps\Vyse_Split\Vyse_4_Split.mp4", label4_Vyse_Split, loop=1, size=tamanho_video)
    player_04.play()





######## KAYO ####### KAYO ######### KAYO ######## KAYO ######## KAYO ########
def Pixel_Kayo():
    global Kayo_Window
    Kayo_Window = ctk.CTkToplevel(PrincipalWindow)
    Kayo_Window.geometry(size_window)
    Kayo_Window.title("Keyo Spots")
    Kayo_Window.protocol("WM_DELETE_WINDOW")
    PrincipalWindow.withdraw()
    Kayo_Window.state("zoomed")
    #adicionar_plano_de_fundo(Kayo_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    Button_Voltar_Principal = ctk.CTkButton(Kayo_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))


    # Comeco da Janela Kayo
    Kayo_Spots_Text = ctk.CTkLabel(Kayo_Window, text="Kayo| Spots Maps", font=("Arial", 16, "bold"))
    Kayo_Spots_Text.pack(pady=(20,0))


    # LISTA DE MAPAS | KAYO
    button_frame = ctk.CTkFrame(Kayo_Window)
    button_frame.pack(fill="both", expand=True, padx=10, pady=10)
    imagens_mapas()
    # BIND
    Button_Kayo_Bind = ctk.CTkButton(button_frame, text="", command=Pixel_Kayo_Bind, image=Bind_Final_Image,fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Kayo_Bind.grid(row=0, column=0, padx=10, pady=10)
    # ASCENT 
    Button_Kayo_Ascent = ctk.CTkButton(button_frame, text="", command=Pixel_Kayo_Ascent, image=Ascent_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Kayo_Ascent.grid(row=0, column=1, padx=10, pady=10)
    # SUNSET
    Button_Kayo_Sunset = ctk.CTkButton(button_frame, text="", command=Pixel_Kayo_Sunset, image=Sunset_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Kayo_Sunset.grid(row=0, column=2, padx=10, pady=10)
    # LOTTUS
    Button_Kayo_Lotus = ctk.CTkButton(button_frame, text="", command=Pixel_Kayo_Lotus, image=Lotus_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Kayo_Lotus.grid(row=1, column=0, padx=10, pady=10)
    # HAVEN
    Button_Kayo_Haven = ctk.CTkButton(button_frame, text="", command=Pixel_Kayo_Haven, image=Haven_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Kayo_Haven.grid(row=1, column=1, padx=10, pady=10)
    # SPLIT 
    Button_Kayo_Split = ctk.CTkButton(button_frame, text="", command=Pixel_Kayo_Split, image=Split_Final_Image, fg_color=None, hover_color=None, width=200, height=80, font=("Arial", 16, "italic"))
    Button_Kayo_Split.grid(row=1, column=2, padx=10, pady=10)




def Pixel_Kayo_Bind():
    Kayo_Bind_Window = ctk.CTkToplevel(Kayo_Window)
    Kayo_Bind_Window.geometry(size_window)
    Kayo_Bind_Window.title("Kayo | Bind")
    Kayo_Bind_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Kayo_Bind_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Kayo_Window.withdraw()
    Kayo_Bind_Window.state("zoomed")
    #adicionar_plano_de_fundo(Kayo_Bind_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Kayo_Bind = Label(Kayo_Bind_Window)
    label1_Kayo_Bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Kayo_Maps/Kayo_Bind/Kayo_1_Bind.mp4", label1_Kayo_Bind, loop=1, size=tamanho_video)
    player_01.play()

    label2_Kayo_Bind = Label(Kayo_Bind_Window)
    label2_Kayo_Bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Bind\Kayo_2_Bind.mp4", label2_Kayo_Bind, loop=1, size=tamanho_video)
    player_02.play()

    label3_Kayo_Bind = Label(Kayo_Bind_Window)
    label3_Kayo_Bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Bind\Kayo_3_Bind.mp4", label3_Kayo_Bind, loop=1, size=tamanho_video)
    player_03.play()

    label4_Kayo_Bind = Label(Kayo_Bind_Window)
    label4_Kayo_Bind.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Bind\Kayo_4_Bind.mp4", label4_Kayo_Bind, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Kayo_Ascent():
    Kayo_Ascent_Window = ctk.CTkToplevel(Kayo_Window)
    Kayo_Ascent_Window.geometry(size_window)
    Kayo_Ascent_Window.title("Kayo | Ascent")
    Kayo_Ascent_Window.protocol("WM_DELETE_WINDOW", close_window)
    Button_Voltar_Principal = ctk.CTkButton(Kayo_Ascent_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Kayo_Window.withdraw()
    Kayo_Ascent_Window.state("zoomed")
# #adicionar_plano_de_fundo(Kayo_Ascent_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Kayo_Ascent = Label(Kayo_Ascent_Window)
    label1_Kayo_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Kayo_Maps/Kayo_Ascent/Kayo_1_Ascent.mp4", label1_Kayo_Ascent, loop=1, size=tamanho_video)
    player_01.play()

    label2_Kayo_Ascent = Label(Kayo_Ascent_Window)
    label2_Kayo_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Ascent\Kayo_2_Ascent.mp4", label2_Kayo_Ascent, loop=1, size=tamanho_video)
    player_02.play()

    label3_Kayo_Ascent = Label(Kayo_Ascent_Window)
    label3_Kayo_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Ascent\Kayo_3_Ascent.mp4", label3_Kayo_Ascent, loop=1, size=tamanho_video)
    player_03.play()

    label4_Kayo_Ascent = Label(Kayo_Ascent_Window)
    label4_Kayo_Ascent.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Ascent\Kayo_4_Ascent.mp4", label4_Kayo_Ascent, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Kayo_Sunset():
    Kayo_Sunset_Window = ctk.CTkToplevel(Kayo_Window)
    Kayo_Sunset_Window.geometry(size_window)
    Kayo_Sunset_Window.title("Kayo | Sunset")
    Button_Voltar_Principal = ctk.CTkButton(Kayo_Sunset_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Kayo_Window.withdraw()
    #adicionar_plano_de_fundo(Kayo_Sunset_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    Kayo_Sunset_Window.state("zoomed")
    # VIDEOS SPOT
    label1_Kayo_Sunset = Label(Kayo_Sunset_Window)
    label1_Kayo_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents Maps/Kayo_Maps/Kayo_Sunset/Kayo_1_Sunset.mp4", label1_Kayo_Sunset, loop=1, size=tamanho_video)
    player_01.play()

    label2_Kayo_Sunset = Label(Kayo_Sunset_Window)
    label2_Kayo_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Sunset\Kayo_2_Sunset.mp4", label2_Kayo_Sunset, loop=1, size=tamanho_video)
    player_02.play()

    label3_Kayo_Sunset = Label(Kayo_Sunset_Window)
    label3_Kayo_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Sunset\Kayo_3_Sunset.mp4", label3_Kayo_Sunset, loop=1, size=tamanho_video)
    player_03.play()

    label4_Kayo_Sunset = Label(Kayo_Sunset_Window)
    label4_Kayo_Sunset.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Sunset\Kayo_4_Sunset.mp4", label4_Kayo_Sunset, loop=1, size=tamanho_video)
    player_04.play()



def Pixel_Kayo_Lotus():
    Kayo_Lotus_Window = ctk.CTkToplevel(Kayo_Window)
    Kayo_Lotus_Window.geometry(size_window)
    Kayo_Lotus_Window.title("Kayo | Lotus")
    Button_Voltar_Principal = ctk.CTkButton(Kayo_Lotus_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Kayo_Window.withdraw()
    Kayo_Lotus_Window.state("zoomed")
    adicionar_plano_de_fundo(Kayo_Lotus_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    # VIDEOS SPOT
    label1_Kayo_Lotus = Label(Kayo_Lotus_Window)
    label1_Kayo_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Kayo_Maps/Kayo_Lotus/Kayo_1_Lotus.mp4", label1_Kayo_Lotus, loop=1, size=tamanho_video)
    player_01.play()

    label2_Kayo_Lotus = Label(Kayo_Lotus_Window)
    label2_Kayo_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Lotus\Kayo_2_Lotus.mp4", label2_Kayo_Lotus, loop=1, size=tamanho_video)
    player_02.play()

    label3_Kayo_Lotus = Label(Kayo_Lotus_Window)
    label3_Kayo_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Lotus\Kayo_3_Lotus.mp4", label3_Kayo_Lotus, loop=1, size=tamanho_video)
    player_03.play()

    label4_Kayo_Lotus = Label(Kayo_Lotus_Window)
    label4_Kayo_Lotus.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Lotus\Kayo_4_Lotus.mp4", label4_Kayo_Lotus, loop=1, size=tamanho_video)
    player_04.play()


def Pixel_Kayo_Haven():
    Kayo_Haven_Window = ctk.CTkToplevel(Kayo_Window)
    Kayo_Haven_Window.geometry(size_window)
    Kayo_Haven_Window.title("Kayo | Haven")
    Button_Voltar_Principal = ctk.CTkButton(Kayo_Haven_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Kayo_Window.withdraw()
 #   adicionar_plano_de_fundo(Kayo_Haven_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    Kayo_Haven_Window.state("zoomed")
    Kayo_Haven_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    # VIDEOS SPOT

def Pixel_Kayo_Split():
    Kayo_Split_Window = ctk.CTkToplevel(Kayo_Window)
    Kayo_Split_Window.geometry(size_window)
    Kayo_Split_Window.title("Kayo | Split")
    Button_Voltar_Principal = ctk.CTkButton(Kayo_Split_Window, text="Voltar", command=voltar_principalwindow)
    Button_Voltar_Principal.pack(pady=(2,0))
    Kayo_Window.withdraw()
    Kayo_Split_Window.state("zoomed")
 #   adicionar_plano_de_fundo(Kayo_Split_Window, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")
    Kayo_Split_Window.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    # VIDEOS SPOT
    label1_Kayo_Split = Label(Kayo_Split_Window)
    label1_Kayo_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_01 = tkvideo("Agents_Maps/Kayo_Maps/Kayo_Split/Kayo_1_Split.mp4", label1_Kayo_Split, loop=1, size=tamanho_video)
    player_01.play()

    label2_Kayo_Split = Label(Kayo_Split_Window)
    label2_Kayo_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_02 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Split\Kayo_2_Split.mp4", label2_Kayo_Split, loop=1, size=tamanho_video)
    player_02.play()

    label3_Kayo_Split = Label(Kayo_Split_Window)
    label3_Kayo_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_03 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Split\Kayo_3_Split.mp4", label3_Kayo_Split, loop=1, size=tamanho_video)
    player_03.play()

    label4_Kayo_Split = Label(Kayo_Split_Window)
    label4_Kayo_Split.pack(side="left", anchor="w", padx=10, pady=(90,90))
    player_04 = tkvideo(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\Agents_Maps\Kayo_Maps\Kayo_Split\Kayo_4_Split.mp4", label4_Kayo_Split, loop=1, size=tamanho_video)
    player_04.play()





# Funcao para fechar todas as janelas.
def close_window():
    PrincipalWindow.destroy()

def voltar_principalwindow():
    PrincipalWindow.deiconify()

    try:
        Viper_Window.destroy()
    except NameError:
        pass
    try:
        Sage_Window.destroy()
    except NameError:
        pass
    try:
        Sova_Window.destroy()
    except NameError:
        pass
    try:
        Fade_Window.destroy()
    except NameError:
        pass
    try:
        Kayo_Window.destroy()
    except NameError:
        pass
    try:
        Vyse_Window.destroy()
    except NameError:
        pass
    try:
        Deadlock_Window.destroy()
    except NameError:
        pass
    try:
        Killjoy_Window.destroy()
    except NameError:
        pass
    try:
        Cypher_Window.destroy()
    except NameError:
        pass


# Funcao Janela Principal
def Principal_Window_Def():
    # Configuracoes Básicas 
    global PrincipalWindow  # Transforma em variavel global
    PrincipalWindow = ctk.CTk() # Cria a Window
    PrincipalWindow.state("zoomed")
    PrincipalWindow.geometry(size_window)   # Muda a resolucao
    PrincipalWindow.title("Spots | Valorant")   # Altera o titulo da window
    PrincipalWindow.protocol("WM_DELETE_WINDOW", close_window) # Caso o usuario clica no X, fecha a aba
    ctk.set_appearance_mode("dark")     # Seta a aparencia da window para modo escuro
    ctk.set_default_color_theme("dark-blue")  # Seta a aparencia da window para modo escuro  
    PrincipalWindow.iconbitmap(r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\icone_programa.ico")
    adicionar_plano_de_fundo(PrincipalWindow, r"C:\Users\heber\Desktop\PythonCodes\ValorantSpots\plano_de_fundo.jpg")

    Text_Inicial = ctk.CTkLabel(PrincipalWindow, text="Spots Valorant", font=("Arial", 18, "bold"))
    Text_Inicial.grid(pady=(25, 0))


    # Buttons 

    Button_Sage = ctk.CTkButton(PrincipalWindow, text="Sage", image=icone_sage, compound="left", width=290, height=200, command=Pixel_Sage, font=("Arial", 18, "bold"))
    Button_Sage.grid(row=0, column=0, pady=10, padx=10)

    Button_Sova = ctk.CTkButton(PrincipalWindow, text="Sova", image=icone_sova, compound="left", width=290, height=200,command=Pixel_Sova, font=("Arial", 18, "bold"))
    Button_Sova.grid(row=0, column=1, pady=10, padx=10)

    Button_Viper = ctk.CTkButton(PrincipalWindow, text="Viper", image=icone_viper, compound="left", width=290, height=200, command=Pixel_Viper, font=("Arial", 18, "bold"))
    Button_Viper.grid(row=0, column=2, pady=10, padx=10)

    Button_Cypher = ctk.CTkButton(PrincipalWindow, text="Cypher", image=icone_cypher, compound="left", width=290, height=200,command=Pixel_Cypher, font=("Arial", 18, "bold"))
    Button_Cypher.grid(row=1, column=0, pady=10, padx=10)

    Button_Killjoy = ctk.CTkButton(PrincipalWindow, text="Killjoy", image=icone_killjoy, compound="left", width=290, height=200,command = Pixel_Killjoy, font=("Arial", 18, "bold"))
    Button_Killjoy.grid(row=1, column=1, pady=10, padx=10)

    Button_Fade = ctk.CTkButton(PrincipalWindow, text="Viper", image=icone_fade, compound="left", width=290, height=200, command=Pixel_Fade, font=("Arial", 18, "bold"))
    Button_Fade.grid(row=1, column=2, pady=10, padx=10)

    Button_Deadlock = ctk.CTkButton(PrincipalWindow, text="Deadlock", image=icone_deadlock, compound="left", width=290, height=200, command=Pixel_Deadlock, font=("Arial", 18, "bold"))
    Button_Deadlock.grid(row=2, column=0, pady=10, padx=10)

    Button_Vyse = ctk.CTkButton(PrincipalWindow, text="Vyse", image=icone_vyse, compound="left", width=290, height=200, command=Pixel_Vyse, font=("Arial", 18, "bold"))
    Button_Vyse.grid(row=2, column=1, pady=10, padx=10)
    
    Button_Kayo = ctk.CTkButton(PrincipalWindow, text="Kayo", image=icone_kayo, compound="left", width=290, height=200, command=Pixel_Kayo, font=("Arial", 18, "bold"))
    Button_Kayo.grid(row=2, column=2, pady=10, padx=10)



# Comeco do Script
Principal_Window_Def()

PrincipalWindow.mainloop()


## OBSERVACOES ##

# ADICIONAR AS IMAGENS DOS MAPAS!!!
# ADICIONAR AS IMAGENS DOS MAPAS!!!