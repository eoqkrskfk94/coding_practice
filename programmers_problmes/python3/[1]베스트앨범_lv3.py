def solution(genres, plays):
    genreDic = {}
    songDic = {}
    
    for i in range(len(genres)):
        play = plays[i]
        genre = genres[i]
        genreDic[genre] = genreDic.get(genre,0) + play
        songDic[genre] = songDic.get(genre, []) + [(play,i)]
    
    genreSort = sorted(genreDic.items(), key=lambda x: x[1], reverse=True)
    
    # print(genreSort)
    # print(genreSort2)

    answer = []
    for x,t in genreSort:
        songDic[x] = sorted(songDic[x], key=lambda x: (-x[0], x[1]))
        answer += [ idx for (play, idx) in songDic[x][:2] ]
        
    

    print(answer)
    return answer
