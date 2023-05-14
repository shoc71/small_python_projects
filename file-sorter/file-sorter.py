import os
import shutil

print("Which dir? 1.desktop / 2.downloads / 3.documents")
user_input = input("Enter your choice here either as a number or the name : ")

if user_input == ("1" or "desktop"):
    y = os.chdir("Desktop")
elif user_input == ("2" or "downloads"):
    y = os.chdir("Downloads")
elif user_input == ("3" or "documents"):
    y = os.chdir("Documents")

files = os.listdir(os.getcwd())
count = 1

images = [".jpeg",".png",".jpg",".gif"] #extensions for images
words = [".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"] #extensions for text files
videos = [".mp4",".mkv"] #extensions for videos
sounds = [".mp3",".wav",".ogg"] #extensions for sounds
# applications = [".exe"] #extensions for applications
codes = [".py",".js"] #extensions for codes

for file in files:
    folder = ""
    for i in images:
        if file.endswith(i):
            folder = "../Images"
            shutil.move(file, folder)
            break

    for w in words:
        if file.endswith(w):
            folder = "../Text Files"
            shutil.move(file, folder)
            break

    for v in videos:
        if file.endswith(v):
            folder = "../Videos"
            shutil.move(file ,folder)
            break

    for s in sounds:
        if file.endswith(s):
            folder = "../Sounds"
            shutil.move(file ,folder)
            break

    # for a in applications:
    #     if file.endswith(a):
    #         folder = "Applications"
    #         shutil.move(file ,folder)
    #         break

    for c in codes:
        if file.endswith(c):
            folder = "../Codes"
            shutil.move(file ,folder)
            break
        
    print(f"{count} files sorted")
    count += 1
print("All files sorted")
