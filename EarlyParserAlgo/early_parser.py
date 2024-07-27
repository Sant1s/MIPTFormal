import accessify
import dataclasses


@dataclasses.dataclass
class Rule:
    left_part: str
    right_part: str


@dataclasses.dataclass
class Situation:
    left_part: str
    right_part: str
    dot_pos: int
    parent: int

    def __hash__(self):
        return hash((self.left_part, self.right_part, self.dot_pos, self.parent))
    

class EarlyParser:
    def __init__(self) -> None:
        self.grammar: list[Rule]
        self.word: str
        self.START_SITUATION : Situation
        self.TERMINAL_SITUATION : Situation
        

    def fit(self, grammar: list[Rule], start_nonterminal: str) -> None:
        self.grammar = grammar
        self.START_SITUATION = Situation('#', f'{start_nonterminal}', 0, 0)
        self.TERMINAL_SITUATION = Situation('#', f'{start_nonterminal}', 1, 0)
        self.grammar.append(Rule('#', f'{start_nonterminal}'))


    def predict(self, word: str) -> bool:
        self.word = word
        list_situations : list[set[Situation]] = [{self.START_SITUATION} if not _ else set() for _ in range(len(word) + 1)]
        for i, situation in enumerate(list_situations):
            self.__scan(i, list_situations)
            changed = -1
            while changed != len(situation):
                changed = len(situation)
                self.__predict(i, list_situations)
                self.__complete(i, list_situations)
                
        return self.TERMINAL_SITUATION in list_situations[-1]


    @accessify.private
    def __scan(self, index: int, situations: list[set[Situation]]) -> None:
        if index:
            for item in situations[index - 1]:
                if item.dot_pos < len(item.right_part) and item.right_part[item.dot_pos] == self.word[index - 1]:
                    new_situation = Situation(item.left_part, item.right_part, item.dot_pos + 1, item.parent)
                    situations[index].add(new_situation)        
    
    
    @accessify.private
    def __predict(self, index: int, situations: list[set[Situation]]) -> None:
        new = set()
        for item in situations[index]:
            if item.dot_pos == len(item.right_part):
                continue
            expecting_left = item.right_part[item.dot_pos]
            for rule in self.grammar:
                if rule.left_part == expecting_left:
                    new_situation = Situation(rule.left_part, rule.right_part, 0, index)
                    new.add(new_situation)
        situations[index].update(new)  
                
    
    @accessify.private
    def __complete(self, index: int, situations: list[set[Situation]]) -> None:
        new = set()
        for compItem in situations[index]:
            if compItem.dot_pos < len(compItem.right_part):
                continue
            for nextItem in situations[compItem.parent]:
                if nextItem.dot_pos < len(nextItem.right_part) and nextItem.right_part[nextItem.dot_pos] == compItem.left_part:
                    transitives = Situation(nextItem.left_part, nextItem.right_part, nextItem.dot_pos + 1,
                                          nextItem.parent)
                    new.add(transitives)
        situations[index].update(new)