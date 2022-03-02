            self.writeVint(1) # 1 Unknown(Error)
            self.writeVint(0) # ItemID
            self.writeVint(1) # Ammount
            self.writeScId(16, 0) # Brawler ID
            self.writeVint(0) # Skin ID
            self.writeVint(0) # ShopType, 0 = Offer, 2 = Skin, 3 = Star Shop
            self.writeVint(9) # Cost
            self.writeVint(99999) # Timer
            self.writeVint(1) # is Offer Viewed?
            self.writeVint(100) # 100 Unknown
            self.writeBoolean(False) # is Offer Purchased?
            self.writeBoolean(False) # False Unknown
            self.writeVint(0) # ShopDisplay, 0 = Normal, 1 = Daily Deals
            self.writeBoolean(False) # False Unknown
            self.writeVint(0) # 0 Unknown
            self.writeInt(0) # 0 Unknown(Error)
            self.write_string_reference('offerName') # OfferName
            self.writeBoolean(False) # False Unknown
            self.writeString() # Backgrounds
            self.writeVint(0) # 0 Unknown
            self.writeBoolean(False) # True = BG Disappear
            self.writeVint(0) # Extra Type, 1 - (X)Profit, 2 - Profit in Percents(%)
            self.writeVint(0) # % Extra Text
