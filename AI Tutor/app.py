import streamlit as st
import google.generativeai as genai
from PIL import Image

# ----------------- Setup -----------------
# Page config is a native Streamlit way to set the layout
st.set_page_config(page_title="AI Tutor", page_icon="🎓", layout="wide")

# ----------------- Load API key -----------------
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error(f"Error configuring the API. Please check your secrets.toml file. Details: {e}")
    st.stop()

# Initialize models
try:
    text_model = genai.GenerativeModel("gemini-1.5-flash") # Updated for better performance
    vision_model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Error initializing the Generative Models. Details: {e}")
    st.stop()

# ----------------- Session State -----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "awaiting_solution" not in st.session_state:
    st.session_state.awaiting_solution = False
if "last_question" not in st.session_state:
    st.session_state.last_question = None
if "solution_displayed" not in st.session_state:
    st.session_state.solution_displayed = False
if "last_question_type" not in st.session_state:
    st.session_state.last_question_type = None  # "Math" or "Theory"


# ----------------- Helper: Extract text from image -----------------
def extract_text_from_image(img_file):
    try:
        extraction_prompt = (
            "Extract the problem statement from this image as it is. "
            "Also keep all operators such that if it is written in a line then solution should be same."
        )
        img = Image.open(img_file)
        response = vision_model.generate_content([extraction_prompt, img])
        return response.text.strip()
    except Exception as e:
        return f"[Error extracting text: {e}]"


# ----------------- Tutor Function -----------------
def tutor_response(input_data, request_solution=False):
    if request_solution:
        # Explicitly solve step-by-step
        prompt_template = (
            "You are a helpful AI tutor. The student already received hints. "
            "Now provide a clear, step-by-step solution for this problem only:\n\n"
            f"{input_data}"
        )
        return text_model.generate_content(prompt_template).text, "Math"

    else:
        # Hint + classification stage
        prompt_template = (
            "You are a helpful, funny, kind hearted, polite and friendly AI tutor. "
            "First, classify the student's question strictly as 'Math' or 'Theory' "
            "(start your answer with: Type: Math or Type: Theory). "
            "If it's Math: ONLY provide 2-3 helpful hints, do NOT give the solution yet. "
            "If it's Theory: explain the concept simply for a 12-year-old."
        )

        full_prompt = f"{prompt_template}\n\nStudent: {input_data}\nTutor:"
        response = text_model.generate_content(full_prompt).text

        # Extract type from response
        q_type = "Theory"
        if response.strip().lower().startswith("type: math"):
            q_type = "Math"
            response = response.replace("Type: Math", "").strip()
        elif response.strip().lower().startswith("type: theory"):
            q_type = "Theory"
            response = response.replace("Type: Theory", "").strip()

        return response, q_type


# ----------------- Streamlit UI -----------------

# Title and subtitle using native Streamlit elements
st.title("🎓 AI Tutor")
st.markdown("Your intelligent learning companion • Ask questions • Get hints • Learn better")

# Feature highlights using st.container with a border
col1, col2, col3 = st.columns(3)
with col1:
    with st.container(border=True):
        st.markdown("💡 **Smart Hints**")
        st.caption("Get helpful hints before seeing solutions")

with col2:
    with st.container(border=True):
        st.markdown("📸 **Image Support**")
        st.caption("Upload photos of your problems")

with col3:
    with st.container(border=True):
        st.markdown("🧠 **AI Powered**")
        st.caption("Advanced Gemini AI technology")


# Chat container with a fixed height to enable scrolling
chat_container = st.container(height=400)

with chat_container:
    # Display initial welcome message or chat history
    if not st.session_state.chat_history:
        st.info("👋 Welcome to AI Tutor! I'm here to help you learn. Ask a question or upload an image to start.")
    else:
        # Using st.chat_message for native chat bubbles
        for role, msg in st.session_state.chat_history:
            if role == "Student":
                with st.chat_message("user"):
                    st.write(msg)
            elif role == "Tutor":
                with st.chat_message("assistant", avatar="🤖"):
                    st.write(msg)
            elif role == "Tutor (Solution)":
                with st.chat_message("assistant", avatar="📘"):
                    st.write(msg)

# Input area at the bottom
col1, col2 = st.columns([4, 1])

with col1:
    user_text = st.text_input("✍️ Type your question or upload an image below:", placeholder="Enter a math problem or theory question...")

with col2:
    # Adding a small space for vertical alignment with the text input
    st.write("") 
    st.write("")
    if st.button("SEND", use_container_width=True, type="primary"):
        if st.session_state.solution_displayed:
            st.session_state.chat_history = []
            st.session_state.solution_displayed = False
            # Reset other states as well
            st.session_state.last_question = None
            st.session_state.awaiting_solution = False
            st.session_state.last_question_type = None

        if user_text.strip():
            with st.spinner("✨ Thinking..."):
                answer, q_type = tutor_response(user_text)
                st.session_state.chat_history.append(("Student", user_text))
                st.session_state.chat_history.append(("Tutor", answer))
                st.session_state.awaiting_solution = (q_type == "Math")
                st.session_state.last_question = user_text
                st.session_state.last_question_type = q_type
                if q_type == "Theory":
                    st.session_state.solution_displayed = True
            st.rerun()
        else:
            st.warning("⚠️ Please enter a question before sending!")

# File uploader with button logic
uploaded_image = st.file_uploader("📷 Or upload an image of your problem", type=["png", "jpg", "jpeg"])

if uploaded_image:
    if st.button("PROCESS IMAGE", use_container_width=True):
        if st.session_state.solution_displayed:
            st.session_state.chat_history = []
            st.session_state.solution_displayed = False
             # Reset other states as well
            st.session_state.last_question = None
            st.session_state.awaiting_solution = False
            st.session_state.last_question_type = None

        with st.spinner("📷 Reading the image..."):
            extracted_text = extract_text_from_image(uploaded_image)

        if extracted_text.startswith("[Error"):
            st.error(extracted_text)
        else:
            with st.spinner("🤖 Analyzing..."):
                answer, q_type = tutor_response(extracted_text)
                st.session_state.chat_history.append(("Student", f"📷 Image Question: *{extracted_text}*"))
                st.session_state.chat_history.append(("Tutor", answer))
                st.session_state.awaiting_solution = (q_type == "Math")
                st.session_state.last_question = extracted_text
                st.session_state.last_question_type = q_type
                if q_type == "Theory":
                    st.session_state.solution_displayed = True
            st.rerun()

# Show solution button (only for Math)
if st.session_state.awaiting_solution and st.session_state.last_question_type == "Math":
    st.info("💭 **Need more help?** I've given you some hints. When you're ready, I can show you the complete step-by-step solution!")
    
    if st.button("✅ YES, SHOW ME THE SOLUTION", use_container_width=True):
        with st.spinner("🧮 Working on the solution..."):
            answer, _ = tutor_response(st.session_state.last_question, request_solution=True)
            st.session_state.chat_history.append(("Tutor (Solution)", answer))
            st.session_state.awaiting_solution = False
            st.session_state.solution_displayed = True
        st.rerun()