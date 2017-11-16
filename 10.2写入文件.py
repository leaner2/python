#10.2.1写入空文件
filename = 'programming.txt' 
with open(filename, 'w') as file_object:  """ 括号中的参数 w 写入 r 读取 a 附加 """
    file_object.write("I love programming!") 
 
