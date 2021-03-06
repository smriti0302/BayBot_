from datetime import datetime
import tkinter as tk
from tkinter import *
import textwrap
import csv  #Imports
import tkinter 
from googlesearch import *
import webbrowser
from math import log
from random import randint, uniform
from signal import signal, SIGINT
from sys import exit, stdout
from PIL import Image, ImageTk
import sys

class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)        

class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)
          
def proceed():
    ###MAIN CODE
    base = tk.Toplevel()
    base.title("BayBot")
    base.geometry("{0}x{1}+0+0".format(base.winfo_screenwidth(), base.winfo_screenheight()))
    base.resizable(width=FALSE, height=FALSE)

    def send(event):
        msg = EntryBox.get("1.0", 'end-1c').strip()
        EntryBox.delete("0.0", END)
        if msg != '':
               ChatLog.config(state=NORMAL)
               ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
               ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
               wraplength=200, font=("Arial", 10), bg="lightblue", bd=4, justify="left"))
               ChatLog.insert(END,'\n ', "left")
               ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
               ChatLog.yview(END)

               res = "Bot's response goes into here, elongating this message to test textwrap"  #bot Response
               ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
               ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res, 
               wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
               ChatLog.insert(END, '\n ', "right")
               ChatLog.config(state=DISABLED)
               ChatLog.yview(END)
     
    cvds= [
               "Fever",
               "Dry cough",
               "Tiredness",
               "Aches and pains",
               "Sore throat",
               "Diarrhoea",
               "Conjunctivitis",
               "Headache",
               "Loss of taste or smell",
               "Skin rash",
               "Discoloration of fingers and toes",
               "Shortness of breath",
               "Chest pain",
               "Loss of speech or movement"
               ]
    covid_prevention = [
                  "Wash your hands often. Use soap and water or an alcohol-based hand rub.",
                  "Maintain a safe distance from anyone who is coughing or sneezing",
                  "Wear a mask at all times.",
                  "Don't touch your eyes, nose or mouth",
                  "Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze",
                  "Stay at home if you feel unwell",
                  "If you have a fever, cough and difficulty breathing, seek medical attention."
                  ]
    covid_remedies = [
                "Call your healthcare provider or COVID-19 hotline to find out where and when to get a test.",
                "Cooperate with contact-testing procedures to stop the spread of the virus.",
                "If testing is not available, stay home and away from others for 14 days.",
                "While you are in quarantine, do not go to work, to school or to public places. Ask someone to bring you supplies.",
                "Keep at least 1 meter distance from others, even from your family members.",
                "Wear a medical mask to protect others including if/when you need to seek medical care.",
                "Clean your hands frequently",
                "Stay in a separate room from other family members,and if not possible, wear a medical mask",
                "Keep the room well-ventilated",
                "If you share a room, place the beds 1 meter apart",
                "Monitor yourself for any symptoms for 14 days",
                "Call your healthcare provider if you have any of these danger signs: difficulty breathing, loss of speech or mobility,confusion or chest pain.",
                "Stay positive by keeping in touch with loved ones online and by exercising at home."
                ]
    def send_by_button():
        getmsg = EntryBox.get("1.0", 'end-1c').strip()
        msg = textwrap.fill(getmsg,30)
        EntryBox.delete("0.0", END)

        if msg != '':        
            if msg=="1":
                ChatLog.config(state=NORMAL)
                ChatLog.insert(END, current_time, ("small","right","colour"))
                ChatLog.insert(END,msg + '\n\n',("right"))
                ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
                res = "These are the symptoms of COVID-19:"
                ChatLog.insert(END, current_time, ("small", "colour"))
                ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
                ChatLog.config(state=DISABLED)
                ChatLog.yview(END)
                for i in range(len(cvds)):
                    ChatLog.config(state=NORMAL)
                    ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
                    res = cvds[i]
                    ChatLog.insert(END, current_time, ("small", "colour"))
                    ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
                    ChatLog.config(state=DISABLED)
                    ChatLog.yview(END)

            elif msg=="2":
                ChatLog.config(state=NORMAL)
                ChatLog.insert(END, current_time, ("small","right","colour"))
                ChatLog.insert(END,msg + '\n\n',("right"))
                ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
                res = "These are the methods of prevention of COVID-19:"
                ChatLog.insert(END, current_time, ("small", "colour"))
                ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
                ChatLog.config(state=DISABLED)
                ChatLog.yview(END)
                for i in range(len(covid_prevention)):
                    ChatLog.config(state=NORMAL)
                    ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
                    res = covid_prevention[i]
                    ChatLog.insert(END, current_time, ("small", "colour"))
                    ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
                    ChatLog.config(state=DISABLED)
                    ChatLog.yview(END)

            elif msg=="3":
                ChatLog.config(state=NORMAL)
                ChatLog.insert(END, current_time, ("small","right","colour"))
                ChatLog.insert(END,msg + '\n\n',("right"))
                ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
                res = "These are steps to be followed on contracting COVID-19:"
                ChatLog.insert(END, current_time, ("small", "colour"))
                ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
                ChatLog.config(state=DISABLED)
                ChatLog.yview(END)
                for i in range(len(covid_remedies)):
                    ChatLog.config(state=NORMAL)
                    ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
                    res = covid_remedies[i]
                    ChatLog.insert(END, current_time, ("small", "colour"))
                    ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
                    ChatLog.config(state=DISABLED)
                    ChatLog.yview(END)
                         
                        
            else:     
               ChatLog.config(state=NORMAL)
               ChatLog.insert(END, current_time, ("small","right","colour"))
               ChatLog.insert(END,msg + '\n\n',("right"))

               ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))

               res = "I'm afraid I don't know the answer to that."
               ChatLog.insert(END, current_time, ("small", "colour"))
               ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')

               ChatLog.config(state=DISABLED)
               ChatLog.yview(END)
       

    # The following two functions are defined to add a placeholder text or to delete it.
    def deletePlaceholder(event):
        Placeholder.place_forget()
        EntryBox.focus_set()


    def addPlaceholder(event):
            Placeholder.place(x=6, y=421, height=70, width=265)



    #Add menus to the GUI
    main_menu = Menu(base)
    file_menu = Menu(base)
    file_menu.add_command(label="New..")
    file_menu.add_command(label="Save As..")
    file_menu.add_command(label="Exit")
    main_menu.add_cascade(label="File", menu=file_menu)
    #Add the rest of the menu options to the main menu
    main_menu.add_command(label="Edit")
    main_menu.add_command(label="Quit")
    base.config(menu=main_menu)

    now = datetime.now()
    current_time = now.strftime("%D - %H:%M \n")

    # Create Chat window
    ChatLog = Text(base, bd=0, height="500", width="400", font="Helvetica", wrap="word")
    ChatLog.config(state=NORMAL)
    ChatLog.tag_config("right", justify="right")
    ChatLog.tag_config("small", font=("Helvetica", 7))
    ChatLog.tag_config("colour", foreground="#333333")
    ChatLog.insert(END, current_time, ("small","colour"))
    ChatLog.insert(END,textwrap.fill(f"Hello, I am Baymax, your personal healthcare companion. I "+
                                     "can tell you all you need to know about COVID 19. "+
                                     "I can diagnose you based on the symptoms you are experiencing. "+
                                     "I can also identify your BMI(Body Mass Index)."+
                                     "Enter 1 to know about the symptoms of COVID-19. Enter 2 to know how to prevent contracting COVID-19.Enter 3 to know what to do upon contracting COVID-19.",30))
    ChatLog.insert(END,'\n')
    ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
    ChatLog.config(state=DISABLED)

    # Bind scrollbar to Chat window
    scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="double_arrow")
    ChatLog['yscrollcommand'] = scrollbar.set

    # Create Button to send message
    SendButton = Button(base, font=("Comic Sans MS", 12, 'bold'), text="Send", width="8", height="25",
                        bd=0, fg="#750216", activebackground="#AAAAAA", bg="#999999", command=send_by_button)

    # Create the box to enter message
    EntryBox = Text(base, bd=0, fg="#000000", bg="#fff5f5", highlightcolor="#750216",
                    width="29", height="5", font=("Arial",10), wrap="word")

    #Placeholder config and text:
    Placeholder = Text(base, bd=0, fg="#A0A0A0", bg="#fff5f5", highlightcolor="#750216",
                       width="29", height="5", font=("Arial",10), wrap="word")
    Placeholder.insert("1.0", "Enter query here:")

    # Place all components on the screen
    scrollbar.place(x=1510, y=6, height=406)
    ChatLog.place(x=6, y=6, height=410, width=1500)
    EntryBox.place(x=6, y=421, height=70, width=1440)
    SendButton.place(x=1450, y=421, height=70)
    Placeholder.place(x=6, y=421, height=70, width=276)

    Placeholder.bind("<FocusIn>", deletePlaceholder)
    EntryBox.bind("<FocusOut>", addPlaceholder)




    class MyLabel(Label):
        def __init__(self, master, filename):
            im = Image.open(filename)
            seq =  []
            try:
                while 1:
                    seq.append(im.copy())
                    im.seek(len(seq)) # skip to next frame
            except EOFError:
                pass # we're done

            try:
                self.delay = im.info['duration']
            except KeyError:
                self.delay = 100

            first = seq[0].convert('RGBA')
            self.frames = [ImageTk.PhotoImage(first)]

            Label.__init__(self, master, image=self.frames[0])

            temp = seq[0]
            for image in seq[1:]:
                temp.paste(image)
                frame = temp.convert('RGBA')
                self.frames.append(ImageTk.PhotoImage(frame))

            self.idx = 0

            self.cancel = self.after(self.delay, self.play)

        def play(self):
            self.config(image=self.frames[self.idx])
            self.idx += 1
            if self.idx == len(self.frames):
                self.idx = 0
            self.cancel = self.after(self.delay, self.play)        



    anim1 = MyLabel(base, r'giphy.gif')
    anim1.place(x=964, y=492)
    anim2 = MyLabel(base, r'giphy.gif')
    anim2.place(x=482, y=492)
    anim3 = MyLabel(base, r'giphy.gif')
    anim3.place(x=0, y=492)
    anim4 = MyLabel(base, r'baymax.gif')
    anim4.place(x=1250, y=650)


    l = ['A mass or growth in the anal canal',
    'Abdominal bloating',
    'Abdominal pain',
    'Aches in muscles or joints',
    'Acne',
    'Agitation',
    'Anal itching',
    'Anaphylaxis'
    'Anxiety',
    'Back pain',
    'Bitter or acidic taste in the mouth',
    'Bleeding from anus or rectum',
    'Blood in the urine',
    'Blurred vision',
    'Breast lump or thicknening',
    'Breathlessness'
    'Bruising',
    'Bulging eyes',
    'bulging of the soft spots (fontanels) of the babys skull',
    'Burning during urination',
    'cannot climb stairs',
    'Change in the size of breast',
    'Changes to the skin over the breast',
    'Chest pain',
    'Chest tightness or shortness of breath',
    'Clumsiness due to joint and muscle stiffness',
    'Confusion',
    'Convulsions or seizures',
    'Cough',
    'Deformity',
    'Dehydration',
    'Depression',
    'Diarrhoea',
    'Difficulty in walking or bearing weight',
    'Difficulty reasoning', 
    'Difficulty swallowing',
    'Difficulty with planning and organizing',
    'Difficulty with visual and spatial abilities',
    'Dizziness',
    'Double vision',
    'Drooling',
    'Dry mouth',
    'Easily tiring duringExercise or activity',
    'enlarged breast tissue and shrinking testicles',
    'Enlarged hands and feet',
    'Excess facial hair',
    'Excessive sweating and body odor',
    'Extreme hunger',
    'Eye redness',
    'Fatigue',
    'Feeling of fullness in your upper abdomen after eating',
    'Fever',
    'Flushed skin',
    'Foamy mucus',
    'Foamy urine',
    'Foul-smelling "fishy" vaginal odor',
    'Foul-smelling discharge leaking from a sore',
    'Foul-smelling greasy stool',
    'Frequent urination',
    'Gray membrane covering throat and tonsils',
    'Hair loss',
    'Halos around lights',
    'Hard or waxy-looking skin',
    'Headache',
    'Heartburn occurs more than twice a week',
    'High blood pressure',
    'Hives',
    'Immediate throbbing pain',
    'Increased abdominal size',
    'Indigestion',
    'Inflammation and redness',
    'injury in which the bleeding wont stop',
    'Intense joint pain',
    'Intense shivering',
    'Irritability',
    'Itching',
    'Light sensitivity',
    'Limited range of motion',
    'Lips or fingernails turn blue or gray',
    'Little or no urination',
    'Losing weight',
    'Loss of appetite',
    'Low blood pressure',
    'Lower abdominal pain',
    'Malaise',
    'Menstrual cycle irregularities in women',
    'Muscle pain',
    'Muscle weakness',
    'Nasal congestion',
    'Nasal discharge',
    'Nausea',
    'Nausea and vomiting',
    'Not mentally alert',
    'Numbness',
    'Obvious deformity',
    'Oily thickened skin',
    'Pain and numbness in legs or arms',
    'Pain during urination',
    'Pain in the area of the anus',
    'Pain in upper abdomen',
    'Pain in your right shoulder',
    'Pain that increases with activity and decreases with rest',
    'Pain that spreads to your right shoulder or back',
    'Pain that worsens when lying down or bending over',
    'Paralysis',
    'Paranoia',
    'Patchy blind spots',
    'Pelvic pain',
    'Pink or cola-colored urine',
    'Presence of ketones in the urine',
    'Pressure or pain in the eyes',
    'Prickling feeling',
    'Puffy or retracted eyelids',
    'Rapid breathing',
    'Rash',
    'Redness or pitting of the skin',
    'Repeated lung infections',
    'Runny nose',
    'Seizures',
    'Severe sore throat',
    'Sharp pain in neck, arm or back',
    'Skin that retains a dimple',
    'Skin thats pale, hard, cold and numb',
    'Sleepiness or lethargy',
    'Slow-healing sores',
    'Slurred speech',
    'Small outgrowths ofSkin tissue (skin tags)',
    'Sneezing',
    'Sore throat',
    'Squinting',
    'Stiffness',
    'stretch marks',
    'Stretched or shiny skin',
    'Sudden pain at the site of a recent surgery or trauma',
    'Sudden trouble seeing in one or both eyes',
    'Sudden trouble speaking and understanding',
    'Sudden weakness or clumsiness',
    'Swelling',
    'Swelling of the lips',
    'Swelling of tissue directly under your skin',
    'Swollen joints that are hot to the touch and painful to bend',
    'swollen throat',
    'Tenderness over your abdomen when its touched',
    'Tightness or burning',
    'Tunnel vision inThe advanced stages',
    'Unexplained weight loss',
    'Vaginal itching',
    'Vomiting',
    'Watery eyes',
    'Watery or bloody diarrhea',
    'Weight gain',
    'Weight loss',
    'Wheezing',
    'Yellowish skin',
    'Yellowing of eyes']

    #dropdown creation
    w=Label(base, text="Choose the symptoms you are experiencing from the drop downs below")
    w.place(x=40,y=520)
    variable1=StringVar(base)
    variable1.set(l[0])
    w1=OptionMenu(base, variable1, *l)
    w1.config(width=50)
    w1.place(x=40,y=560)

    variable2=StringVar(base)
    variable2.set(l[0])
    w2=OptionMenu(base, variable2, *l)
    w2.config(width=50)
    w2.place(x=40,y=600)


    variable3=StringVar(base)
    variable3.set(l[0])
    w3=OptionMenu(base, variable3, *l)
    w3.config(width=50)
    w3.place(x=40,y=640)

    variable4=StringVar(base)
    variable4.set(l[0])
    w4=OptionMenu(base, variable4, *l)
    w4.config(width=50)
    w4.place(x=40,y=680)

    variable5=StringVar(base)
    variable5.set(l[0])
    w5=OptionMenu(base, variable5, *l)
    w5.config(width=50)
    w5.place(x=40,y=720)

    def exe():
        Index = []
        Disease = []
        Link = []
        Symptoms = []
        Causes = []
        RiskFactor = []
        OverView = []
        Treatment = []
        Medication = []
        HomeRemedies = []

        Input1=variable1.get()
        Input2=variable2.get()
        Input3=variable3.get()
        Input1=Input1.upper()
        Input2=Input2.upper()
        Input3=Input3.upper()
        Input4=variable4.get()
        Input4=Input4.upper()
        Input5=variable5.get()
        Input5=Input5.upper()

        
        def GSearch(FinalisedDisease) :
            query = FinalisedDisease
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 4):
                webbrowser.open("https://google.com/search?q=%s" % query)


        with open(r'MasterData.csv', 'r', encoding='utf-8') as csvfile: 
            csvReader = csv.reader(csvfile)
            for row in csvReader:
                Index.append(row[0]) 
                Disease.append(row[1])  
                Link.append(row[2])     
                Symptoms.append(row[3])
                Causes.append(row[4])
                RiskFactor.append(row[5])
                OverView.append(row[6])
                Treatment.append(row[7])
                Medication.append(row[8])
                HomeRemedies.append(row[9])
     
        Temp = len(Index)
        for i in range(0, 1183):
            if Input1 and Input2 and Input3 and Input4 and Input5 in str.upper(Symptoms[i]) :
                 res = Disease[i]+'  '+Link[i]
                 ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
                 ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res, 
                 wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"),padx=10, pady=10)
                 ChatLog.insert(END, '\n ', "right")
                 ChatLog.config(state=DISABLED)
                 ChatLog.yview(END)


    button=Button(base,text="DONE", command=exe)
    button.config(width=25)
    button.place(x=120,y=780)

    def BMI():
        h=height.get()
        w=weight.get()
        h=float(h)
        w=float(w)
        bmi = w/(h**2)
        if (bmi < 18.5): 
            ChatLog.config(state=NORMAL)
            ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
            res = "You are underweight!! Your BMI is:"+str(bmi)
            ChatLog.insert(END, current_time, ("small", "colour"))
            ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END) 
      
        elif ( bmi >= 18.5 and bmi < 24.9): 
            ChatLog.config(state=NORMAL)
            ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
            res = "Your weight is normal!! Your BMI is:"+str(bmi)
            ChatLog.insert(END, current_time, ("small", "colour"))
            ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)  
      
        elif ( bmi >= 24.9 and bmi < 30): 
            ChatLog.config(state=NORMAL)
            ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
            res = "You are overweight!! Your BMI is:"+str(bmi)
            ChatLog.insert(END, current_time, ("small", "colour"))
            ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END) 
      
        elif ( bmi >=30): 
            ChatLog.config(state=NORMAL)
            ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
            res = "You are obese!! Your BMI is:"+str(bmi)
            ChatLog.insert(END, current_time, ("small", "colour"))
            ChatLog.insert(END,textwrap.fill(res,30)+'\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END) 

        
    l=Label(base,text="BMI CALCULATOR")
    l.place(x=620, y=550)
    l1=Label(base, text="Enter your height in metres:")
    l1.place(x=620, y=600)
    height = Entry(base, bd=5)
    height.place(x=620,y=630)
    l2=Label(base, text="Enter your weight in kg:")
    l2.place(x=620, y=660)
    weight = Entry(base, bd=5)
    weight.place(x=620, y=690)
    b=Button(base, text="DONE", command=BMI)
    b.place(x=620, y=720)

    base.bind('<Return>', send)

    base.mainloop()


root = Tk()
root.title("BayBot")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(width=FALSE, height=FALSE)
root.configure(background='aquamarine2')
anim = MyLabel(root, r'intro.gif')
anim.place(x=500, y=150)
bp=Button(root, text="PROCEED", command=proceed)
bp.config(width=25)
bq=Button(root, text="EXIT",command=root.destroy)
bp.place(x=530, y=650)
bq.config(width=25)
bq.place(x=760, y=650)
root.mainloop()

