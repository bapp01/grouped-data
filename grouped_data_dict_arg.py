class table:
    """
    creating a table
    data = table({"1-5": 2, "6-10": 9, "11-15": 15, "16-20": 20, "21-25": 17, "26-30": 25, "31-35": 2, "36-40": 1})


    The inputs from the variable data should look like this:
    -------------------------------
    | Class Intervals | Frequency |
    |-----------------|-----------|
    |      1-5        |     2     |
    |-----------------|-----------|
    |      6-10       |     9     |
    |-----------------|-----------|
    |      11-15      |     15    |
    |-----------------|-----------|
    |      16-20      |     20    |
    |-----------------|-----------|
    |      21-25      |     17    |
    |-----------------|-----------|
    |      26-30      |     25    |
    |-----------------|-----------|
    |      31-35      |     2     |
    |-----------------|-----------|
    |      36-40      |     1     |
    |-----------------------------|


    Calculations:

    calculating the mean of the table
    data.mean() \\ Output: 20.087912087912088

    calculating the median of the tabke
    data.median() \\ Output: 20.375

    calculating the percentile of the table (default value is 50)
    data.percentile(25) \\ Output: 14.416666666666666

    calculating the decile of the table (default value is 5)
    data.decile(3) \\ Output: 15.825

    calculating the quartile (default value is 2)
    data.quartile(1) \\ Output: 14.416666666666666

    calculating the percentile rank
    data.percentileRank(25) \\ Output: 62.3989010989011

    getting the midpoints of the table
    data.midpoint \\ Output: [3.0, 8.0, 13.0, 18.0, 23.0, 28.0, 33.0, 38.0]

    getting the frequencies x midpoint of the table
    data.fx \\ Output: [6.0, 72.0, 195.0, 360.0, 391.0, 700.0, 66.0, 38.0]

    getting the lower boundaries of the table
    data.lowerBoundaries \\ Output: [0.5, 5.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5]

    getting the cumulative frequencies of the table 
    data.cumulativeFrequencies \\ Output: [2, 11, 26, 46, 63, 88, 90, 91]

    getting the summation of the frequencies 
    data.N \\ Output: 91
    """
    def __init__(self, dictTable):
        self.cumulativeFrequencies = []
        self.frequencies = list(dictTable.values())
        self.classIntervals = [list(map(int, i.split('-'))) for i in list(dictTable)]
        if len(self.frequencies) != len(self.classIntervals):
            raise Exception("frequencies and classIntervals must have the same length")
        elif len(self.frequencies) == 1 and len(self.classIntervals) == 1:
            raise Exception("frequency and classIntervals must have a length greater than 1")
        else:
            self.rows = len(self.frequencies)

        self.interval = (self.classIntervals[0][1] - self.classIntervals[0][0]) + 1
        self.N = sum(self.frequencies)

        #Midpoint
        self.midpoint = [(i[0] + i[1]) / 2 for i in self.classIntervals]

        # fx
        self.fx = [mid * freq for mid, freq in zip(self.midpoint, self.frequencies)]

        #Lower Boundaries
        self.lowerBoundaries = [(j[0] + (self.classIntervals[0][0] - (self.classIntervals[-1][0] - self.classIntervals[-2][1]))) / 2 if i == 0 else (self.classIntervals[i-1][1] + j[0)) / 2 for i, j in enumerate(self.classIntervals)]

        # Cumulative Frequencies
        for i in range(self.rows):
            if i == 1:
                self.cumulativeFrequencies.append(self.frequencies[i-1] + self.frequencies[i])
            elif i >= 2:
                self.cumulativeFrequencies.append(self.frequencies[i] + self.cumulativeFrequencies[i-1])
            else:
                self.cumulativeFrequencies.append(self.frequencies[i])

    def percentileRank(self, P):
        for i, j in enumerate(self.classIntervals):
            if P >= j[0] and P <= j[1]:
                break
        return ((((P - self.lowerBoundaries[i]) * self.frequencies[i]) / self.interval) + self.cumulativeFrequencies[i - 1]) + (100/self.N)
 
    def percentile(self, k=50):
        if k > 99:
            raise Exception("k must not be higher than 99")
        else:
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
        return sum(self.fx) / self.N
    
    # I have to admit that this code was from ChatGPT
    def median(self):
        middlePosition = self.N / 2
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
