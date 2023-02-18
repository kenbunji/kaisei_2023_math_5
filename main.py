"""開成中学校　2023年入試問題 算数 5 (4)

"""


def meet_cond(num: int) -> bool:
    """条件に当てはまる数かを検査する（0,8,9を含まない）

    Args:
        num (int): 検査する整数
    Returns:
        bool: Trueなら条件に当てはまる。Falseなら条件に当てはまらない

    """
    for char in str(num):
        if char in '089':
            return False  # 禁止された数(0,8,9)を含む
    return True  # 条件に当てはまる


cnt = 0
print('#', 'a', 'b')
for a in range(0, 9724):  # aは9723以下
    b = 9723 - a
    if meet_cond(a) is False:
        continue
    if meet_cond(b) is False:
        continue
    cnt += 1
    print(cnt, a, b)
