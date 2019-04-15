from datetime import datetime,timedelta
from reservation.models import Reservation
import time


class CalendrierResa :
	
	#Attributs
    nbDaysMonth = []
    allDays = []
    allDays2 = []
    dateDebut = datetime
    dateFin = datetime

	#Methodes
    def __init__(self,idate,nbJoursDelta):

        self.allDays.clear()
        self.allDays2.clear()
        self.nbDaysMonth.clear()

        dateCurr = idate

        delta = timedelta(days=nbJoursDelta)
        oneDay = timedelta(days=1)

        dateDebut = dateCurr - delta
        dateDebut = dateDebut.replace(day=1)

        dateFin = dateCurr + delta

        old_month = dateDebut.strftime("%Y%m")
        nb = 0
        while dateDebut.strftime("%Y%m") <= dateFin.strftime("%Y%m") :
            self.allDays.append(dateDebut.strftime("%Y%m%d"))
            self.allDays2.append(dateDebut.strftime("%d"))
            nb = nb + 1
            dateDebut = dateDebut + oneDay

            if dateDebut.strftime("%Y%m") != old_month :
                self.nbDaysMonth.append({'mois': old_month, 'nbjrs': nb})
                old_month =  dateDebut.strftime("%Y%m")
                nb = 0



        