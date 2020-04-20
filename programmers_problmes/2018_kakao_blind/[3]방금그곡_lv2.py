def solution(m, musicinfos):
    answer = '(None)'
    maxim = 0
    m = m.replace('C#','c')
    m = m.replace('D#','d')
    m = m.replace('F#','f')
    m = m.replace('G#','g')
    m = m.replace('A#','a')
    
    for i in range(len(musicinfos)):
        start,end,name,song = musicinfos[i].split(',')
        start_h, start_m = map(int,start.split(':'))
        end_h, end_m = map(int,end.split(':'))
              
        time =(end_h-start_h)*60 + (end_m - start_m)
        
        song = song.replace('C#','c')
        song = song.replace('D#','d')
        song = song.replace('F#','f')
        song = song.replace('G#','g')
        song = song.replace('A#','a')
        
        #song = song * (time//len(song)) + song[0:time%len(song)]
        
        if len(song) > time:
            song = song[:time]
        
        elif len(song) < time:
            temp = time//len(song)
            temp2 = time%len(song)

            new_song = song*temp
            if temp2 > 0:
                new_song += song[:temp2]
            
            song = new_song
        

        if m in song:
            if len(song) > maxim:
                answer = name
                maxim = len(song)
        
        
    return answer
