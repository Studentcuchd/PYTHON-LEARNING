def write_to_file(content,filename):
    with open(filename,"w") as writer_mode:
        writer_mode.write(content)

def readfile(filename):
    with open(filename,"r") as reader_mode:
        return reader_mode.read().splitlines()