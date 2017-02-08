def decimalDegrees2DMS(value,type):
    """
        Converts a Decimal Degree Value into
        Degrees Minute Seconds Notation.
        
        Pass value as double
        type = {Latitude or Longitude} as string
        
        returns a string as D°M'S"Direction
        created by: anothergisblog.blogspot.com 
    """
    degrees = int(value)
    submin = abs( (value - int(value) ) * 60)
    minutes = int(submin)
    subseconds = abs((submin-int(submin)) * 60)
    direction = ""
    if type == "Longitude":
        if degrees < 0:
            direction = "W"
        elif degrees > 0:
            direction = "E"
        else:
            direction = ""
    elif type == "Latitude":
        if degrees < 0:
            direction = "S"
        elif degrees > 0:
            direction = "N"
        else:
            direction = "" 
    notation = str(degrees) + "°" + str(minutes) + "'" +\
               str(subseconds)[0:5] + "'"+"'" + direction
    return notation