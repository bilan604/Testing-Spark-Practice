import json


class Parser(tuple[int, int]):
    @staticmethod
    def str_to_int(s: str):
        return int(s)
    
    @staticmethod
    def json_to_df(s: str):
        return json.loads(s)