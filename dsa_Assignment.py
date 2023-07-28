#1q Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])
array = [5, 2, 3, 4, 1, 6, 7]
summ = int(input())
print("Array= ", array)
find(array, len(array), summ)


#2q Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
 
def reverseList(A, start, end):
  while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1
A = list(map(int,input().split()))
print(A)
reverseList(A, 0, 5)
print(A)



#3q  Write a program to check if two strings are a rotation of each other?

def are_rotational(str1,str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str2
    if temp.count(str2) > 0:
        return True
    return False
string1 = input('enter the first string:')
string2 = input('enter the seconf string:')
if are_rotational(string1,string2):
    print('yes, the strings are rotations of each other.')
else:
    print('no the strings are not rotations pf each other.')


#4q Write a program to print the first non-repeated character from a string?

string = input('enter the string: ')
index = int(input('enter the index number: '))
fnc = ""
if len(string) == 0:
    print('empty string!')
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(string)-1:
    print('all characters are repeating!')
else:
   print('first non repeating character is ',fnc)


#5q Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(m, from_rod, to_rod, aux_rod):
    if m == 0:
        return
    tower_of_hanoi(m-1, from_rod, aux_rod, to_rod)
    print("move disk", m, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(m-1, aux_rod, to_rod, from_rod)
m = int(input('enter the number: '))
tower_of_hanoi(m, 'A', 'B', 'C' )


#6q Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def is_operator(z):
    if z == "+":
        return True
    if z == "-":
        return True
    if z == "/":
        return True
    if z == "*":
        return True
    return False
def post_topre(post_exp):
    s = []
    length = len(post_exp)
    for i in range(length):
        if (is_operator(post_exp[i])):
            op_1 = s[-1]
            s.pop()
            op_2 = s[-1]
            s.pop()
            temp = post_exp[i] + op_2 + op_1
            s.append(temp)
        else:
            s.append(post_exp[i])
    ans = ""
    for i in s:
        ans += i
    return ans
if __name__ == "__main__":
    post_exp = "AB+CD-"
    print("prefix: ", post_topre(post_exp))


#7q Write a program to convert prefix expression to infix expression.

def prefix_to_infix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not is_operator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()
def is_operator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
if __name__ == "__main__":
    str = "*-A/BC-/AKL"
    print("INFIX EXPRESSION: ",prefix_to_infix(str))
    
#8q Write a program to check if all the brackets are closed in a given code snippet.

def check_brackets(code):
    brackets = {'(':')','{':'}','[':']'}
    stack = []
    for character in code:
        if character in brackets.keys():
            stack.append(character)
        elif character in brackets.values():
            if not stack or brackets[stack.pop()] != character:
                return False
            return len(stack) == 0
snippet = input('enter code snippet: ')
if check_brackets(snippet):
    print('all brackets are closed!')
else:
    print('all brackets are not closed!')


#9q Write a program to reverse a stack.

class stack:
    def __init__(self):
        self.elements = []
    def push(self,value):
        self.elements.append(value)
    def pop(self):
        return self.elements.pop()
    def empty(self):
        return self.elements == []
    def show(self):
        for value in reversed(self.elements):
            print(value)
def bottom_insert(n, value):
    if n.empty():
        n.push(value)

    else:
        popped = n.pop()
        bottom_insert(n, value)
        n.push(popped)
def reverse(n):
    if n.empty():
        pass
    else:
        popped = n.pop()
        reverse(n)
        bottom_insert(n, popped)
stack_object = stack()
stack_object.push(int(input()))
stack_object.push(int(input()))
stack_object.push(int(input()))
stack_object.push(int(input()))
stack_object.push(int(input()))
print("orginal stack")
stack_object.show()
print('\nstack after reversing')
reverse(stack_object)
stack_object.show()


#10q Write a program to find the smallest number using a stack.

class stack:
    def __init__(self):
        self.items = []
        self.min_items =[]
    def push(self,item):
        self.items.append(item)
        if not self.min_items or item <= self.min_items[-1]:
            self.min_items.append(item)
    def pop(self):
        if not self.items:
            return None
        item = self.items.pop()
        if item == self.min_items[-1]:
            self.min_items.pop()
        return item
    def get_min(self):
        if not self.min_items:
            return None
        return self.min_items[-1]
stack_obj = stack()
stack_obj.push(int(input()))
stack_obj.push(int(input()))
stack_obj.push(int(input()))
stack_obj.push(int(input()))
stack_obj.push(int(input()))
print('smallesr number: ',stack_obj.get_min())
