from dataclasses import dataclass


@dataclass(order=True)
class Situation:
    left_non_terminal: str
    right_part: list[str]
    dot_pos: int
    next_letter: str

    def __hash__(self):
        return hash((self.left_non_terminal, tuple(self.right_part), self.dot_pos, self.next_letter))
