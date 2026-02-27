personalized Entrance Exam coach
Solution Approach – Stepwise Explanation

Step 1: Frontend Layer (Presentation Layer)
Developed using HTML, CSS, and JavaScript.
Collects user inputs such as login credentials and subject scores (M1, EDA, DMS).
Validates input data before submission.
Sends data securely to the backend using a REST API in JSON format.

Step 2: Backend Layer (Application Layer)
Implemented using the Flask framework.
Receives user data via POST request.
Processes scores using adaptive planning logic:
Sorts subjects into weak, medium, and strong categories.
Assigns higher study priority to weaker subjects.
Generates a structured 7-day study plan.

Step 3: Data Layer (Database/Dataset Layer)
Stores predefined chapters and topics for each subject.
The planning engine dynamically retrieves relevant topics.
Ensures structured and organized study scheduling.

Step 4: Response & Output Generation
Backend returns the personalized study plan in JSON format.
Frontend dynamically displays:
Subject priority levels
Day-wise study schedule

Key Advantages
Modular architecture
Clear separation of concerns
Scalable and maintainable design
Efficient client-server communication
