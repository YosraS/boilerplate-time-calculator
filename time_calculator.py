
class MyTime:
  def __init__(self,myhour,myminute,myampm=None,myday=0,dayname=None):
        
        self.myhour=myhour
        self.myminute=str(myminute).zfill(2)
        self.myampm=myampm
        self.myday=myday
        self.dayname=dayname
  

  def ConvertMinutes(self):
      
      return((int(self.myhour)*60)+int(self.myminute))
  def __str__(self):
      if int(self.myhour)==0:
          self.myhour=12
      if self.myampm is None:
          return str(self.myhour)+':'+str(self.myminute)
      else:
          return str(self.myhour)+':'+str(self.myminute)+' '+str(self.myampm)
  def Changeampm(self):
    if self.myampm=='AM':
        self.myampm='PM'
    elif self.myampm=='PM':
        self.myampm='AM'
        self.myday=int(self.myday)+1

def addBis(x,y):
  return (int(x.myhour())+int(y.myhour))
      
def Transform(t):#t=10:55 AM
  if 'AM' in t or 'PM' in t:
    x,y=t[0:-3].split(':')
    z=t[-2:]
    return MyTime(x,y,z)
  else:#t=24:12
    x,y=t.split(':')
    return MyTime(x,y)

def ConvertMinMyTime(x,ampm=None):
    hour=int(x/60)
    minute=int(x%60)
    return(MyTime(hour,minute,ampm))



def day_name(day,nbdays):
  days_week={1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}
  
  for k, v in days_week.items():
    if v.upper() == day.upper():
        key=k
  if int(nbdays)>0:
    #nbdays=int(nbdays)%7
    #key=key+nbdays
    key=key+nbdays
    while key>7:
      key=key-7
  return str(days_week[key].capitalize())


def add_time(start, duration,start_day=None):
 
  start_time=Transform(start)
  duration_time=Transform(duration)#was false
  new_date=ConvertMinMyTime(start_time.ConvertMinutes()+duration_time.ConvertMinutes(),start_time.myampm)
      
  days_week={1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}
  
  while new_date.myhour>=24:
      new_date.myhour -=24
      new_date.myday+=1
  while new_date.myhour>=12:
      new_date.Changeampm()
      new_date.myhour-=12
  #  new_date_hour=new_date.myhour
  # while new_date_hour>=12:
  #     new_date.Changeampm()
  #     new_date_hour-=12
  if start_day is None:
      if new_date.myday==0:
          return str(new_date)
      elif new_date.myday==1:
          return str(new_date)+" (next day)"
      else:
          return str(new_date)+" ("+str(new_date.myday)+" days later)"
  elif start_day.lower() in days_week.values():
      if new_date.myday==0:
          return str(new_date)+", "+str(day_name(start_day,new_date.myday))
      elif new_date.myday==1:
          return str(new_date)+", "+str(day_name(start_day,new_date.myday))+" (next day)"
      else:
          return str(new_date)+", "+str(day_name(start_day,new_date.myday))+" ("+str(new_date.myday)+" days later)"
      
