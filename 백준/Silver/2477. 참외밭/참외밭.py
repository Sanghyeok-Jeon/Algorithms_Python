k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(6)]

directions = [edge[0] for edge in edges]
lengths = [edge[1] for edge in edges]

max_length_index = lengths.index(max(lengths))

right_index = (max_length_index + 1) % 6
left_index = (max_length_index - 1 + 6) % 6

if lengths[right_index]> lengths[left_index]:
    second_max_length_index = right_index
else:
    second_max_length_index = left_index

big_area = lengths[max_length_index] * lengths[second_max_length_index]

small_area = lengths[(max_length_index + 3) % 6] * lengths[(second_max_length_index + 3) % 6]

area = big_area - small_area

total_melons = area * k

print(total_melons)