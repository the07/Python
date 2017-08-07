#encoding=utf-8
import io

f = io.open('poem.txt', 'wt', encoding='utf-8')
f.write(u'Imagine a non english lannguage here')

f.close()

text = io.open('poem.txt', encoding='ascii').read()
print(text)
