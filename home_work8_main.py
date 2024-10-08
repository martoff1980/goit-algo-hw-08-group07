import heapq


def heap_sort(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in iterable:
        heapq.heappush(h, value)

    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    return [heapq.heappop(h) for _ in range(len(h))]


def min_coast(cables, n=0, cost=0):
    global totalcost
    if cables == []:
        return
    if n <= 1:
        cost += cables.pop(0)
        totalcost = cost
    else:
        cost += cables.pop(0)
        totalcost += cost
    min_coast(cables, n+1, cost)


# набір кабелів, їх довжини, будуть як масив у вигляді цілих чисел
cables = [3, 2, 1, 4]
print("Набір кабелів:", cables)

# сортування кабелів
sorted_cables = heap_sort(cables)
print("Відсортованні кабеля:", sorted_cables)

# очислення вартості за допомогою рекурсії
totalcost = 0
min_coast(sorted_cables)
print("Мінімальна вартість з'єднання:", totalcost)
