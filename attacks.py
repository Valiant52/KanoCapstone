import json
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def find_group_in_data(group_name, data):
    for item in data:
        if item['group'].lower() == group_name.lower():
            return item
    return None

def display_group_info(group_info):
    print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Group Name:{Style.RESET_ALL} {group_info['group']}")
    print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Phase:{Style.RESET_ALL} {group_info['phase']}")
    print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Attack Type:{Style.RESET_ALL} {group_info['attack']}")
    print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Data Sources:{Style.RESET_ALL}")
    for i, source in enumerate(group_info['data_sources'], start=1):
        print(f"  {i}. {source}")
    print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Technique:{Style.RESET_ALL} {group_info['technique']}")

def main():
    attacks_data = load_json_data('attacks.json')
    
    while True:
        group_name = input(Fore.YELLOW + "Enter a group name: " + Style.RESET_ALL)
        group_info = find_group_in_data(group_name, attacks_data)
        
        if group_info:
            display_group_info(group_info)
        else:
            print(Fore.RED + "Error: Group not found :(" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
