""""Module with class Student"""


class Student:
    """Student class"""
    def __init__(self, name, conf):
        self.__name = name
        self.__exam_max = conf['exam_max']
        self.__exam = 0
        self.__lab_max = conf['lab_max']
        self.__lab_num = conf['lab_num']
        self.__points = [0 for i in range(self.__lab_num)]
        self.__additional_points = []
        # number of attempts to pass the lab and exam
        self.__attempt_max = 3
        self.__exam_attempt = 0
        self.__labs_attempts = [0 for i in range(self.__lab_num)]
        self.__k = conf['k']

    def make_lab(self, attempt_points, lab=-1):
        """Adds points for accomplished lab"""
        if attempt_points > self.__lab_max:
            attempt_points = self.__lab_max
        if 0 < lab < self.__lab_num and self.__labs_attempts[lab - 1] < self.__attempt_max:
            self.__points[lab - 1] = attempt_points
            self.__labs_attempts[lab - 1] += 1
        elif lab == -1:
            for i in range(self.__attempt_max):
                if self.__labs_attempts[i] == 0:
                    self.__points[i] = attempt_points
                    self.__labs_attempts[i] += 1
                    break
        elif lab >= self.__lab_num:
            self.__additional_points.append(attempt_points)
        return self

    def make_exam(self, exam_points):
        """Adds final exam mark"""
        if exam_points > self.__exam_max:
            exam_points = self.__exam_max
        if self.__exam_attempt <= self.__attempt_max:
            self.__exam_attempt += 1
            self.__exam = exam_points
        return self

    def is_certified(self):
        """Returns amount of points for course and result"""
        points_sum = 0
        for lab_points in self.__points:
            points_sum += lab_points
        points_sum += self.__exam
        if points_sum >= (self.__exam_max + (self.__lab_num * self.__lab_max))*self.__k:
            return points_sum, True
        return points_sum, False

    def __str__(self):
        return "Student's __name: {} \n"\
               "Points for exam:  {} \n" \
               "Points for labs: {} \n" \
               "Additional points for tasks: {}"\
            .format(self.__name, self.__exam, self.__points, self.__additional_points)
