### SRC - This is an okay start, but there is a lot
### missing and you need to show several test cases 
### from the "Random clothes" worksheet question.

def enqueue(Queue,item): 
    if not len(Queue)==5:
        Queue.append(item)
    else:
        return"FUll"
def dequeue(Queue,item): 
    if not len(Queue)==0:
        Queue.append(item)
    else:
        return"Empty"
def isFUll(Queue):
    return(len(Queue)=="Maxsize")

def isEmpty(Queue):
    return(len(Queue)==0)