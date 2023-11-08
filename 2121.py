import sys
input = sys.stdin.readline

answer = 0
dots = int(input().strip())
tx, ty = map(int, input().strip().split())
dotlist = []
dictlist = dict()
for i in range(dots):
    inx, iny = map(int, input().strip().split())
    dotlist.append([inx, iny])
    if inx not in dictlist:
        dictlist[inx] = [iny]
    else:
        dictlist[inx].append(iny)

for i in range(len(dotlist)):
    tmx, tmy = dotlist[i]
    if tmy + ty in dictlist[tmx] and tmx+tx in dictlist and tmy in dictlist[tmx+tx] and tmy + ty in dictlist[tmx+tx]:
        answer +=1 
# if [tmpx+tx, tmpy+ty] in dotlist and [tmpx, tmpy+ty] in dotlist and [tmpx+tx, tmpy] in dotlist:
#     answer += 1

print(answer)