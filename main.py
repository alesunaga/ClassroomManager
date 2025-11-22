class School:
    """
    Base class for all educational institutions. 
    It manages core properties like name and student count validation.
    """
    def __init__(self, name, numberOfStudents=0):
        self.name = name
        # The student count attribute is set through the setter method 
        # to ensure initial validation.
        self.setNumberOfStudents(numberOfStudents)
        
    def getNumberOfStudents(self):
        """Getter method: Returns the current number of students."""
        return self.numberOfStudents
    
    def setNumberOfStudents(self, new_number):
        """
        Setter method: Validates and sets the number of students.
        Raises ValueError if the number is negative.
        """
        if not isinstance(new_number, int):
            raise TypeError("The number of students must be an integer.")
            
        if new_number < 0:
            # Raising an exception is the best practice for validation failure
            raise ValueError("Number of students cannot be negative.")
        
        self.numberOfStudents = new_number

    def __repr__(self):
        """String representation of the School object."""
        return f"{self.name} | Type: {self.__class__.__name__} | Students: {self.numberOfStudents}"


class ElementarySchool(School):
    """
    Subclass for elementary education (inherits validation from School).
    """
    def __init__(self, name, numberOfStudents=0, has_makerspace=True):
        super().__init__(name, numberOfStudents)
        self.level = "Elementary"
        self.has_makerspace = has_makerspace
    
    def get_level_info(self):
        return f"{self.name} is an {self.level} school. Makerspace available: {self.has_makerspace}"


class HighSchool(School):
    """
    Subclass for secondary education (inherits validation from School).
    """
    def __init__(self, name, numberOfStudents=0, requires_thesis=True):
        super().__init__(name, numberOfStudents)
        self.level = "High School"
        self.requires_thesis = requires_thesis
    
    def get_level_info(self):
        return f"{self.name} is a {self.level}. Thesis required for graduation: {self.requires_thesis}"

# --- Example Usage ---
# 1. Create instances of the subclasses
elementary = ElementarySchool("Innovation Hub", 450)
high_school = HighSchool("Technology Academy", 800, requires_thesis=False)

# 2. Test inherited methods (validation and getter)
try:
    high_school.setNumberOfStudents(820)
    print(high_school)
    
    # 3. Test specialized methods
    print(elementary.get_level_info())
    
    # 4. Test validation failure (inherited)
    elementary.setNumberOfStudents(-10) 
    
except ValueError as e:
    print(f"\nError: {e}")
