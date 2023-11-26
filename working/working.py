import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    #LOOKING FOR A MATCH
    if match:=re.search(r'([0-9]{1,2}):?([0-9]{2})? (AM|PM) to ([0-9]{1,2}):?([0-9]{2})? (AM|PM)',s):

        #MAPPING OUT A TIME COMPONENTS TO VARIABLES
        startHour=int(match.group(1))
        try:
            startMin=int(match.group(2))
        except (TypeError,ValueError):
            startMin=0

        startDT=match.group(3)

        endHour=int(match.group(4))

        try:
            endMin=int(match.group(5))
        except (TypeError,ValueError):
            endMin=0

        endDT=match.group(6)

        # FORMATTING TIME FORMAT

        if startHour in range(1,13) and endHour in range(1,13) and startMin in range(0,60) and endMin in range(0,60):
            if startDT=="PM":
                startHour +=12
                if startHour==24:
                    startHour=12
            elif startDT=="AM":
                if startHour==12:
                    startHour=0
            else:
                raise ValueError
#
            if endDT=="PM":
                endHour +=12
                if endHour==24:
                    endHour=12
            elif endDT=="AM":
                if endHour==12:
                    endHour=0
            else:
                raise ValueError

            # PRINTING OUT FORMATED STRING

            return(f"{startHour:02d}:{startMin:02d} to {endHour:02d}:{endMin:02d}")
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()

