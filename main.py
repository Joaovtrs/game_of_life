import sys
import os

paths = []

for root, dirs, files in os.walk('src'):
    if 'play.py' in files:
        paths.append(root)

print('Chose:')

for i in range(len(paths)):
    print(f'{i}: {paths[i]}')

path = paths[int(input())]
sys.path.append(path)

try:
    import play
except ModuleNotFoundError:
    print('Import error')
