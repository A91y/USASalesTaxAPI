from django.test import TestCase

# Create your tests here.

class SalesTaxDataTest():
    def __init__(self, zipCode, state, combined_rate, local_rate, state_rate, population):
        self.zipCode = zipCode
        self.state = state
        self.combined_rate = combined_rate
        self.local_rate = local_rate
        self.state_rate = state_rate
        self.population = population