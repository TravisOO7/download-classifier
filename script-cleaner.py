import os
import shutil
from pathlib import Path

directory_path = Path('E:/Downloads/')
path = 'E:/Downloads/'

if __name__ == '__main__':
    
    for filename in directory_path.iterdir():
        if filename.is_file():
            # print(filename)
            fname = str(filename)
            if "Unconfirmed" in fname:
                continue
            i = len(fname)
            reversed_filename = fname[::-1]

            for j in reversed_filename:
                if(j == '.'):
                    break
                i-=1
            
            if i == 0:
                continue

            extension = fname[i::]
            # print(extension)

            file = fname[len(path)::]
            # print(file)

            if extension == 'pdf' or extension == 'PDF':
                new_file_name = "PDF/"
            elif extension == 'docx' or extension == 'doc':
                new_file_name = "WORD/"
            elif extension == 'zip' or extension == 'rar':
                new_file_name = "ZIP/"
            elif extension == 'exe' or extension == 'msi':
                new_file_name = "Setups/"
            elif extension == 'jpg' or extension == 'png' or extension == 'jpeg':
                new_file_name = "Images/"
            elif extension == 'pptx' or extension == 'ppt':
                new_file_name = "Presentations/"
            elif extension == 'cpp' or extension == 'py' or extension == 'php' or extension == 'sql' or extension == 'ipynb':
                new_file_name = "CodeFiles/"
            elif extension == 'xlsx':
                new_file_name = "Excel/"
            elif extension == 'csv' or extension == 'arff':
                new_file_name = "Datasets/"
            elif extension == 'mp4' or extension == 'mp3' or extension == 'mkv':
                new_file_name = "Videos/"
            elif extension == 'model':
                new_file_name = "MLModels/"
            else:
                new_file_name = "Miscelleneous/"
            # print(path + new_file_name + file)
            if not os.path.exists(path + new_file_name):
                os.makedirs(path + new_file_name)
            shutil.move(filename, path + new_file_name + file)
            
