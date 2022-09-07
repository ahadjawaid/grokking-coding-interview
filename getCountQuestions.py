import os

path = os.getcwd()


def recursiveCount(path):
    count = 0
    filesInPath = os.listdir(path)
    for file in filesInPath:
        if '.py' not in file and file != 'getCountQuestions.py':
            newPath = os.path.join(path, file)
            count += recursiveCount(newPath)
        else:
            count += 1
    return count


print(recursiveCount(path))
