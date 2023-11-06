

# # 1. WAP of file handling using 
#       a.open()
#       close()
#       writelines()
#       append()
#       read()
#       readlines()


# y= open('myfile.txt' , 'r+')
# print(y.read())

# print(y.write("Hello Guyssss !!!!!!"))






# with open('myfile.txt', 'w') as file:
#       content = file.write('Hello World')
#       print(content)


# with open('myfile.txt', 'a') as file:
#       content = file.write('Welcomes You')
#       print(content)


# with open('myfile.txt', 'r') as file:
#       content = file.readlines()
#       print(content)
      
# 2. WAP that tells and sets the position of a file pointer


# with open('myfile.txt', 'r') as file:
#     current_position = file.tell()
#     print(f"Current position: {current_position}")
#     new_position = 20
#     file.seek(new_position)
#     updated_position = file.tell()
#     print(f"New position: {updated_position}")
#     content = file.read()
#     print("Content from the new position:")
#     print(content)



# 3. WAP that copies ist 10  bytes of a binary file into another

# with open('myfile.txt', 'rb') as data, open('new.txt', 'wb') as newfile :
    
#     datas = data.read(10)
#     newfile.write(datas)
