from stack import *

class ToDoList:
    ''' A class to create a To-Do list.
    '''

    def __init__(self):
        '''(ToDoList)->None
        Creates an empty list.
        '''
        self.tasks = []

    def add_task(self,task):
        '''(ToDoList,task)->None
        Adds a new task to the list
        '''
        self.tasks.append(task)

    def delete_task(self, index):
        '''(ToDoList,index)->None
        Deletes a task from the list using it's index value.
        '''
        del(self.tasks[index])

    def __len__(self):
        '''(ToDoList)->None
        Returns the number of items in the list.
        '''
        count=0
        for i in self.tasks:
            count+=1
        return count
    
    def __str__(self):
        '''(ToDoList)->None
        Returns all the items in the list.
        '''
        
        count=1
        s=''
        for i in self.tasks:
            s+="%d: %s\n" % (count,i)
            count+=1
        return(s)

    
commands = Stack()
todolist = ToDoList()
redos = Stack()

print("Welcome to your temporary To Do List")
print("-------------------------------------")
print("At any point, you may type: \n" \
            "'v' to view whole list \n" \
            "'d' to delete an existing item \n" \
            "'u' to undo what you just added, \n"
            "'r' to redo what you previously undid")
print("-------------------------------------")

while True:
    c = input("What is something you need to get done? \n")
    if (c == 'v'):
        print(todolist)
    elif (c == 'd'):
        # MODIFY THIS ACCORDING TO INSTRUCTIONS #
        try:
            num = int(input("Delete which task?"))
            element=todolist.tasks[num-1]
            commands.push(('delete',element, num-1))
            todolist.delete_task(num-1)
            print(todolist)
        except:
            if todolist.tasks==[]:
                print("The index is invalid")
    elif (c == 'u'):
        try:
            c=commands.pop()
            redos.push(c)
            if (c[0]=='insert'):
                del(todolist.tasks[int(c[2])])
            elif (c[0]=='delete'):
                todolist.tasks.insert(c[2],c[1])
            print(todolist)
        except:
            if commands.isEmpty():
                print("Undo operation is not possible at this point")
        
    elif (c == 'r'):
        try:
            c=redos.pop()
            commands.push(c)
            if (c[0]=='insert'):
                todolist.tasks.insert(c[2],c[1])
            elif (c[0]=='delete'):
                del(todolist.tasks[c[2]])
            print(todolist)
        except:
            if redos.isEmpty():
                print("Redo operation is not possible at this point")            
    else:
        todolist.add_task(c)
        commands.push(('insert', c, len(todolist)-1))
        
