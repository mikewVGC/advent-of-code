
import re

class Machine():
    def __init__(self, lights, buttons, joltage):
        self.lights = lights
        self.buttons = buttons
        self.joltage = joltage

        self.masks = []

        # these should not be lists
        for button in self.buttons:
            mask = [ 0 ] * len(self.lights)
            for light in button:
                mask[light] = 1

            self.masks.append(mask)


    def press_button(self, number):
        for light in self.buttons[number]:
            self.lights[light] = 0 if self.lights[light] == 1 else 0

def turn_on_all_lights(machine):
    needed_mask = []
    for i, light in enumerate(machine.lights):
        needed_mask.append(1 if light == 0 else 0)

    print(needed_mask)

machines = []

with open("2025/input/day10-example", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        items = line.split(' ')
        lights = list(map(lambda x: 1 if x == '#' else 0, list(items[0][1:-1])))
        buttons = list(map(lambda x: list(map(lambda x: int(x), x)), list(map(lambda x: x.split(','), list(map(lambda x: x[1:-1], items[1:len(items) - 1]))))))
        joltage = list(map(lambda x: int(x), items[len(items) - 1][1:-1].split(',')))

        machines.append(
            Machine(lights, buttons, joltage)
        )


for machine in machines:
    turn_on_all_lights(machine)
