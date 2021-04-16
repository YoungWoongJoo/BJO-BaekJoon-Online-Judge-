"""
회의실 배정

문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 (2의31승)-1보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

"""
import sys

n=int(sys.stdin.readline()) #input()함수보다 sys.stdin.readline()함수가 더빠름
#readline함수를 이용했을시 약 300ms, input함수를 이용했을시 약 4초가 걸림
#입력의 횟수가 많아질수록 성능 차이가 심해짐
#입력을 받을 때 readline함수를 이용하는 것을 습관화하자!
time_list=[]
for i in range(n):
	start_time,end_time=map(int,sys.stdin.readline().split())
	time_list.append((start_time,end_time))

time_list.sort(key=lambda x:(x[1],x[0])) #끝나는시간,시작시간 우선순위로 정렬
#끝나는시간이빠를수록 더많이 회의를 할수있음

end,count=0,0

for t in time_list:
	if end<=t[0]:
		count+=1
		end=t[1]

print(count)
