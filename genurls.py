import os


def juin(lines):
    result = ""
    for ll in lines:
        result += ll
        result += ":"

    return result[:-1]


def get_url(filename):
    f = open(filename)
    lines = f.readlines()
    version = ""
    source = ""

    for line in lines:
        splited_line = line.split(":")
        if splited_line[0] == "Version":
            version = splited_line[1].strip()
        if splited_line[0] == "Source0":
            source = juin(splited_line[1:]).strip()

    if version == "" or source == "":
        return None

    source = source.replace("%{version}", version).strip()
    return source


specs_files = []
for root, dirs, files in os.walk(r'SPECS/'):
    for file in files:
        if file.endswith('.spec'):
            specs_files.append('SPECS/'+file)

for source in specs_files:
    s = get_url(source)
    if s is not None:
        print(s)

