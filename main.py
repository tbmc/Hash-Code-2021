from typing import Tuple, List, Dict
from collections import defaultdict
from read_data import read_data

OUTPUT_TYPE = Dict[int, List[Tuple[str, int]]]


def simple_compute(file_name: str) -> None:
    data = read_data(f"data/{file_name}.txt")
    output: OUTPUT_TYPE = defaultdict(list)

    counter = 0
    for intersection, (column_1, column_2) in data.intersection_dict.items():
        for road in column_2:
            output[intersection].append((road, 1))

    print(f"Intersection with only 1 input road: {counter}")
    write_to_file(f"output/{file_name}.txt", output)


def compute_with_counter(file_name: str) -> None:
    data = read_data(f"data/{file_name}.txt")
    output: OUTPUT_TYPE = defaultdict(list)

    road_counter: Dict[str, int] = defaultdict(lambda: 0)
    for road_list in data.car_list:
        for road in road_list:
            road_counter[road] += 1

    for intersection, (_, column_2) in data.intersection_dict.items():
        count = sum(map(lambda s: road_counter[s], column_2))
        if count != 0:
            for road in column_2:
                number_of_car = road_counter[road]
                if number_of_car > 0:
                    _, _, road_time = data.road_dict[road]
                    road_time_divided = road_time / 4
                    number_of_car = int(number_of_car / (count / 10) / road_time_divided)
                    number_of_car = max(number_of_car, 1)
                    # number_of_car = min(number_of_car, 5)
                    output[intersection].append((road, number_of_car))

    write_to_file(f"output/{file_name}.txt", output)


def write_to_file(file_path: str, output: OUTPUT_TYPE) -> None:
    output_list_final = [len(output)]
    for intersection, list_of_roads in output.items():
        output_list_final.append(intersection)
        output_list_final.append(len(list_of_roads))
        for road_name, time_green in list_of_roads:
            output_list_final.append(f"{road_name} {time_green}")

    out = "\n".join(map(str, output_list_final))
    with open(file_path, "w") as f:
        f.write(out)


if __name__ == "__main__":
    for name in "abcdef":
        compute_with_counter(name)

