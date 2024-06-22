import streamlit as st

def calculate_sgpa(semester, subjects, credits):
    st.title("SGPA Calculator 2021 Scheme")
    
    if semester < 1 or semester > 8:
        st.write("Semester yet to come ;)")
        return
    
    st.header(f"Calculating SGPA for Semester {semester}")
    
    marks = []
    for subject, credit in zip(subjects, credits):
        mark = st.number_input(f"{subject} - Enter marks", min_value=0, max_value=100, step=1)
        marks.append(mark)
    
    grade_points = []
    for mark in marks:
        if mark in range(90, 101):
            grade_points.append(10)
        elif mark in range(80, 90):
            grade_points.append(9)
        elif mark in range(70, 80):
            grade_points.append(8)
        elif mark in range(60, 70):
            grade_points.append(7)
        elif mark in range(55, 60):
            grade_points.append(6)
        elif mark in range(50, 55):
            grade_points.append(5)
        elif mark in range(40, 50):
            grade_points.append(4)
        else:
            grade_points.append(0)
    
    weighted_sum = sum(gp * credit for gp, credit in zip(grade_points, credits))
    total_credits = sum(credits)
    sgpa = weighted_sum / total_credits
    
    st.success(f"Your SGPA for semester {semester} is {round(sgpa, 2)}")

def main():
    semester = st.number_input(
        "Which semester's SGPA do you want to calculate?",
        min_value=1,
        max_value=8,
        step=1
    )
    
    if semester == 1:
        subjects = [
            "21MAT11 - Calculus and Differential Equations",
            "21PHY12 - Engineering Physics",
            "21ELE13 - Basic Electrical Engineering",
            "21CIV14 - Elements of Civil Engineering and Mechanics",
            "21EVN15 - Engineering Visualization",
            "21PHYL16 - Engineering Physics Laboratory",
            "21ELEL17 - Basic Electrical Engineering Laboratory",
            "21EGH18 - Communicative English",
            "21IDT19 - Innovation and Design Thinking"
        ]
        credits = [3, 3, 3, 3, 3, 1, 1, 2, 1]
        calculate_sgpa(semester, subjects, credits)
    
    elif semester == 2:
        subjects = [
            "21MAT21 - Advanced Calculus and Numerical Methods",
            "21CHE22 - Engineering Chemistry",
            "21PSP23 - Problem solving through programming",
            "21ELN24 - Basic Electronics & Communication Engineering",
            "21EME25 - Elements of Mechanical Engineering",
            "21CHEL26 - Engineering Chemistry Laboratory",
            "21CPLL27 - Computer Programming Laboratory",
            "21EGH28 - Professional Writing skills in English",
            "21SFH9 - Scientific Foundations of Health"
        ]
        credits = [3, 3, 3, 3, 3, 1, 1, 2, 1]
        calculate_sgpa(semester, subjects, credits)
    
    elif semester == 3:
        subjects = [
            "21MAT31 - Transform Calculus, Fourier Series and Numerical Techniques",
            "21CS32 - Data Structures and Algorithm",
            "21CS33 - Analog and Digital Electronics",
            "21CS34 - Computer Organization and Architecture",
            "21CSL35 - Object Oriented Programming with JAVA Laboratory",
            "21UH36 - Social Connect and Responsibility",
            "21CIP37 - Constitution of India and Professional Ethics",
            "21CSL381 - Mastering Office"
        ]
        credits = [3, 4, 4, 3, 1, 1, 1, 1]
        calculate_sgpa(semester, subjects, credits)
    
    elif semester == 4:
        subjects = [
            "21CS41 - Mathematical Foundations for Computing",
            "21CS42 - Design and Analysis of Algorithms",
            "21CS43 - Microcontroller and Embedded Systems",
            "21CS44 - Operating Systems",
            "21BE5 - Biology For Engineers",
            "21KSK/KBK46 - Samskrutika/Balake Kannada",
            "21CSL481 - Web Programming",
            "21UH49 - Universal Human Values",
            "21INT49 - Inter/Intra Institutional Internship"
        ]
        credits = [3, 4, 4, 3, 2, 1, 1, 1, 1]
        calculate_sgpa(semester, subjects, credits)

    elif semester == 5:
        subjects = [
            "21CS51 - Automata Theory and Compiler Design",
            "21CS52 - Computer Networks",
            "21CS53 - Database Management Systems",
            "21CS54 - Artificial Intelligence and Machine Learning",
            "21CSL55 - Database Management Systems Laboratory with Mini Project",
            "21RMI56 - Research Methodology & Intellectual Property Rights",
            "21CIV57 - Environmental Studies",
            "21CSL581 - Angular JS and Node JS"
        ]
        credits = [3,4,3,3,1,2,1,1]
        calculate_sgpa(semester, subjects, credits)
    
    elif semester == 6:
        subjects = [
            "21CS61 - Software Engineering & Project Management",
            "21CS62 - Fullstack Development",
            "21CS63 - Computer Graphics and Fundamental of Image Processing",
            "21CS644 - Data Science and Visualization",
            "21CS642 - Advance JAVA Programming",
            "21ME652 - Renewable Energy Power Plants",
            "21CIV - Traffic Engineering",
            "21CSL66 - Computer Graphics and Image Processing Laboratory",
            "21CSMP67 - Mini Project",
            "21INT68 - Innovation/Entrepreneurship/Societal Internship",
        ]
        credits = [3,4,3,3,3,3,3,1,2,3]
        calculate_sgpa(semester, subjects, credits)

    else:
        st.write("Semester yet to come ;)")

if __name__ == "__main__":
    main()