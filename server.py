import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer
from datetime import datetime
from datetime import timedelta

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_get_days_until_bday(self, date):
    splitted_date = date.split('/')
    day = int(splitted_date[0])
    month = int(splitted_date[1])

    today = datetime.today()
    current_year = today.year

    bday_this_year = datetime(current_year, month, day)

    if bday_this_year < today:
      bday_next_year = datetime(current_year + 1, month, day)
      return (bday_next_year - today).days

    return (bday_this_year - today).days

  def exposed_is_leap(self, year):
    year = int(year)
    if year < 1:
      raise ValueError('O ano não pode ser negativo')
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

  def exposed_add_days_to_date(self, date_str, days):
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime("%d/%m/%Y")  

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

