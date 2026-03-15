import random
question = [

    {
        "questions": "What's the capital of Pakistan",
        "options": ["Karachi", "Istanbul", "Dehli", "Islamabad"],
        "Answer": "Islamabad"
    },
    {
        "questions": "Who discovered gravity when an apple fell from a tree?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
        "Answer": "Isaac Newton"
    },
    {
        "questions": "Which sport is known as 'the beautiful game'?",
        "options": ["Basketball", "Cricket", "Football", "Tennis"],
        "Answer": "Football"
    },
    {
        "questions": "Which programming language is known for its snake logo?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "Answer": "Python"
    },
    {
        "questions": "Who was the first President of the United States?",
        "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
        "Answer": "George Washington"
    },
    {
        "questions": "Which planet is called the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Mercury"],
        "Answer": "Mars"
    },
    {
        "questions": "In which year did World War II end?",
        "options": ["1940", "1945", "1950", "1939"],
        "Answer": "1945"
    },
    {
        "questions": "Who wrote 'Pride and Prejudice'?",
        "options": ["Jane Austen", "Charlotte Brontë", "Emily Dickinson", "Mary Shelley"],
        "Answer": "Jane Austen"
    },
    {
        "questions": "Which is the largest mammal on Earth?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "Answer": "Blue Whale"
    },
    {
        "questions": "Which country hosted the 2016 Summer Olympics?",
        "options": ["China", "Brazil", "UK", "Japan"],
        "Answer": "Brazil"
    }
]





for item in question:
 q = item["questions"]
 opt = item['options']

rightans = item['Answer']


userinp = input("Enter the correct answer: ")

if userinp == rightans:
 print("congratulations you answered correctly")
else:
 print("Sorry wrong answer")