#LISTS 使用[]來列清單，用,來分割項目
'''lists are used to store items. A list is created using 
[]square brackets with commas separating item'''
words=["hello","world","!"]
print(words[0])  #序列是從0開始
print(words[1])
print(words[2])
print(words[1][2])  #會得到第world的r

#順序也可以用-號表示，倒數的意思
words=["hello","world","!"]
print(words[-3])  #倒數是從-1開始
print(words[-2])
print(words[-1])
print(words[-2][2]) 

#LIST + while loop
x = 0
sometest = ["HELLO","WORLD",":)"]
while x < 3 :
     print(sometest[ x ])  
     
     x = x + 1
     continue 
while x == 3 :
     print(sometest[ x -1 ])   #:)
     x = x + 1
     print("end")
    

#an empty list is created with an empty pair of square brackets[]
'''
 the queue is ggoing to be empty in the beginning and get populated with
 people data later
 In some code samples you might see a comma after the last item in the list.
 It's not mandatory, but perfectly valid'''
empty_list = []
print(empty_list) #[]
print(type(empty_list)) #<class 'list'>

#compare with print
x = ["a"]
print(x[0])  #a
print(x)   #["a"]

    

#LISTS can contaim several different type of items
#lists can also be nested within other lists.
num = 3
things = ["string",2,[1,2,num],4,4.56]
print(things[1]) #2
print(things[2])   #[1,2,3]
print(things[2][2])   #3   #int object is not subscrible.
print(things[0])    #string



#str可以直接輸入LIST，其他代碼則不可以
str="hello world"
print(str[6])  #w (空格也算)

#SPLIT()，可以用列出STR中的字串清單
W="I love learning Python using sololearn!"
print(W) #I love learning Python using sololearn!

W="I love learning Python using sololearn!".split()
print(W)  #['I', 'love', 'learning', 'Python', 'using', 'sololearn!']

#list用來列出字串中每個英文字母單一列出
#['I', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u', '.']
s ='I love you.'
a = list(s)
print(a)


#len get the number of items in a list
#len is written before the lsit, it is beging called on, without a dot
str = "Hello World!"
i = 0
while i < len(str):
    print(str[i])
    i += 1

#'i' change all'a' in list without know the position of all 'a'  
#['i', 'b', 'c', 'g', 'i', 'a', 'a']
'''
['i', 'b', 'c', 'g', 'i', 'a', 'a']
['i', 'b', 'c', 'g', 'i', 'a', 'a']
['i', 'b', 'c', 'g', 'i', 'a', 'a']
['i', 'b', 'c', 'g', 'i', 'a', 'a']
['i', 'b', 'c', 'g', 'i', 'i', 'a']
['i', 'b', 'c', 'g', 'i', 'i', 'i']    
lst = ['a','b','c','g','i','a','a']'''


#不知道這個h代碼做什麼用處
lst = ['a','b','c','g','i','a','a']
for h in range(len(lst)):
    if lst[h] == 'a':
       lst[h] = 'i'
    print(lst)  
#上面的範例換這個方式一次替換掉  chain可以用隨便變數代稱
#['i', 'b', 'c', 'g', 'i', 'i', 'i']  
lst = ['a','b','c','g','i','a','a']   
lst = [chain.replace('a','i') for chain in lst]  
print(lst) 

#上面範例第三種寫法
lst = ['a','b','c','g','i','a','a']
lst = "".join(lst)    
print(lst)   #abcgiaa，把list連結一起，用空格
lst = lst.replace("a","i")  #把"a"用"i"取代
lst = list(lst) #再把他們變回LIST
print(lst)  
#上面的寫法再濃縮
lst = ['a','b','c','g','i','a','a']
lst = list("".join(lst).replace("a","i") )
print(lst)  


    
#利用字串中的空格，再利用*可以創造間隔與圖形    
str = "Hello World"   #len(str) :11
i = 0
while i < len(str):
    print(str[5] * i, str[i])
    i += 1
 
    
    
#end=""可以把結果列成一條，如果沒有就會成為好幾行的答案  
#alphabeta l p h a b e t    
num = 0
Y = "abcdefghijklmnopqrstuvwxyz"
order = [0,11,15,7,0,1,4,19]  #8
while num < len(order):
    print(Y[order[num]],end="")
    num += 1
    continue 
print(Y[0],Y[11],Y[15],Y[7],Y[0],Y[1],Y[4],Y[19]) #與上行print的結果連成一條


#list operations
nums = [7,7,7,7,7]
nums[2] = 5  #取代掉順序2的值為5
print(nums)   #[7, 7, 5, 7, 7]
 
#[5,5,5,5,5]
nums = [7,7,7,7,7]
x = 0
while x < len(nums):
    nums [x] =5
    x += 1
print(nums)      

#a[2:5],2表示list中的序列0-1-2,5則是從1-2-3-4-5
# [1, 2, 'a', 'b', 'c', 6]
a=[1,2,3,4,5,6]
a[2:5]=['a','b','c']
print(a)


a=[1,2,3,4,5,6]
a[2:5]='a','b','c' ##得到跟上面一樣的結果
print(a)


#也可以替換再替換
nums=[7,7,7,7,7]
nums[:2]=1,2,3 #[1, 2, 3, 7, 7, 7]  #:前面空白表示是0
nums[3:5]=4,5
print(nums)  #[1, 2, 3, 4, 5, 7]

#reassign by list item
#[1, 'a', 'b', 'c', 5]
a = [1,2,3,4,5]
reassign = ['a','b','c']
a[1:4] = reassign 
print(a)

#用while做必須加break，不然會形成loop
#no change
nums = [7,7,7,7,7,7]
nums[0:5] = [4]
print(nums)      #[4, 7]
while nums == [4]:
    print(nums)
    break
else:
    print('no change')

# [4]
nums = [7,7,7,7,7]
nums[0:5] = [4] 
print(nums)     #[4]
while nums == [4]:
    print(nums)
    break
else:
    print('no change')  
      
#同樣的答案可以用IF做出來
nums=[7,7,7,7,7]
nums[0:5] = [4] 
if nums == []:
    print(nums)
else:
    print('wrong')

#用LIST置換LIST
a = [1,2,3,4,5,6]
a[3] = a[1]
print(a[3])    #2



#list可以倍數增加 "*" 或用"+"添加
f = [1,2,3]
g = [4,5,6]
print( f * 2 )  #[1, 2, 3, 1, 2, 3]
print( f + g )   #[1, 2, 3, 4, 5, 6]
print( g + f)    #[4, 5, 6, 1, 2, 3]
i = 0
while i <= 2:
    f[i] = f[i] + g[i]   #f[0]=1+4=5 , F[1]=2+5=7, f[2]=3+6=9
    i += 1
    print(f)  #[5, 7, 9]

#check if the items is in the list
words=[1,2,3,4,5,6]
print(1 in words)    #True
print(2 in words)    #True
print("happy" in words)   #False
if(1 and 4 in words) == True:    
    print('right')
if(1 or 7 in words) == True:
    print('right')
else:
    print("wrong")
    
    
#範例1  check in 
nums = [10,9,8,7,6,5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[0])
else:
    print("no")
#範例2  check not in 
nums = [10,9,8,7,6,5]
nums[0] = nums[1]-5   
print(nums)  #[4, 9, 8, 7, 6, 5]
if  not 4 in nums:   #not寫在4前後答案都一樣
    print("no")
else:
    print(nums[0])
    
#to check if an item is not in a list
nums=[10,9,8,7,6,5]
print(not 4 in nums)
print(4 not in nums)
print(not 5 in nums)
print(5 not in nums)

#範例3
nums = [1,2,3]
nums[1] = nums[2] * 14  #42
if 28 in nums: 
    print(nums[0])
elif 10 > nums[1]:
    print(nums[2] - 1)
else:
    print('should be',nums[1])
    
    

#附加清單 .append() 或是 +=[]，會直接新增在結尾

nums = [1,2,3]
nums.append(4)
print(nums)
nums += [0]
print(nums)
nums[:1]=5,6
print(nums)
nums[:0]=7,8  # [7, 8, 5, 6, 2, 3, 4, 0]
print(nums)
nums[1:2]=9,10     #[7, 9, 10, 5, 6, 2, 3, 4, 0]
print(nums)
nums[:0]=11,12,13   #[11, 12, 13, 7, 9, 10, 5, 6, 2, 3, 4, 0]
print(nums)


#insert只能插入一個item
'''Insert method is similar to append, except that it allow you to insert a 
new item at any position in the listappend. Elements, that are after the 
inserted item, are shifted to the right.'''
words = ["python", "Fun"]
a = 1
words.insert(a,'is')
print(words)   #['python', 'is', 'Fun']
words.insert(-1,'so')  #可以直接輸入想要插入的位置
print(words) 
words.insert(0,'learning')
print(words) 


#.index用來找出list 中的位置
#ValueError: 'z' is not in list
letters= ['q','r','s','p','u']
print(letters.index('r'))  #1
print(letters.index('p'))  #3
print(letters.index('u')) #4

letters= ['q','r','s',['r','p'],'u']
print(letters.index('r'))  #1
print(letters.index(['r','p']))  #'p'找不到，不能找[[]]中的單一東西
print(letters.index('u')) #4

#max(list):return the list with maximun value
#min(list):return the list with minimum value
#list.count(item):returns a count of how many times an item occurs in a list
#list.remove(item):removes an object from a list
#list.reverse():reverses items in a list

words =['a','b','c','e','1',2,3,4]
#max(words)  #not supported between instances of 'int' and 'str'
words.reverse()    #只能整個list顛倒
print(words)   #[4, 3, 2, '1', 'e', 'c', 'b', 'a']

num = [1,2,3,4,5,6,7,8]
print(max(num))
print(min(num))
print(num.count(3))  #1
print(num.count(3 and 1))  #1
print(num.count(3 or 1))  #1
print(num.count(3 and 9))   #0
num.remove(3)  #不能直接用print
print(num)
num.reverse()  #不能直接用print
print(num)

alp =['a','b','c','e']
print(max(alp))  #e

x =['a','b','c','e','1','2','3','4']
print(max(x))   #e


#.extend(()) 等同於.append()
#append() takes exactly one argument
C=[1,2]
C.extend((3,4))
C.append(5)
C += [6,7]
print(C)  #[1, 2, 3, 4, 5, 6, 7]

#[9]  #[9, 10]
i = 9
x = i+1
nums = []
while i <= x:   #，9+1=10，再回到WHILE加入清單，之後變成11，再回到WHILE>X10
    nums.append(i)
    i += 1
    print(nums)  
    
#範例2   
i = 9
x = 9   #如果這裡x >i，跑第一次while就False，停住了
nums = []
while i >= x and i <= 15:
    nums.append(i)
    i += 1  
    print(nums)  
   

#我們再賴看看不同的附加結果
nums = [2] * 3
print(nums)    #[2, 2, 2]


#[[2, 7, 3], [2, 7, 3], [2, 7, 3]]
nums= [[2]] * 3    #[[2], [2], [2]]
nums[0].append(7)   #[[2,7], [2,7], [2,7]]
nums[1].append(3) 
print(nums)  


#[[2, 7], [2, 3], [2]]
nums=[[2], [2], [2]]
nums[0].append(7)
nums[1].append(3)
print(nums) 

 
#to get the number of items in a list
nums=[[2, 7], [7, 3], [2, 7, 3]]
print(len(nums))    #3
print(len(nums[0]))  #2


#Insert和append功能相似，但是可以加在任何位置你想要
w=['python','fun']
index=1
w.insert(index,'is')
print(w)
#there's no need to use index
w=['python','fun']
w.insert(1,'is')
w.insert(-3,'oh')  #w.insert(-0,'oh') 也是可以得到相同的答案
print(w)

#index method finds the first occurrence of a list and return its index
#if the item isn't in the list, it raise a "ValueError
L=["p","q","r","s","p","u"]
print(L.index('r'))  #2
print(L.index("p"))  #0
print(L.index('z'))  #ValueError: 'z' is not in list
print(max(L))   #u
print(min(L))   #p
print(L.count("p"))   #2
L.remove("p")  #只能移除清單內第一個選項,一次只能給一個條件
print(L)

#想要一次清掉所有選項 用WHILE LOOP
L=["p","q","r","s","p","u"]
while "p" in L:
    L.remove("p")
print(L)

#reverse
W = [4,3,2,1,0]
W.reverse()
print(W)


#RANGE #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(10))
print(numbers)


#create a range from 10 to 20 every 2 steps
a = range(10,20,2)
b = list(a)
print(a)  #range(10, 20, 2)
print(b) #[10, 12, 14, 16, 18]


#range()與list(range())
print(range(5))     #range(0, 5)
print(list(range(5)))  #[0, 1, 2, 3, 4]
print(list(range(0,5)))  #[0, 1, 2, 3, 4]
print(list(range(10,1,-1)))  #[10, 9, 8, 7, 6, 5, 4, 3, 2]
'''list(range(1,5,1.0)) #ERROR with FLOAT'''



#Iteration means you need to perform code on each item in a list 
words = ['hello','world','spam','egg']
x = 0
while x < len(words):
    print( words[x] + "!") 
    x = x + 1
    
#FOR LOOP is a shortcut for the while loop of iteration
# FOR LOOP，把清單中的東西一個一個拿出來
cars = ['Toyota','Honda']
for car in cars:   #car只是暫時的代稱
    print(car)  #第一次跑car='Toyata',第二次car='Honda'，所以總共跑兩次的迴圈
    
words=['hello','world','spam','egg']  
for word in words:
   print(word+"!")


stars = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
for star in stars:
    print("Hi",star) 
   
#字串也可以當清單
cars = 'Audi'
for c in cars:
    print(len(cars))     # 4 4 4 4   跑了四行
print('A' in cars)   #True
print('udi' in  cars)  #True

#比較
cars = ['Audi']
for c in cars:
    print(len(cars))     # 1  
print('A' in cars)   #False
print('udi' in  cars)  #False
      

words = ['hello','world','spam','egg']  
for word in words:  #word可以用anything代替
 print(word+"!")

words = ['hello','world','spam','egg']  
for anything in words:
 print(anything+"!")

words=['hello','world','spam','egg']
for each in words:
 print(each+"!")
  
words = ['hello','world','spam','egg']  
for x in words:
 print(x+"!")
 
 ##不可用於數字
'''
numbers=[1,2,3,4,5,6]
for 1 in numbers:
    print(1+"A")
'''
        
#i可以用任意代替
N = 10
for i in range( 1, N+1):
    print(i)

#一樣的答案
for i in range(1,11):
    print(i)
    
#for loop+range常常被用來重複指定次數的CODE
for i in range(5):
    print('hello!')

#用for loop 字串做出圖形
a = 0 
for i in range(10):
   if a <= i:
      print("*"*a)
      a+=1
print()



