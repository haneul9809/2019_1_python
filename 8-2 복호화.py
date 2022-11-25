encrypted_text="Mpwf!xjmm!gjoe!b!xbz/"

plain_text=""
for c in encrypted_text:
    x=ord(c)
    x=x-1
    cc=chr(x)
    plain_text=plain_text+cc
print(plain_text)
