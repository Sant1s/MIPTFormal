from grammar import Grammar, GrammarRule
from lr_parser import LRParser

def main() -> None:
    numbers = list(map(int, input("Enter number of non-terminals, terminals, rules: ").split()))
    alphabet = {}
    rules = set()
    
    non_terminals = input("Enter non terminal: ")
    non_terminals = non_terminals.split()
    for item in non_terminals:
        alphabet[item] = False
    
    terminals = input("Enter terminal: ")
    terminals = terminals.split()
    for item in terminals:
        alphabet[item] = True
        
    for _ in range(numbers[2]):
        rule = input("Enter rule (like A->aB): ")
        left_part, right_part = rule.split('->')
        rules.add(GrammarRule(left_part, [letter for letter in right_part]))
        
    start_non_terminal = input("Enter start non terminal: ")
    
    grammar = Grammar(alphabet, rules, start_non_terminal)
    parser = LRParser(grammar)
    parser.build_states("S#", start_non_terminal)
    parser.build_table()
    
    number_of_words = int(input("Enter number of words: "))
    for _ in range(number_of_words):
        print("Yes" if parser.predict(input("Enter word: ")) else "No")


if __name__ == '__main__':
    main()