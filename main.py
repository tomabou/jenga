import numpy as np

dp = np.zeros((100, 100, 4), dtype=int)
dp -= 1


def grundySenteWin(x, y, m):
    oldx = x
    if dp[x, y, m] >= 0:
        return dp[x, y, m]

    num = []
    nm = m+1
    if nm == 4:
        nm = 1
        x += 1

    if x > 0:
        num.append(grundySenteWin(x-1, y, nm))
        num.append(grundySenteWin(x-1, y+1, nm))

    if y > 0:
        num.append(grundySenteWin(x, y-1, nm))

    number = 0
    for i in range(100):
        if not i in num:
            number = i
            break

    dp[oldx, y, m] = number

    return number


def isSenteWin(x, y, m):
    oldx = x
    if dp[x, y, m] >= 0:
        return dp[x, y, m] == 1

    ans = False
    nm = (m+1) % 3
    if nm == 0:
        x += 1

    if x > 0:
        ans |= not isSenteWin(x-1, y, nm)
        ans |= not isSenteWin(x-1, y+1, nm)

    if y > 0:
        ans |= not isSenteWin(x, y-1, nm)

    if ans:
        dp[oldx, y, m] = 1
    else:
        dp[oldx, y, m] = 0

    return ans


def calc(n):
    ans = isSenteWin(n-1, 0, 2)
    print("{} {} ".format(n, ans))


def calc2(n):
    ans = grundySenteWin(n-1, 0, 2)
    print("{} {} ".format(n, ans))


def main():
    for i in range(1, 50):
        calc2(i)

    print(dp[:20, :20, 1])
    print(dp[:20, :20, 2])
    print(dp[:20, :20, 3])


if __name__ == '__main__':
    main()
