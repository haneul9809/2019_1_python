money=int(input("투입한 돈 : ")) #투입한 돈을 입력한다.
price=int(input("물건 값 : ")) #물건 값을 입력한다.

change=money-price #거스름돈을 계산한다.

print("거스름돈 : ",change) #거스름돈을 출력한다.

coin500s=change//500 #500원 동전의 갯수를 구한다.
change=change%500 #500원 동전의 갯수를 제외한 나머지 금액을 구한다.
coin100s=change//100 #100원 동전의 갯수를 구한다.
change=change%100 #100원 동전의 갯수를 제외한 나머지 금액을 구한다.
coin50s=change//50
change=change%50
coin10s=change//10

print("500원 동전의 개수 : ",coin500s) #500원짜리 동전의 개수를 출력한다.
print("100원 동전의 개수 : ",coin100s) #100원짜리 동전의 개수를 출력한다.
print("50원 동전의 개수 : ",coin50s)
print("10원 동전의 개수 : ",coin10s)
