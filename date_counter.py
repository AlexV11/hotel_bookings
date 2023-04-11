from datetime import datetime, timedelta

# haz una funcion que cuente cuantos dias caen en fin de semana
def count_weekend_nights(arriving_date, nights):
    arriving_date = datetime.strptime(arriving_date, '%Y-%m-%d')
    weekend_nights = 0
    for i in range(nights):
        arriving_date = arriving_date + timedelta(days=1)
        if arriving_date.weekday() == 5 or arriving_date.weekday() == 6:
            weekend_nights += 1
    return weekend_nights