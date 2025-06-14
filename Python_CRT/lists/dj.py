size= 10
songs=[]
for i in range (size):
    temp=input(("Enter the song name:"))
    songs.append(temp)
print(songs)
rev=songs[::-1]
print("the playlist in the reverse order is:",rev) 