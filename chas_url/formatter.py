import json


def formatting(one_dict) -> str:
    return json.dumps(one_dict, indent=4)
