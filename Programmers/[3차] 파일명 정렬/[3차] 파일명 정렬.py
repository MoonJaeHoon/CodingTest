import re
def solution(files):
    new_files = []
    for file in files:
        pat = re.compile("[0-9]+")
        span = pat.search(file).span()
        file_split = [file[:span[0]], file[span[0]:span[1]], file[span[1]:]]
        new_files.append(file_split)
    new_files=sorted(new_files,key=lambda x: int(x[1]))
    new_files=sorted(new_files,key=lambda x: x[0].lower())
    return [''.join(new_file) for new_file in new_files]