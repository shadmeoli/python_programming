import math

# i will create an entry class to hold logic for the whole program
class Operations:

    def __init__(self):

        self.answer = ''
        self.choices = {
            1: "sqrt",
            2: "log",
            3: "factorial"
            }
        # prompting the user on start up
        print(" Welcome to the simple math helper,\n")
        self.action_choice = int(input('''What would you like to calculate,
1. sqrt
2. log
3. factorial
'''))
        
        # asking for value for user input
        self.num_to_be_computed = int(input(f"Enter the number to {self.choices[self.action_choice]} : "))


    def run(self):
        if self.choices[self.action_choice] == 'sqrt':
            print(round(math.sqrt(self.num_to_be_computed)))
        elif self.choices[self.action_choice] == 'log':
            print(round(math.log(self.num_to_be_computed)))
        elif self.choices[self.action_choice] == 'factorial':
            print(round(math.factorial(self.num_to_be_computed)))



if __name__ == "__main__":
    ops = Operations()
    ops.run()