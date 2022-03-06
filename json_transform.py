#!/usr/bin/env python3

import argparse
import json


def convert_attribute_option(attr_options_array: list) -> dict:
    attr_options_obj = {}
    option_counter = {}
    for attr_option in attr_options_array:
        code = attr_option["productAttribute"]["code"]
        try:
            option_counter[code] = option_counter[code] + 1
        except KeyError:
            option_counter[code] = 1
        attr_options_obj[f"productAttribute_{code}_{option_counter[code]}"] = attr_option
    return attr_options_obj


def transform(input_obj: dict) -> dict:
    output_list = []
    for item in input_obj["ordersWithDetails"]["items"]:
        for orderItem in item["orderItems"]:
            for ticket in orderItem["tickets"]:
                item_infos = {key: val for key, val in item.items() if key != "orderItems"}
                order_infos = {key: val for key, val in orderItem.items() if key not in ["tickets", "product"]}
                product_infos = {key: val for key, val in orderItem["product"].items() if key != "productItemAttributeOptions"}
                product_infos["productItemAttributeOptions"] = convert_attribute_option(orderItem["product"]["productItemAttributeOptions"])
                ticket_infos = {key: val for key, val in ticket.items()}
                ticket_obj = {**item_infos, **order_infos, **ticket_infos, **product_infos}
                output_list.append(ticket_obj)
    return output_list


def transform_json(input_str: str) -> str:
    return json.dumps(transform(json.loads(input_str)), ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file path")
    parser.add_argument("output", help="output file path")
    args = parser.parse_args()
    input_file_path = args.input
    output_file_path = args.output
    with open(input_file_path, "r") as input_file:
        output = transform_json(input_file.read())
    with open(output_file_path, "w") as output_file:
        output_file.write(output)
