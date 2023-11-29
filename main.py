from early_parser import EarlyParser, Rule

def main():
    print('Введите количество нетерминалов, терминалов и правил грамматики:')
    nonterminal_count, terminal_count, rules_count = map(int, input().split())

    print(f'Введите {nonterminal_count} нетерминалов:')
    nonterminals = [x for x in input().split()]

    if terminal_count:
        print(f'Введите {terminal_count} терминалов:')
        terminals = [x for x in input().split()]

    print(f'Введите {rules_count} правил:')
    rules: list[Rule] = []
    for _ in range(rules_count):
        left_part, right_part = input().split('->')
        rules.append(Rule(left_part, right_part))

    print('Введите старовый символ грамматики:')
    start_nonterminal = input()

    print('Введиет число слов для проверки:')
    number_words_to_check = int(input())

    parser = EarlyParser()
    parser.fit(rules, start_nonterminal)

    print('Введите слова для проверки:')
    for _ in range(number_words_to_check):
        word = input()
        print('Yes') if parser.predict(word) else print('No')



if __name__ == '__main__':
    main()