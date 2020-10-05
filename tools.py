from datetime import datetime, timedelta

def define_start_end_dete(aDate):
    startDate = aDate.date()
    delta = timedelta(1)
    endDate = startDate + delta

    return startDate, endDate

def dates_to_str(startDate, endDate):
    start = startDate.strftime('%YY-%m-%d')
    end = endDate.strftime('%YY-%m-%d')

    return start, end

def str_to_date(str_of_date):
    date = str_of_date.replace(',','')
    formattedDate = datetime.strptime(date, '%b %d %Y')

    return formattedDate

def str_to_date2(str_of_date):
    formattedDate = datetime.strptime(str_of_date, '%d/%m/%Y')

    return formattedDate

def date_to_str(date):
    formattedDate = datetime.strftime(date, '%b %d, %Y')

    return formattedDate

def add_ond_day(date):
    delta = timedelta(1)
    newDate = date + delta

    return newDate

