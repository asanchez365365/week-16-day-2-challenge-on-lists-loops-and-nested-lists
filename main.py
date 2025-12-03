# School Supply Order Tracking – Logic Challenge

## Objective
# Students will apply their understanding of lists, nested lists, slicing, sorting, list grouping, and logical decision-making to solve a real-world data organization problem without using code.

# ---

# ## Scenario
# You are helping the main office organize student supply requests for the week. Each request includes:

# - Student name  
# - Item requested  
# - Quantity requested  

# All requests must be stored together in one organized system.

# ---

## Student Tasks (Python Coding)

### 1. Create Student Requests
# Create a collection that stores information for **3 different student requests**.  
# Each student request must include:
# - Student name  Alisson
# - Item requested  Pencil
# - Quantity requested 2

# - Student name  Bob
# - Item requested  Notebooks
# - Quantity requested  7

# - Student name  Charlie
# - Item requested  Eraser
# - Quantity requested  4

student_requests = [
    {"student_name": "Alisson", "item_requested": "Pencil", "quantity_requested": 2},
    {"student_name": "Bob", "item_requested": "Notebooks", "quantity_requested": 7},
    {"student_name": "Charlie", "item_requested": "Eraser", "quantity_requested": 4}
]
print(student_requests)

# ---

### 2. Identify Key Information
# From your collection:
# - Identify the **first student’s name** Alisson
# - Identify the **last student’s requested item only** 

first_student_name = student_requests[0]["student_name"]
last_student_item = student_requests[-1]["item_requested"]

print(f"First student's name: {first_student_name}")
print(f"Last student's requested item: {last_student_item}")
# ---

### 3. Quantity Extraction
# Create a **separate list that contains only the quantities requested** by the students.

quantities_list = [request["quantity_requested"] for request in student_requests]

print("Quantities List:")
print(quantities_list)

### 4. Order Size Analysis
# Analyze the quantities:
# - If **any quantity is greater than 5**, label the order:
#   “Large order detected!”
# - Otherwise label the order:
#   “Orders within normal limits.”

print(" Order Size Analysis:")

if any(q > 5 for q in quantities_list):
    print("Large order detected!")
else:
    print("Orders within normal limits.")


# ---

### 5. Quantity Organization
# Re-organize the quantity list from **smallest to largest** and display the final result.
quantities_list.sort()
print(quantities_list)
# ---

# ## Challenge Extension: Classroom Storage Grid

# You are also given a grid showing classroom supply counts:

# Classroom 1: 8, 12, 5  
# Classroom 2: 7, 3, 9  
# Classroom 3: 10, 6, 4  

# Answer the following:

# 1. What is the **middle number** in the second classroom’s list?  
# 2. Create a new list that extracts **only the last number** from each classroom.
# 3. Explain **why this information must be stored as a nested structure instead of a single list.**

# ---

## What This Assignment Tests
# - Understanding how grouped data is stored
# - Nested structure reasoning
# - Data extraction using position
# - Organizational logic
# - Real-world decision-making with quantities

# ---

## Submission Requirements
# - All answers must be written in words and/or tables.
# - No programming code may be used.
# - Show clear reasoning for each response.

# ---

## Academic Integrity
# This is an individual logic and reasoning task. All work must be your own.

# ---

# Instructor: Marvin Evins  
# Course:  AP Computer Science Principles  
