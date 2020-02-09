def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        possible = True
        skills = []
        for level in tree:
            if level in skill:
                skills.append(level)
        print(skills)
        
        for i in range(len(skills)):
            if skill[i] != skills[i]:
                possible = False
        
        if possible:
            answer += 1
            
    return answer
