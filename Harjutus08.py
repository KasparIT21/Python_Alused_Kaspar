####################
#    Ülesanne 8    #
#  Kaspar Tõnisson #
#    16.02.2022    #
#      IT-21       #
####################


class Autod:
    Automark = 'teadmata'
    Aasta = 0
    Hind = 0
    Varv = 'teadmata'
    Kiirus = 0
    
    def lisaAutomark(self,x):
        self.Automark = x
        
    def lisaAasta(self,x):
        self.Aasta = x
        
    def lisaHind(self,x):
        self.Hind = x
        
    def lisaVarv(self,x):
        self.Varv = x
        
    def lisaKiirus(self,x):
        self.Kiirus = x
        
        
    def kuva(self):
        print('Automark: {} \nAasta: {} \nHind: {}€ \nVärv: {} \nKiirus: {}km/h'.format(self.Automark, self.Aasta, self.Hind, self.Varv, self.Kiirus))
        
uusObjekt = Autod()
uusObjekt.lisaAutomark('KIA')
uusObjekt.lisaAasta(2014)
uusObjekt.lisaHind(30000)
uusObjekt.lisaVarv('Hõbe')
uusObjekt.lisaKiirus(198)
uusObjekt.kuva()
print()
sObjekt = Autod()
sObjekt.lisaAutomark('Škoda')
sObjekt.lisaAasta(2017)
sObjekt.lisaHind(20000)
sObjekt.lisaVarv('Hõbe')
sObjekt.lisaKiirus(180)
sObjekt.kuva()
