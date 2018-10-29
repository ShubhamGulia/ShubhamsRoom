class Enemy:
    life=3
    def attack(self):
        self.life =self.life -1
        print('Ouch')

    def check_status(self):
        if (self.life < 0):
            print('I am dead')
        else:
            print("lives left :" + str(self.life))


# Each object is independent of other
Enemy1=Enemy()
Enemy2=Enemy()
Enemy1.attack()
Enemy1.check_status()
Enemy1.attack()
Enemy1.check_status()
Enemy1.attack()
Enemy1.check_status()
Enemy1.attack()
Enemy1.check_status()
Enemy2.attack()
Enemy2.attack()
Enemy2.check_status()
