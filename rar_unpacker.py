from rarfile import RarFile

def un_rar(file_name, output_path = None):
    RarFile.open(file_name)

if __name__ == '__main__':
    file_name = 'to_unpack.rar'
    output_path = './'
    un_rar(file_name)
