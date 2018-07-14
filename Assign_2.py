from random import randint

"""
Assign2

Libraries and Functions always come in handy to developers by allowing reusability of existing code.
There are certain well known inherent libraries that you have access to after installing python.
By using these libraries and functions in them, write a program (in Python 3) to guess a randomly generated number between 1 and 10.

"""

class Rand_Game():

    def _Init(self, Entry = None):
        
        
        print('******************************************************')
        print('Let\'s start the game!')
        print('The game is guessed number between 1 and 10')
        print('Good Luck!')
        print("if you want exit the game, you should type the 'exit'")
        print('******************************************************')
        print('')
        
        Ans = self._Input_Handler()
        Entry = {"Sys": randint(1, 10),
                 "User" : Ans,
                 "Counter" : 0,
                 "Selected" : ''
                 }
        
        return Entry


    def Start(self, Entry = None):
        
        
        Entry = self._Init() if Entry is None else Entry
        
        if(Entry['User'] is False):                                                 
            return None;                                                             
        
        if(Entry["Counter"] == 0):                                                  
            Entry['Selected'] = Entry['Selected'] + str(Entry['User'])              
        else:                                                      
            Entry['Selected'] = Entry['Selected'] + ', ' + str(Entry['User'])
        Entry['Counter'] = Entry['Counter'] + 1                                     

        if(Entry['User'] == Entry['Sys']):                                          
            Chck = self._Result(True, Entry)                                        
            return None if Chck is False else self.Start()                          
        else:
            Ans = self._Result(False, Entry)
            Entry['User'] = Ans                                                   
            return self.Start(Entry = Entry)                
            

    def _Result(self, Flags, Entry):

        if(Flags is True):
            print('****************************************')
            print("Congratulations! You win this game")
            print("Number that is your guessed is Correct!")
            print("Number of trying: " + str(Entry['Counter']))
            print('****************************************')
            print('')
            print('')
            Re = input('Should you replay this game? (y/n) ')
            Chck = self._Checker(Re)
            return Chck

        else:
            print("******************************************************")
            print('Unfortunately, your answer is not correct')
            print('You take '+ str(Entry['Counter']) +' games, you can retry it')
            print('You Selected these : ' + Entry['Selected'])
            print("if you want exit the game, you should type the 'exit'")
            print('******************************************************')
            print('')
            Ans = self._Input_Handler()
            return Ans
            
        



    def _Input_Handler(self):
        while(1):
            Ans = input('Please input the number between 1 and 10\n')
            try:
                Ans = int(Ans)
                if(Ans > 10 or Ans < 0):
                    pass;
                else:
                    break;
            except:
                if(Ans == 'exit'):
                    return False
                pass;

        return Ans
    
    def _Checker(self, Re):
        
        Chck = {'y' : True, 'ye' : True, 'yes' : True,
                'n' : False, 'no' : False
                }
        try:
            return Chck[Re.lower()]

        
        except:
            Re = input('Should you replay this game? (y/n) ')
            return self._Checker(Re)


if '__main__' == __name__:
    Rand_Game = Rand_Game()
    Rand_Game.Start()
