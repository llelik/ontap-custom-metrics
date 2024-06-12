#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'duration_to_seconds': self.duration_to_seconds,
        }

    def duration_to_seconds(duration):
        # Remove the 'PT' prefix from the duration string
        duration = duration[2:]
        
        # Initialize variables to store the extracted values
        years = 0
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
        
        # Extract the values for years, days, hours, minutes, and seconds
        if 'Y' in duration:
            years_index = duration.index('Y')
            years = int(duration[:years_index])
            duration = duration[years_index+1:]
        
        if 'D' in duration:
            days_index = duration.index('D')
            days = int(duration[:days_index])
            duration = duration[days_index+1:]
        
        if 'H' in duration:
            hours_index = duration.index('H')
            hours = int(duration[:hours_index])
            duration = duration[hours_index+1:]
        
        if 'M' in duration:
            minutes_index = duration.index('M')
            minutes = int(duration[:minutes_index])
            duration = duration[minutes_index+1:]
        
        if 'S' in duration:
            seconds_index = duration.index('S')
            seconds = int(duration[:seconds_index])
        
        # Calculate the total duration in seconds
        total_seconds = (
            years * 365 * 24 * 60 * 60 +
            days * 24 * 60 * 60 +
            hours * 60 * 60 +
            minutes * 60 +
            seconds
        )
        
        return total_seconds

             