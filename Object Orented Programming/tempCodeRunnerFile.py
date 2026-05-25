class Influencer:
    def __init__(self,followers):
        self.followers=followers

    def influencer(self,followers):
        if followers > 1000:
            print("Viral Creator")
        else:
            print("Growing Creator")




person=Influencer(983)
print("Followers",person.followers)
person.influencer(983)