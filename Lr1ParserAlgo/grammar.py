from dataclasses import dataclass, field


@dataclass(init=True)
class GrammarRule:
    left_non_terminal: str
    right_part: list[str]

    def __hash__(self):
        return hash((self.left_non_terminal, tuple(self.right_part)))


@dataclass
class Grammar:
    alphabet: dict[str, bool] = field(default_factory=dict)
    rules: set[GrammarRule] = field(default_factory=set)
    start: str = ""
    new_start: str = ""
