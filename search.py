import os
def search(dirname):
    try: #예외처리
        file_names = os.listdir(dirname)
        for file_name in file_names:
            full_filename = os.path.join(dirname, file_name)
            ext = os.path.splitext(full_filename)[-1]
            if os.path.isdir(full_filename): #True라면 full_filename이 폴더(directory)임
                search(full_filename)
            else:
                if ext == ".py": #찾고싶은 확장자
                    print(full_filename)
    except PermissionError: #권한 때문에 파일이나 폴더에 접근이 안 될 수도 있어서
        pass
search("C:/")