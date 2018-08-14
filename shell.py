import disk


def get_filename():
    return input('\nFile Name: ')


def get_search_name():
    return input('\nSearch For: ')


def print_results(num, line):
    return print('\n{}: {}'.format(num, line.strip()))


def main():
    get_filename()
    get_search_name()
    print_results(num, line)


if __name__ == '__main__':
    main()
