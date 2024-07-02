#Fibonacci Sequence:
#Generate the Fibonacci sequence up to a certain number of terms
num=int(input("enter how many numbers you want in your fibonacci sequence:"))
list1=[0,1]
for i in range(num-2):
    list1.append(list1[i]+list1[i+1])
    fibonacciSequence=str(list1)
print("Required fibonnaci sequence is: ",fibonacciSequence.strip("[]"))
#finding fibonacci sequence using while loop
fibonacci_sequence=[0,1]
