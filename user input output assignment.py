first =int(input("Enter first number :"))
second =int(input("Enter second number :"))
third =int(input("Enter third  number :"))
fourth =int(input("Enter fourth  number :"))



if first< second and first < third and first < fourth :
    print(first,"is the smallest number")

elif second< first and second < third and second < fourth:
    print(second, "is the smallest number")

elif third < first and third < second and third< fourth:
    print(third, "is the smallest number")

else:
    print(fourth, "is the smallest number")
