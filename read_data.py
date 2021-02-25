from typing import Tuple, List, Dict
from collections import defaultdict


ROAD_DICT_TYPE = Dict[str, Tuple[int, int, int]]


def read_data(file_path: str) -> Tuple[ROAD_DICT_TYPE, Dict[int, List[str]], List[List[str]]]:
    with open(file_path) as f:
        content = f.read()

    content = list(map(lambda s: s.strip(), content.strip().split("\n")))
    D, I, S, V, F = map(int, content[0].split())
    roads = content[1:S + 1]
    cars = content[S + 1:]

    road_dict: ROAD_DICT_TYPE = {}  # key, (start, end, time)
    intersection_dict: Dict[int, List[str]] = defaultdict(list)  # id, [connected roads]
    cards_list: List[List[str]] = []  # roads it wants to travel through

    for road in roads:
        start, end, name, time = road.split()
        start = int(start)
        end = int(end)
        time = int(time)

        road_dict[name] = start, end, time
        intersection_dict[start].append(name)

    for car in cars:
        cards_list.append(car.split()[1:])

    return road_dict, intersection_dict, cards_list



