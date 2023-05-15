
def percentchange(x, y):
    try:
        return ((x - y)*100/y)
    except ZeroDivisionError:
        return 0
#calculate real and percent change between all columns for all possible time frames
def calculate_changes(df, columns, time_frames, years):
    for column in columns:
        for time_frame in time_frames:
            start_year, end_year = time_frame.split('-')
            df[f'{column} % Change', 'None', f'{time_frame}'] = percentchange(df[(column, int(end_year), 'None')], df[(column, int(start_year), 'None')])
            df[f'{column} Change', 'None', f'{time_frame}'] = (df[(column, int(end_year), 'None')] - df[(column, int(start_year), 'None')])

    return df
#generate all possible time frames from a list of years
def generate_time_frames(years):
    time_frames = []
    for i in range(len(years)-1):
        for j in range(i+1, len(years)):
            time_frames.append(f"{years[i]}-{years[j]}")
    return time_frames
