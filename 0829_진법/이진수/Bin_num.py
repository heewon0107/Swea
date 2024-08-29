T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    bin_ = ""
    for o in num:
        if o == "0":
            bin_ += "0000"
        if o == "1":
            bin_ += "0001"
        if o == "2":
            bin_ += "0010"
        if o == "3":
            bin_ += "0011"
        if o == "4":
            bin_ += "0100"
        if o == "5":
            bin_ += "0101"
        if o == "6":
            bin_ += "0110"
        if o == "7":
            bin_ += "0111"
        if o == "8":
            bin_ += "1000"
        if o == "9":
            bin_ += "1001"
        if o == "A":
            bin_ += "1010"
        if o == "B":
            bin_ += "1011"
        if o == "C":
            bin_ += "1100"
        if o == "D":
            bin_ += "1101"
        if o == "E":
            bin_ += "1110"
        if o == "F":
            bin_ += "1111"
    print(f"#{tc} {bin_}")