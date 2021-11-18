def solution(sizes):
    w_max, h_max = 0, 0

    for card in sizes:
      if card[0] < card[1]:
        tmp = card[0]
        card[0] = card[1]
        card[1] = tmp

      if w_max < card[0]:
        w_max = card[0]
      if h_max < card[1]:
        h_max = card[1]

    return w_max * h_max
