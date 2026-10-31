class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        ad=0
        for i in range(len(seats)):
            ad+=abs(seats[i]-students[i])
        return ad