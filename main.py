from typing import Tuple, List, Dict
from collections import defaultdict
from read_data import read_data

OUTPUT_TYPE = Dict[int, List[Tuple[str, int]]]


def simple_compute(file_name: str) -> None:
    data = read_data(f"data/{file_name}.txt")
    output: OUTPUT_TYPE = defaultdict(list)

    for intersection, (input_road, output_road) in data.intersection_dict.items():
        for road in input_road:
            output[intersection].append((road, 1))

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
    simple_compute("a")

