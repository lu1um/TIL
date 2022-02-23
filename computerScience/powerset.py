
def powerset(idx, N):
    if idx == N:
        print(bit)
        return
    else:
        bit[idx] = 0
        powerset(idx+1, N)  # [0,,] - [0,0,] - [0,0,0]
        bit[idx] = 1        #       \ [0,1,] - [0,1,0]
        powerset(idx+1, N)  #                \ [0,1,1] 과 같이 차곡차곡 생성된다.


a = [1,2,3]
N = len(a)
bit = [0] * N

powerset(0, N)