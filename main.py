import streamlit as st
st.title("SGPA Calculator 2021 Scheme")

semester = st.number_input(
    "_Which semester's SGPA do you want to calculate?_",
    min_value=1,
    max_value=8,
    step=1
)

if semester == 1:
    a = st.number_input("21MAT11 - Calculus and Differential Equations", min_value=0, max_value=100, step=1)
    b = st.number_input("21PHY12 - Engineering Physics", min_value=0, max_value=100, step=1)
    c = st.number_input("21ELE13 - Basic Electrical Engineering", min_value=0, max_value=100, step=1)
    d = st.number_input("21CIV14 - Elements of Civil Engineering and Mechanics", min_value=0, max_value=100, step=1)
    e = st.number_input("21EVN15 - Engineering Visualization", min_value=0, max_value=100, step=1)
    f = st.number_input("21PHYL16 - Engineering Physics Laboratory", min_value=0, max_value=100, step=1)
    g = st.number_input("21ELEL17 - Basic Electrical Engineering Laboratory", min_value=0, max_value=100, step=1)
    h = st.number_input("21EGH18 - Communicative English", min_value=0, max_value=100, step=1)
    j = st.number_input("21IDT19 - Innovation and Design Thinking", min_value=0, max_value=100, step=1)
    marks = [a, b, c, d, e, f, g, h, j]
    grade_point = []
    for i in marks:
        if i in range(90, 101):
            grade_point.append(10)
        elif i in range(80, 90):
            grade_point.append(9)
        elif i in range(70, 80):
            grade_point.append(8)
        elif i in range(60, 70):
            grade_point.append(7)
        elif i in range(55, 60):
            grade_point.append(6)
        elif i in range(50, 55):
            grade_point.append(5)
        elif i in range(40, 50):
            grade_point.append(4)
        else:
            grade_point.append(0)
    sgpa = (grade_point[0] * 3 + grade_point[1] * 3 + grade_point[2] * 3 + grade_point[3] * 3 + grade_point[4] * 3 +
            grade_point[5] + grade_point[6] + grade_point[7] * 2 + grade_point[8]) / 20
    st.success(f"Your SGPA for semester {semester} is {round(sgpa, 2)}")
elif semester == 2:
    a = st.number_input("21MAT21 - Advanced Calculus and Numerical Methods", min_value=0, max_value=100, step=1)
    b = st.number_input("21CHE22 - Engineering Chemistry", min_value=0, max_value=100, step=1)
    c = st.number_input("21PSP23 - Problem solving through programming", min_value=0, max_value=100, step=1)
    d = st.number_input("21ELN24 - Basic Electronics & Communication Engineering", min_value=0, max_value=100, step=1)
    e = st.number_input("21EME25 - Elements of Mechanical Engineering", min_value=0, max_value=100, step=1)
    f = st.number_input("21CHEL26 - Engineering Chemistry Laboratory", min_value=0, max_value=100, step=1)
    g = st.number_input("21CPLL27 - Computer Programming Laboratory", min_value=0, max_value=100, step=1)
    h = st.number_input("21EGH28 - Professional Writing skills in English", min_value=0, max_value=100, step=1)
    j = st.number_input("21SFH9 - Scientific Foundations of Health", min_value=0, max_value=100, step=1)
    marks = [a, b, c, d, e, f, g, h, j]
    grade_point = []
    for i in marks:
        if i in range(90, 101):
            grade_point.append(10)
        elif i in range(80, 90):
            grade_point.append(9)
        elif i in range(70, 80):
            grade_point.append(8)
        elif i in range(60, 70):
            grade_point.append(7)
        elif i in range(55, 60):
            grade_point.append(6)
        elif i in range(50, 55):
            grade_point.append(5)
        elif i in range(40, 50):
            grade_point.append(4)
        else:
            grade_point.append(0)
    sgpa = (grade_point[0] * 3 + grade_point[1] * 3 + grade_point[2] * 3 + grade_point[3] * 3 + grade_point[4] * 3 +
            grade_point[5] + grade_point[6] + grade_point[7] * 2 + grade_point[8]) / 20
    st.success(f"Your SGPA for semester {semester} is {round(sgpa, 2)}")
elif semester == 3:
    a = st.number_input("21MAT31 - Transform Calculus, Fourier Series and Numerical Techniques ", min_value=0, max_value=100, step=1)
    b = st.number_input("21CS32 - Data Structures and Algorithm", min_value=0, max_value=100, step=1)
    c = st.number_input("21CS33 - Analog and Digital Electronics", min_value=0, max_value=100, step=1)
    d = st.number_input("21CS34 - Computer Organization and Architecture ", min_value=0, max_value=100, step=1)
    e = st.number_input("21CSL35 - Object Oriented Programming with JAVA Laboratory ", min_value=0, max_value=100, step=1)
    f = st.number_input("21UH36 - Social Connect and Responsibility", min_value=0, max_value=100, step=1)
    g = st.number_input("21CIP37 - Constitution of India and Professional Ethics ", min_value=0, max_value=100, step=1)
    h = st.number_input("21CSL381 - Mastering Office", min_value=0, max_value=100, step=1)
    marks = [a, b, c, d, e, f, g, h]
    grade_point = []
    for i in marks:
        if i in range(90, 101):
            grade_point.append(10)
        elif i in range(80, 90):
            grade_point.append(9)
        elif i in range(70, 80):
            grade_point.append(8)
        elif i in range(60, 70):
            grade_point.append(7)
        elif i in range(55, 60):
            grade_point.append(6)
        elif i in range(50, 55):
            grade_point.append(5)
        elif i in range(40, 50):
            grade_point.append(4)
        else:
            grade_point.append(0)
    sgpa = (grade_point[0]*3 + grade_point[1]*4 + grade_point[2]*4 + grade_point[3]*3 + grade_point[4] + grade_point[5]
            + grade_point[6] + grade_point[7])/18
    st.success(f"Your SGPA for semester {semester} is {round(sgpa,2)}")

elif semester == 4:
    a = st.number_input("21CS41 - Mathematical Foundations for Computing ", min_value=0, max_value=100, step=1)
    b = st.number_input("21CS42 - Design and Analysis of Algorithms", min_value=0, max_value=100, step=1)
    c = st.number_input("21CS43 - Microcontroller and Embedded Systems", min_value=0, max_value=100, step=1)
    d = st.number_input("21CS44 - Operating SystemS", min_value=0, max_value=100, step=1)
    e = st.number_input("21BE5 - Biology For Engineers", min_value=0, max_value=100, step=1)
    f = st.number_input("21KSK/KBK46 - Samskrutika/Balake Kannada", min_value=0, max_value=100, step=1)
    g = st.number_input("21CSL481 - Web Programming", min_value=0, max_value=100, step=1)
    h = st.number_input("21UH49 - Universal Human Values", min_value=0, max_value=100, step=1)
    j = st.number_input("21INT49 - Inter/Intra Institutional Internship", min_value=0, max_value=100, step=1)
    marks = [a, b, c, d, e, f, g, h, j]
    grade_point = []
    for i in marks:
        if i in range(90, 101):
            grade_point.append(10)
        elif i in range(80, 90):
            grade_point.append(9)
        elif i in range(70, 80):
            grade_point.append(8)
        elif i in range(60, 70):
            grade_point.append(7)
        elif i in range(55, 60):
            grade_point.append(6)
        elif i in range(50, 55):
            grade_point.append(5)
        elif i in range(40, 50):
            grade_point.append(4)
        else:
            grade_point.append(0)
    sgpa = (grade_point[0] * 3 + grade_point[1] * 4 + grade_point[2] * 4 + grade_point[3] * 3 + grade_point[4]*2 +
            grade_point[5] + grade_point[6] + grade_point[7] + grade_point[8]) / 22
    st.success(f"Your SGPA for semester {semester} is {round(sgpa, 2)}")
else:
    st.write("Semester yet to come ;)")