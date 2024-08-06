# 알파벳을 숫자로 변환

alphabet = input()
if len(alphabet) <= 200:  # 알파벳의 최대 길이 200
    for char in alphabet:
        # 문자를 아스키 코드로 바꿔주고 숫자로 바꾸기 위한 -64 후 출력.
        # chr(ord(char) -64)
        print(ord(char)-64, end=" ")
