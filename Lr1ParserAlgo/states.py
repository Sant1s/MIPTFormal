from lr_situation import Situation
from grammar import GrammarRule
from dataclasses import dataclass

SHIFT = 's'
REDUCE = 'r'
ACCEPT = 'a'


@dataclass(init=True, eq=True)
class State:
    situations: set[Situation]

    def __hash__(self):
        return hash(frozenset(self.situations))


@dataclass(init=True)
class LrTableState:
    state_type: str = None
    goto_state: str = None
    rule: GrammarRule = None

    @staticmethod
    def get_shift(goto_state: str):
        return LrTableState(SHIFT, goto_state=goto_state)

    @staticmethod
    def get_reduce(rule: GrammarRule):
        return LrTableState(REDUCE, rule=rule)

    @staticmethod
    def get_accept():
        return LrTableState(ACCEPT)
