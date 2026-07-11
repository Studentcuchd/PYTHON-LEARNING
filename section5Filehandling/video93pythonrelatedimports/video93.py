# from utils.common.importop import write_save_file, read_file


# another way 
from .common.importop import write_save_file, read_file

write_save_file(file="section5Filehandling/textfiles/video93.txt", content="Hiparag this is import method")

print(read_file("section5Filehandling/textfiles/video93.txt"))