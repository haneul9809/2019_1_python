print("안녕하세요?")
name=input("이름이 어떻게 되시나요? : ")
print("만나서 반갑습니다. "+name+"씨") #+는 숫자와 숫자, 문자와 문자를 연결

print("이름의 길이는 다음과 같군요 : ",end='')
print(len(name))

age=int(input("나이가 어떻게 되시나요? : "))
print("내년이면 ",str(age+1),"이 되시는군요.") #,는 문자와 숫자를 연결