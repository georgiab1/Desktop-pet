import tkinter as tk
import time
import random

class pet():
    def __init__(self):

        self.window = tk.Tk()
        self.idle = [tk.PhotoImage(file='idle2.gif', format='gif -index %i' % (i)) for i in range(16)]
        self.reading = [tk.PhotoImage(file='readsnake.gif', format='gif -index %i' % (i)) for i in range(7)]
        self.sleep = [tk.PhotoImage(file='sleep2.gif', format='gif -index %i' % (i)) for i in range(12)]
        self.music = [tk.PhotoImage(file='dancesnake.gif', format='gif -index %i' % (i)) for i in range(4)]
        self.heart = [tk.PhotoImage(file='heartsnake3.gif', format='gif -index %i' % (i)) for i in range(16)]
        self.cold = [tk.PhotoImage(file='snowsnake.gif', format='gif -index %i' % (i)) for i in range(17)]
        self.skater = [tk.PhotoImage(file='skateright2.gif', format='gif -index %i' % (i)) for i in range(4)]
        self.boatl = [tk.PhotoImage(file='boatsnake.gif', format='gif -index %i' % (i)) for i in range(6)]
        
        self.gelato = [tk.PhotoImage(file='icecreamsnake.gif', format='gif -index %i' % (i)) for i in range(12)]
        self.veniceidle = [tk.PhotoImage(file='masksnakeidle.gif', format='gif -index %i' % (i)) for i in range(16)]
        

        
        self.frame_index = 0
        self.img = self.idle[self.frame_index]
        self.timestamp = time.time()
        self.window.config(highlightbackground='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'white')
        self.label = tk.Label(self.window, bd=0, bg='white')
        self.x = 0
        #you can change where reginald is by changing the 0 here
        self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))

        self.label.configure(image=self.img)
 
        self.window.after(0, self.snakeevents)
        self.window.mainloop()
        count = int(0)


    def mover(self):
        global event
        if event == 2:

            self.x += 1

            x = True
            if time.time() > self.timestamp + 0.15:
                self.timestamp = time.time()
                self.frame_index = (self.frame_index + 1) % 4
                self.img = self.skater[self.frame_index]

            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.mover)
            if self.x>1500:
                self.x = 0

        else:
            return
            

        
    def movel(self):
        global event
        if event == 3:
            self.x -= 1
            self.img = self.boatl[self.frame_index]
            if time.time() > self.timestamp + 0.15:
                self.timestamp = time.time()
                self.frame_index = (self.frame_index + 1) % 6
                self.img = self.boatl[self.frame_index]

            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.movel)
            if self.x<0:
                self.x = 1500

        else:
            return
        
    def idlesnake(self):
        global event
        if event == 0:

            
            self.img = self.idle[self.frame_index]
            #if you want the animation slower- increase 0.25 to like 0.35 maybe?
            if time.time() > self.timestamp + 0.25:
                self.timestamp = time.time()

                self.frame_index = (self.frame_index + 1) % 16
                self.img = self.idle[self.frame_index]
            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.idlesnake)

        else:
            self.frame_index = 0
            return        

    def sleepysnake(self):
        global event
        if event == 1:

            self.img = self.sleep[self.frame_index]
            #same as with idle, if you want the animation slower- increase 0.25 to like 0.35 maybe?
            if time.time() > self.timestamp + 0.25:
                self.timestamp = time.time()
                
                self.frame_index = (self.frame_index + 1) % 12
                self.img = self.sleep[self.frame_index]

            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.sleepysnake)
        

        else:
            self.frame_index = 0
            return
        
    def booksnake(self):
        global event
        if event == 4:
   
            self.img = self.reading[self.frame_index]
            if time.time() > self.timestamp + 0.25:
                self.timestamp = time.time()

                self.frame_index = (self.frame_index + 1) % 7
                self.img = self.reading[self.frame_index]
            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.booksnake)

        else:
            self.frame_index = 0
            return        

    def musicsnake(self):
        global event
        if event == 5:

            self.img = self.music[self.frame_index]
            if time.time() > self.timestamp + 0.25:
                self.timestamp = time.time()
                
                self.frame_index = (self.frame_index + 1) % 4
                self.img = self.music[self.frame_index]

            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.musicsnake)
        

        else:
            self.frame_index = 0
            return 
    def heartsnake(self):
        global event
        if event == 6:

            self.img = self.heart[self.frame_index]
            if time.time() > self.timestamp + 0.25:
                self.timestamp = time.time()
                
                self.frame_index = (self.frame_index + 1) % 16
                self.img = self.heart[self.frame_index]

            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.heartsnake)
        

        else:
            self.frame_index = 0
            return
        
    def chillysnake(self):
        global event
        if event == 7:

            self.img = self.cold[self.frame_index]
            if time.time() > self.timestamp + 0.25:
                self.timestamp = time.time()
                
                self.frame_index = (self.frame_index + 1) % 17
                self.img = self.cold[self.frame_index]

            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.chillysnake)
        

        else:
            self.frame_index = 0
            return

    def masksnake(self):
        global event
        if event == 8:

            self.img = self.veniceidle[self.frame_index]
            if time.time() > self.timestamp + 0.25:
                self.timestamp = time.time()
                
                self.frame_index = (self.frame_index + 1) % 16
                self.img = self.veniceidle[self.frame_index]

            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.masksnake)
        

        else:
            self.frame_index = 0
            return

    def icecreamsnake(self):
        global event
        if event == 9:

            self.img = self.gelato[self.frame_index]
            if time.time() > self.timestamp + 0.25:
                self.timestamp = time.time()
                
                self.frame_index = (self.frame_index + 1) % 12
                self.img = self.gelato[self.frame_index]

            self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
            self.label.configure(image=self.img)
            self.label.pack()
            self.window.after(10, self.icecreamsnake)
        

        else:
            self.frame_index = 0
            return


        
    def snakeevents(self):
                
                global event
                event = random.randint(0,9)
                self.frame_index = 0
                self.window.geometry('120x120+{x}+0'.format(x=str(self.x)))
                self.label.configure(image=self.img)
                self.label.pack()
                
                if event == 0:
                    self.frame_index = 0
                    self.window.after(0, self.idlesnake)
                        
                elif event == 1:
                    self.frame_index = 0
                    self.window.after(0, self.sleepysnake)
        
                elif event == 2:
                    self.window.after(0, self.mover)
                    self.frame_index = 0
                    
                elif event == 3:
                    self.window.after(0, self.movel)
                    self.frame_index = 0
                    
                elif event == 4:
                    self.frame_index = 0
                    self.window.after(0, self.booksnake)
                        
                elif event == 5:
                    self.frame_index = 0
                    self.window.after(0, self.musicsnake)
        
                elif event == 6:
                    self.window.after(0, self.heartsnake)
                    self.frame_index = 0
                    
                elif event == 7:
                    self.window.after(0, self.chillysnake)
                    self.frame_index = 0
                    
                elif event == 8:
                    self.window.after(0, self.masksnake)
                    self.frame_index = 0   

                elif event == 9:
                    self.window.after(0, self.icecreamsnake)
                    self.frame_index = 0
                    
                #if you want animations to change slower- increase 13000
                self.window.after(13000, self.snakeevents)






                

pet()
