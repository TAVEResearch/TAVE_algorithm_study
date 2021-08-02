def solution(phone_number: str) -> str:
    answer = []
    answer.append("*" * (len(phone_number) - 4))
    answer.append(phone_number[(len(phone_number) - 4):])
    
    return "".join(answer)
