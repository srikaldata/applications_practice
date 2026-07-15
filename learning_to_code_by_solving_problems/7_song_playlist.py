# song playlist order change

# button 1 - move first song to the end
# button 2 - more last song to the start
# button 3 - swap the first and second songs
# button 4 - plays the playlist 

# initial song order
songs_order = 'ABCDE'

# initializing button value
button =0

# looping through different songs based on user input
while button != 4 and button < 4 and button > -1 :
    button = int(input('enter the button number: '))
    num_presses= int(input('num of times the button needs to be pressed: '))
    
    for _ in range(num_presses):
        if button == 1:
            print('you have pressed button 1')
            songs_order=songs_order[1:]+songs_order[0]
            
        elif button ==2:
            print('you have pressed button 2')
            songs_order=songs_order[-1]+songs_order[:-1]
        
        elif button==3:
            print('you have pressed button 3')
            songs_order=songs_order[1]+songs_order[0]+songs_order[2:]

output =''
for song in songs_order:
    output += song + ' '

print(output[:-1])
