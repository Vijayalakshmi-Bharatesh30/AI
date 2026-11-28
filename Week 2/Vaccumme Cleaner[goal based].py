class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = 0

    def perceive(self):
        return self.environment[self.position]

    def act(self):
        if self.perceive() == "Dirty":
            print(f"Position {self.position}: Cleaning...")
            self.environment[self.position] = "Clean"
        elif self.position < len(self.environment) - 1:
            self.position += 1
            print(f"Moving to position {self.position}")
        else:
            print("Goal achieved: All positions are clean!")

    def goal_achieved(self):
        return all(state == "Clean" for state in self.environment)

    def run(self):
        while not self.goal_achieved():
            self.act()



environment = ["Dirty", "Dirty"]

vacuum = VacuumCleaner(environment)
vacuum.run()

print("Final environment:", environment)
