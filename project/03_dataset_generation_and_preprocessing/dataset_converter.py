import os
import shutil

dataset = "gemstone__.v6-only_safe_gems.voc"
os.chdir("C:/Users/USER/Downloads/" + dataset + '/')

print(os.getcwd())
try:
    os.mkdir("Annotations")
    os.mkdir("ImageSets")
    os.mkdir("ImageSets/Main")
    os.mkdir("JPEGImages")
except FileExistsError:
    print("Already Exists!")

print("train file...")
file1 = open("./ImageSets/Main/train.txt", 'w')
files1 = os.listdir('C:/Users/USER/Downloads/' + dataset + '/train/')
for filename in files1:
    file_name, file_ext = filename.rsplit('.', maxsplit=1)
    if file_ext == 'jpg':
        file1.write(file_name + '\n')
file1.close()

print("test file...")
file2 = open("./ImageSets/Main/test.txt", 'w')
files2 = os.listdir('C:/Users/USER/Downloads/' + dataset + '/test/')
for filename in files2:
    file_name, file_ext = filename.rsplit('.', maxsplit=1)
    if file_ext == 'jpg':
        file2.write(file_name + '\n')
file2.close()

print("val file...")
file3 = open("./ImageSets/Main/val.txt", 'w')
files3 = os.listdir('C:/Users/USER/Downloads/' + dataset + '/valid/')
for filename in files3:
    file_name, file_ext = filename.rsplit('.', maxsplit=1)
    if file_ext == 'jpg':
        file3.write(file_name + '\n')
file3.close()

print("train_val file...")
FILE_NAME = []
for filename in files1:
    file_name, file_ext = filename.rsplit('.', maxsplit=1)
    if file_ext == 'jpg':
        FILE_NAME.append(file_name)
for filename in files2:
    file_name, file_ext = filename.rsplit('.', maxsplit=1)
    if file_ext == 'jpg':
        FILE_NAME.append(file_name)
FILE_NAME.sort()
file4 = open("./ImageSets/Main/trainval.txt", 'w')
for filename in FILE_NAME:
    file4.write(filename + '\n')
file4.close()

print("moving files from train set...")
for filename in files1:
    file_name, file_ext = filename.rsplit('.', maxsplit=1)
    if file_ext == 'jpg':
        shutil.move('C:/Users/USER/Downloads/' + dataset + '/train/' + filename,
                    'C:/Users/USER/Downloads/' + dataset + '/JPEGImages/' + filename)
    elif file_ext == 'xml':
        shutil.move('C:/Users/USER/Downloads/' + dataset + '/train/' + filename,
                    'C:/Users/USER/Downloads/' + dataset + '/Annotations/' + filename)

print("moving files from test set...")
for filename in files2:
    file_name, file_ext = filename.rsplit('.', maxsplit=1)
    if file_ext == 'jpg':
        shutil.move('C:/Users/USER/Downloads/' + dataset + '/test/' + filename,
                    'C:/Users/USER/Downloads/' + dataset + '/JPEGImages/' + filename)
    elif file_ext == 'xml':
        shutil.move('C:/Users/USER/Downloads/' + dataset + '/test/' + filename,
                    'C:/Users/USER/Downloads/' + dataset + '/Annotations/' + filename)

print("moving files from valid set...")
for filename in files3:
    file_name, file_ext = filename.rsplit('.', maxsplit=1)
    if file_ext == 'jpg':
        shutil.move('C:/Users/USER/Downloads/' + dataset + '/valid/' + filename,
                    'C:/Users/USER/Downloads/' + dataset + '/JPEGImages/' + filename)
    elif file_ext == 'xml':
        shutil.move('C:/Users/USER/Downloads/' + dataset + '/valid/' + filename,
                    'C:/Users/USER/Downloads/' + dataset + '/Annotations/' + filename)

try:
    os.rmdir('train')
    os.rmdir('test')
    os.rmdir('valid')
except FileExistsError:
    print("already deleted!")

files_labels = os.listdir('C:/Users/USER/Downloads/gemstone_dataset/train/')
file_label = open("./labels.txt", 'w')
for labels in files_labels:
    file_label.write(labels + '\n')
file_label.close()