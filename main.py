class Machine(object):
    cost_per_kWh = 0.5

    def __init__(self, prod, cost, average):
        self.prod = prod
        self.cost = cost
        self.average = average

    def parts_for_payback(self):
        return self.cost / self.average

    def payback_time(self):
        return self.parts_for_payback()/self.prod


class CncMachine(Machine):
    def __init__(self, prod, cost, average, resource):
        Machine.__init__(self, prod, cost, average)
        self.resource = resource # the number of hours the machine will operate under warranty

    def payback_rate(self): # how many times the machine will pay back
        return self.resource/Machine.payback_time(self)


class MillingMachine(Machine):
    def __init__(self, prod, cost, average, power):
        Machine.__init__(self, prod, cost, average)
        self.power = power

    def part_cost(self):
        return Machine.cost_per_kWh * self.power/1000 / self.prod


machine1 = CncMachine(prod=12, cost=4000, average=5, resource=10000)
machine2 = MillingMachine(prod=3, cost=1200, average=4, power=1200)

print(machine1.payback_rate())
print(machine2.part_cost())