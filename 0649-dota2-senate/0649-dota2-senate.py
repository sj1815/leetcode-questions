class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        # Fill initial queues with indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulation
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)  # R bans D, R comes back next round
            else:
                dire.append(d + n)     # D bans R, D comes back next round

        return "Radiant" if radiant else "Dire"
