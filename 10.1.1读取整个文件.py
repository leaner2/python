with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

#10.1.2 文件路径
    #绝对路径：with open('C:\users\other_files\text_files\filename.txt') as file_object:
print('\n\n')

#10.1.3 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line) #去除空行用line.rstrip
print('\n\n')

#10.1.4 创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() #raadlines() 把文件中的每一行读取后存储在列表中
    for line in lines:
        print(line.rstrip())
print('\n\n')                        
#10.1.5使用文件内容
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    includings = ''
    for line in lines:
        includings += line.rstrip()
    print(includings)
    print(len(includings))
#包含一百万位的大型文件

filename = 'rode.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    including = ''
    for line in lines:
        including += line.rstrip()
    print(including[:600] + "...")
    print(len(including))

print('\n\n')
#10.1.7 圆周率中包含你的生日吗
filename = 'rode.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    including = ''
    for line in lines:
        including += line.rstrip()
    check_including = input("enter what do you wang to check: ")
    if check_including in including:
        print("there has what you want!")
    else:
        print("nothing you want")



































    
