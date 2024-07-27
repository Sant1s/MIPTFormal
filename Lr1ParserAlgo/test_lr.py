from grammar import Grammar, GrammarRule
from lr_parser import LRParser

start = "S"
new_start = "S#"


alphabet = {"S": False, "a": True, "b": True}
rules = {GrammarRule("S", []), GrammarRule("S", ["a", "S", "b", "S"])}
grammar = Grammar(alphabet, rules, start)
parser = LRParser(grammar)
parser.build_states(new_start, start)
parser.build_table()


def test_one():
    assert parser.predict("abab") is True


def test_two():
    assert parser.predict("aabb") is True


def test_three():
    assert parser.predict("bbb") is False


def test_four():
    assert parser.predict("aaaabbbabb") is True


def test_five():
    assert parser.predict("aaaaabbbbbabaabbabaabbb") is False

