School Management System: Inheritance and Data Validation

🌟 Overview: 

Object-Oriented School StructureThis project demonstrates the core Object-Oriented Programming (OOP) principle of Inheritance in Python. We establish a hierarchical structure starting with a base School class, which manages fundamental properties and validation logic.Specialized classes, like ElementarySchool and HighSchool, then inherit all the robust features of the parent class while adding their own unique attributes and methods (e.g., has_makerspace or requires_thesis).The structure ensures:Code Reusability: Student count validation (setNumberOfStudents) only needs to be defined once in the parent School class.Consistency: All derived schools automatically adhere to the same non-negative student count rule.Specialization: Subclasses can be extended with unique features relevant to their educational level.

🛠️ Installation and UsagePrerequisitesThis is a pure Python implementation and requires only a standard Python 3 environment.

Code Structure (Inheritance)The base School class contains the shared validation logic:class School:

    def __init__(self, name, numberOfStudents=0):
        # ... validation logic ...
        self.setNumberOfStudents(numberOfStudents)
        
    # The dedicated setter method enforcing validation
    def setNumberOfStudents(self, new_number):
        if not isinstance(new_number, int):
            raise TypeError("The number of students must be an integer.")
            
        if new_number < 0:
            raise ValueError("Number of students cannot be negative.")
        
        self.numberOfStudents = new_numbe
        
        # ... other methods like getNumberOfStudents() and __repr__ ...


Example

The example below demonstrates how the validation logic (defined in the parent School class) is automatically inherited and used by the HighSchool subclass, along with calling a specialized method:# Create an instance of the specialized class
high_school = HighSchool("Technology Academy", 800)

# 1. Validation (Inherited from School)
try:
    high_school.setNumberOfStudents(820)
    print(f"Update successful: {high_school.getNumberOfStudents()} students.")
    
    #
    try:
        high_school.setNumberOfStudents(820)
        print(f"Update successful: {high_school.getNumberOfStudents()} students.")
    #2. Specialization (Method defined only in HighSchool)
        print(high_school.get_level_info())
    
    # 3. Validation failure (Inherited, fails gracefully)
        high_school.setNumberOfStudents(-10)
        except ValueError as e:
        print(f"\nERROR: {e}") 


🤝 ContributingContributions are welcome! If you have suggestions for additional validation checks (e.g., maximum class size limits) or improvements to the documentation, please open an issue or submit a pull request.📄 LicenseThis project is licensed under the MIT License - see the LICENSE file for details.
