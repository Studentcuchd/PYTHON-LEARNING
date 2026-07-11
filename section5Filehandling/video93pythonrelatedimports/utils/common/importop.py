def read_file(content):
    with open(content,"r") as file_reader:
        return file_reader.read().splitlines()
    
def write_save_file(content,file):
    with open(file,"w") as writer_file:
        writer_file.write(content)
    
