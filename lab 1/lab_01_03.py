'''m = 10
pi = 3.1415927

print(" '"'m = %4d; pi= %4.3f'"' " % (m, pi))
print(" '"'m = {}; pi = {}'"'".format(m, pi))
year = input("Введите число: ")
print(year)
r1 = input("Введите количество баллов по русскому языку: ")
m1 = input("Введите количество баллов по математике: ")
p1 = input("Введите количество баллов по профильному предмету: ")

print("Количество баллов по русскому языку: ", r1)
print("Количество баллов по математике: ", m1)
print("Количество баллов по профильному предмету: ", p1) '''


c = input("Введите двенадцатиразрядное число :");
s = 0
for i in range(12):
    k = (c % 10)
    s = s + k*(14**i)
    c = c//10
print(s)





