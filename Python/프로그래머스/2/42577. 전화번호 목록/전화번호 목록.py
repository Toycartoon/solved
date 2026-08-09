def solution(phone_book):
    phone_book.sort()

    ans = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            ans = False
    
    return ans
