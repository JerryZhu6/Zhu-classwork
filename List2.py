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