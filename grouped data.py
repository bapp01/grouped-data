class table:
    """
    creating a table
    data = table(classIntervals=["1-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40"], frequencies=[2,9,15,20,17,25,2,1])

    calculating the mean of the table
    data.mean()

    calculating the median of the tabke
    data.median()

    calculating the percentile of the table (default value is 50)
    data.percentile(25)

    calculating the decile of the table (default value is 5)
    data.decile(3)

    calculating the quartile (default value is 2)
    data.quartile(1)

    getting the midpoints of the table
    data.midpoint

    getting the frequencies x midpoint of the table
    data.fx

    getting the lower boundaries of the table
    data.lowerBoundaries

    getting the cumulative frequencies of the table 
    data.cumulativeFrequencies

    getting the summation of the frequencies 
    data.N
    """
    def __init__(self, classIntervals, frequencies):
        cumulativeFrequencies = []
        lowerBoundaries = []
        midpoint = []
        fx  = []
        self.fx = fx 
        self.midpoint = midpoint
        self.lowerBoundaries = lowerBoundaries
        self.cumulativeFrequencies = cumulativeFrequencies
        self.frequencies = frequencies
        self.classIntervals = classIntervals
        if len(frequencies) != len(classIntervals):
            raise Exception("frequencies and classIntervals must have the same length")
        elif len(frequencies) == 1 and len(classIntervals) == 1:
            raise Exception("frequency and classIntervals must have a length greater than 1")
        else:
            self.rows = len(frequencies)
        
        self.classIntervals = [i.replace(" ", "") for i in classIntervals]

        self.interval = (int(classIntervals[0][(classIntervals[0].find('-') + 1):]) - int(classIntervals[0][0:classIntervals[0].find('-')])) + 1
        self.N = sum(frequencies)

        intervalBefore = int(classIntervals[0][0:classIntervals[0].find('-')]) - (int(classIntervals[-1][0:classIntervals[-1].find('-')]) - int(classIntervals[-2][classIntervals[-2].find('-') + 1:]))

        #Midpoint
        for i in range(self.rows):
            midpoint.append((int(classIntervals[i][0:classIntervals[i].find('-')]) + int(classIntervals[i][classIntervals[i].find('-')+1:])) / 2)

        #fx
        for i in range(self.rows):
            fx.append(midpoint[i] * frequencies[i])


        #Lower Boundaries
        for i in range(self.rows):
            if i == 0:
                lowerBoundaries.append((int(classIntervals[i][0:classIntervals[i].find('-')]) + intervalBefore) / 2)
                # lowerBoundaries.append((int(classIntervals[i][0:classIntervals[i].find('-')]) + intervalBefore) / 2)

            else:
                lowerBoundaries.append((int(classIntervals[i-1][classIntervals[i-1].find('-')+1:]) + int(classIntervals[i][0:classIntervals[i].find('-')]))/ 2)

        #Cumulative Frequencies
        for i in range(self.rows):
            if i == 1:
                cumulativeFrequencies.append(frequencies[i-1] + frequencies[i])
            elif i >= 2:
                cumulativeFrequencies.append(frequencies[i] + cumulativeFrequencies[i-1])
            else:
                cumulativeFrequencies.append(frequencies[i])
            
    def percentile(self, k=50):
        if k > 99:
            raise Exception("k must not be higher than 99")
        else:
            pass
        KN100 = (k * self.N) / 100
        for i in range(self.rows):
            if KN100 <= self.cumulativeFrequencies[i]:
                if i == 0:
                    cfb = i
                else:
                    cfb = self.cumulativeFrequencies[i-1]
                LB = self.lowerBoundaries[i]
                f = self.frequencies[i]
                break
            else:
                pass
        return (((KN100 - cfb) / f) * self.interval) + LB 

    def decile(self, k=5):
        if k > 9:
            raise Exception("k must not be higher than 9")
        else:
            pass
        KN10 = (k * self.N) / 10
        for i in range(self.rows):
            if KN10 <= self.cumulativeFrequencies[i]:
                cfb = self.cumulativeFrequencies[i-1]
                LB = self.lowerBoundaries[i]
                f = self.frequencies[i]
                break
            else:
                pass
        return (((KN10 - cfb) / f) * self.interval) + LB 
    
    def quartile(self, k=2):
        if k > 3:
            raise Exception("k must not be higher than 3")
        else:
            pass
        KN4 = (k * self.N) / 4
        for i in range(self.rows):
            if KN4 <= self.cumulativeFrequencies[i]:
                cfb = self.cumulativeFrequencies[i-1]
                LB = self.lowerBoundaries[i]
                f = self.frequencies[i]
                break
            else:
                pass
        return (((KN4 - cfb) / f) * self.interval) + LB 
    
    def mean(self):
        return sum(self.fx) / sum(self.frequencies)
    
    # I have to admit that this code was from ChatGPT
    def median(self):
        N = sum(self.frequencies)
        middlePosition = N / 2
        cf = 0
        medianIntervalIndex = -1

        for i, frequency in enumerate(self.frequencies):
            cf += frequency
            if cf >= middlePosition:
                medianIntervalIndex = i
                break
        LB = self.lowerBoundaries[medianIntervalIndex]
        frequencyToReach = middlePosition - (cf - frequency)
        return LB + ((frequencyToReach / frequency) * self.interval)

data1 = table(["30-39", "40-49 ", "50-59", "60-69", "70-79", "80-89", "90-99"], [3, 5, 8, 11, 6, 4, 3])
print(data1.mean())
