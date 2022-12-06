from datetime import datetime, timedelta

class WeektimeProperties:
    
    def dayToWeekday(self, x):
        z = datetime.strptime(x, "%Y-%m-%d")
        y = z.strftime('%A')
        return y

    def validWeekday(self, days):
        #Loop days you want in the next 21 days:
        today = datetime.now()
        weekdays = []
        for i in range (0, days):
            x = today + timedelta(days=i)
            y = x.strftime('%A')
            if y == 'Monday' or y == 'Saturday' or y == 'Wednesday' or y == 'Friday':
                weekdays.append(x.strftime('%Y-%m-%d'))
        return weekdays
        
if __name__ == '__main__':
    weektime = WeektimeProperties()
    
    
    