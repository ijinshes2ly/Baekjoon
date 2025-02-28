```python
X = int(input("영수증에 적힌 총 금액을 입력하세요:"))
N= int(input(품목 수를 입력하세요:))
total=a=b=0                     # total,a,b =0 되면 반복 가능 객체로 취급하지 않아서 안됨. #a=상품가격,b=상품갯수

for i in range(N):
  a,b = map(int,input().split())  # 여러개 입력 받고 싶으면 찢고 split 함수와 반복가능객체 받는 map!
  total += a*b                     
if total== X:
    print("Yes")
else:
    print("No")
```
