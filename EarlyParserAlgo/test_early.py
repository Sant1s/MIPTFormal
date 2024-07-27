# from src.early_parser import EarlyParser, Rule
import pytest
from early_parser import EarlyParser, Rule


def test_one_simple():
    rules: list[Rule] = [Rule('S', 'A'), Rule('A', 'aB'), Rule('B', 'b')]
    early = EarlyParser()
    early.fit(rules, 'S')
    assert early.predict('ab') == True
    assert early.predict('aba') == False


def test_two_default():
    rules: list[Rule] = [Rule('S', 'aA'), Rule('S', 'aB'), Rule('B', 'b'), Rule('A', 'b')]
    early = EarlyParser()
    early.fit(rules, 'S')
    assert early.predict('aba') == False
    
    
def test_three_uncertainty():
    rules: list[Rule] = [Rule('S', 'aA'), Rule('S', 'aB'), Rule('B', 'b'), Rule('A', 'b')]
    early = EarlyParser()
    early.fit(rules, 'S')
    assert early.predict('ab') == True
    assert early.predict('aba') == False
    
    
def test_four_medium():
    rules: list[Rule] = [Rule('S', 'aFbF'), Rule('F', 'aFb'), Rule('F', '')]
    early = EarlyParser()
    early.fit(rules, 'S')
    assert early.predict('aabb') == True
    assert early.predict('aba') == False
    
    
def test_five_medium():
    rules: list[Rule] = [Rule('S', 'aSbS'), Rule('S', 'bSaS'), Rule('S', '')]
    early = EarlyParser()
    early.fit(rules, 'S')
    assert early.predict('abb') == False
    assert early.predict('abab') == True
    
    
def test_six_hard():
    rules: list[Rule] = [Rule('S', 'aB'), Rule('A', 'a'), Rule('A', 'Ba'), Rule('B', 'ABC'), Rule('B', 'b'), Rule('C', 'BA'), Rule('C', 'c')]
    early = EarlyParser()
    early.fit(rules, 'S')
    assert early.predict('ababba') == True
    assert early.predict('abababbaba') == True
    assert early.predict('abababba') == False
