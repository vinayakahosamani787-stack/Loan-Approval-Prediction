
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="LoanWise | AI Loan Intelligence",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# PREMIUM CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* GLOBAL BACKGROUND */
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0, 112, 255, 0.18), transparent 28%),
        radial-gradient(circle at 90% 25%, rgba(130, 60, 255, 0.15), transparent 30%),
        radial-gradient(circle at 50% 100%, rgba(0, 190, 255, 0.10), transparent 35%),
        #050505;
    color: white;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HIDE STREAMLIT BRANDING */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* HERO CARD */
.hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #ffffff 0%, #e9efff 55%, #dce5ff 100%);
    padding: 48px;
    border-radius: 28px;
    color: #080b16;
    margin-bottom: 30px;
    border: 1px solid rgba(255,255,255,0.9);
    box-shadow:
        0 25px 55px rgba(0, 0, 0, 0.65),
        0 0 35px rgba(75, 130, 255, 0.22),
        inset 0 3px 8px rgba(255,255,255,1);
    transition: all 0.35s ease;
}

.hero:hover {
    transform: translateY(-6px);
    box-shadow:
        0 32px 65px rgba(0,0,0,0.75),
        0 0 45px rgba(75,130,255,0.35);
}

.hero::after {
    content: "";
    position: absolute;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(65,120,255,0.22), transparent 70%);
    right: 5%;
    top: -65px;
    pointer-events: none;
}

.hero-tag {
    display: inline-block;
    background: #101a36;
    color: #ffffff;
    padding: 8px 16px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 18px;
}

.hero h1 {
    color: #080b16;
    font-size: 55px;
    font-weight: 900;
    letter-spacing: -2px;
    margin: 0;
}

.hero p {
    color: #39435a;
    font-size: 17px;
    line-height: 1.7;
    max-width: 700px;
}

.hero-highlight {
    color: #2459d6;
    font-weight: 900;
}

/* SECTION HEADINGS */
.section-title {
    color: #ffffff;
    font-size: 27px;
    font-weight: 900;
    letter-spacing: -0.5px;
}

.section-subtitle {
    color: #aeb7ca;
    font-size: 14px;
    margin-bottom: 20px;
}

/* METRIC CARDS */
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #ffffff, #e8edfa);
    padding: 24px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.9);
    box-shadow:
        0 18px 30px rgba(0,0,0,0.55),
        0 0 18px rgba(85,130,255,0.10),
        inset 0 3px 7px #ffffff;
    transition: all 0.3s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow:
        0 25px 40px rgba(0,0,0,0.65),
        0 0 25px rgba(85,130,255,0.25);
}

div[data-testid="stMetric"] label {
    color: #526078 !important;
    font-weight: 700 !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #101a36 !important;
    font-weight: 900 !important;
}

/* FORM PANEL */
div[data-testid="stForm"] {
    background: linear-gradient(145deg, #ffffff, #edf1fa);
    padding: 32px;
    border-radius: 25px;
    border: 1px solid #ffffff;
    box-shadow:
        0 22px 45px rgba(0,0,0,0.65),
        0 0 25px rgba(85,130,255,0.12),
        inset 0 3px 8px #ffffff;
}

/* FORM HEADINGS */
div[data-testid="stForm"] h4 {
    color: #101a36 !important;
    font-weight: 900;
    letter-spacing: 0.3px;
}

/* FORM LABELS */
div[data-testid="stForm"] label {
    color: #26334c !important;
    font-weight: 750 !important;
}

/* INPUT FIELDS */
div[data-testid="stForm"] input {
    background: #ffffff !important;
    color: #101a36 !important;
    border: 1px solid #cbd5e8 !important;
    border-radius: 12px !important;
}

/* SELECT BOXES */
div[data-testid="stForm"] div[data-baseweb="select"] > div {
    background: #ffffff !important;
    color: #101a36 !important;
    border: 1px solid #cbd5e8 !important;
    border-radius: 12px !important;
}

/* DROPDOWN TEXT */
div[data-testid="stForm"] [data-baseweb="select"] * {
    color: #101a36;
}

/* INPUT FOCUS */
div[data-testid="stForm"] input:focus {
    border: 1px solid #477bff !important;
    box-shadow: 0 0 0 3px rgba(71,123,255,0.15) !important;
}

/* PREDICTION BUTTON */
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #101a36, #2459d6, #6339c9);
    color: #ffffff !important;
    border: none;
    border-radius: 15px;
    height: 58px;
    width: 100%;
    font-size: 16px;
    font-weight: 900;
    letter-spacing: 1px;
    box-shadow:
        0 9px 0 #17264c,
        0 15px 28px rgba(35,80,200,0.35);
    transition: all 0.25s ease;
}

div[data-testid="stFormSubmitButton"] button:hover {
    transform: translateY(-4px);
    box-shadow:
        0 12px 0 #17264c,
        0 20px 35px rgba(35,80,200,0.5);
    border: none;
}

div[data-testid="stFormSubmitButton"] button p {
    color: white !important;
}

/* RESULT CARDS */
.result-approved,
.result-rejected {
    padding: 38px;
    border-radius: 25px;
    text-align: center;
    background: linear-gradient(145deg, #ffffff, #edf1fa);
    box-shadow:
        0 20px 40px rgba(0,0,0,0.6),
        inset 0 3px 8px #ffffff;
    transition: all 0.3s ease;
}

.result-approved {
    border: 2px solid #35c879;
    color: #12632f;
}

.result-rejected {
    border: 2px solid #f06464;
    color: #a32121;
}

.result-approved:hover,
.result-rejected:hover {
    transform: translateY(-6px);
}

.result-icon {
    font-size: 55px;
    margin-bottom: 10px;
}

.result-approved h2,
.result-rejected h2 {
    font-weight: 900;
    letter-spacing: 1px;
}

.result-approved p,
.result-rejected p {
    font-size: 15px;
    color: #414b5e;
}

/* DIVIDERS */
hr {
    border-color: #343c4d !important;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #8994a9;
    font-size: 13px;
    padding-top: 35px;
    line-height: 1.8;
}

/* MOBILE RESPONSIVENESS */
@media (max-width: 768px) {
    .hero {
        padding: 28px;
    }

    .hero h1 {
        font-size: 38px;
    }

    div[data-testid="stForm"] {
        padding: 18px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

@st.cache_resource
def load_model():
    return joblib.load("models/best_model.pkl")


try:
    model = load_model()
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()


# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">✦ AI POWERED FINANCIAL INTELLIGENCE</div>
    <h1>LoanWise<span style="color:#2459d6;">.</span></h1>
    <p>
        Your intelligent loan prediction assistant.
        Experience smarter financial insights powered by
        <span class="hero-highlight">Machine Learning.</span>
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# METRIC CARDS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🤖 AI MODEL", "Logistic Regression")

with col2:
    st.metric("🎯 TEST ACCURACY", "86.18%")

with col3:
    st.metric("⚡ SYSTEM", "AI Prediction")


st.write("")
st.markdown(
    '<div class="section-title">✦ Loan Application</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Complete the applicant details to generate an AI-based prediction.'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# APPLICANT FORM
# ==========================================

with st.form("loan_prediction_form"):

    st.markdown("#### 👤 PERSONAL INFORMATION")

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])

    with col2:
        married = st.selectbox("Marital Status", ["Yes", "No"])

    with col3:
        dependents = st.selectbox(
            "Dependents",
            ["0", "1", "2", "3+"]
        )

    col1, col2 = st.columns(2)

    with col1:
        education = st.selectbox(
            "Education",
            ["Graduate", "Not Graduate"]
        )

    with col2:
        self_employed = st.selectbox(
            "Self Employed",
            ["Yes", "No"]
        )

    st.divider()

    st.markdown("#### 💳 FINANCIAL INFORMATION")

    col1, col2 = st.columns(2)

    with col1:
        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0,
            value=5000,
            step=500
        )

        coapplicant_income = st.number_input(
            "Co-applicant Income",
            min_value=0,
            value=0,
            step=500
        )

        loan_amount = st.number_input(
            "Loan Amount (in thousands)",
            min_value=0.0,
            value=150.0,
            step=10.0
        )

    with col2:
        loan_term = st.selectbox(
            "Loan Term (months)",
            [360, 180, 120, 84, 60, 36, 12]
        )

        credit_history = st.selectbox(
            "Credit History",
            [1.0, 0.0],
            format_func=lambda x:
            "Good Credit History" if x == 1.0
            else "Poor Credit History"
        )

        property_area = st.selectbox(
            "Property Area",
            ["Urban", "Semiurban", "Rural"]
        )

    st.write("")

    submit_button = st.form_submit_button(
        "✦  GENERATE LOAN PREDICTION"
    )


# ==========================================
# PREDICTION RESULT
# ==========================================

if submit_button:

    input_data = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    try:
        prediction = model.predict(input_data)[0]

        st.divider()

        st.markdown(
            '<div class="section-title">✦ AI Prediction Result</div>',
            unsafe_allow_html=True
        )

        if prediction == 1:
            st.markdown("""
            <div class="result-approved">
                <div class="result-icon">✓</div>
                <h2>LOAN PREDICTED: APPROVED</h2>
                <p>
                    The model predicts that this application
                    belongs to the approved category.
                </p>
                <h3>RESULT: Y</h3>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="result-rejected">
                <div class="result-icon">✕</div>
                <h2>LOAN PREDICTED: REJECTED</h2>
                <p>
                    The model predicts that this application
                    belongs to the rejected category.
                </p>
                <h3>RESULT: N</h3>
            </div>
            """, unsafe_allow_html=True)

        st.caption(
            "This is a machine-learning prediction, "
            "not an actual bank decision."
        )

    except Exception as e:
        st.error(f"Prediction error: {e}")


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    <hr>
    <b>LOANWISE · AI LOAN INTELLIGENCE</b><br>
    Built with Python · Scikit-learn · Streamlit<br>
    Educational project demonstration only.
    Predictions are not guarantees of loan approval.
</div>
""", unsafe_allow_html=True)
