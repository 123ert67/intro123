import streamlit as st

# Page configuration
st.set_page_config(page_title="Siwat Rattanatechanont", page_icon="🧸")

# Title
st.title("🧸 Siwat")

# Introduction
st.title("I'm Siwat Rattanatechanont (Pooh)")
st.title('A Bit About Me 👀')
st.write("""
Welcome to my page! I’m Siwat, a current student at Debsirin School. My academic journey 
has been both challenging and rewarding, and 
I’m excited to share a bit about my experiences and achievements.
""")
st.subheader('My Journey in Science🧪')
st.write("One of the highlights of my academic career so far has been participating in the Thailand Young Physicists' Tournament (TYPT). Competing in this prestigious contest allowed me to delve deeply into the world of physics, collaborate with brilliant minds, and develop my problem-solving skills. The experience was both intellectually stimulating and incredibly rewarding.")
st.subheader("Television Adventure🎥")
st.write("In addition to my academic and scientific interests, I had the exciting opportunity to be a contestant on the Thai game show Genwit. This experience was a fun and dynamic way to test my quick thinking and adaptability in a lively, competitive environment. It was an incredible experience that added a unique dimension to my personal growth.")
st.subheader("Lifelong Learning and Safety⚕️")
st.write("In addition to my scientific pursuits, I’m also committed to being prepared for emergencies. I have completed a CPR and First Aid course, which has equipped me with essential life-saving skills. This certification is important to me because I believe in the value of being prepared to help others in critical situations.")
st.image("https://images.contentstack.io/v3/assets/blt8a393bb3b76c0ede/blt98f4923943e018f8/656017f7867c0b37e1388a44/staying-alive-a-history-of-cpr-header.jpg", use_column_width=True)



# Current Activities
st.subheader("🧑‍💻 What I'm Doing Now")
st.write("""
- 💻 Studying Computer Science
- 🎮 Learning arduino & raspberry pi
- 🤖 Learning anything with Machine Learning
""")

# Tech Stack & Skills
st.subheader("📚 Tech Stack & Skills")

# Programming Languages
with st.expander("👨‍💻 Programming Languages"):
    st.image("https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54", use_column_width=True)
    st.image("https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white", use_column_width=True)
# Frontend Development
with st.expander("🪟 Frontend Development"):
    st.image("https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white", use_column_width=True)

# Backend Development
with st.expander("☠️ Backend Development"):
    st.image("https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white", use_column_width=True)

# AI & ML
with st.expander("🤖 AI & ML"):
    st.image("https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black", use_column_width=True)
    st.image("https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white", use_column_width=True)

# Dev Tools
with st.expander("🐥 Dev Tools"):
    st.image("https://skillicons.dev/icons?i=git,github,raspberrypi,arduino", use_column_width=True)

# My Skills
st.subheader("🐥 My Skills")
st.image("https://skillicons.dev/icons?i=python,cpp,php", use_column_width=True)

# Future Plans
st.subheader("🔮 What in Future")
st.write("""
- [ ] Study Computer Science (university degree)
""")

# Contact Information
st.subheader("📩 Connect with Me")
st.write("""
- 📩 siwat696@gmail.com
""")

# Footer
st.write("Thank you krub for reading :) 💯💪")
