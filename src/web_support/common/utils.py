import datetime

def generate_recent_academic_years(num_years=4):
    current_year = datetime.datetime.now().year
    return [f"{year}-{year + 1}" for year in range(current_year - num_years, current_year + 1)]