# Advanced Student Grade Predictor (Excellence Level)

def get_grade_by_marks(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F (Fail)"

def main():
    print("*******************************************")
    print("   Welcome to the Excellence Grade System   ")
    print("*******************************************\n")

    # Input: Marks
    try:
        marks = float(input("Apne Total Marks enter karein (out of 100): "))
        if not (0 <= marks <= 100):
            raise ValueError("Marks 0 aur 100 ke beech hone chahiye.")
        
        # Input: Attendance (Adding a professional touch)
        attendance = float(input("Apni Attendance Percentage enter karein (0-100): "))
        if not (0 <= attendance <= 100):
            raise ValueError("Attendance 0 aur 100 ke beech honi chahiye.")

    except ValueError as e:
        print(f"\n❌ Error: {e}. Kripya sahi input dalein.")
        return

    # Calculate Base Grade
    grade = get_grade_by_marks(marks)

    # Check Attendance Criteria (Minimum 75% required for full marks)
    if attendance < 75:
        print("\n⚠️ Warning: Attendance kam hone ki wajah se grade downgrade kiya ja raha hai.")
        if grade != "F (Fail)":
             # Simple logic: downgrade by 1 step if not already F
             grades_list = ["F (Fail)", "D", "C", "B", "A", "A+"]
             current_grade_index = grades_list.index(grade)
             if current_grade_index > 0:
                 grade = grades_list[current_grade_index - 1]
        else:
            print("   Attendance kam hai, lekin marks pehle hi F hain.")

    # Final Output
    print("\n-------------------------------------------")
    print(f"Results for {name_of_student if 'name_of_student' in locals() else 'Student'}:")
    print(f"  - Marks: {marks}/100")
    print(f"  - Attendance: {attendance}%")
    print(f"  - Final Calculated Grade: **{grade}**")
    print("-------------------------------------------\n")
    print("--- Program Ended Successfully ---\n")

if __name__ == "__main__":
    # Optional: Add an input for student name
    name_of_student = input("Apna naam enter karein: ")
    main()
