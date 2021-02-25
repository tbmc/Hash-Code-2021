from typing import Tuple, List, Dict
from collections import defaultdict
from dataclasses import dataclass


ROAD_DICT_TYPE = Dict[str, Tuple[int, int, int]]


@dataclass
class DataContainer:
    duration: int
    intersection_number: int
    street_number: int
    car_number: int
    bonus_points: int

    road_dict: ROAD_DICT_TYPE
    intersection_dict: Dict[int, Tuple[List[str], List[str]]]
    car_list: List[List[str]]


def read_data(file_path: str) -> DataContainer:
    with open(file_path) as f:
        content = f.read()

    content = list(map(lambda s: s.strip(), content.strip().split("\n")))
    D, I, S, V, F = map(int, content[0].split())
    roads = content[1:S + 1]
    cars = content[S + 1:]

    road_dict: ROAD_DICT_TYPE = {}  # key, (start, end, time)
    # id, # (list of input road, list of output roads)
    intersection_dict: Dict[int, Tuple[List[str], List[str]]] = defaultdict(lambda: ([], []))
    car_list: List[List[str]] = []  # roads it wants to travel through

    for road in roads:
        start, end, name, time = road.split()
        start = int(start)
        end = int(end)
        time = int(time)

        road_dict[name] = start, end, time
        intersection_dict[start][0].append(name)
        intersection_dict[end][1].append(name)

    for car in cars:
        car_list.append(car.split()[1:])

    return DataContainer(D, I, S, V, F, road_dict, intersection_dict, car_list)



