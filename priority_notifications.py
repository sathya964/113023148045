import heapq

weights = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

notifications = [
    {
        "ID": "1",
        "Type": "Placement",
        "Message": "CSX Hiring",
        "Timestamp": "2026-04-22 17:51:18"
    },
    {
        "ID": "2",
        "Type": "Result",
        "Message": "Mid Sem Result",
        "Timestamp": "2026-04-22 17:51:30"
    },
    {
        "ID": "3",
        "Type": "Event",
        "Message": "Farewell",
        "Timestamp": "2026-04-22 17:51:06"
    }
]

def get_top10(notifications):

    heap = []

    for n in notifications:

        score = weights[n["Type"]]

        heapq.heappush(
            heap,
            (-score, n["Timestamp"], n)
        )

    result = []

    for _ in range(min(10, len(heap))):
        result.append(
            heapq.heappop(heap)[2]
        )

    return result

top_notifications = get_top10(notifications)

for n in top_notifications:
    print(n)