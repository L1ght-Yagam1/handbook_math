import sys
import queue

INF = -1

def list_graph(n, first_input):
    res = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n+1):
            if first_input[j] == '1':
                res[i].append(j)

        first_input = sys.stdin.readline().split()
    return res

def bfs(graph, n, start, end):
    visited = [0 for _ in range(n)]
    dist = [INF for _ in range(n)]
    q = queue.Queue()

    visited[start] = 1
    dist[start] = 0
    q.put(start)

    while not q.empty():
        v = q.get()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                dist[i] = dist[v] + 1
                q.put(i)
                if i == end:
                    return dist[i]
    return -1

def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные сос12тоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    n = int(sys.stdin.readline().strip())
    first_input = sys.stdin.readline().split()
    graph = list_graph(n - 1, first_input)


    start, end = sys.stdin.readline().split()

    result = bfs(graph, n, int(start), int(end))

    print(result)

if __name__ == '__main__':
    main()