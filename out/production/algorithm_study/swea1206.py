T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2]:
            left = max(arr[i-1], arr[i-2])
            if arr[i] > arr[i+1] and arr[i] > arr[i+2]:
                right = max(arr[i+1], arr[i+2])
                result += arr[i] - max(left, right)
    print(f'#{test_case} {result}')
            