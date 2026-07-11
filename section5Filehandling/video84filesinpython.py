file_read=open("section5 Filehandling/textfiles/video84file.txt","r")

print(file_read.read())

file_read.close()






name_of_user=input("Enter your name=")
file_writer=open("section5 Filehandling/textfiles/video84file.txt","w")
file_writer.write(name_of_user)

file_writer.close()




# create a file and append
file_create=open("section5 Filehandling/textfiles/video84append.txt","a")
file_create.close()

# append value
file_append=open("section5 Filehandling/textfiles/video84file.txt","a")

file_append.write("Rohan")


file_append.close()




