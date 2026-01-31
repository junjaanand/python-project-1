chatbot_data = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "hey": "Hey! How are you doing?",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I am a simple Python chatbot.",
    "who created you": "I was created by a Python developer.",
    "what can you do": "I can answer basic questions.",
    "bye": "Goodbye! Have a nice day.",
    "goodbye": "See you later!",
    "thanks": "You're welcome!",
    
    "what is python": "Python is a popular programming language.",
    "python uses": "Python is used in web, AI, ML, data science, and more.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine learning is a subset of AI.",
    "what is deep learning": "Deep learning uses neural networks.",
    "what is programming": "Programming is writing instructions for computers.",
    "what is coding": "Coding is converting logic into code.",
    "what is oop": "OOP stands for Object-Oriented Programming.",
    "what is function": "A function is a block of reusable code.",
    "what is variable": "A variable stores data in memory.",
    
    "what is list": "A list stores multiple items and is mutable.",
    "what is tuple": "A tuple stores multiple items and is immutable.",
    "what is dictionary": "A dictionary stores data in key-value pairs.",
    "what is set": "A set stores unique items.",
    "what is loop": "A loop repeats code execution.",
    "for loop": "For loop iterates over a sequence.",
    "while loop": "While loop runs while condition is true.",
    "what is if": "If statement is used for decision making.",
    "what is elif": "Elif checks multiple conditions.",
    "what is else": "Else runs if no condition is true.",
    
    "what is string": "String is a sequence of characters.",
    "what is integer": "Integer is a whole number.",
    "what is float": "Float is a decimal number.",
    "what is boolean": "Boolean has True or False values.",
    "what is input": "Input takes data from the user.",
    "what is print": "Print displays output.",
    "what is error": "Error stops program execution.",
    "what is bug": "A bug is a mistake in code.",
    "what is debugging": "Debugging is fixing bugs.",
    "what is syntax": "Syntax is the rule of writing code.",
    
    "what is git": "Git is a version control system.",
    "what is github": "GitHub is a code hosting platform.",
    "what is repo": "Repo means repository.",
    "what is commit": "Commit saves code changes.",
    "what is push": "Push uploads code to GitHub.",
    "what is pull": "Pull downloads latest code.",
    "what is branch": "Branch allows parallel development.",
    "what is merge": "Merge combines branches.",
    "what is clone": "Clone copies a repository.",
    "what is fork": "Fork creates a copy of a repo.",
    
    "what is vscode": "VS Code is a code editor.",
    "what is terminal": "Terminal is used to run commands.",
    "what is pip": "Pip installs Python packages.",
    "what is streamlit": "Streamlit is used to build web apps in Python.",
    "what is flask": "Flask is a Python web framework.",
    "what is django": "Django is a full-stack Python framework.",
    "what is api": "API allows apps to communicate.",
    "what is json": "JSON is a data format.",
    "what is database": "Database stores data.",
    "what is sql": "SQL is used to query databases.",
    
    "what is chatbot": "A chatbot is a program that talks to users.",
    "how chatbot works": "Chatbots use rules or AI models.",
    "rule based chatbot": "Rule-based chatbot uses predefined rules.",
    "ai chatbot": "AI chatbot learns from data.",
    "nlp": "NLP stands for Natural Language Processing.",
    "what is model": "Model is trained data representation.",
    "what is training": "Training teaches a model.",
    "what is dataset": "Dataset is a collection of data.",
    "what is cloud": "Cloud provides online computing services.",
    "what is deployment": "Deployment means making app live."
}

def getResponse(userMsg):
    userMsg = userMsg.lower()
    for eachkey in chatbot_data :
        if eachkey in userMsg:
            return chatbot_data[eachkey]
    return "sorry i can't answer it now.."
        
# take user input
while True:
    user_input = input("USER  : ")
    ai_reply = getResponse(user_input)
    print(ai_reply)

    if "bye" in user_input.lower():
        break;
    