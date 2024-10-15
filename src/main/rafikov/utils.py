def saveFile(file, data):
    with open(file, 'a') as f:
        f.write(f'{data}')