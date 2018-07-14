
"""
Assign 1
You’ve learned about dictionaries, strings and how you can manipulate strings by joining them using different methods.
However, there are other useful aspects of string manipulation such as extracting the relevant data out of a string.
Write a program (in Python 3) to print “I have attended ------ sessions!!” from the below variable dataset containing sessionIDs

Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

"""


def Ss_Attended(Sessions_Attended = None):
    Sessions = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
    Attended = set(Sessions['sessions'].split(',')) & set(Sessions_Attended['sessions'].split(','))
    print('Ans:')
    print('I have attended '+str(len(Attended))+' sessions!!')
    
 

if __name__ == "__main__":
    Sessions_input = input("Type the Sessions (Eg. Sessions_Attended = {'sessions' : '1011,2344,'})\n")
    exec(Sessions_input)
    Ss_Attended(Sessions_Attended = Sessions_Attended)
        
    
        
