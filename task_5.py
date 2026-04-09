class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return self.victories
    
    def number_of_draws(self):
        return self.draws   
    
    def number_of_losses(self):
        return self.losses
    
    def total_points(self):
        return self.victories * 3 + self.draws 

class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return self.victories
    
    def number_of_draws(self):
        return self.draws   
    
    def number_of_losses(self):
        return self.losses
    
    def total_points(self):
        return self.victories * 2 + self.draws
    

footbal_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)   

for team in (footbal_team, hockey_team):
    print(f"Victories: {team.number_of_wins()}")
    print(f"Draws: {team.number_of_draws()}")
    print(f"Losses: {team.number_of_losses()}")
    print(f"Total points: {team.total_points()}")