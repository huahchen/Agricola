class Improvement:
    def __init__(self, name, prereq, cost, vp, concise, description, effect = None, image = None, minor = True):
        self.name = name
        self.prereq = prereq
        self.cost = cost
        self.vp = vp
        self.concise = concise
        self.description = description
        self.effect = effect
        self.image = image
        self.minor = minor
