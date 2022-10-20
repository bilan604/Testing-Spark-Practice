from __future__ import annotations


class Parser(tuple[int, int]):
    @staticmethod
    def parse(str_dimonsion: str):
        return int(str_dimonsion)