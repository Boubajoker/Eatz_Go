import os
from typing import Any
import random

main_msg = print("EatzGo Copyright (c) Boubajoker 2021. All right reserved.\nProject under MIT License. Type `-h` or `--help` to get help.")
help_msg = """
                        EatzGoShell Internal Documentation
EatzGo Copyright (c) Boubajoker 2021. All right reserved. Project under MIT License.

EatzGoShell is a developer option of EatzGo, here you can type varius types of commands to execute actions in the directory. 

Commands:
    <-- buildit-in's commands -->
        -h: The command that your typed seconds ago.
        cd: Generate an \"str\" text of the actual directory.
        quit: Quit the shell.

    <-- shell commands -->
        Usage: EatzGo --<option>
               EatzGo --<option> [mod:str]

        EatzGo --set_meals [mod]: set the meal in the file "meals.txt". [mod]=w+, a+
        EatzGo --open_caches: open cache folder.
        EatzGo --open_logs: open logs folder.
"""
#class `EatzGoShell`
class EatzGoShell(object):
    def __init__(self) -> Any:
        super().__init__()

        self.running = True
        while self.running:
            self.input_command = input("->")

            # buildit-in's commands
            if self.input_command == "":
                pass
            elif self.input_command == "cd":
                os.system("cd")
            elif self.input_command == "quit":
                self.running = False
            elif self.input_command == "-h":
                print(help_msg)
            elif self.input_command == "--help":
                print(help_msg)
            elif self.input_command == "clear":
                os.system("clear")
            elif self.input_command == "cls":
                os.system("cls")
            # shell commands
            elif self.input_command == "EatzGo --set_meals a+":
                self.meals = input("put your meals here ->")
                with open(".meals/meals.txt", "a+") as f:
                    f.write("\n" + self.meals)
                    f.close()
            elif self.input_command == "EatzGo --set_meals w+":
                self.meals = input("put your meals here ->")
                with open(".meals/meals.txt", "w+") as f:
                    f.write(self.meals)
                    f.close()
            elif self.input_command == "EatzGo --open_caches":
                os.system("start cache/EatzGoServices.log")
            elif self.input_command == "EatzGo --open_logs":
                os.system("start log/cookie.log")
            elif self.input_command == "EatzGo":
                os.system("EatzGo")
            else:
                self.commands = ["EatzGo --set_meal a+", "EatzGo --set_meal w+", "EatzGo --open_caches", "EatzGo --open_logs"]
                print(f"[ERROR]:\"{self.input_command}\" is not defined. You can try this: {random.choice(self.commands)}")

if __name__ == '__main__':
    EatzGoShell()