room_number = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411                  
}

instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee' 
}

meeting_time = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.' 
}

def course_info():
    # Get input and convert to uppercase
    course_num = input('Enter your course number: ').upper()
    
    # Convert dictionary keys to uppercase for comparison
    course_exists = course_num in [key.upper() for key in room_number.keys()]
    
    if course_exists:
        # Find the original key that matches the uppercase input
        original_key = next(key for key in room_number.keys() if key.upper() == course_num)
        print(f"Your Course {original_key} is in room {room_number[original_key]} with Professor {instructors[original_key]} at {meeting_time[original_key]}")
    else:
        print('Course not found.')

# Call the function to run it
course_info()
    
        
       
    

    