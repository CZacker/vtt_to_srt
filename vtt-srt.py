import os

if __name__ == '__main__':
    path = input("Enter your VTT_path: ")
    file=os.listdir(path)
    for fn in file:
        with open(path+'/'+fn, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(lines)
        with open(path+'/'+fn.split('.')[0]+'.srt', "w", encoding="utf-8") as f_w:
            for line in lines:
                if "WEBVTT" in line:
                    continue
                f_w.write(line)
