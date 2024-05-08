import streamlit as st
import nltk
from nltk import word_tokenize, pos_tag
from nltk.chat.util import Chat, reflections
# Download NLTK resources
import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
# Use double backslashes
# nltk.data.path.append(r"C:\Users\DIVINE FAVUR\Documents\nltk\punkt")

# Define responses for the chatbot
patterns = [r"hi|hello|hey|what's up",
    r"how are you|how's it going",
    r"what is Earlycode|Earlycode",
    r"bye|goodbye",
    r"what is your name",
    r"when do the company open during the week.",
    r"what is the company open hours",
    r"about your business",
    r"what is python Boot camp",
    r"how can i contact early code",
    r"what is web design masterclass",
    r"what is office essential",
    r"what services does your company offer",
    r"How can i Register for a course",
    r"Are the programs private lessons|Are their private lessons",
    r"Are the programs available online|Are their online classes",
    r"how long are the programs|how long will the course take|how long will the program take",
    r"How many days in a week will i come for lectures",
    r"I am a complete novice|I don't know anything about computers|I am not a computer literate",
    r"Will i get a certificate after the course.|certificate",
    r"what is coding|what is coding in simple terms|coding",
    r"I don't have a laptop|provision for a laptop",]

responses = [["Hello!"],
    ["I'm good, thank you."],
    ["We are providing an education that empowers. Early Code empowers and creates the platform for experts to teach everyone technical skills that count.Also at early code, we offer coding courses with quality and world-class content and lecture standards."],
    ["Goodbye!,Have a Blissful Day."],
    ["I'm the Early code Chatbot, available to provide assistance in the best possible manner."],
    ["We operate six days per week."],
    ["Our operating hours are from 9:00 in the morning until 6:00 in the evening."],
    ["We provide various tech services, including web development and data analytics."],
    ["Python boot camps provide a structured and immersive learning experience for individuals looking to acquire programming skills and kickstart their careers in technology. They offer a fast-paced and intensive learning environment that is ideal for those who want to quickly gain proficiency in Python programming and related technologies.Especially does in path of DataAnalytic,Data science"],
    ["You can contact our mobile line 0809388733636 or visit our website early code.net"],
    ["web design masterclass typically refers to an in-depth training program or course that teaches individuals how to design and create websites."],
    ["Office essentials typically refer to software tools commonly used in office environments for various tasks such as document creation, data analysis, presentations, communication, and organization."],
    ["We are a tech company that offers various  services and nice courses including Web Development, Python Boot camp, Office Essentials, Python with Data Science, and App Development and so more courses."],
    ["You can Register on our website or you can visit any of the Early code Branches or call this number +234-708-7777-367"],
    ["No, when you enrol you will be learning with others in a class."],
    ["No, lectures are conducted in a real-time physical classes with physical instructors present with you from start to finish."],
    ["Programs duration vary, it can range from 2 weeks to 3 months."],
    ["Class schedule varies across courses but it is usually 3 days per week, except for coding for kids courses."],
    ["Yes, required that you can perform basic computer operations like right-click,left-click, creating files and folders, etc."],
    ["Yes, you will be issued a certificate which is verifiable on our institution's website to proof that the certificate is authentic."],
    ["Coding, in simple terms, refers to the process of writing instructions for a computer to follow. These instructions are typically written using a programming language, which is a set of rules and syntax that computers understand."],
    ["Yes, laptops are provided for students to use in our training centers."],] 

# Combine patterns and responses using zip
pairs = list(zip(patterns, responses))

# Create a chatbot using NLTK
chatbot =Chat(pairs, reflections)
chat_history = []  # Initialize empty chat history

# Streamlit UI
st.title("Earlycode-Bot")

# User input field
user_input = st.text_input("You:")

# Send button to submit user input
if st.button("Send"):
    user_input = user_input.lower()
    # Get the chatbot response
    response = chatbot.respond(user_input)
    
    # Tokenize the user's input and perform POS tagging
    words = word_tokenize(user_input)
    tagged_words = pos_tag(words)
    
    # Extract nouns from the tagged words
    nouns = [word for word, pos in tagged_words if pos.startswith("NN")]
    
    # If there are nouns in the user input, modify the chatbot response
    if nouns:
        # Join the nouns into a single string
        noun_str = " ".join(nouns)
        if "service" in noun_str.lower():
            response = "We are providing an education that empowers. Early Code empowers and creates the platform for experts to teach everyone technical skills that count.Also at early code, we offer coding courses with quality and world-class content and lecture standards."
        elif "register" in noun_str.lower():
            response="You can Register on our website [Earlycode](https://www.earlycode.net/auth/signup) or you can visit any Earlycode Branch or call this number +234-708-7777-367"
        elif "branch" in noun_str.lower():
            response="Our company has branches located in Nyanya and Kubwa.."
        elif "name" in noun_str.lower():
            response="I'm the Earlycode Chatbot, available to provide assistance in the best possible manner."
        elif "earlycode" in noun_str.lower():
            response="We are providing an education that empowers. Early Code empowers and creates the platform for experts to teach everyone technical skills that count.Also at early code, we offer coding courses with quality and world-class content and lecture standards."
        elif "code" in noun_str.lower():
            response = "Coding is a fundamental skill in computer science and is used to create software, websites, mobile apps, and other digital technologies. It requires logical thinking, problem-solving skills, and attention to detail."
        elif "hour" in noun_str.lower():
            response="Our operating hours are from 9:00am in the morning until 6:00pm in the evening."
        elif "time" in noun_str.lower():
             response="Our operating hours are from 9:00 in the morning until 6:00 in the evening."
        elif "phone number" in noun_str.lower():
            response="The phone number for kubwa branch is +234-708-7777-367 mean while nyanya branch cell number is +234-708-888-2568 "
        elif "contact" in noun_str.lower():
            response = "You can contact us through our website[Earlycode](https://www.earlycode.net/) or by mobile phone +234-708-7777-367 or +234-708-888-2568"
        elif "python bootcamp" in noun_str.lower():
            response = "A Python Bootcamp is an intensive training program or course designed to teach participants the fundamentals and advanced concepts of the Python programming language"
        elif "javascript" in noun_str.lower():
            response= "JavaScript is the main programming language for the web but its usage has also evolved to the development of ios and Android apps.if you are venturing into web app,IOS/Android Development,this course will pave the way for you and equip you with the base and prerequisite skills for the development of such apps"
        elif "web development with laravel"in noun_str.lower():
            response="In this course, you will learn how to use laravel to build modern,powerful web applications.You will start by setting up your development environment and learning the basics pf Laravel Framework.You will learn about routing,controllers,views, and models,and how they all work together to create web application."
        elif "ui/ux" in noun_str.lower():
            response="in this course, you will learn the essential skills needed to create digital user interface that captivate users and enhance overall usability.By using industry-standard tools,you will not only refine your design prowness but also gain practical insights into the iterative process of refining prototypes for optimal user engagement"
        elif "kids" in noun_str.lower():
            response="Kids can acquire coding skills and build the foundational knowledge that they need to build relevant career skills.this program takes kids from the elementary level to the point of understanding concepts and principles used by professional developers.The course accepts kids from 6 to 13 years of age."
        elif "android and ios development" in noun_str.lower():
            response="Learn to build all both Android and IOS app with the latest and most accepted technologies.This course involves core coding and software development lessons.The course is advanced but designed for those who have never even written computer codes before. it starts with the elementary things and gradually proceeds to intermediate concepts and coding exercise and later to the advanced sections"
        elif "react" in noun_str.lower():
            response="in this course you will learn the fundamentals of React.js, including components,state, and the virtual DOM.you will also learn how to use React hooks,a new feature in React that allows you to use state and other React features without writing a class"
        elif "entrepreneurship" in noun_str.lower():
            response="This course is for you if you want to get a job in tech,build a successful career in tech, or launch a business or start-up in tech.This course is versatile and promising as it deals with all three aspects,in this course,you will learn how to prepare your curriculum vitae, start and scale up a tech career, and launch a profitable business in the tech industry"
        elif "bootstrap" in noun_str.lower():
            response="learn the skill of designing websites, HTML is the language of the web and it's used to write the structure of every website.The CSS skill to be acquired will be used to style and create beautiful website projects.Bootstrap is framework css that helps the designer to avoid commonly used codes repeatedly,instead,blocks of styling codes are written in shorter and simpler codes"
        elif "tailwind" in noun_str.lower():
            response="Tailwind CSS is a utility-first CSS framework designed to enable users to create application faster and easier.You will learn how to use utility classes to control the layout,color,spacing,typography,shadows, and more to create a completely custom component design with"
        elif "php" in noun_str.lower():
            response="PHP backend refers to the server-side component of a web application or website that is written in PHP (Hypertext Preprocessor). PHP is a popular scripting language that is widely used for web development."
        elif "computer literate" in noun_str.lower():
            response="You don't need to necessarily be literate to succeed in any field you choose, thanks to the guidance of instructors and your dedication."
        elif "courses" in noun_str.lower():
            response = """We offer a variety of courses at Earlycode, including:
- Javascript BootCamp
- Python Bootcamp
- Web Development With Laravel
- UI/UX And Prototype Design
- Coding for Kids
- Android & IOS Development
- Web Development With React And Next JS
- Entrepreneurship In Digital Economies
- Web Design Masterclass(BOOTSTRAP)
- Web Design Masterclass(TAILWIND CSS)
- PHP Backend Development
- Data Analysis(1 Month)
- Python Programming(5 weeks)
- Python with Data Science(13 weeks)

For more information on the courses, you can visit our website [Earlycode](https://www.earlycode.net/)."""
        elif "duration" in noun_str.lower():
            response="""The duration of each course:
- Javascript- 5weeks period
- Web Development with Laravel - 12 weeks Period
- UI/UX AND PROTOTYPE DESIGN- 6 weeks period
- Android and IOS Development- 12 weeks period.
- Web Development with React and Next JS- 12weeks period
- PHP Backend Development- 5weeks period
- Web Design Masterclass(Bootstrap)- 4 weeks period
- Web Design Masterclass(Tailwind css)- 4 weeks period
- Entrepreneurship In Digital Economics - 1 weeks period
- Coding for Kids- on this duration contact us now to get more information +234-708-7777-367.
- Python Bootcamp- 6weeks period
- SPSS- 1 week period
- Office Essential- 8 weeks Period
- Python with Data science- 12 weeks Period
- for more information visit our website[Earlycode](https://www.earlycode.net/) or contact us at +234-708-7777-367.
"""
        elif "development" in noun_str.lower():
            response = "Web development includes options such as web development with React and JavaScript, as well as web development with Laravel."
        elif "website" in noun_str.lower():
            response = "Feel free to explore our website at https://www.earlycode.net/ to discover more about the array of courses we provide."  
        elif "location" in noun_str.lower():
            response= "Our primary operations are based in Abuja, with two branches situated at the following addresses: one in Kubwa at the 1st floor of Pronet Mall, 62 Gado Nasko Road, and the other in Nyanya at the 3rd floor of EFKO Mall, Nyanya-Karshi Road, opposite First Bank, beside Chicken Republic. For additional details, please contact us at +234-708-7777-367 or +234-708-8882-568."
        elif "class section" in noun_str.lower():
            response = "The duration is only for 2hours class session 3days in a week."
        elif "laptop" in noun_str.lower():
            response= "If you happen not to have a laptop, Early Code offers you a laptop during class session."
        elif "address" in noun_str.lower():
            response= "Our primary operations are based in Abuja, with two branches situated at the following addresses: one in Kubwa at the 1st floor of Pronet Mall, 62 Gado Nasko Road, and the other in Nyanya at the 3rd floor of EFKO Mall, Nyanya-Karshi Road, opposite First Bank, beside Chicken Republic. For additional details, please contact us at +234-708-7777-367 or +234-708-8882-568."
        elif "payment" in noun_str.lower():
            response="Start by completing the registration for your choice course, you will be redirected to the next page where you can make payment online or bank transfer.[Earlycode](https://www.earlycode.net/auth/signup)"
        elif "programs" in noun_str.lower():
            response="Programs duration vary it can range from 2 weeks to 3 Months.for more information you can visit the website [Earlycode](https://www.earlycode.net/auth/signup)"
        elif "online" in noun_str.lower():
            response="No, lectures are conducted in a real-time physical classes with physical instructors present with you from start to finish."
        elif "private" in noun_str.lower():
            response="No, when you enrol you will be learning with others in a class."
        elif "week" in noun_str.lower():
            response="Class schedule varies across courses but it is usually 3 days per week, except for coding for kids courses."
        elif "novice" in noun_str.lower():
            response="Yes, required that you can perform basic computer operations like right-click,left-click, creating files and folders, etc."
        elif "certificate" in noun_str.lower():
            response="Yes, you will be issued a certificate which is verifiable on our institution's website to proof that the certificate is authentic."
        elif "installments" in noun_str.lower():
            response="No, there are no provisions to make payments in installments. We require payments to be made in full before the start date of enrolled courses."
        elif "analysis" in noun_str.lower():
            response="Data analysis is the process of examining, cleaning, transforming, and interpreting data to discover meaningful insights, patterns, and trends. It involves applying statistical and computational techniques to understand the structure of datasets, extract useful information, and support decision-making."
        elif "science" in noun_str.lower():
            response="Data science is an interdisciplinary field that combines principles, techniques, and methodologies from various disciplines such as statistics, computer science, mathematics, and domain-specific knowledge to extract insights and knowledge from structured and unstructured data. It encompasses a range of activities including data collection, data cleaning, data analysis, machine learning, and data visualization."
        elif "android" in noun_str.lower():
            response="Android Programming: Android programming involves developing applications for devices that use the Android operating system.iOS programming involves developing applications for devices that use the iOS operating system, such as iPhones, iPads, and iPod Touch devices."
        elif "office essential" in noun_str.lower():
            response="Office essentials typically refer to software tools commonly used in office environments for various tasks such as document creation, data analysis, presentations, communication, and organization"
        elif "ui" in noun_str.lower():
            response="UI (User Interface) and UX (User Experience) design are two aspects of creating digital products like websites, mobile apps, or software that focus on how users interact with and experience the product.UI design deals with the look and feel of the product. It involves designing the visual elements that users interact with, such as buttons, icons, colors, fonts, and overall layout. UI designers strive to create interfaces that are visually appealing, intuitive to use, and consistent across different screens or pages."
        elif "thank you":
            response="You're welcome. I'm happy to assist you."
    
    


    
    if not response:
        response = "Apologies, I didn't quite grasp that. Alternatively, you can visit our website [Earlycode](https://www.earlycode.net/) for more information, or feel free to reach out to us at +234-708-7777-367 with any further inquiries. Thank you.."
    # Add user's message to chat history
    chat_history.append({"user": "You", "message": user_input})
    
    # Add chatbot's response to chat history
    chat_history.append({"user": "ChatBot", "message": response})


# Display chat history
for chat in chat_history:
    if chat["user"] == "You":
        st.write(f"You: {chat['message']}")
    else:
        st.write(f"ChatBot: {chat['message']}")
