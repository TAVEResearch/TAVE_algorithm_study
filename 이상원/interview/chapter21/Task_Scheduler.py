# p.595
import collections


def leastInterval(tasks: list, n: int) -> int:
    # 우선순위 큐로 그리디 풀기
    counter = collections.Counter(tasks)
    print(counter)
    result = 0

    while True:
        sub_count = 0
        # 개수 순 추출
        for task, _ in counter.most_common(n + 1):
            # most_common은 최대 힙과 같은 역할
            print(task)
            sub_count += 1
            result += 1

            counter.subtract(task)
            print(f'counter : {counter}')
            # 0 이하인 아이템을 목록에서 완전히 제거
            counter += collections.Counter()

        if not counter:
            break
        result += n - sub_count + 1
    return result


if __name__ == '__main__':
    task = ["A", "A", "A", "B", "C", "D"]
    n = 2
    print(leastInterval(task, n))
