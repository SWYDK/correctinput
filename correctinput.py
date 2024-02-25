def ask(asktype, question):
    while True:
        try:
            result = asktype(input(question))
            return result
        except ValueError:
            print('Incorrect input!')



def help():
    return 'Create correct input as \'int_result = ask(int, \'Введите целое число: \')\' \n You can use int/str/boolean/list/dict'




