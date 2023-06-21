class table:
    """
    creating a table
    data = table(classIntervals=["1-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40"], frequencies=[2,9,15,20,17,25,2,1])

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
    def __init__(self, classIntervals, frequencies):
        cumulativeFrequencies = []
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


        self.interval = (int(classIntervals[0].split('-')[1]) - int(classIntervals[0].split('-')[0]) + 1)
        self.N = sum(frequencies)

        #Midpoint
        self.midpoint = [(int(interval.split('-')[0]) + int(interval.split('-')[1])) / 2 for interval in self.classIntervals]

        # fx
        self.fx = [mid * freq for mid, freq in zip(self.midpoint, self.frequencies)]

        #Lower Boundaries
        self.lowerBoundaries = [(int(interval.split('-')[0]) + (int(self.classIntervals[0].split('-')[0]) - (int(self.classIntervals[-1].split('-')[0]) - int(self.classIntervals[-2].split('-')[1])))) / 2 if i == 0 else (int(self.classIntervals[i-1].split('-')[1]) + int(interval.split('-')[0])) / 2 for i, interval in enumerate(self.classIntervals)]

        # Cumulative Frequencies
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
