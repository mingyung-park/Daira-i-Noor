# 25305 커트라인

n,k=map(int,input().split())
score=list(map(int, input().split()))
score.sort()
print(score[-k])