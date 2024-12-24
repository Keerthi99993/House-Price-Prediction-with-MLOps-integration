from abc import ABC,abstractmethod

#step1 :create an abstract base class
class DiningExperience(ABC):
    
    #the template method defining the skeleton of the dining8
    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage()
        
    #abstract methods to serve each course (to be implemented
    @abstractmethod
    def serve_appetizer(self):
        pass

    @abstractmethod
    def serve_main_course(self):
        pass

    @abstractmethod
    def serve_dessert(self):
        pass

    @abstractmethod
    def serve_beverage(self):
        pass

#step 2: create concrete classes that implements the template
class ItalianDinner(DiningExperience):
    def serve_appetizer(self):
        print("Serving bruschetta as appetizer")

    def serve_main_course(self):
        print("SErving pasta as the main course")

    def serve_dessert(self):
        print("Serving tiramisu as dessert")

    def serve_beverage(self):
        print("Serving wine as the beverage")



class ChineseDinner(DiningExperience):
    def serve_appetizer(self):
        print("Serving spring roolls as appetizer")

    def serve_main_course(self):
        print("SErving stir-fried noodles as the main course")

    def serve_dessert(self):
        print("Serving fortune cookies as dessert")

    def serve_beverage(self):
        print("Serving tea as the beverage")



#step 3:Client code
if __name__=="__main__":
    print("Itakian Dinner:")
    italian_dinner=ItalianDinner()
    italian_dinner.serve_dinner()

    print("\n Chinese Dinner:")
    chinese_dinner=ItalianDinner()
    chinese_dinner.serve_dinner()

    

