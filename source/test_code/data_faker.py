import random

import numpy as np
import pandas as pd
import names


scores = [i for i in np.arange(4, 10.5, 0.5)]

class_list = {'Alpha': [0.2, 0.01],
              'Bravo': [0.3, 0.01],
              'Charlie': [0.5, 0.01],
              'Delta': [0.4, 0.02],
              'Echo': [0.1, 0.02]}

class_students = {
                k: [names.get_full_name() for i in range(50)]
                for k in class_list
}


def random_score(low_percentage, na_percentage):
    if random.random() < na_percentage:
        return None
    else:
        if random.random() < low_percentage:
            return random.choice(scores[:7])
        else:
            return random.choice(scores[7:])


def generate_score():
    data = []
    for class_name in class_students:
        for name in class_students[class_name]:
            data.append([
                        name,
                        class_name,
                        # Math Score
                        random_score(class_list[class_name][0],
                                     class_list[class_name][1]),
                        # English Score
                        random_score(class_list[class_name][0],
                                     class_list[class_name][1]),
                        # Science Score
                        random_score(class_list[class_name][0],
                                     class_list[class_name][1]),
                        ])
    return data


dataframe = pd.DataFrame(generate_score(), columns=['Name', 'Class',
                                                    'Math', 'English',
                                                    'Science'])
dataframe.to_excel('students_score.xlsx')
