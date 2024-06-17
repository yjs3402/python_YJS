song='''동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강세
대한사람 대한으로 길이 보전하세
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강세
대한사람 대한으로 길이 보전하세
'''

print(song[0:4])
print(song[5:9])
print(song[10:13])
print(song[14:17])
print(song[18:22])
print(song[23:27])
print(song[28:32])
print(song[33:35])
print(song[36:39])
print(song[40:43])
print(song[44:48])
print(song[49:53])
print(song[54:58])
print(song[59:61])
print(song[62:66])





for i in range(6):
    position = song.find('세')
    print(song[position-1:position+1])
    song = song[position+1:]
    

'''    
se0 = -1
se1 = song[se0+1:].find("세")+se0+1
se2 = song[se1+1:].find("세")+se1+1
se3 = song[se2+1:].find("세")+se2+1
se4 = song[se3+1:].find("세")+se3+1
se5 = song[se4+1:].find("세")+se4+1
se6 = song[se5+1:].find("세")+se5+1
print(song[se1-1:se1+1])
print(song[se2-1:se2+1])
print(song[se3-1:se3+1])
print(song[se4-1:se4+1])
print(song[se5-1:se5+1])
print(song[se6-1:se6+1])'''











