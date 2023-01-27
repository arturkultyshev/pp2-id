quiz = {
    'Which is the currency of Kazakhstan?': ('tenge', 'kaz'),
    'Name one of the past/present presidents of Kazakhstan': ('tokayev', 'nazarbayev'),
    'What year Kazakhstan proclaim independence?': '1991'
}
cor_ans = 0
for i in quiz.keys():
    print(i)
    ans = str(input())
    if ans.lower() in quiz[i]:
        cor_ans += 1
        continue
    else:
        continue

print(cor_ans)