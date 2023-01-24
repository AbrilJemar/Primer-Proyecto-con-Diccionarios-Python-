Playlist = {}
Playlist['Playlist'] ={}
Playlist['Songs'] = []

def App():
    Add_Playlist = True
    
    while Add_Playlist:
        Playlist_Name = input('Enter playlist name: ')
        
        while (Playlist_Name.strip() ==  ""):
            Playlist_Name = input('Invalid field. Try again: ')
        
        
        Playlist['Playlist'] = Playlist_Name
        print(f'\r\nThe name of your playlist is {Playlist_Name}')
        Add_Playlist = False
        

def Add_Songs():
    Add_Song = True
    
    while Add_Song:
        
        Name = Playlist['Playlist']
        Pregunta = input(f'\r\nDo you want to add songs to playlist "{Name}"? (Yes/No): ')
        
        if (isinstance(Pregunta, str)):
            Pregunta = Pregunta.capitalize()
            
        match Pregunta:
            case 'Yes':
                Song = input('\r\nEnter the song name: ')
                while (Song.strip() ==  ""):
                    Song = input('Invalid name. Try again: ')
                
                Playlist['Songs'].append(Song)
                
            case 'No':
                if Playlist['Songs'] == []:
                    Playlist_name = Playlist['Playlist']  
                    print(f'\r\nThe playlist "{Playlist_name}" is empty')
                    
                else: 
                    Playlist_name = Playlist['Playlist']  
                    print(f'\r\nPlaylist "{Playlist_name}"')
                    print('Songs:')
                    Accountant = 0
                    
                    for Song in Playlist['Songs']:
                        Accountant = Accountant + 1
                        print(str(Accountant) + '. ' + Song)
                
                Add_Song = False
            case _:
                print('Invalid field. Try again')
        
        
        
    

Stay = True
while Stay:
    App()
    Add_Songs()
    
    while Stay: 
        Exit = input('\r\nDo you want to save the playlist and exit? (Yes/No): ')
        if (isinstance(Exit, str)):
            Exit = Exit.capitalize()   
        
        match Exit:
            case 'Yes':
                print('\r\nPlaylist saved successfully. \r\nGoodBye.')
                Stay = False
        
            case 'No':
                print('\r\nOk.')
                Add_Songs()
            
            case _:
                print('Invalid field.')
                



    
