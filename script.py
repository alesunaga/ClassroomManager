class ClassroomManager:
    """
    Manages student count for a class, ensuring the number is non-negative.
    """
    def __init__(self, name, student_count=0):
        self.name = name
        # Use an underscore (_) to denote a protected attribute, 
        # which is managed by the property methods.
        self._number_of_students = student_count 
    
    @property
    def number_of_students(self):
        """Getter: Returns the current number of students."""
        return self._number_of_students
    
    @number_of_students.setter
    def number_of_students(self, new_number):
        """
        Setter: Validates and sets the number of students.
        Raises ValueError if the number is negative.
        """
        # Optional: Add type checking for robustness
        if not isinstance(new_number, int):
            raise TypeError("The number of students must be an integer.")
            
        if new_number < 0:
            # Raise an exception instead of just printing a message
            raise ValueError("The number of students cannot be negative.")
        
        self._number_of_students = new_number

# --- Example Usage ---
try:
    # 1. Successful assignment
    makerspace_class = ClassroomManager("Makerspace")
    makerspace_class.number_of_students = 25  
    print(f"Class '{makerspace_class.name}' updated: {makerspace_class.number_of_students} students.")
    
    # 2. Assignment resulting in a ValueError
    print("\nAttempting to set a negative number...")
    makerspace_class.number_of_students = -5  
    
except ValueError as e:
    print(f"Validation Error Caught: {e}") 
except TypeError as e:
    print(f"Type Error Caught: {e}")
