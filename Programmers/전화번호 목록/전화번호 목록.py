# def solution(phone_book):
#     answer=True
#     for i in phone_book:
#         new_book = phone_book.copy()
#         new_book.remove(i)
#         if len([j for j in new_book if j.startswith(i)]) != 0:
#             return False
#     return answer

def solution(phone_book):
    for i in phone_book:
        new_book = phone_book.copy()
        new_book.remove(i)
        for j in new_book:
            if j.startswith(i):
                return False
    return True