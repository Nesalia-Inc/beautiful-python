from typing import NamedTuple, override

from dataclasses import dataclass
from enum import Enum, auto


""" 

Dans cette vidéo, on va voir un des élément qui cause le plus de problème dans ton code et on va voir étape par étape comment le résoudre à l'aide d'un exemple. 

L'une des plus grande cause d'un code de mauvaise qualité sont les fonctions et les méthodes qui ont trop de lignes et ont plusieurs rôles. 

Quand une fonction fait plusieurs choses en même temps, elle devient compliquée à comprendre et à maintenir. La règle que je suis toujours qui s'appelle le Single Responsibility Principle est que chacune de mes fonctions doit faire uniquement une chose et la faire correctement. 

1. Commencer par expliquer l'exemple
2. Créer les classes Subject, Grade et Student 
3. Ajouter les deux méthodes dans la classe Student 
4. Créer la classe AverageGetter
5. Créer la fonction get_best_student
6. Créer la page de rapport 


"""


class Subject(Enum):
    MATH = auto()
    SCIENCE = auto()
    LITERATURE = auto()


class Grade(NamedTuple):
    subject : Subject
    results : int


@dataclass(frozen=True)
class Student:
    name : str 
    grades : list[Grade]
    
    
    def has_subject(self, subject : Subject) -> bool:
        student_subjects = [grade.subject for grade in self.grades]
        
        return subject in student_subjects
    
    def get_grade(self, subject : Subject) -> Grade:
        for grade in self.grades:
            if grade.subject == subject:
                return grade 
            
        raise ValueError
    
    
    

class AverageGetter:
    def _get_students_count_in_subject(self, students : list[Student], subject : Subject) -> int:
        return sum([student.has_subject(subject) for student in students])
    
    def _get_students_total_in_subject(self, students : list[Student], subject : Subject) -> float:
        total = 0
        
        for student in students:
            if student.has_subject(subject):
                total += student.get_grade(subject).results
                
        return total
    
    def get_multiple_students_average(self, students : list[Student], subject : Subject) -> float:
        total = self._get_students_total_in_subject(students, subject)
        count = self._get_students_count_in_subject(students, subject)
        
        return total / count if count > 0 else 0



class BestStudentGetter:
    def get_best_student_in_subject(self, students : list[Student], subject : Subject) -> Student:
        best_student = max(students, key=lambda student: student.get_grade(subject).results)
        return best_student
    
    
    


class Rapport:
    def __init__(self) -> None:
        self._message = ""
        
    
    def __str__(self) -> str:
        return self._message
        
    
    def _add_average_score(self, average : float, subject : Subject) -> str:
        return f"Average score in {subject.name.capitalize()}: {average:.2f}\n"
    
    def _add_best_student(self, best_student : Student, subject : Subject) -> str:
        return f"Best student in {subject.name.capitalize()}: {best_student.name} with score {best_student.get_grade(subject).results}\n"
    
    
    @classmethod
    def build(cls, average : float, best_student : Student, subject : Subject) -> "Rapport":
        rapport = cls()
        rapport._message += cls._add_average_score(rapport, average, subject)
        rapport._message += cls._add_best_student(rapport, best_student, subject)
        
        return rapport
    
    
    
class BasicRapportBuilder:
    @classmethod
    def build(cls, subject : Subject) -> "Rapport":
        average = AverageGetter().get_multiple_students_average(students, Subject.MATH)
        best_student = BestStudentGetter().get_best_student_in_subject(students, Subject.MATH)
        
        return Rapport.build(average, best_student, subject)



def create_rapport(average : float, best_student : Student, subject : Subject) -> str:
    summary = f"Average score in {subject.name.capitalize()}: {average:.2f}\n"
    summary += f"Best student in {subject.name.capitalize()}: {best_student.name} with score {best_student.get_grade(subject).results}\n"
    
    return summary




if __name__ == '__main__':
    students = [Student("Bob", [Grade(Subject.MATH, 90), Grade(Subject.SCIENCE, 88), Grade(Subject.LITERATURE, 82)]),
                Student("Alice", [Grade(Subject.MATH, 85), Grade(Subject.SCIENCE, 88), Grade(Subject.LITERATURE, 82)]),
                Student("Charlie", [Grade(Subject.MATH, 95), Grade(Subject.SCIENCE, 88), Grade(Subject.LITERATURE, 82)])]
    
    print(AverageGetter().get_multiple_students_average(students, Subject.MATH))
    print(BestStudentGetter().get_best_student_in_subject(students, Subject.MATH))
    
    print(BasicRapportBuilder.build(Subject.MATH))