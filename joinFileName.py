import sys
import argparse

parser = argparse.ArgumentParser(
    description='Create python file and function.')
parser.add_argument('-f', type=str, dest='fileName')
parsedArgs = parser.parse_args()
fileName = parsedArgs.__getattribute__('fileName')

fileName = '_'.join(list(map(lambda x: x.lower(), fileName.split())))

with open(fileName + '.py', 'w') as f:
    f.write(f'def {fileName}():\n')
    f.write(f'\tpass')
