from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    initianal_price = models.FloatField()

    class Positions(models.TextChoices):
        GOALKEEPER = "goalkeeper", "Goalkeeper"
        LEFTBACK = "left-back", "Left-back"
        RIGHTBACK = "right-back", "Right-back"
        DEFENDER = "defender", "Defender"
        MIDFIELDER = "midfielder", "Midfielder"
        ATTACKER = "attacker", "Attacker"

    position = models.CharField(max_length=50, choices=Positions.choices)

    def __str__(self):
        return f"{self.name} - {self.position}"
        
class Team(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class MyTeam(models.Model):
    players = models.ManyToManyField(Player)
    
    def __str__(self):
        return [player.name for player in self.players.all()].__str__()

class Match(models.Model):
    date = models.DateTimeField()
    home_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="home_team_matches")
    home_team_score = models.IntegerField(default=0)
    away_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="away_team_matches")
    away_team_score = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.home_team.name} : {self.home_team_score} x {self.away_team_score} : {self.away_team.name}"

class Action(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name="actions")
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="actions")
    minute = models.IntegerField()
    match = models.ForeignKey(Match, on_delete=models.PROTECT, related_name="actions")

    class Actions(models.TextChoices):
        GOAL = "goal", "Goal" 
        ASSIST = "assist", "Assist"
        YELLOW_CARD = "yellow card", "Yellow Card"
        RED_CARD = "red card", "Red Card"
        PENALTY = "penalty", "Penalty"
        SUBSTITUTION = "substitution", "Substitution"
        FOUL = "foul", "Foul"

    action = models.CharField(max_length=50, choices=Actions.choices)
    
    def __str__(self):
        return f"{self.player.name}, {self.action} : {self.minute} min"