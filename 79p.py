ame_p=2000
cala_p=3000
capu_p=3500

ame=int(input("아메리카노 판매 개수 : "))
cala=int(input("카페라테 판매 개수 : "))
capu=int(input("카푸치노 판매 개수 : "))

sale=(ame*ame_p)+(cala*cala_p)+(capu*capu_p)

print("총 매출은 ",sale,"입니다.")

money=100000

print("총 재료비용은 100,000원이고 ,",sale-money,"원의 수익이 있습니다.")
