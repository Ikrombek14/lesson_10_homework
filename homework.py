
#3
# def payment_options(amount):
#     if amount < 1:
#         return 0
#     elif amount == 1:
#         return 1
#     elif amount == 2:
#         return 2
#     else:
#         ways = [0] * (amount + 1)
#         ways[0] = 1
#         for coin in [1, 2]:
#             for i in range(coin, amount + 1):
#                 ways[i] += ways[i - coin]
#         return ways[amount]
# amount = int(input("Enter the amount: "))
# print(payment_options(amount))

#4
# a=int(input("Enter the a: "))
# b=int(input("Enter the b: "))
# c=int(input("Enter the c: "))
#
# max_=max(a,b,c)
# min_=min(a,b,c)
# d={}
# for i in range(min_,max_+1):
#     sum_=sum(int(i) for i in str(i))
#     print(i,sum_)
#     d[i]=sum_
# Masalani davomini ishlay olmadim qolganini tushuntirib bering.



#5
# numbers = [2,7,11,15]
# target = 9
#
# if numbers[0]+numbers[1] == target:
#     print(numbers.index(numbers[0]),numbers.index(numbers[1]))
# elif numbers[1]+numbers[2] == target:
#     print(numbers.index(numbers[1]),numbers.index(numbers[2]))
# elif numbers[2]+numbers[3] == target:
#     print(numbers.index(numbers[2]),numbers.index(numbers[3]))
# elif numbers[3]+numbers[0] == target:
#     print(numbers.index(numbers[3]),numbers.index(numbers[0]))

#6
# s = "bbbbb"
# char_set = set()  # Belgilarni saqlash uchun to'plam
# left = 0  # "Window"ning boshlanishi
# longest = 0  # Eng uzun substring uzunligini saqlash
#
#
# for right in range(len(s)):
#
#     while s[right] in char_set:
#         char_set.remove(s[left])
#         left += 1
#
#     char_set.add(s[right])
#     longest = max(longest, right - left + 1)
# print(longest)

#7
# nums = [10,20,30,40,50,60,70,80,90]
# l=[]
# index=0
# while nums:
#     index=(index+2)%len(nums)
#     l.append(nums.pop(index))
# print(l)


#10

# a=int(input("Enter the a: "))
# b=int(input("Enter the b: "))
#
# while b:
#     a,b=b,a%b
# print(a)


#12
# num=int(input("Enter the number: "))
# num_str=str(num)
# print(num_str==num_str[::-1])


