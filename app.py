import streamlit as st
import streamlit.components.v1 as components
import base64
from PIL import Image
import io
import time

# Page configuration
st.set_page_config(
    page_title="Personal Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    /* Main title styling */
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #2E3B4E;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeIn 1.5s ease-in;
    }
    
    /* Section title styling */
    .section-title {
        font-size: 2rem;
        font-weight: 600;
        color: #2E3B4E;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    
    /* Card styling */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: background-color 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
    }
    
    /* Animation keyframes */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Skill badge styling */
    .skill-badge {
        display: inline-block;
        background-color: #f0f2f6;
        color: #2E3B4E;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* Project card styling */
    .project-card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
    }
    
    /* Contact form styling */
    .contact-form {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Social media icon styling */
    .social-icon {
        font-size: 1.5rem;
        margin: 0 0.5rem;
        color: #2E3B4E;
        transition: color 0.3s ease;
    }
    
    .social-icon:hover {
        color: #3498db;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
def navigation():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Home", "About", "Projects", "Skills", "Resume", "Contact"]
    )
    return page

# Home page
def home():
    st.markdown('<h1 class="main-title">Welcome to My Portfolio</h1>', unsafe_allow_html=True)
    
    # Hero section with animation
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div style="animation: fadeIn 1.5s ease-in;">
            <h2 style="font-size: 2.5rem; color: #2E3B4E;">Hi, I'm [Your Name]</h2>
            <p style="font-size: 1.2rem; color: #666;">A passionate Python developer with expertise in web development, data science, and machine learning.</p>
            <div style="margin-top: 2rem;">
                <a href="#contact" style="text-decoration: none;">
                    <button style="background-color: #3498db; color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 5px; font-weight: 500; cursor: pointer;">Get in Touch</button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Placeholder for profile image
        st.image("https://via.placeholder.com/400x400", use_column_width=True)
    
    # Featured projects section
    st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>Project 1</h3>
            <p>A brief description of the project and its key features.</p>
            <div style="margin-top: 1rem;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">Flask</span>
                <span class="skill-badge">SQLite</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>Project 2</h3>
            <p>A brief description of the project and its key features.</p>
            <div style="margin-top: 1rem;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">Django</span>
                <span class="skill-badge">PostgreSQL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="project-card">
            <h3>Project 3</h3>
            <p>A brief description of the project and its key features.</p>
            <div style="margin-top: 1rem;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">TensorFlow</span>
                <span class="skill-badge">NumPy</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# About page
def about():
    st.markdown('<h1 class="main-title">About Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Placeholder for profile image
        st.image("https://via.placeholder.com/300x300", use_column_width=True)
    
    with col2:
        st.markdown("""
        <div style="animation: fadeIn 1.5s ease-in;">
            <h2 style="font-size: 2rem; color: #2E3B4E;">My Journey</h2>
            <p style="font-size: 1.1rem; color: #666; line-height: 1.6;">
                I'm a passionate Python developer with a strong background in web development, data science, and machine learning. 
                I enjoy solving complex problems and building innovative solutions that make a difference.
            </p>
            <p style="font-size: 1.1rem; color: #666; line-height: 1.6;">
                With over [X] years of experience in the industry, I've worked on various projects ranging from small-scale applications 
                to large enterprise solutions. I'm constantly learning and exploring new technologies to stay at the forefront of innovation.
            </p>
            <div style="margin-top: 2rem;">
                <h3 style="font-size: 1.5rem; color: #2E3B4E;">Education</h3>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li style="margin-bottom: 1rem;">
                        <strong>Bachelor's Degree in Computer Science</strong><br>
                        University Name, Graduation Year
                    </li>
                    <li style="margin-bottom: 1rem;">
                        <strong>Master's Degree in Software Engineering</strong><br>
                        University Name, Graduation Year
                    </li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Projects page
def projects():
    st.markdown('<h1 class="main-title">My Projects</h1>', unsafe_allow_html=True)
    
    # Project filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        category = st.selectbox(
            "Category",
            ["All", "Web Development", "Data Science", "Machine Learning", "Mobile Apps"]
        )
    
    with col2:
        technology = st.selectbox(
            "Technology",
            ["All", "Python", "Flask", "Django", "TensorFlow", "PyTorch", "React", "Node.js"]
        )
    
    with col3:
        year = st.selectbox(
            "Year",
            ["All", "2023", "2022", "2021", "2020"]
        )
    
    # Project grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>E-commerce Platform</h3>
            <p>A full-stack e-commerce platform with user authentication, product management, and payment integration.</p>
            <div style="margin-top: 1rem;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">Django</span>
                <span class="skill-badge">PostgreSQL</span>
                <span class="skill-badge">React</span>
            </div>
            <div style="margin-top: 1rem;">
                <a href="#" style="text-decoration: none;">
                    <button style="background-color: #3498db; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; font-weight: 500; cursor: pointer;">View Project</button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>Data Visualization Dashboard</h3>
            <p>An interactive dashboard for visualizing and analyzing large datasets with real-time updates.</p>
            <div style="margin-top: 1rem;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">Streamlit</span>
                <span class="skill-badge">Plotly</span>
                <span class="skill-badge">Pandas</span>
            </div>
            <div style="margin-top: 1rem;">
                <a href="#" style="text-decoration: none;">
                    <button style="background-color: #3498db; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; font-weight: 500; cursor: pointer;">View Project</button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>Machine Learning Model</h3>
            <p>A machine learning model for predicting customer behavior and optimizing marketing strategies.</p>
            <div style="margin-top: 1rem;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">TensorFlow</span>
                <span class="skill-badge">Scikit-learn</span>
                <span class="skill-badge">NumPy</span>
            </div>
            <div style="margin-top: 1rem;">
                <a href="#" style="text-decoration: none;">
                    <button style="background-color: #3498db; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; font-weight: 500; cursor: pointer;">View Project</button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>Mobile App</h3>
            <p>A cross-platform mobile application for task management and productivity tracking.</p>
            <div style="margin-top: 1rem;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">Kivy</span>
                <span class="skill-badge">SQLite</span>
                <span class="skill-badge">Firebase</span>
            </div>
            <div style="margin-top: 1rem;">
                <a href="#" style="text-decoration: none;">
                    <button style="background-color: #3498db; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; font-weight: 500; cursor: pointer;">View Project</button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Skills page
def skills():
    st.markdown('<h1 class="main-title">My Skills</h1>', unsafe_allow_html=True)
    
    # Skills categories
    categories = ["Programming Languages", "Web Development", "Data Science", "Machine Learning", "Databases", "Tools & Technologies"]
    
    for category in categories:
        st.markdown(f'<h2 class="section-title">{category}</h2>', unsafe_allow_html=True)
        
        if category == "Programming Languages":
            st.markdown("""
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                <span class="skill-badge">Python</span>
                <span class="skill-badge">JavaScript</span>
                <span class="skill-badge">Java</span>
                <span class="skill-badge">C++</span>
                <span class="skill-badge">SQL</span>
            </div>
            """, unsafe_allow_html=True)
        
        elif category == "Web Development":
            st.markdown("""
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                <span class="skill-badge">HTML</span>
                <span class="skill-badge">CSS</span>
                <span class="skill-badge">JavaScript</span>
                <span class="skill-badge">React</span>
                <span class="skill-badge">Node.js</span>
                <span class="skill-badge">Flask</span>
                <span class="skill-badge">Django</span>
            </div>
            """, unsafe_allow_html=True)
        
        elif category == "Data Science":
            st.markdown("""
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                <span class="skill-badge">NumPy</span>
                <span class="skill-badge">Pandas</span>
                <span class="skill-badge">Matplotlib</span>
                <span class="skill-badge">Seaborn</span>
                <span class="skill-badge">Jupyter</span>
            </div>
            """, unsafe_allow_html=True)
        
        elif category == "Machine Learning":
            st.markdown("""
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                <span class="skill-badge">TensorFlow</span>
                <span class="skill-badge">PyTorch</span>
                <span class="skill-badge">Scikit-learn</span>
                <span class="skill-badge">Keras</span>
                <span class="skill-badge">OpenCV</span>
            </div>
            """, unsafe_allow_html=True)
        
        elif category == "Databases":
            st.markdown("""
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                <span class="skill-badge">SQLite</span>
                <span class="skill-badge">MySQL</span>
                <span class="skill-badge">PostgreSQL</span>
                <span class="skill-badge">MongoDB</span>
                <span class="skill-badge">Firebase</span>
            </div>
            """, unsafe_allow_html=True)
        
        elif category == "Tools & Technologies":
            st.markdown("""
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                <span class="skill-badge">Git</span>
                <span class="skill-badge">Docker</span>
                <span class="skill-badge">AWS</span>
                <span class="skill-badge">Linux</span>
                <span class="skill-badge">VS Code</span>
            </div>
            """, unsafe_allow_html=True)

# Resume page
def resume():
    st.markdown('<h1 class="main-title">My Resume</h1>', unsafe_allow_html=True)
    
    # Resume sections
    sections = ["Education", "Experience", "Skills", "Projects", "Certifications"]
    
    for section in sections:
        st.markdown(f'<h2 class="section-title">{section}</h2>', unsafe_allow_html=True)
        
        if section == "Education":
            st.markdown("""
            <div class="card">
                <h3>Bachelor's Degree in Computer Science</h3>
                <p>University Name, Graduation Year</p>
                <p>Relevant Coursework: Data Structures, Algorithms, Database Systems, Web Development</p>
            </div>
            <div class="card">
                <h3>Master's Degree in Software Engineering</h3>
                <p>University Name, Graduation Year</p>
                <p>Relevant Coursework: Advanced Algorithms, Software Architecture, Distributed Systems</p>
            </div>
            """, unsafe_allow_html=True)
        
        elif section == "Experience":
            st.markdown("""
            <div class="card">
                <h3>Senior Python Developer</h3>
                <p>Company Name, Duration</p>
                <ul>
                    <li>Led the development of a full-stack web application using Django and React</li>
                    <li>Implemented CI/CD pipelines using GitHub Actions and Docker</li>
                    <li>Mentored junior developers and conducted code reviews</li>
                </ul>
            </div>
            <div class="card">
                <h3>Python Developer</h3>
                <p>Company Name, Duration</p>
                <ul>
                    <li>Developed and maintained Python applications for data processing</li>
                    <li>Collaborated with cross-functional teams to deliver high-quality solutions</li>
                    <li>Optimized code for better performance and scalability</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        elif section == "Skills":
            st.markdown("""
            <div class="card">
                <h3>Programming Languages</h3>
                <p>Python, JavaScript, Java, C++, SQL</p>
            </div>
            <div class="card">
                <h3>Web Development</h3>
                <p>HTML, CSS, JavaScript, React, Node.js, Flask, Django</p>
            </div>
            <div class="card">
                <h3>Data Science & Machine Learning</h3>
                <p>NumPy, Pandas, Matplotlib, TensorFlow, PyTorch, Scikit-learn</p>
            </div>
            <div class="card">
                <h3>Databases</h3>
                <p>SQLite, MySQL, PostgreSQL, MongoDB, Firebase</p>
            </div>
            <div class="card">
                <h3>Tools & Technologies</h3>
                <p>Git, Docker, AWS, Linux, VS Code</p>
            </div>
            """, unsafe_allow_html=True)
        
        elif section == "Projects":
            st.markdown("""
            <div class="card">
                <h3>E-commerce Platform</h3>
                <p>A full-stack e-commerce platform with user authentication, product management, and payment integration.</p>
                <p>Technologies: Python, Django, PostgreSQL, React</p>
            </div>
            <div class="card">
                <h3>Data Visualization Dashboard</h3>
                <p>An interactive dashboard for visualizing and analyzing large datasets with real-time updates.</p>
                <p>Technologies: Python, Streamlit, Plotly, Pandas</p>
            </div>
            <div class="card">
                <h3>Machine Learning Model</h3>
                <p>A machine learning model for predicting customer behavior and optimizing marketing strategies.</p>
                <p>Technologies: Python, TensorFlow, Scikit-learn, NumPy</p>
            </div>
            """, unsafe_allow_html=True)
        
        elif section == "Certifications":
            st.markdown("""
            <div class="card">
                <h3>Python for Data Science</h3>
                <p>Coursera, Year</p>
            </div>
            <div class="card">
                <h3>Web Development with Django</h3>
                <p>Udemy, Year</p>
            </div>
            <div class="card">
                <h3>Advanced Python Programming</h3>
                <p>edX, Year</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Download resume button
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <a href="#" style="text-decoration: none;">
            <button style="background-color: #3498db; color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 5px; font-weight: 500; cursor: pointer;">Download Resume</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Contact page
def contact():
    st.markdown('<h1 class="main-title">Get in Touch</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="animation: fadeIn 1.5s ease-in;">
            <h2 style="font-size: 2rem; color: #2E3B4E;">Contact Information</h2>
            <p style="font-size: 1.1rem; color: #666; line-height: 1.6;">
                Feel free to reach out to me for collaborations, job opportunities, or just to say hello!
            </p>
            <div style="margin-top: 2rem;">
                <p style="font-size: 1.1rem; color: #666;">
                    <strong>Email:</strong> your.email@example.com
                </p>
                <p style="font-size: 1.1rem; color: #666;">
                    <strong>Phone:</strong> +1 (123) 456-7890
                </p>
                <p style="font-size: 1.1rem; color: #666;">
                    <strong>Location:</strong> City, Country
                </p>
            </div>
            <div style="margin-top: 2rem;">
                <h3 style="font-size: 1.5rem; color: #2E3B4E;">Social Media</h3>
                <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                    <a href="#" style="text-decoration: none;">
                        <span class="social-icon">📱</span>
                    </a>
                    <a href="#" style="text-decoration: none;">
                        <span class="social-icon">💼</span>
                    </a>
                    <a href="#" style="text-decoration: none;">
                        <span class="social-icon">🐦</span>
                    </a>
                    <a href="#" style="text-decoration: none;">
                        <span class="social-icon">📸</span>
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-form">
            <h2 style="font-size: 2rem; color: #2E3B4E;">Send a Message</h2>
            <form>
                <div style="margin-bottom: 1rem;">
                    <label for="name" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Name</label>
                    <input type="text" id="name" style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 5px;">
                </div>
                <div style="margin-bottom: 1rem;">
                    <label for="email" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Email</label>
                    <input type="email" id="email" style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 5px;">
                </div>
                <div style="margin-bottom: 1rem;">
                    <label for="subject" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Subject</label>
                    <input type="text" id="subject" style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 5px;">
                </div>
                <div style="margin-bottom: 1rem;">
                    <label for="message" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Message</label>
                    <textarea id="message" rows="5" style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 5px;"></textarea>
                </div>
                <button type="submit" style="background-color: #3498db; color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 5px; font-weight: 500; cursor: pointer;">Send Message</button>
            </form>
        </div>
        """, unsafe_allow_html=True)

# Main function
def main():
    page = navigation()
    
    if page == "Home":
        home()
    elif page == "About":
        about()
    elif page == "Projects":
        projects()
    elif page == "Skills":
        skills()
    elif page == "Resume":
        resume()
    elif page == "Contact":
        contact()

 