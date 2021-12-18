"""
This code will help you know the number of meeting rooms required
"""

from heapq import heapify, heappush, heappop

def meetingRooms(meetings):
    # Base Case
    if meetings is None or len(meetings) == 0:
        return 0
    # Sort the array
    meetings.sort(key=lambda x: x[0])

    # Creating min-heap to store end times
    heap = []
    heapify(heap)
    # Enter first meeting end point
    heappush(heap, meetings[0][1])

    # if new meeting start >= minimum end point then pop and push meaning
    # It can accomodate multiple meetings
    for i in range(1, len(meetings)):
        if meetings[i][0] >= heap[0]:
            heappop(heap)
            heappush(heap, meetings[i][1])
        else:
            heappush(heap, meetings[i][1])

    return len(heap)

def main():
    n = int(input().strip())
    meetings = list()

    for _ in range(n):
        meetings.append(list(map(int,input().strip().split())))

    answer = meetingRooms(meetings)
    print(answer)

if __name__=="__main__":
    main()