f = open('newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'FileIO']
text = '\n'.join(lines)
f.writelines(text)
f.close()