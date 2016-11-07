# ダイクストラ法
# http://www.geocities.jp/m_hiroi/light/pyalgo22.html#note1

#         10    10
#      Ａ──Ｂ──Ｃ
#  20／  ＼          ＼20
#  ／      ＼ 30       ＼
#Ｄ          ＼          Ｅ
#  ＼20        ＼      ／
#    ＼          ＼  ／20
#      Ｆ──Ｇ──Ｈ
#         10   10

adjacent = [
    [ 0, 10,  0, 20,  0,  0,  0, 30],   # A (0)
    [10,  0, 10,  0,  0,  0,  0,  0],   # B (1)
    [ 0, 10,  0,  0, 20,  0,  0,  0],   # C (2)
    [20,  0,  0,  0,  0, 20,  0,  0],   # D (3)
    [ 0,  0, 20,  0,  0,  0,  0, 20],   # E (4)
    [ 0,  0,  0, 20,  0,  0, 10,  0],   # F (5)
    [ 0,  0,  0,  0,  0, 10,  0, 10],   # G (6)
    [30,  0,  0,  0, 20,  0, 10,  0]    # H (7)
]

MAX_SIZE = 8
MAX_VALUE = 0x10000000

visited = [False] * MAX_SIZE
cost = [MAX_VALUE] * MAX_SIZE
prev = [None] * MAX_SIZE

def search(start):
    cost[start] = 0
    prev[start] = start
    while True:
        min = MAX_VALUE
        next = -1
        visited[start] = True
        # 頂点の選択
        for i in range(MAX_SIZE):
            if visited[i]: continue
            if adjacent[start][i]:
                d = cost[start] + adjacent[start][i]
                if d < cost[i]:
                    cost[i] = d
                    prev[i] = start
            if min > cost[i]:
                min = cost[i]
                next = i
        start = next
        if next == -1: break
    # 経路の表示
    print_path()

def print_path():
    for i in range(MAX_SIZE):
        print("%d, prev = %d, cost = %d" %  (i, prev[i], cost[i]))