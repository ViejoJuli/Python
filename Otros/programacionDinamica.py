#Como imprimir:https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python

def fibonnaci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fibonnaci(n-1)+fibonnaci(n-2)
print("El fibonacci normal es %s"%(fibonnaci(5)))
def dfibonnaci(n,mem={0:0,1:1}):
    if n in mem:
        return mem[n]
    mem[n]=dfibonnaci(n-1,mem)+dfibonnaci(n-2,mem) #Asi se agrega a un diccionario
    return mem[n]
print("El fibonacci dinamico es %s"%(dfibonnaci(100)))