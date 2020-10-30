# -*- coding: utf-8 -*-

import os
import io

title='mycloud'
url = f'https://cdn.jsdelivr.net/gh/carycoti/{title}/'
gitignore = ['.gitignore', '.git']
with open('.gitignore', 'r') as f:
        for item in f:
            gitignore.append(item)


def make(s, f):
    d=os.listdir('.')
    f.write('<ul>\n')
    for i in d:
        if(not [False for item in gitignore if i in item]):
            if os.path.isdir(i):
                f.write(f'<li><a href="{s}{i}/">{i}/</a>')
                os.chdir(i)
                make(s+i+'/', f)
                os.chdir('..')
                f.write('</li>\n')
            else:
                f.write(f'<li><a href="{s}{i}">{i}</a></li>\n')
    f.write('</ul>\n')


with open('index.html','w') as f:
    f.write(f'<!DOCTYPE html>\n<html>\n')
    f.write(f'<head>\n<title>{title}</title>\n')
    f.write(f'<meta http-equiv="Content-Typecontent="text/html; charset=UTF-8" />\n')
    f.write(f'</head>\n<body>\n<h1>{title}</h1>\n')
    f.write('<h2>Sitemap</h2>\n')
    make(url, f)
    f.write('</body>\n</html>')
    
print('DONE')
