import moviepy.editor
from tkinter import *
from tkinter.filedialog import askopenfilename
from moviepy.editor import VideoFileClip,AudioFileClip,CompositeVideoClip


# SELECCIONAR IMAGEN
def selectimg():
    global image
    

    filetypes = (('Image files', '*.*'),
    ('All files', '*.*'))

    image=askopenfilename(
    initialdir='downloads',
    title='Select Image',
    filetypes=filetypes)
    
    label3 = Label(text='Image')
    label3.pack(anchor=CENTER,padx=4, pady=2)
    label3['text'] = image
    label3.place(x=120,y=8)
    
# SELECCIONAR AUDIO
def selectaudi():
    global audio

    filetypes2 = (('Audio files', '*.*'),
        ('All files', '*.*'))

    audio=askopenfilename(
    initialdir='downloads',
    title='Select Audio',
    filetypes=filetypes2)

    label2 = Label(text='Audio')
    label2.pack(padx=4, pady=2)
    label2['text'] = audio
    label2.place(x=120,y=40)




def merge():
    global audio
    global image


    audio_clip = moviepy.editor.AudioFileClip(audio,fps=44100,buffersize=200000, nbytes=4)
    image_clip = moviepy.editor.ImageClip(image)
    image_clip = image_clip.resize(height=1080)
    clip1_clip = image_clip.set_position(("center","center"))
    

    video_clip = CompositeVideoClip([clip1_clip])
    video_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.audio = audio_clip
    video_clip.fps = 1
    video_clip.write_videofile(f'{audio}.mp4',threads=6, fps=1,codec="libx264",audio_bitrate="192k",temp_audiofile=None)
    
    label0=Label(root,text="Done",font=("Arial",18,"bold"),fg="green",bg="#363636")
    label0.pack()
    label0.place(x=350,y=250)
    

    
    
# Boton para cerrar la ventana
def clse():
    
    root.destroy()
  
  


        
root = Tk()
root.geometry('600x300')
root.title('Audio + Image')
root.config(bg="#363636")



label1 = Label(text="Image Selected")
label1.config(bg="green",font=("Arial 10 bold"))
label1.pack(padx=4, pady=2)
label1.place(x=10,y=7)



label4 = Label(text="Audio Selected")
label4.config(bg="green",font=("Arial 10 bold"))
label4.pack(padx=4, pady=8)
label4.place(x=10,y=40)


 
b=Button(root,text="Merge",bg="#651791",fg="black",command=merge)
b.place(x=330,y=150)
b.config(font=("Arial 15 bold"))



button1 = Button(root ,text='Select image',bg="#c4c2c3",fg="black", command=selectimg)
button1.place(x=180,y=150)
button1.config(font=("Arial 15 bold"))



button2 = Button(root ,text='Select audio',bg="#c4c2c3", command=selectaudi)
button2.place(x=180,y=200)
button2.config(font=("Arial 15 bold"))

ex_button = Button(root, text="Exit",bg="#85152d", command=clse)
ex_button.place(x=500,y=200)
ex_button.config(font=("Arial 15 bold"))

root.mainloop()