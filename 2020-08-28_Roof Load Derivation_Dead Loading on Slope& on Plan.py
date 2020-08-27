#### PITCH ROOF- lOADING  TYPES DATABABSE:  ACCORDING TO BRITISH CODE OF PRACTICE

"""   DEAD LOADS MEASURED ON THE SLOPE LENGTHS """
"""   IMPOSED LOADS AS PER UK BRITISH  STANDARDS-EN ANNEX """

import math

class PitchRoofTypeA():  ####COMPOSITION OF ROOF

### CONNECTORS

    def __init__(self, SeamRoofing, PlywoodThick, ZincMembrane, Rafters, FlexiBatts, Battens, SolarPanels, Pitch):
        self.SeamRoofing = SeamRoofing  #### Standing Seam Roofing
        self.PlywoodThick = PlywoodThick  ###  Plywwod Thickness
        self.ZincMembrane = ZincMembrane  ####
        self.Rafters = Rafters  ###@400mm/CC or @600mm /CC
        self.FlexiBatts = FlexiBatts  ####Rockwool Flexi Batts
        self.Battens = Battens
        self.SolarPanels = SolarPanels
        self.Pitch = Pitch

    ### METHODOLOGY

    def DeadLoadingOnSlope(self):
        return (( self.SeamRoofing + self.PlywoodThick + self.ZincMembrane + self.Rafters + self.FlexiBatts + self.Battens + self.SolarPanels)) / 100

    @property
    def DeadLoadingOnPlan(self):
        return ((self.SeamRoofing + self.PlywoodThick + self.ZincMembrane + self.Rafters + self.FlexiBatts + self.Battens + self.SolarPanels) / 100) / math.cos(
            math.radians(self.Pitch))


x = PitchRoofTypeA(20, 12, 6.5, 7.5, 3.5, 12, 23, 1)

x.Pitch = 45                       ### Angle in Degrees

print(x.DeadLoadingOnSlope())       #### in kN/m^2
print(x.DeadLoadingOnPlan)          ### kN/m^2

