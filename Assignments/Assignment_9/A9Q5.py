'''

5. Write a program which accepts one number and checks whether it is divisible by 3 and
5
Input: 15
Output: Divisible by 3 and 5

'''

def divisible(x):
    if x%3 == 0 and x%5==0:
        print("Divisible by 3 and 5")

divisible(15)