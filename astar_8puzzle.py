
import heapq

# Take the initial puzzle as input
start = []

for i in range(3):
    row = list(map(int, input("Enter row: ").split()))
    start.extend(row)

start = tuple(start)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i in range(9):
        value = state[i]

        if value != 0:
            goal_pos = value - 1

            r1, c1 = i // 3, i % 3
            r2, c2 = goal_pos // 3, goal_pos % 3

            distance += abs(r1 - r2) + abs(c1 - c2)

    return distance


# A* Search
def astar(start):
    pq = [(heuristic(start), 0, start, [start])]
    visited = {start: 0}

    while pq:
        f, cost, state, path = heapq.heappop(pq)

        if cost > visited[state]:
            continue

        if state == goal:
            return path, cost

        # Find position of empty tile (0)
        pos = state.index(0)
        row, col = pos // 3, pos % 3

        # Possible movements: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_pos = new_row * 3 + new_col

                new_state = list(state)

                new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]

                new_state = tuple(new_state)
                new_cost = cost + 1

                if new_cost < visited.get(new_state, float('inf')):
                    visited[new_state] = new_cost
                    new_f = new_cost + heuristic(new_state)

                    heapq.heappush(pq, (new_f, new_cost, new_state, path + [new_state]))

    return [], -1


# Run the algorithm
if sorted(start) != list(range(9)):
    print("Invalid puzzle")
elif sum(start[i] > start[j] for i in range(9) for j in range(i+1, 9) if start[i] and start[j]) % 2:
    print("Puzzle cannot be solved")
else:
    path, cost = astar(start)

    for step, state in enumerate(path):
        print("\nStep:", step)

        for i in range(0, 9, 3):
            print(state[i:i+3])

    print("\nTotal moves:", cost)
