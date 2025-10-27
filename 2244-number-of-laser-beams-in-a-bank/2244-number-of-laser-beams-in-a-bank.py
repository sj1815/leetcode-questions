class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams, prev_devices = 0, 0
        for row in bank:
            devices = row.count("1")
            if devices:
                beams += devices * prev_devices
                prev_devices = devices
        return beams

