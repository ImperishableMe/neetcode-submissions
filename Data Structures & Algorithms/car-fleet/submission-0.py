class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [car for car in zip(position, speed)]
        cars.sort()
        print(cars)
        """
            t[i] ? (target - position[i]) / speed[i]
            => t[i] * speed[i] ? (target - pos[i])
            t[i] > t[j] 
            => (target - pos[i]) / speed[i] > (target - pos[j]) / speed[j]
            => (target - pos[i]) * speed[j] > (target - pos[j]) * speed[i]
        """
        n = len(speed)
        fleets, cur_fleet = 1, n - 1

        def time_diff(i: int, j: int) -> int:
            return (target - cars[i][0]) * cars[j][1] - (target - cars[j][0]) * cars[i][1]

        for i in range(n - 2, -1, -1):
            if time_diff(i, cur_fleet) > 0:
                cur_fleet = i
                fleets += 1
        return fleets

