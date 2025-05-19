from colorama import init, Fore

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
         print(Fore.BLUE + message)

def mode(massage, is_warning=False):
    if is_warning:
        print(Fore.RED + massage)
    else:
        print(Fore.BLUE + massage)

