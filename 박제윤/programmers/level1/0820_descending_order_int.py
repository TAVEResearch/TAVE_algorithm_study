
def solution(num: int) -> int:
  # int -> str -> list -> reverse sorting -> str -> int
  return int("".join(sorted(list(str(num)), reverse = True)))
