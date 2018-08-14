import shell

with open(shell.get_filename()) as file:
    search_name = shell.get_search_name()
    num = 0
    for line in file:
        num = num + 1
        if search_name in line.lower():
            shell.print_results(num, line)
