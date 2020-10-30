import os
import io
title='mycloud'
url = f'https://cdn.jsdelivr.net/gh/carycoti/{title}/'
gitignore = ['.gitignore', '.git']
with open('.gitignore', 'r') as f:
        for item in f:
            gitignore.append(item)
print(gitignore)
def make(s):
    d=os.listdir('.')
    with open('index.html','w') as f:
        f.write(f'<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>{title}</title></head><body><h1>{title}</h1><ul>\n')
        f.write('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>Sitemap</title></head><body><h2>Sitemap</h1><ul>\n')
        for i in d:
            if(not [False for item in gitignore if i in item]):
                if(os.path.isdir(i)):
                    os.chdir(i)
                    make(s+i+'/')
                    os.chdir('..')
                    f.write(f'<li><a href="{url}{i}">{i}/</a></li>\n')
                else:
                    f.write(f'<li><a href="{url}{i}">{i}</a></li>\n')

make('https://github.com/carycoti/mycloud/')
print('DONE')
