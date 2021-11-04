def solution(dartResult: str) -> int:
  nums = [0]

  for s in dartResult:
    if s == "S":
      nums[-1] **= 1
      nums.append(0)
    elif s == "D":
      nums[-1] **= 2
      nums.append(0)
    elif s == "T":
      nums[-1] **= 3
      nums.append(0)
    
    # "*"이 입력 값일때, 이전 값과 그 이전 값을 모두 2배처리
    elif s == "*":
      nums[-2] *= 2      
      if len(nums) > 2:
        nums[-3] *= 2
    elif s == "#":
      nums[-2] *= -1
    # 숫자인 경우 두 자리일 수도 있으니 기존에 이미 수가 들어 있다면 자릿수가 올라간것
    else:
      nums[-1] = nums[-1] * 10 + int(s)

    print(nums)
  return sum(nums)

dart_Result_list = ["1S2D*3T", # 37 -> (1^1 * 2) + (2^2 * 2) + (3^3)
                    "1D2S#10S", # 9
                    "1D2S0T", # 3
                    "1S*2T*3S", # 23
                    "1D#2S*3S", # 5
                    "1T2D3D#", # -4
                    "1D2S3T*"] # 59

for dart_result in dart_Result_list:
  print(dart_result)
  print(solution(dart_result))
