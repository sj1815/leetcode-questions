class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        trained_players = 0
        trainer_index = 0

        while trained_players < len(players) and trainer_index < len(trainers):
            if trainers[trainer_index] >= players[trained_players]:
                trained_players += 1
            trainer_index += 1
        
        return trained_players
        