"""You have participated in your college-level coding fest which was there for 6 days 
Task:
WAPP to give the Final report which includes
1. Activities for the day including timeline
2. Number of teams/participants for the day
3. project_names
4. technologies used
5. PPT Demonstrations given
6. Winner of Day
7. Runner up of the day
8. best performer of the day
9. Host of the program for that day"""
class CodingFest:
    def __init__(self, day, activities, participants, projects, technologies, ppt_demos, winner, runner_up, best_performer, host):
        self.day = day
        self.activities = activities
        self.participants = participants
        self.projects = projects
        self.technologies = technologies
        self.ppt_demos = ppt_demos
        self.winner = winner
        self.runner_up = runner_up
        self.best_performer = best_performer
        self.host = host
    def Display_Details(self):
        print(f"Day:{self.day}")
        print(f"activities:{self.activities}")
        print(f"participants:{self.participants}")
        print(f"project:{self.project}")
        print(f"technologies:{self.technologies}")
        print(f"ppt_demos:{self.ppt_demos}")
        print(f"winner:{self.winner}")
        print(f"runner_up:{self.runner_up}")
        print(f"best_performer:{self.best_performer}")
        print(f"host:{self.host}")
        print("----------------------------------------")
c1=CodingFest(1,"python",10,)
c2=CodingFest(2,)
c3=CodingFest(3,)
c4=CodingFest(4,)
c5=CodingFest(5,)
c6=CodingFest(6,)