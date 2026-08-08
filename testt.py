import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Spa CRM | Business Analyst Case Study",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# GLOBAL THEME / CSS
# =========================================================

st.markdown(
    """
    <style>

    :root {
        --primary-color: #194339;
        --primary-dark: #12352d;
        --background: #ffffff;
        --soft-background: #f4f7f6;
        --text-color: #1f2937;
        --muted-text: #66736f;
        --border-color: #dfe7e4;
    }

    /* Main page */
    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    body {
        color: var(--text-color);
    }

    /* Headings */
    h1 {
        color: var(--primary-color) !important;
        font-size: 3rem !important;
        font-weight: 750 !important;
    }

    h2,
    h3,
    h4 {
        color: var(--primary-color) !important;
    }

    h2 {
        margin-top: 2rem !important;
    }

    /* Hero */
    .hero {
        padding: 2.5rem;
        background-color: var(--soft-background);
        border: 1px solid var(--border-color);
        border-radius: 18px;
        margin-bottom: 2rem;
    }

    .hero h1 {
        margin-bottom: 0.8rem;
    }

    .hero p {
        color: var(--text-color);
        line-height: 1.7;
    }

    /* Small labels */
    .small-label {
        font-size: 0.8rem;
        color: var(--primary-color);
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.5rem;
    }

    /* Cards */
    .card {
        padding: 1.3rem;
        border: 1px solid var(--border-color);
        border-radius: 14px;
        background-color: #ffffff;
        height: 100%;
    }

    /* Highlight */
    .highlight {
        padding: 1rem 1.2rem;
        border-left: 4px solid var(--primary-color);
        background-color: var(--soft-background);
        margin: 1rem 0;
    }

    /* Project overview */
    .project-overview h2 {
        color: var(--primary-color) !important;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .project-overview p {
        font-size: 1.15rem;
        line-height: 1.8;
        color: var(--text-color);
        margin-bottom: 1.4rem;
    }

    .project-overview strong {
        color: var(--primary-color);
        font-weight: 700;
    }

    /* Buttons */
    div.stButton > button,
    div.stDownloadButton > button {
        background-color: var(--primary-color);
        color: #ffffff;
        border: 1px solid var(--primary-color);
        border-radius: 8px;
    }

    div.stButton > button:hover,
    div.stDownloadButton > button:hover {
        background-color: var(--primary-dark);
        color: #ffffff;
        border-color: var(--primary-dark);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: var(--soft-background);
        border-right: 1px solid var(--border-color);
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: var(--primary-color) !important;
    }

    /* Alerts */
    [data-testid="stAlert"] {
        border-radius: 10px;
    }

    /* Dataframes */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border-color);
        border-radius: 10px;
        overflow: hidden;
    }

    /* Footer */
    .footer {
        margin-top: 4rem;
        padding-top: 1.5rem;
        border-top: 1px solid var(--border-color);
        font-size: 0.9rem;
        color: var(--muted-text);
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.title("Spa CRM")
st.sidebar.caption("Business Analyst Case Study")

page = st.sidebar.radio(
    "Case Study",
    [
        "01 · Project Overview",
        "02 · Business Problem",
        "03 · Current-State Analysis",
        "04 · Requirements Gathering",
        "05 · CRM Evaluation",
        "06 · CRM Selection",
        "07 · Future-State Design",
        "08 · Implementation",
        "09 · Testing & UAT",
        "10 · Go-Live & Adoption",
        "11 · Benefits & Review",
        "12 · Traceability",
    ],
)

st.sidebar.divider()

st.sidebar.markdown(
    """
**BA Techniques**

- Stakeholder Analysis
- BPMN / Process Mapping
- Root Cause Analysis
- Requirements Analysis
- MoSCoW Prioritisation
- Weighted Decision Matrix
- Fit-Gap Analysis
- User Stories
- UAT
- Benefits Realisation
"""
)

# =========================================================
# SHARED DATA
# =========================================================

business_problems = pd.DataFrame(
    [
        {
            "ID": "P01",
            "Problem": "Customer information is scattered across multiple channels",
            "Impact": "Staff spend additional time finding information and records may be duplicated or incomplete.",
        },
        {
            "ID": "P02",
            "Problem": "Staff cannot easily access complete customer history",
            "Impact": "Limited visibility of previous visits, treatments and interactions reduces service personalisation.",
        },
        {
            "ID": "P03",
            "Problem": "Booking confirmations and follow-ups are inconsistent",
            "Impact": "Customers may not receive timely communication and staff rely on manual follow-up.",
        },
        {
            "ID": "P04",
            "Problem": "Customers sometimes miss appointments",
            "Impact": "Lost revenue, unused therapist capacity and disruption to scheduling.",
        },
        {
            "ID": "P05",
            "Problem": "Management has limited retention and service-performance reporting",
            "Impact": "Management cannot easily identify trends or support data-driven decisions.",
        },
    ]
)

requirements = pd.DataFrame(
    [
        ["BR-01", "Business", "Centralise customer information to provide staff with a consistent customer view.", "Must"],
        ["BR-02", "Business", "Improve access to customer booking and service history.", "Must"],
        ["BR-03", "Business", "Standardise appointment booking and confirmation.", "Must"],
        ["BR-04", "Business", "Reduce manual effort in appointment communication and follow-up.", "Must"],
        ["BR-05", "Business", "Improve visibility of customer retention and service performance.", "Should"],

        ["FR-01", "Functional", "Allow authorised staff to create a customer profile.", "Must"],
        ["FR-02", "Functional", "Search customers by name, phone number or email.", "Must"],
        ["FR-03", "Functional", "Display customer information in a single profile.", "Must"],
        ["FR-04", "Functional", "Display previous appointments associated with the customer.", "Must"],
        ["FR-05", "Functional", "Allow authorised staff to update customer information.", "Must"],
        ["FR-06", "Functional", "Identify potential duplicate customer records.", "Should"],
        ["FR-07", "Functional", "Display available appointment time slots.", "Must"],
        ["FR-08", "Functional", "Display therapist availability.", "Must"],
        ["FR-09", "Functional", "Allow staff to create customer appointments.", "Must"],
        ["FR-10", "Functional", "Link each appointment to the relevant customer profile.", "Must"],
        ["FR-11", "Functional", "Prevent conflicting therapist bookings.", "Must"],
        ["FR-12", "Functional", "Allow staff to reschedule or cancel appointments.", "Must"],
        ["FR-13", "Functional", "Automatically send confirmation when an appointment is created.", "Must"],
        ["FR-14", "Functional", "Support configured communication channels for confirmations.", "Should"],
        ["FR-15", "Functional", "Automatically send appointment reminders based on configured rules.", "Must"],
        ["FR-16", "Functional", "Allow staff to view appointment communication status.", "Should"],
        ["FR-17", "Functional", "Provide appointment-volume reporting.", "Should"],
        ["FR-18", "Functional", "Report cancellation and no-show rates.", "Should"],
        ["FR-19", "Functional", "Provide customer retention and repeat-visit reporting.", "Should"],
        ["FR-20", "Functional", "Provide service-performance reporting.", "Should"],

        ["NFR-01", "Non-Functional", "Return customer search results within two seconds under normal operating conditions.", "Should"],
        ["NFR-02", "Non-Functional", "Require authenticated user access.", "Must"],
        ["NFR-03", "Non-Functional", "Control customer-data access based on staff roles.", "Must"],
        ["NFR-04", "Non-Functional", "Support common booking activities with minimal navigation.", "Should"],
        ["NFR-05", "Non-Functional", "Be available during normal spa operating hours.", "Must"],
        ["NFR-06", "Non-Functional", "Provide traceability for changes to key customer and appointment data.", "Should"],
        ["NFR-07", "Non-Functional", "Handle personal information according to applicable privacy requirements.", "Must"],
    ],
    columns=["ID", "Type", "Requirement", "Priority"],
)

traceability = pd.DataFrame(
    [
        ["P01", "BR-01", "FR-01 / FR-02 / FR-03", "US-01", "UAT-01"],
        ["P02", "BR-02", "FR-04", "US-02", "UAT-02"],
        ["P03", "BR-03 / BR-04", "FR-13 / FR-15", "US-03", "UAT-03"],
        ["P04", "BR-04", "FR-15 / FR-18", "US-04", "UAT-04"],
        ["P05", "BR-05", "FR-17 / FR-18 / FR-19 / FR-20", "US-05", "UAT-05"],
    ],
    columns=[
        "Business Problem",
        "Business Requirement",
        "Functional Requirement",
        "User Story",
        "UAT",
    ],
)

# =========================================================
# HELPER COMPONENTS
# =========================================================

def page_header(number, title, description):
    st.caption(f"SECTION {number}")
    st.title(title)
    st.write(description)
    st.divider()


def footer():
    st.markdown(
        """
        <div class="footer">
        Spa CRM Selection & Implementation — Business Analyst Portfolio Case Study
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 01 PROJECT OVERVIEW
# =========================================================
if page == "01 · Project Overview":

    st.markdown(
        """
<div class="hero">
<div class="small-label">Business Analyst Portfolio Project</div>

<h1>Spa CRM Selection & Implementation</h1>

<p style="font-size:1.2rem;">
Analysing customer-management challenges, defining CRM requirements,
evaluating suitable solutions and planning implementation for a
spa services business.
</p>
</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("#### Role")
        st.write("Business Analyst")

    with c2:
        st.markdown("#### Project Type")
        st.write("CRM Selection & Implementation")

    with c3:
        st.markdown("#### Industry")
        st.write("Spa & Wellness Services")

    st.divider()

    st.markdown(
        """
<div class="project-overview">

<h2>Project Overview | Background</h2>

<p>
Wellness Perth Spa is a medium-sized wellness business with
<strong>three locations across WA</strong>.
Customer information, appointments, and interactions are currently managed through
<strong>Excel and disconnected communication channels</strong>,
making it difficult for staff to access complete customer histories
and for management to track performance.
</p>

<p>
Over the past two years,
<strong>missed bookings, late reminders, and inconsistent communication</strong>
have contributed to increasing customer complaints,
lower satisfaction, and declining customer retention.
</p>

<p>
This project aims to
<strong>identify and implement the best-fit CRM solution</strong>
to improve customer management, operational efficiency,
and customer experience.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.header("Project Objective")

    st.info(
        """
Identify the business needs, evaluate suitable CRM solutions and define an
implementation approach that improves customer information management,
appointment communication and management reporting.
"""
    )

    st.header("Key Deliverables")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Discovery")
        st.markdown(
            """
- Problem statement
- Stakeholder analysis
- Root cause analysis
- As-Is process
"""
        )

    with col2:
        st.markdown("### Solution")
        st.markdown(
            """
- Requirements catalogue
- CRM evaluation matrix
- Fit-gap analysis
- To-Be process
"""
        )

    with col3:
        st.markdown("### Delivery")
        st.markdown(
            """
- User stories
- UAT scenarios
- Training plan
- Benefits framework
"""
        )

    footer()

# =========================================================
# 02 BUSINESS PROBLEM
# =========================================================

elif page == "02 · Business Problem":

    page_header(
        "02",
        "Business Problem",
        "Understanding the operational challenges affecting customer management, appointment handling and business performance.",
    )

    # =====================================================
    # PROBLEM STATEMENT
    # =====================================================

    st.markdown(
        """
<div class="business-problem-section">

<h2>Problem Statement</h2>

<p>
Wellness Perth Spa relies on
<strong>Excel spreadsheets and disconnected communication channels</strong>
to manage customer information and appointments. This results in
<strong>fragmented customer records, inconsistent appointment reminders, and limited visibility into customer activity and retention.</strong>
These issues have contributed to increasing customer complaints,
lower customer satisfaction, and declining return customer rates,
highlighting the need for a more
<strong>centralised and reliable customer management solution.</strong>
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # CURRENT PAIN POINTS
    # =====================================================

    st.markdown(
        """
<style>

.business-problem-section {
    margin-bottom: 2.5rem;
}

.business-problem-section h2 {
    color: #194339 !important;
    font-size: 1.7rem;
    font-weight: 700;
    margin-bottom: 1.2rem;
}

.business-problem-section p {
    color: #1f2937;
    font-size: 1.15rem;
    line-height: 1.85;
    margin: 0;
}

.business-problem-section strong {
    color: #194339;
    font-weight: 700;
}

.pain-points-card {
    background-color: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 18px;
    padding: 2rem 2.2rem;
    margin-top: 1rem;
    margin-bottom: 2.5rem;
    box-shadow: 0 4px 14px rgba(25, 67, 57, 0.08);
}

.pain-points-title {
    color: #194339;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.pain-point-row {
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
    margin-bottom: 1.25rem;
}

.pain-point-row:last-child {
    margin-bottom: 0;
}

.pain-point-icon {
    color: #d64545;
    font-size: 1.55rem;
    font-weight: 300;
    line-height: 1.35;
    flex-shrink: 0;
}

.pain-point-text {
    color: #374151;
    font-size: 1.08rem;
    line-height: 1.65;
}

.pain-point-text strong {
    color: #194339;
    font-weight: 700;
}

</style>

<div class="pain-points-card">

<div class="pain-points-title">CURRENT PAIN POINTS</div>

<div class="pain-point-row">
<div class="pain-point-icon">×</div>
<div class="pain-point-text">
<strong>Fragmented customer data</strong> — customer information is stored across multiple Excel spreadsheets
</div>
</div>

<div class="pain-point-row">
<div class="pain-point-icon">×</div>
<div class="pain-point-text">
<strong>No complete customer view</strong> — staff cannot easily access customer history across locations
</div>
</div>

<div class="pain-point-row">
<div class="pain-point-icon">×</div>
<div class="pain-point-text">
<strong>Manual booking management</strong> — appointment tracking relies heavily on manual processes
</div>
</div>

<div class="pain-point-row">
<div class="pain-point-icon">×</div>
<div class="pain-point-text">
<strong>Inconsistent reminders</strong> — customers receive late or missed appointment reminders
</div>
</div>

<div class="pain-point-row">
<div class="pain-point-icon">×</div>
<div class="pain-point-text">
<strong>Limited reporting</strong> — management lacks visibility into customer retention and service performance
</div>
</div>

<div class="pain-point-row">
<div class="pain-point-icon">×</div>
<div class="pain-point-text">
<strong>Declining customer experience</strong> — increasing complaints and fewer returning customers
</div>
</div>

</div>
""",
        unsafe_allow_html=True,
    )

     # =====================================================
    # ROOT CAUSE ANALYSIS
    # =====================================================

    st.markdown(
        """
<style>

.root-cause-section {
    margin-top: 3.5rem;
    margin-bottom: 1.5rem;
}

.root-cause-section h2 {
    color: #194339 !important;
    font-size: 2rem;
    font-weight: 750;
    margin-bottom: 0.8rem;
}

.root-cause-intro {
    font-size: 1.05rem;
    line-height: 1.75;
    color: #374151;
    max-width: 1050px;
    margin-bottom: 1rem;
}

.root-cause-intro strong {
    color: #194339;
    font-weight: 700;
}

.root-analysis-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-top: 2rem;
    margin-bottom: 2.5rem;
}

.analysis-card {
    background: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    box-shadow: 0 3px 12px rgba(25, 67, 57, 0.06);
}

.analysis-card h3 {
    color: #194339 !important;
    font-size: 1.05rem;
    margin-top: 0 !important;
    margin-bottom: 1rem;
}

.analysis-card ul {
    padding-left: 1.25rem;
    margin-bottom: 0;
}

.analysis-card li {
    color: #374151;
    line-height: 1.65;
    margin-bottom: 0.9rem;
}

.analysis-card strong {
    color: #194339;
    font-weight: 700;
}

.convergence-card {
    background: #fff9eb;
    border: 1px solid #e0c274;
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
}

.convergence-card h3 {
    color: #7b5900 !important;
    font-size: 1.05rem;
    margin-top: 0 !important;
    margin-bottom: 1rem;
}

.convergence-card p {
    color: #745b1e;
    line-height: 1.7;
}

.convergence-card strong {
    color: #5f4500;
    font-weight: 700;
}

@media (max-width: 900px) {

    .root-analysis-grid {
        grid-template-columns: 1fr;
    }

}

</style>

<div class="root-cause-section">

<h2>Why are customer complaints increasing and retention declining?</h2>

<div class="root-cause-intro">
A <strong>Fishbone (Ishikawa) analysis</strong> with Five-Whys drill-downs
identifies the underlying causes behind
<strong>missed bookings, late reminders, fragmented customer information,
and poor management visibility</strong>.
The analysis suggests that these are not isolated staff or booking issues.
They largely stem from the business continuing to rely on
<strong>manual and disconnected customer-management processes</strong>
as it has expanded across multiple locations.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # FISHBONE IMAGE
    # fishbone.png is in the same folder as testt.py
    # =====================================================

    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent
    fishbone_path = BASE_DIR / "fishbone.png"

    if fishbone_path.exists():

        st.image(
            str(fishbone_path),
            use_container_width=True,
        )

    else:

        st.error(
            "Fishbone image could not be found. "
            "Make sure fishbone.png is in the same GitHub folder as testt.py."
        )

    # =====================================================
    # FIVE WHYS — PARALLEL ANALYSIS
    # =====================================================

    st.markdown(
        """
<style>

/* =====================================================
   FIVE WHYS
===================================================== */

.five-whys-section {
    margin-top: 2.8rem;
    margin-bottom: 3rem;
}

.five-whys-section h2 {
    color: #194339 !important;
    font-size: 1.8rem;
    font-weight: 750;
    margin-bottom: 0.5rem;
}

.five-whys-subtitle {
    color: #6b7280;
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 2rem;
}


/* THREE PARALLEL CHAINS */

.whys-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.4rem;
    align-items: stretch;
}


/* EACH ANALYSIS COLUMN */

.whys-column {
    background: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 16px;
    padding: 1.4rem;
    box-shadow: 0 3px 12px rgba(25, 67, 57, 0.06);
}


/* COLUMN TITLE */

.whys-column-title {
    color: #194339;
    font-size: 1.05rem;
    font-weight: 750;
    line-height: 1.4;
    min-height: 48px;
    margin-bottom: 1.2rem;
}


/* FLOW */

.why-flow {
    display: flex;
    flex-direction: column;
}


/* NORMAL BOX */

.why-box {
    background: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 10px;
    padding: 0.85rem 0.9rem;
    color: #374151;
    font-size: 0.92rem;
    line-height: 1.5;
    text-align: center;
}


/* EVIDENCE / STARTING PROBLEM */

.why-box.evidence {
    background: #f4f7f6;
    border: 1px solid #b8ccc6;
    color: #194339;
    font-weight: 650;
}


/* ROOT CAUSE */

.why-box.root {
    background: #194339;
    border-color: #194339;
    color: #ffffff;
    font-weight: 700;
}


/* ARROWS */

.why-arrow {
    text-align: center;
    color: #194339;
    font-size: 1.3rem;
    font-weight: 700;
    height: 32px;
    line-height: 32px;
}


/* =====================================================
   CONVERGENCE
===================================================== */

.convergence-section {
    margin-top: 3rem;
    margin-bottom: 2rem;
}

.convergence-section h2 {
    color: #194339 !important;
    font-size: 1.8rem;
    font-weight: 750;
    margin-bottom: 1rem;
}

.convergence-section p {
    font-size: 1.08rem;
    line-height: 1.8;
    color: #374151;
}


/* CONVERGENCE ARROWS */

.convergence-arrows {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    text-align: center;
    color: #194339;
    font-size: 1.8rem;
    margin-top: 0.5rem;
    margin-bottom: 0.4rem;
}


/* MAIN CONVERGENCE RESULT */

.convergence-highlight {
    background: #194339;
    color: #ffffff;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin: 0 auto 1.7rem auto;
    text-align: center;
    font-size: 1.15rem;
    font-weight: 700;
    max-width: 900px;
    line-height: 1.55;
}


/* CASE STUDY NOTE */

.simulated-note {
    margin-top: 1.5rem;
    padding: 0.9rem 1rem;
    background: #fff9eb;
    border: 1px solid #e0c274;
    border-radius: 10px;
    color: #745b1e;
    font-size: 0.92rem;
    line-height: 1.6;
}


/* =====================================================
   RESPONSIVE
===================================================== */

@media (max-width: 900px) {

    .whys-grid {
        grid-template-columns: 1fr;
    }

    .whys-column-title {
        min-height: auto;
    }

    .convergence-arrows {
        display: none;
    }

}

</style>


<div class="five-whys-section">

<h2>Five-Whys — where each cause bottoms out</h2>

<div class="five-whys-subtitle">
Three key business symptoms were investigated to identify the underlying
process, data and reporting issues.
</div>


<div class="whys-grid">


<!-- =================================================
     CHAIN 1
================================================= -->

<div class="whys-column">

<div class="whys-column-title">
Late / missed reminders
</div>

<div class="why-flow">

<div class="why-box evidence">
~14% of appointment reminders are not sent on time
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
Reminders depend on staff manually reviewing appointments
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
Workload and processes differ across locations
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
No automated reminder workflow
</div>

<div class="why-arrow">↓</div>

<div class="why-box root">
Customer communication relies on manual processes that no longer scale
</div>

</div>
</div>


<!-- =================================================
     CHAIN 2
================================================= -->

<div class="whys-column">

<div class="whys-column-title">
Booking / customer-data errors
</div>

<div class="why-flow">

<div class="why-box evidence">
~18% of records are duplicate or incomplete
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
Information is maintained across different spreadsheets
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
Staff update customer information independently
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
No shared customer record across locations
</div>

<div class="why-arrow">↓</div>

<div class="why-box root">
No central source of truth for customer information
</div>

</div>
</div>


<!-- =================================================
     CHAIN 3
================================================= -->

<div class="whys-column">

<div class="whys-column-title">
Declining retention visibility
</div>

<div class="why-flow">

<div class="why-box evidence">
Return rate fell from 61% to 47% before the trend was clearly identified
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
Management reporting is manually prepared
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
Data must be consolidated across spreadsheets
</div>

<div class="why-arrow">↓</div>

<div class="why-box">
No central reporting capability
</div>

<div class="why-arrow">↓</div>

<div class="why-box root">
Management lacks timely customer-performance information
</div>

</div>
</div>


</div>
</div>


<!-- =====================================================
     CONVERGENCE INSIGHT
===================================================== -->

<div class="convergence-section">

<h2>Convergence insight</h2>

<p>
All three drill-downs converge on one underlying issue:
</p>


<div class="convergence-arrows">
<div>↘</div>
<div>↓</div>
<div>↙</div>
</div>


<div class="convergence-highlight">
Customer-management capability has not scaled with business growth.
</div>


<p>
Wellness Perth Spa expanded to three locations while continuing to rely on
<strong>Excel, manual workflows and disconnected communication channels</strong>.
This has created fragmented customer data, inconsistent processes and limited
management visibility — contributing to booking errors, missed reminders and
declining customer retention.
</p>


<div class="simulated-note">
<strong>Case-study note:</strong>
Figures shown are simulated for this case study and are used to establish a
measurable project baseline.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    footer()

# =========================================================
# 03 CURRENT-STATE ANALYSIS
# =========================================================

elif page == "03 · Current-State Analysis":

    page_header(
        "03",
        "Current-State Analysis",
        "Understanding how customer information and appointment booking are currently managed before defining the future-state solution.",
    )

    # =====================================================
    # SECTION STYLING
    # =====================================================

    st.markdown(
        """
<style>

.current-state-intro {
    margin-bottom: 2rem;
}

.current-state-intro h2 {
    color: #194339 !important;
    font-size: 1.8rem;
    font-weight: 750;
    margin-bottom: 0.8rem;
}

.current-state-intro p {
    color: #374151;
    font-size: 1.05rem;
    line-height: 1.75;
    max-width: 1050px;
}

.current-state-intro strong {
    color: #194339;
    font-weight: 700;
}


/* ============================================
   FINDINGS
============================================ */

.current-findings {
    margin-top: 2.5rem;
    margin-bottom: 2rem;
}

.current-findings h2 {
    color: #194339 !important;
    font-size: 1.8rem;
    font-weight: 750;
    margin-bottom: 1.3rem;
}

.findings-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.2rem;
}

.finding-card {
    background: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 14px;
    padding: 1.3rem 1.4rem;
    box-shadow: 0 3px 10px rgba(25, 67, 57, 0.05);
}

.finding-number {
    color: #194339;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    margin-bottom: 0.5rem;
}

.finding-title {
    color: #194339;
    font-weight: 700;
    font-size: 1.05rem;
    margin-bottom: 0.4rem;
}

.finding-text {
    color: #4b5563;
    font-size: 0.96rem;
    line-height: 1.6;
}


/* ============================================
   ANALYSIS INSIGHT
============================================ */

.current-state-insight {
    background: #f4f7f6;
    border-left: 5px solid #194339;
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    margin-top: 2rem;
    margin-bottom: 2rem;
}

.current-state-insight strong {
    color: #194339;
}


/* ============================================
   MOBILE
============================================ */

@media (max-width: 800px) {

    .findings-grid {
        grid-template-columns: 1fr;
    }

}

</style>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # AS-IS PROCESS
    # =====================================================

    st.markdown(
        """
<div class="current-state-intro">

<h2>As-Is Process</h2>

<p>
The current-state process was mapped to understand how a customer enquiry
moves from initial contact through to appointment confirmation.
The analysis highlights where
<strong>manual activities, disconnected information sources and inconsistent processes</strong>
create operational inefficiencies.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # AS-IS PROCESS IMAGE
    # Image is in same directory as testt.py
    # =====================================================

    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent
    as_is_path = BASE_DIR / "AS-IS process.png"

    if as_is_path.exists():

        st.image(
            str(as_is_path),
            use_container_width=True,
        )

    else:

        st.error(
            "As-Is process image could not be found. "
            "Make sure 'AS-IS process.png' is in the same GitHub folder as testt.py."
        )

    # =====================================================
    # KEY CURRENT-STATE FINDINGS
    # =====================================================

    st.markdown(
        """
<div class="current-findings">

<h2>Key Current-State Findings</h2>

<div class="findings-grid">


<div class="finding-card">

<div class="finding-number">01</div>

<div class="finding-title">
Multiple information sources
</div>

<div class="finding-text">
Staff may need to search spreadsheets, booking information and
communication channels to identify an existing customer and understand
their previous interactions.
</div>

</div>


<div class="finding-card">

<div class="finding-number">02</div>

<div class="finding-title">
No complete customer view
</div>

<div class="finding-text">
Customer information and appointment history are not maintained in a
single shared record, limiting visibility across the three locations.
</div>

</div>


<div class="finding-card">

<div class="finding-number">03</div>

<div class="finding-title">
Manual appointment activities
</div>

<div class="finding-text">
Several booking, confirmation and follow-up activities depend on staff
remembering to complete manual steps.
</div>

</div>


<div class="finding-card">

<div class="finding-number">04</div>

<div class="finding-title">
Inconsistent processes
</div>

<div class="finding-text">
Customer information and booking activities may be handled differently
between staff members and locations because there is no centralised
workflow.
</div>

</div>


<div class="finding-card">

<div class="finding-number">05</div>

<div class="finding-title">
Limited process visibility
</div>

<div class="finding-text">
Management cannot easily monitor customer activity, missed appointments
or follow-up performance without manually consolidating information.
</div>

</div>


<div class="finding-card">

<div class="finding-number">06</div>

<div class="finding-title">
Process does not scale efficiently
</div>

<div class="finding-text">
The current spreadsheet-based approach becomes increasingly difficult
to coordinate as customer volume and cross-location activity increase.
</div>

</div>


</div>

</div>


<div class="current-state-insight">

<strong>Current-state insight:</strong>
The process analysis confirms that customer-data fragmentation,
manual booking activities and inconsistent workflows are embedded
throughout the customer journey rather than occurring at a single step.

</div>
""",
        unsafe_allow_html=True,
    )

    footer()

# =========================================================
# 04 REQUIREMENTS GATHERING
# =========================================================

elif page == "04 · Requirements Gathering":

    page_header(
        "04",
        "Requirements Gathering",
        "Translating stakeholder needs, current-state findings and business objectives into structured CRM requirements.",
    )

    # =====================================================
    # STYLING
    # =====================================================

    st.markdown(
        """
<style>

.requirements-intro {
    margin-bottom: 2.5rem;
}

.requirements-intro h2 {
    color: #194339 !important;
    font-size: 1.8rem;
    font-weight: 750;
    margin-bottom: 0.8rem;
}

.requirements-intro p {
    color: #374151;
    font-size: 1.05rem;
    line-height: 1.75;
    max-width: 1050px;
}

.requirements-intro strong {
    color: #194339;
    font-weight: 700;
}


/* STAKEHOLDERS */

.stakeholder-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 1rem;
    margin-top: 1.5rem;
    margin-bottom: 3rem;
}

.stakeholder-card {
    background: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 14px;
    padding: 1.2rem;
    box-shadow: 0 3px 10px rgba(25, 67, 57, 0.05);
}

.stakeholder-card h3 {
    color: #194339 !important;
    font-size: 1rem;
    margin-top: 0 !important;
    margin-bottom: 0.7rem;
}

.stakeholder-card p {
    font-size: 0.92rem;
    color: #4b5563;
    line-height: 1.55;
}


/* ELICITATION */

.elicitation-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    margin-top: 1.3rem;
    margin-bottom: 3rem;
}

.elicitation-card {
    background: #f4f7f6;
    border: 1px solid #dfe7e4;
    border-radius: 14px;
    padding: 1.3rem;
}

.elicitation-number {
    color: #194339;
    font-size: 0.8rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
}

.elicitation-title {
    color: #194339;
    font-weight: 700;
    font-size: 1.05rem;
    margin-bottom: 0.5rem;
}

.elicitation-text {
    color: #4b5563;
    line-height: 1.6;
    font-size: 0.95rem;
}


/* INSIGHT TO REQUIREMENT */

.requirement-flow {
    margin-top: 1.5rem;
    margin-bottom: 3rem;
}

.requirement-flow-box {
    background: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    text-align: center;
    color: #374151;
    font-size: 1rem;
    line-height: 1.6;
}

.requirement-flow-box strong {
    color: #194339;
}

.requirement-flow-box.final {
    background: #194339;
    color: #ffffff;
    border-color: #194339;
}

.requirement-flow-box.final strong {
    color: #ffffff;
}

.requirement-arrow {
    text-align: center;
    color: #194339;
    font-size: 1.5rem;
    margin: 0.4rem 0;
}


/* MOSCOW */

.moscow-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-top: 1.5rem;
    margin-bottom: 2.5rem;
}

.moscow-card {
    border: 1px solid #dfe7e4;
    border-radius: 14px;
    padding: 1.2rem;
    background: #ffffff;
}

.moscow-card h3 {
    color: #194339 !important;
    margin-top: 0 !important;
    font-size: 1rem;
}

.moscow-card p {
    color: #4b5563;
    line-height: 1.7;
    font-size: 0.92rem;
}


/* MOBILE */

@media (max-width: 1000px) {

    .stakeholder-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .moscow-grid {
        grid-template-columns: repeat(2, 1fr);
    }

}

@media (max-width: 700px) {

    .stakeholder-grid,
    .elicitation-grid,
    .moscow-grid {
        grid-template-columns: 1fr;
    }

}

</style>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # INTRODUCTION
    # =====================================================

    st.markdown(
        """
<div class="requirements-intro">

<h2>Requirements Gathering Approach</h2>

<p>
Requirements were gathered by combining
<strong>stakeholder needs, current-state process findings and business objectives</strong>.
The purpose was to define what the future customer-management capability
must support before evaluating potential CRM solutions.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # STAKEHOLDERS
    # =====================================================

    st.subheader("Stakeholders")

    st.markdown(
        """
<div class="stakeholder-grid">

<div class="stakeholder-card">
<h3>Spa Manager</h3>
<p>
Needs visibility into customer retention, service performance,
operational activity and business reporting.
</p>
</div>

<div class="stakeholder-card">
<h3>Receptionist</h3>
<p>
Needs fast customer lookup, simple booking,
appointment management and reduced manual administration.
</p>
</div>

<div class="stakeholder-card">
<h3>Therapist</h3>
<p>
Needs access to relevant customer history,
previous services, notes and customer preferences.
</p>
</div>

<div class="stakeholder-card">
<h3>Marketing</h3>
<p>
Needs customer segmentation, retention information
and reliable data for targeted campaigns.
</p>
</div>

<div class="stakeholder-card">
<h3>Customer</h3>
<p>
Needs an easy booking experience, accurate confirmations,
timely reminders and appropriate handling of personal information.
</p>
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # ELICITATION METHODS
    # =====================================================

    st.subheader("Elicitation Methods")

    st.markdown(
        """
<div class="elicitation-grid">

<div class="elicitation-card">
<div class="elicitation-number">01</div>
<div class="elicitation-title">Stakeholder Interviews</div>
<div class="elicitation-text">
Understand business objectives, user needs,
pain points and reporting expectations.
</div>
</div>

<div class="elicitation-card">
<div class="elicitation-number">02</div>
<div class="elicitation-title">Process Walkthrough</div>
<div class="elicitation-text">
Review the As-Is customer and appointment process
to identify information needs, hand-offs and inefficiencies.
</div>
</div>

<div class="elicitation-card">
<div class="elicitation-number">03</div>
<div class="elicitation-title">Data & Document Review</div>
<div class="elicitation-text">
Review customer spreadsheets, booking records,
communication practices and existing reporting.
</div>
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # FROM INSIGHT TO REQUIREMENT
    # =====================================================

    st.subheader("From Stakeholder Need to Requirement")

    st.markdown(
        """
<div class="requirement-flow">

<div class="requirement-flow-box">
<strong>Stakeholder Insight</strong><br>
“I have to search several places to find a customer's information.”
</div>

<div class="requirement-arrow">↓</div>

<div class="requirement-flow-box">
<strong>Business Need</strong><br>
Staff need one reliable and accessible view of customer information.
</div>

<div class="requirement-arrow">↓</div>

<div class="requirement-flow-box">
<strong>BR-01</strong><br>
Centralise customer information to provide staff with a consistent customer view.
</div>

<div class="requirement-arrow">↓</div>

<div class="requirement-flow-box final">
<strong>FR-02 / FR-03 / FR-04</strong><br>
Search customers quickly, display a central customer profile
and provide access to appointment history.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # REQUIREMENTS CATALOGUE
    # =====================================================

    st.subheader("Requirements Catalogue")

    st.write(
        """
        Requirements were grouped into business, functional and
        non-functional requirements, then prioritised using MoSCoW.
        """
    )

    type_filter = st.multiselect(
        "Requirement Type",
        options=list(requirements["Type"].unique()),
        default=list(requirements["Type"].unique()),
        key="requirements_type_filter",
    )

    priority_filter = st.multiselect(
        "Priority",
        options=["Must", "Should", "Could", "Won't"],
        default=["Must", "Should"],
        key="requirements_priority_filter",
    )

    filtered_requirements = requirements[
        requirements["Type"].isin(type_filter)
        & requirements["Priority"].isin(priority_filter)
    ]

    st.dataframe(
        filtered_requirements,
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        label="Download Requirements Catalogue",
        data=requirements.to_csv(index=False),
        file_name="spa_crm_requirements.csv",
        mime="text/csv",
        key="requirements_download",
    )

    # =====================================================
    # MOSCOW PRIORITISATION
    # =====================================================

    st.subheader("MoSCoW Prioritisation")

    st.markdown(
        """
<div class="moscow-grid">

<div class="moscow-card">
<h3>Must Have</h3>
<p>
Customer profile<br>
Customer search<br>
Customer history<br>
Appointment booking<br>
Therapist availability<br>
Appointment confirmation<br>
Automated reminders
</p>
</div>

<div class="moscow-card">
<h3>Should Have</h3>
<p>
Retention reporting<br>
No-show reporting<br>
Communication status<br>
Duplicate detection<br>
Service-performance reporting
</p>
</div>

<div class="moscow-card">
<h3>Could Have</h3>
<p>
Birthday campaigns<br>
Advanced customer segmentation<br>
Loyalty automation<br>
Additional marketing workflows
</p>
</div>

<div class="moscow-card">
<h3>Won't Have — Phase 1</h3>
<p>
AI recommendations<br>
Customer mobile app<br>
Predictive analytics<br>
Advanced personalisation
</p>
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.info(
        """
        The prioritised requirements become the evaluation criteria used in the
        next phase to compare and select the most suitable CRM solution.
        """
    )

    footer()

# =========================================================
# 05 CRM EVALUATION
# =========================================================

elif page == "05 · CRM Evaluation":

    page_header(
        "05",
        "CRM Evaluation",
        "Comparing shortlisted Vietnamese CRM solutions using requirements-driven evaluation criteria.",
    )

    # =====================================================
    # EVALUATION APPROACH — HORIZONTAL
    # =====================================================

    st.markdown(
        """
<style>

.evaluation-section {
    margin-top: 1.5rem;
    margin-bottom: 3rem;
}

.evaluation-section h2 {
    color: #194339 !important;
    font-size: 1.8rem;
    font-weight: 750;
    margin-bottom: 0.5rem;
}

.evaluation-subtitle {
    color: #6b7280;
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 1.8rem;
}

.evaluation-wrapper {
    width: 100%;
    overflow-x: auto;
    padding-bottom: 0.5rem;
}

.evaluation-flow {
    display: flex;
    flex-direction: row;
    align-items: stretch;
    gap: 0.55rem;
    width: 100%;
    min-width: 1050px;
}

.evaluation-card {
    flex: 1 1 0;
    min-width: 145px;
    background: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 14px;
    padding: 1.15rem 0.9rem;
    min-height: 165px;
    box-shadow: 0 3px 10px rgba(25, 67, 57, 0.06);
    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        border-color 0.2s ease;
}

.evaluation-card:hover {
    transform: translateY(-3px);
    border-color: #194339;
    box-shadow: 0 7px 18px rgba(25, 67, 57, 0.10);
}

.evaluation-step {
    width: 31px;
    height: 31px;
    border-radius: 50%;
    background: #194339;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.78rem;
    font-weight: 700;
    margin-bottom: 0.9rem;
}

.evaluation-title {
    color: #194339;
    font-size: 0.95rem;
    font-weight: 700;
    line-height: 1.35;
    margin-bottom: 0.55rem;
}

.evaluation-description {
    color: #6b7280;
    font-size: 0.81rem;
    line-height: 1.5;
}

.evaluation-arrow {
    flex: 0 0 25px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #194339;
    font-size: 1.45rem;
    font-weight: 700;
}

.evaluation-card.final {
    background: #194339;
    border-color: #194339;
}

.evaluation-card.final .evaluation-step {
    background: #ffffff;
    color: #194339;
}

.evaluation-card.final .evaluation-title {
    color: #ffffff;
}

.evaluation-card.final .evaluation-description {
    color: #dce9e5;
}


/* =====================================================
   CRM SHORTLIST CARDS
===================================================== */

.crm-shortlist {
    margin-top: 1.2rem;
    margin-bottom: 3rem;
}

.crm-shortlist-title {
    color: #194339;
    font-size: 1.8rem;
    font-weight: 750;
    margin-bottom: 0.4rem;
}

.crm-shortlist-subtitle {
    color: #6b7280;
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.crm-note {
    background: #f4f7f6;
    border-left: 4px solid #194339;
    border-radius: 8px;
    padding: 1rem 1.2rem;
    color: #374151;
    line-height: 1.6;
    margin-top: 1rem;
    margin-bottom: 2rem;
}


/* =====================================================
   EVALUATION SCALE
===================================================== */

.score-scale {
    background: #f4f7f6;
    border: 1px solid #dfe7e4;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    margin-bottom: 1.5rem;
    color: #4b5563;
    font-size: 0.92rem;
    line-height: 1.7;
}

.score-scale strong {
    color: #194339;
}

</style>

<div class="evaluation-section">

<h2>Evaluation Approach</h2>

<div class="evaluation-subtitle">
A structured evaluation process was used to move from defined business
requirements to an evidence-based CRM recommendation.
</div>

<div class="evaluation-wrapper">

<div class="evaluation-flow">

<div class="evaluation-card">
<div class="evaluation-step">01</div>
<div class="evaluation-title">Requirements</div>
<div class="evaluation-description">
Define business, functional and non-functional requirements.
</div>
</div>

<div class="evaluation-arrow">→</div>

<div class="evaluation-card">
<div class="evaluation-step">02</div>
<div class="evaluation-title">Define Evaluation Criteria</div>
<div class="evaluation-description">
Translate priority requirements into measurable CRM selection criteria.
</div>
</div>

<div class="evaluation-arrow">→</div>

<div class="evaluation-card">
<div class="evaluation-step">03</div>
<div class="evaluation-title">Shortlist Solutions</div>
<div class="evaluation-description">
Identify Vietnamese CRM solutions that could meet the spa's operational needs.
</div>
</div>

<div class="evaluation-arrow">→</div>

<div class="evaluation-card">
<div class="evaluation-step">04</div>
<div class="evaluation-title">Requirements Fit Analysis</div>
<div class="evaluation-description">
Assess how well each shortlisted solution satisfies priority requirements.
</div>
</div>

<div class="evaluation-arrow">→</div>

<div class="evaluation-card">
<div class="evaluation-step">05</div>
<div class="evaluation-title">Weighted Decision Matrix</div>
<div class="evaluation-description">
Compare solutions using weighted business and technical criteria.
</div>
</div>

<div class="evaluation-arrow">→</div>

<div class="evaluation-card final">
<div class="evaluation-step">06</div>
<div class="evaluation-title">Recommendation</div>
<div class="evaluation-description">
Recommend the best-fit platform based on functional fit and overall value.
</div>
</div>

</div>
</div>
</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # SHORTLISTED CRM SOLUTIONS
    # =====================================================

    st.markdown(
        """
<div class="crm-shortlist">

<div class="crm-shortlist-title">
Shortlisted CRM Solutions
</div>

<div class="crm-shortlist-subtitle">
Three Vietnamese customer-management platforms were shortlisted based on
functional relevance, local-market suitability and alignment with the
requirements identified for Wellness Perth Spa.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent

    kiotviet_logo = BASE_DIR / "kiotviet.png"
    getfly_logo = BASE_DIR / "getfly.png"
    misa_logo = BASE_DIR / "misa_amis.png"

    crm1, crm2, crm3 = st.columns(3)

    # =====================================================
    # KIOTVIET SALON
    # =====================================================

    with crm1:

        if kiotviet_logo.exists():
            st.image(
                str(kiotviet_logo),
                width=150,
            )
        else:
            st.caption("Add kiotviet.png to display logo")

        st.markdown("### KiotViet Salon")

        st.markdown("**Spa-Specific Management Platform**")

        st.write(
            """
            Industry-specific solution designed for salon and spa operations,
            combining customer management with appointment and service workflows.
            """
        )

        st.markdown(
            """
**Relevant capabilities**

- Central customer information
- Customer service history
- Appointment scheduling
- Staff / room allocation
- Appointment reminders
- Zalo ZNS communication
- Operational reporting
            """
        )

        st.markdown(
            "[Official website](https://www.kiotviet.vn/kiotviet-salon/)"
        )

    # =====================================================
    # GETFLY CRM
    # =====================================================

    with crm2:

        if getfly_logo.exists():
            st.image(
                str(getfly_logo),
                width=150,
            )
        else:
            st.caption("Add getfly.png to display logo")

        st.markdown("### Getfly CRM")

        st.markdown("**Customer Engagement CRM**")

        st.write(
            """
            Vietnamese CRM focused on centralised customer management,
            customer engagement and configurable marketing and follow-up automation.
            """
        )

        st.markdown(
            """
**Relevant capabilities**

- Central customer database
- Interaction history
- Customer segmentation
- Email / SMS / ZNS automation
- Automated follow-up workflows
- KPI reporting
- REST API integration
            """
        )

        st.markdown(
            "[Official website](https://getfly.vn/en/)"
        )

    # =====================================================
    # MISA AMIS CRM
    # =====================================================

    with crm3:

        if misa_logo.exists():
            st.image(
                str(misa_logo),
                width=150,
            )
        else:
            st.caption("Add misa_amis.png to display logo")

        st.markdown("### MISA AMIS CRM")

        st.markdown("**Enterprise CRM Platform**")

        st.write(
            """
            Broader CRM platform focused on customer management,
            sales workflows, reporting, automation and integration
            across business applications.
            """
        )

        st.markdown(
            """
**Relevant capabilities**

- Central customer information
- Customer classification
- Customer reporting
- Workflow support
- 50+ reports
- Mobile access
- API and system integrations
            """
        )

        st.markdown(
            "[Official website](https://amis.misa.vn/en/crm/)"
        )

    st.markdown(
        """
<div class="crm-note">

<strong>Shortlisting rationale:</strong>
KiotViet Salon provides the strongest spa-specific operational fit.
Getfly CRM provides stronger general CRM and customer-engagement automation,
while MISA AMIS CRM provides broader enterprise reporting and integration capability.

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # REQUIREMENTS FIT SUMMARY
    # =====================================================

    st.subheader("Requirements Fit Summary")

    fit_summary = pd.DataFrame(
        [
            [
                "Central Customer Profile",
                "Strong",
                "Strong",
                "Strong",
            ],
            [
                "Customer / Service History",
                "Strong",
                "Strong",
                "Strong",
            ],
            [
                "Spa Appointment Scheduling",
                "Strong",
                "Partial",
                "Partial",
            ],
            [
                "Staff / Room Scheduling",
                "Strong",
                "Limited",
                "Limited",
            ],
            [
                "Automated Reminders",
                "Strong",
                "Strong",
                "Partial",
            ],
            [
                "Customer Segmentation",
                "Moderate",
                "Strong",
                "Strong",
            ],
            [
                "Reporting & Analytics",
                "Strong",
                "Strong",
                "Strong",
            ],
            [
                "Integration Capability",
                "Moderate",
                "Strong",
                "Strong",
            ],
            [
                "Spa-Specific Fit",
                "Strong",
                "Moderate",
                "Moderate",
            ],
        ],
        columns=[
            "Requirement Area",
            "KiotViet Salon",
            "Getfly CRM",
            "MISA AMIS CRM",
        ],
    )

    st.dataframe(
        fit_summary,
        hide_index=True,
        use_container_width=True,
    )

    st.caption(
        """
        Fit ratings are portfolio-case assessments based on publicly documented
        capabilities. A real procurement exercise would validate them through
        vendor demonstrations, trials and stakeholder workshops.
        """
    )

    # =====================================================
    # INTERACTIVE WEIGHTED DECISION MATRIX
    # =====================================================

    st.subheader("Interactive Weighted Decision Matrix")

    st.caption(
        """
        Adjust the weighting to explore how different business priorities
        affect the CRM recommendation.
        """
    )

    st.markdown(
        """
<div class="score-scale">
<strong>Scoring scale:</strong>
1 = Poor fit &nbsp;&nbsp;|&nbsp;&nbsp;
2 = Limited fit &nbsp;&nbsp;|&nbsp;&nbsp;
3 = Moderate fit &nbsp;&nbsp;|&nbsp;&nbsp;
4 = Good fit &nbsp;&nbsp;|&nbsp;&nbsp;
5 = Strong fit
</div>
""",
        unsafe_allow_html=True,
    )

    criteria_defaults = {
        "Customer Management": 15,
        "Appointment Management": 25,
        "Automation & Reminders": 15,
        "Reporting & Analytics": 10,
        "Usability": 10,
        "Integration": 5,
        "Security & Privacy": 5,
        "Implementation Effort": 5,
        "Cost": 10,
    }

    weights = {}

    col_a, col_b = st.columns(2)

    criteria_items = list(criteria_defaults.items())

    for i, (criterion, default) in enumerate(criteria_items):

        target_col = col_a if i % 2 == 0 else col_b

        with target_col:

            weights[criterion] = st.slider(
                criterion,
                min_value=0,
                max_value=30,
                value=default,
                step=5,
                key=f"crm_weight_{criterion}",
            )

    total_weight = sum(weights.values())

    if total_weight != 100:

        st.warning(
            f"Current total weighting is {total_weight}%. "
            "For formal evaluation, weights should total 100%."
        )

    else:

        st.success("Weights total 100%.")

    # =====================================================
    # CRM SCORES
    #
    # Illustrative BA portfolio scoring based on documented
    # product capabilities and expected implementation fit.
    # =====================================================

    crm_scores = {

        "KiotViet Salon": {
            "Customer Management": 4,
            "Appointment Management": 5,
            "Automation & Reminders": 5,
            "Reporting & Analytics": 4,
            "Usability": 5,
            "Integration": 3,
            "Security & Privacy": 4,
            "Implementation Effort": 5,
            "Cost": 4,
        },

        "Getfly CRM": {
            "Customer Management": 5,
            "Appointment Management": 3,
            "Automation & Reminders": 5,
            "Reporting & Analytics": 4,
            "Usability": 4,
            "Integration": 5,
            "Security & Privacy": 4,
            "Implementation Effort": 3,
            "Cost": 3,
        },

        "MISA AMIS CRM": {
            "Customer Management": 5,
            "Appointment Management": 2,
            "Automation & Reminders": 3,
            "Reporting & Analytics": 5,
            "Usability": 4,
            "Integration": 5,
            "Security & Privacy": 5,
            "Implementation Effort": 3,
            "Cost": 3,
        },
    }

    # =====================================================
    # MATRIX TABLE
    # =====================================================

    matrix_rows = []

    for criterion in weights:

        matrix_rows.append(
            {
                "Criterion": criterion,
                "Weight %": weights[criterion],
                "KiotViet Salon": crm_scores["KiotViet Salon"][criterion],
                "Getfly CRM": crm_scores["Getfly CRM"][criterion],
                "MISA AMIS CRM": crm_scores["MISA AMIS CRM"][criterion],
            }
        )

    matrix_df = pd.DataFrame(matrix_rows)

    st.dataframe(
        matrix_df,
        hide_index=True,
        use_container_width=True,
    )

    # =====================================================
    # CALCULATE WEIGHTED RESULTS
    # =====================================================

    results = {}

    for crm in crm_scores:

        weighted_total = 0

        for criterion, weight in weights.items():

            weighted_total += (
                crm_scores[crm][criterion] * weight
            )

        if total_weight > 0:

            results[crm] = (
                weighted_total / total_weight
            )

        else:

            results[crm] = 0

    result_df = pd.DataFrame(
        {
            "CRM Solution": results.keys(),
            "Weighted Score / 5": [
                round(score, 2)
                for score in results.values()
            ],
        }
    ).sort_values(
        "Weighted Score / 5",
        ascending=False,
    )

    # =====================================================
    # EVALUATION RESULT
    # =====================================================

    st.subheader("Evaluation Result")

    st.dataframe(
        result_df,
        hide_index=True,
        use_container_width=True,
    )

    winner = result_df.iloc[0]["CRM Solution"]
    winning_score = result_df.iloc[0]["Weighted Score / 5"]

    st.success(
        f"Recommended solution: {winner} — "
        f"Weighted score {winning_score}/5"
    )

    # =====================================================
    # RECOMMENDATION
    # =====================================================

    if winner == "KiotViet Salon":

        st.markdown(
            """
### Recommendation Rationale

**KiotViet Salon** is the preferred solution because its native
appointment-management capability aligns closely with the spa's
highest-priority operational requirements.

The platform provides an integrated environment for:

- customer profiles and service history;
- appointment scheduling;
- staff and room allocation;
- automated appointment reminders;
- customer communication; and
- operational reporting.

This reduces the amount of additional configuration or integration
required compared with a general-purpose CRM.

**Trade-off:** KiotViet may provide less enterprise-level CRM flexibility
and integration capability than Getfly CRM or MISA AMIS CRM. However,
for the current business problem, operational fit and ease of
implementation are given higher priority.
            """
        )

    elif winner == "Getfly CRM":

        st.markdown(
            """
### Recommendation Rationale

**Getfly CRM** becomes the preferred solution under the selected
weightings because of its strong customer-management, automation and
integration capability.

It would be particularly suitable if Wellness Perth Spa prioritised
customer engagement and CRM automation over native spa appointment
management.

Additional appointment configuration or integration would likely be
required.
            """
        )

    else:

        st.markdown(
            """
### Recommendation Rationale

**MISA AMIS CRM** becomes the preferred solution under the selected
weightings because of its strong reporting, customer-management and
integration capabilities.

It would be more appropriate if the business prioritised broader
enterprise CRM capability and scalability.

However, additional configuration or integration would likely be
required to support detailed spa appointment operations.
            """
        )

    st.info(
        """
        **BA decision principle:** The recommended solution is not simply the
        CRM with the most features. The selection is based on which platform
        provides the strongest fit against the business's prioritised
        requirements with acceptable implementation effort and cost.
        """
    )

    st.caption(
        """
        This is a simulated portfolio procurement exercise. Product capabilities
        are based on publicly available vendor information, while criterion
        weightings and evaluation scores represent the assumptions used for
        this case study.
        """
    )

    footer()
# =========================================================
# 06 CRM SELECTION
# =========================================================

elif page == "06 · CRM Selection":

    page_header(
        "06",
        "CRM Selection",
        "Documenting the preferred solution, rationale and remaining implementation gaps.",
    )

    st.subheader("Recommended Solution")

    st.success(
        "CRM B — Spa-Specific Management Platform"
    )

    st.write(
        """
        CRM B was selected because it provides the strongest alignment with
        the spa's operational requirements, particularly appointment scheduling,
        therapist availability, customer records, automated communication and
        ease of use.

        Although general-purpose CRM platforms may provide stronger traditional
        CRM and reporting capabilities, they require additional configuration or
        integration to support spa-specific appointment workflows.
        """
    )

    st.subheader("Decision Rationale")

    decision = pd.DataFrame(
        [
            [
                "Appointment Management",
                "Strong native capability",
                "Critical",
            ],
            [
                "Customer Records",
                "Meets central-profile requirements",
                "Critical",
            ],
            [
                "Automated Communication",
                "Supports confirmations and reminders",
                "Critical",
            ],
            [
                "Usability",
                "Suitable for operational staff",
                "High",
            ],
            [
                "Implementation Effort",
                "Lower than heavily configurable CRM options",
                "High",
            ],
            [
                "Reporting",
                "Meets core requirements with some configuration",
                "Medium",
            ],
        ],
        columns=[
            "Factor",
            "Finding",
            "Importance",
        ],
    )

    st.dataframe(
        decision,
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Fit-Gap Analysis")

    gap = pd.DataFrame(
        [
            [
                "Customer Profile",
                "Supported",
                "None",
                "Standard configuration",
            ],
            [
                "Appointment Scheduling",
                "Supported",
                "None",
                "Standard configuration",
            ],
            [
                "Reminder Automation",
                "Supported",
                "Minor",
                "Configure reminder rules",
            ],
            [
                "Retention Reporting",
                "Partial",
                "Moderate",
                "Configure/customise reports",
            ],
            [
                "Existing Customer Data",
                "Not migrated",
                "Major",
                "Data cleansing and migration",
            ],
            [
                "Staff Knowledge",
                "New system",
                "Major",
                "Training and SOP",
            ],
            [
                "Operating Process",
                "Current manual steps",
                "Moderate",
                "Process redesign and adoption",
            ],
        ],
        columns=[
            "Requirement Area",
            "Capability",
            "Gap",
            "Response",
        ],
    )

    st.dataframe(
        gap,
        hide_index=True,
        use_container_width=True,
    )

    footer()

# =========================================================
# 07 FUTURE STATE
# =========================================================

elif page == "07 · Future-State Design":

    page_header(
        "07",
        "Future-State Design",
        "Redesigning the customer and booking process around the selected CRM solution.",
    )

    # =====================================================
    # TO-BE PROCESS
    # =====================================================

    st.markdown(
        """
<div class="current-state-intro">

<h2>To-Be Process</h2>

<p>
The future-state process was designed to address the key weaknesses identified
in the current-state analysis. The proposed process introduces a
<strong>centralised customer record, integrated appointment management,
automated communication and improved information visibility</strong>
across all spa locations.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent
    to_be_path = BASE_DIR / "TO-BE Process.png"

    if to_be_path.exists():

        st.image(
            str(to_be_path),
            use_container_width=True,
        )

    else:

        st.error(
            "To-Be process image could not be found. "
            "Make sure 'TO-BE Process.png' is in the same GitHub folder as testt.py."
        )

    # =====================================================
    # AS-IS VS TO-BE
    # =====================================================

    st.subheader("As-Is vs To-Be")

    comparison = pd.DataFrame(
        [
            [
                "Customer Search",
                "Search multiple sources",
                "Search central CRM profile",
            ],
            [
                "Customer History",
                "Fragmented across files/channels",
                "Single customer view",
            ],
            [
                "Appointment Availability",
                "Manual checking",
                "CRM availability view",
            ],
            [
                "Booking",
                "Manual record",
                "CRM-linked appointment",
            ],
            [
                "Confirmation",
                "Dependent on staff",
                "Automatically generated",
            ],
            [
                "Reminders",
                "Manual and inconsistent",
                "Automated reminder workflow",
            ],
            [
                "Reporting",
                "Manual consolidation",
                "Centralised reporting",
            ],
        ],
        columns=[
            "Area",
            "As-Is",
            "To-Be",
        ],
    )

    st.dataframe(
        comparison,
        hide_index=True,
        use_container_width=True,
    )

    st.info(
        """
        The future-state process reduces manual hand-offs, creates a single source
        of customer information and introduces automation for critical appointment
        communications.
        """
    )

    footer()

# =========================================================
# 08 IMPLEMENTATION
# =========================================================

elif page == "08 · Implementation":

    page_header(
        "08",
        "Implementation Planning",
        "Translating the selected solution into deliverable work, migration activities and change actions.",
    )

    st.subheader("Implementation Phases")

    phases = pd.DataFrame(
        [
            [
                "1",
                "Preparation",
                "Confirm scope, roles, risks and implementation schedule",
            ],
            [
                "2",
                "Configuration",
                "Configure customer fields, booking rules, reminders and permissions",
            ],
            [
                "3",
                "Data Migration",
                "Clean, map, import and validate customer data",
            ],
            [
                "4",
                "Testing",
                "System testing and defect resolution",
            ],
            [
                "5",
                "UAT",
                "Business-user validation of critical workflows",
            ],
            [
                "6",
                "Training",
                "Train reception, therapists, manager and marketing users",
            ],
            [
                "7",
                "Go-Live",
                "Deploy CRM and provide hypercare",
            ],
            [
                "8",
                "Review",
                "Measure adoption, KPIs and improvement opportunities",
            ],
        ],
        columns=[
            "Phase",
            "Activity",
            "Outcome",
        ],
    )

    st.dataframe(
        phases,
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Epics")

    epics = pd.DataFrame(
        [
            ["EP-01", "Customer Management"],
            ["EP-02", "Appointment Management"],
            ["EP-03", "Communication Automation"],
            ["EP-04", "Reporting & Analytics"],
            ["EP-05", "Data Migration"],
            ["EP-06", "Security & Access"],
        ],
        columns=[
            "Epic",
            "Name",
        ],
    )

    st.dataframe(
        epics,
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Sample User Stories")

    st.markdown(
        """
### US-01 — Customer Search

**As a receptionist**,  
I want to search for customers by name, phone number or email,  
so that I can quickly access the correct customer profile.

**Acceptance Criteria**

- Given a customer exists in the CRM
- When the receptionist enters a matching name, phone number or email
- Then the CRM displays the relevant customer record

---

### US-02 — Customer History

**As a therapist**,  
I want to view relevant customer treatment and appointment history,  
so that I can provide a more personalised service.

---

### US-03 — Appointment Confirmation

**As a customer**,  
I want to receive confirmation after making an appointment,  
so that I know the booking has been successfully recorded.

---

### US-04 — Appointment Reminder

**As a receptionist**,  
I want appointment reminders to be sent automatically,  
so that the spa does not rely solely on manual follow-up.

---

### US-05 — Management Reporting

**As a spa manager**,  
I want to view customer-retention and service-performance information,  
so that I can identify trends and support business decisions.
        """
    )

    st.subheader("Data Migration")

    st.code(
        """
Existing Customer Data
        ↓
Data Profiling
        ↓
Remove Duplicates
        ↓
Clean Missing / Invalid Data
        ↓
Map Existing Fields → CRM Fields
        ↓
Test Migration
        ↓
Validate Records
        ↓
Production Migration
        ↓
Post-Migration Reconciliation
        """,
        language=None,
    )

    st.subheader("Key Risks")

    risks = pd.DataFrame(
        [
            [
                "R01",
                "Poor data quality",
                "High",
                "Clean and validate data before migration",
            ],
            [
                "R02",
                "Staff resistance to new process",
                "Medium",
                "Early engagement, training and feedback",
            ],
            [
                "R03",
                "Incorrect configuration",
                "Medium",
                "Configuration review and UAT",
            ],
            [
                "R04",
                "Migration data loss",
                "High",
                "Backup, test migration and reconciliation",
            ],
            [
                "R05",
                "Low user adoption",
                "High",
                "Usage monitoring and post-go-live support",
            ],
        ],
        columns=[
            "Risk",
            "Description",
            "Impact",
            "Mitigation",
        ],
    )

    st.dataframe(
        risks,
        hide_index=True,
        use_container_width=True,
    )

    footer()

# =========================================================
# 09 TESTING & UAT
# =========================================================

elif page == "09 · Testing & UAT":

    page_header(
        "09",
        "Testing & UAT",
        "Validating that the selected and configured CRM supports critical business requirements.",
    )

    st.subheader("UAT Objectives")

    st.write(
        """
        UAT confirms that the configured CRM supports the agreed business processes
        and is suitable for operational use before go-live.
        """
    )

    uat = pd.DataFrame(
        [
            [
                "UAT-01",
                "Create & Find Customer",
                "FR-01 / FR-02 / FR-03",
                "Create a customer and search by phone",
                "Correct customer profile is displayed",
            ],
            [
                "UAT-02",
                "View Customer History",
                "FR-04",
                "Open an existing customer profile",
                "Previous appointments are visible",
            ],
            [
                "UAT-03",
                "Appointment Confirmation",
                "FR-13",
                "Create a new appointment",
                "Confirmation is automatically generated",
            ],
            [
                "UAT-04",
                "Appointment Reminder",
                "FR-15",
                "Trigger configured reminder rule",
                "Reminder is sent according to configuration",
            ],
            [
                "UAT-05",
                "Retention Reporting",
                "FR-19",
                "Open retention report",
                "Repeat-customer data is displayed",
            ],
        ],
        columns=[
            "UAT ID",
            "Scenario",
            "Requirement",
            "Test",
            "Expected Result",
        ],
    )

    st.dataframe(
        uat,
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Sample UAT Scenario")

    st.markdown(
        """
### UAT-03 — Automated Appointment Confirmation

**Precondition**

Receptionist is logged into the CRM and a valid customer profile exists.

**Steps**

1. Search for the customer.
2. Open the customer profile.
3. Select **Create Appointment**.
4. Select a service.
5. Select an available therapist.
6. Select an available date and time.
7. Save the appointment.

**Expected Result**

- Appointment is successfully created.
- Appointment is linked to the customer's profile.
- Selected therapist/time is reserved.
- Customer receives the configured confirmation.
        """
    )

    st.subheader("Entry & Exit Criteria")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### UAT Entry")
        st.write(
            """
            - Configuration completed
            - Critical defects resolved
            - Test data prepared
            - UAT users identified
            - Requirements baseline approved
            """
        )

    with c2:
        st.markdown("### UAT Exit")
        st.write(
            """
            - All critical scenarios executed
            - No unresolved critical defects
            - Business acceptance obtained
            - Go-live recommendation completed
            """
        )

    footer()

# =========================================================
# 10 GO-LIVE & ADOPTION
# =========================================================

elif page == "10 · Go-Live & Adoption":

    page_header(
        "10",
        "Go-Live, Training & Adoption",
        "Supporting users through the transition from current processes to the new CRM.",
    )

    st.subheader("Training Plan")

    training = pd.DataFrame(
        [
            [
                "Receptionist",
                "Customer search, booking, cancellation, reminders",
                "Workshop + Quick Guide",
            ],
            [
                "Therapist",
                "Customer history, treatment notes",
                "Short Workshop + SOP",
            ],
            [
                "Manager",
                "Dashboard, reporting, user oversight",
                "Manager Training",
            ],
            [
                "Marketing",
                "Segments, customer lists and campaign workflows",
                "Workshop",
            ],
        ],
        columns=[
            "Audience",
            "Training Content",
            "Method",
        ],
    )

    st.dataframe(
        training,
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Go-Live Plan")

        # =====================================================
    # IMPLEMENTATION / GO-LIVE TIMELINE
    # =====================================================

    st.markdown(
        """
<style>

.timeline-section {
    margin-top: 2.5rem;
    margin-bottom: 3rem;
}

.timeline-section h2 {
    color: #194339 !important;
    font-size: 1.8rem;
    font-weight: 750;
    margin-bottom: 0.4rem;
}

.timeline-subtitle {
    color: #6b7280;
    font-size: 1rem;
    margin-bottom: 1.8rem;
}

.timeline-card {
    background: #ffffff;
    border: 1px solid #dfe7e4;
    border-radius: 18px;
    padding: 2rem;
    box-shadow: 0 4px 14px rgba(25, 67, 57, 0.06);
    overflow-x: auto;
}

.timeline-grid {
    display: grid;
    grid-template-columns: 230px repeat(12, minmax(55px, 1fr));
    min-width: 1050px;
    align-items: center;
}


/* WEEK HEADERS */

.week-header {
    text-align: center;
    color: #7b8b86;
    font-size: 0.8rem;
    font-weight: 600;
    padding-bottom: 1rem;
}


/* TASK LABEL */

.task-label {
    color: #374151;
    font-size: 0.95rem;
    padding: 0.8rem 1rem 0.8rem 0;
    text-align: right;
}


/* CELLS */

.timeline-cell {
    min-height: 46px;
    border-left: 1px solid #edf1ef;
    position: relative;
}


/* BARS */

.timeline-bar {
    height: 34px;
    border-radius: 7px;
    margin-top: 6px;
    margin-bottom: 6px;
}

.bar-primary {
    background: #194339;
}

.bar-secondary {
    background: #37695d;
}

.bar-light {
    background: #78a399;
}

.bar-soft {
    background: #b7cec8;
}


/* MILESTONES */

.milestone-row {
    border-top: 1px solid #dfe7e4;
    margin-top: 0.8rem;
}

.milestone-label {
    color: #194339;
    font-weight: 700;
    text-align: right;
    padding-right: 1rem;
}

.milestone-cell {
    position: relative;
    height: 50px;
}

.milestone {
    width: 14px;
    height: 14px;
    background: #194339;
    transform: rotate(45deg);
    position: absolute;
    left: 50%;
    top: 15px;
    margin-left: -7px;
}


/* MOBILE */

@media (max-width: 900px) {

    .timeline-card {
        padding: 1.2rem;
    }

}

</style>

<div class="timeline-section">

<h2>Implementation & Go-Live Timeline</h2>

<div class="timeline-subtitle">
12-week CRM implementation with parallel workstreams and key milestone gates.
</div>

<div class="timeline-card">

<div class="timeline-grid">

<!-- HEADER -->
<div></div>

<div class="week-header">W1</div>
<div class="week-header">W2</div>
<div class="week-header">W3</div>
<div class="week-header">W4</div>
<div class="week-header">W5</div>
<div class="week-header">W6</div>
<div class="week-header">W7</div>
<div class="week-header">W8</div>
<div class="week-header">W9</div>
<div class="week-header">W10</div>
<div class="week-header">W11</div>
<div class="week-header">W12</div>


<!-- =========================================
     REQUIREMENTS & PLANNING
========================================= -->

<div class="task-label">Requirements & Planning</div>

<div class="timeline-cell"><div class="timeline-bar bar-primary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-primary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-primary"></div></div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>


<!-- =========================================
     CRM CONFIGURATION
========================================= -->

<div class="task-label">CRM Configuration</div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>

<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>


<!-- =========================================
     DATA CLEANSING & MIGRATION
========================================= -->

<div class="task-label">Data Cleansing & Migration</div>

<div class="timeline-cell"></div>

<div class="timeline-cell"><div class="timeline-bar bar-light"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-light"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-light"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-light"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-light"></div></div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>


<!-- =========================================
     AUTOMATION & REPORTING
========================================= -->

<div class="task-label">Automation & Reporting</div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>

<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>


<!-- =========================================
     SYSTEM TESTING
========================================= -->

<div class="task-label">System Testing</div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>

<div class="timeline-cell"><div class="timeline-bar bar-light"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-light"></div></div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>


<!-- =========================================
     UAT
========================================= -->

<div class="task-label">User Acceptance Testing</div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>

<div class="timeline-cell"><div class="timeline-bar bar-primary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-primary"></div></div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>


<!-- =========================================
     TRAINING
========================================= -->

<div class="task-label">Staff Training</div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>

<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-secondary"></div></div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>


<!-- =========================================
     GO LIVE
========================================= -->

<div class="task-label">Go-Live</div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>

<div class="timeline-cell"><div class="timeline-bar bar-primary"></div></div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>


<!-- =========================================
     HYPERCARE
========================================= -->

<div class="task-label">Hypercare & Adoption Support</div>

<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>
<div class="timeline-cell"></div>

<div class="timeline-cell"></div>

<div class="timeline-cell"><div class="timeline-bar bar-soft"></div></div>
<div class="timeline-cell"><div class="timeline-bar bar-soft"></div></div>


<!-- =========================================
     MILESTONES
========================================= -->

<div class="milestone-label">Milestones</div>

<div class="milestone-cell"></div>

<div class="milestone-cell"></div>

<div class="milestone-cell">
<div class="milestone"></div>
</div>

<div class="milestone-cell"></div>

<div class="milestone-cell"></div>

<div class="milestone-cell">
<div class="milestone"></div>
</div>

<div class="milestone-cell"></div>

<div class="milestone-cell"></div>

<div class="milestone-cell">
<div class="milestone"></div>
</div>

<div class="milestone-cell">
<div class="milestone"></div>
</div>

<div class="milestone-cell"></div>

<div class="milestone-cell">
<div class="milestone"></div>
</div>

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.subheader("Adoption Measures")

    adoption = pd.DataFrame(
        [
            [
                "Active User Rate",
                "% of expected staff regularly accessing CRM",
            ],
            [
                "CRM Booking Rate",
                "% of appointments recorded through new process",
            ],
            [
                "Customer Profile Completeness",
                "% of required customer fields completed",
            ],
            [
                "Reminder Automation Rate",
                "% of eligible appointments receiving reminders",
            ],
            [
                "User Feedback",
                "Staff satisfaction and reported usability issues",
            ],
        ],
        columns=[
            "Measure",
            "Purpose",
        ],
    )

    st.dataframe(
        adoption,
        hide_index=True,
        use_container_width=True,
    )

    footer()

# =========================================================
# 11 BENEFITS & REVIEW
# =========================================================

elif page == "11 · Benefits & Review":

    page_header(
        "11",
        "Benefits & Post-Implementation Review",
        "Measuring whether the CRM implementation addresses the original business problems.",
    )

    st.subheader("Problem → Solution → Benefit")

    benefit_map = pd.DataFrame(
        [
            [
                "Fragmented customer information",
                "Central customer profile",
                "Faster access to reliable customer information",
            ],
            [
                "Limited customer history",
                "Integrated booking and service history",
                "Improved visibility and personalisation",
            ],
            [
                "Inconsistent follow-ups",
                "Automated confirmations and reminders",
                "More consistent customer communication",
            ],
            [
                "Appointment no-shows",
                "Reminder workflow + no-show reporting",
                "Potential reduction in avoidable missed appointments",
            ],
            [
                "Limited reporting",
                "CRM dashboards and reports",
                "Improved management visibility",
            ],
        ],
        columns=[
            "Original Problem",
            "CRM Response",
            "Expected Benefit",
        ],
    )

    st.dataframe(
        benefit_map,
        hide_index=True,
        use_container_width=True,
    )

    st.subheader("Benefits Realisation Targets")

    targets = pd.DataFrame(
        [
            [
                "Customer profile lookup time",
                "3 minutes",
                "< 30 seconds",
            ],
            [
                "Follow-up completion",
                "40%",
                "> 90%",
            ],
            [
                "Appointment no-show rate",
                "12%",
                "< 7%",
            ],
            [
                "Repeat booking rate",
                "45%",
                "60%",
            ],
            [
                "Manual report preparation",
                "3 hours",
                "< 30 minutes",
            ],
        ],
        columns=[
            "KPI",
            "Illustrative Baseline",
            "Target",
        ],
    )

    st.dataframe(
        targets,
        hide_index=True,
        use_container_width=True,
    )

    st.caption(
        """
        These figures are illustrative project targets for the simulated case study
        and should not be presented as actual measured business results.
        """
    )

    st.subheader("Post-Implementation Review")

    st.write(
        """
        The review would assess:

        - whether critical business requirements were achieved;
        - whether staff adopted the new processes;
        - whether expected operational benefits were realised;
        - outstanding defects or process issues;
        - stakeholder feedback;
        - opportunities for Phase 2 improvement.
        """
    )

    st.subheader("Phase 2 Opportunities")

    st.write(
        """
        - Customer loyalty programme
        - Advanced customer segmentation
        - Birthday and re-engagement campaigns
        - Customer self-service booking
        - Advanced BI reporting
        - Additional automation
        """
    )

    footer()

# =========================================================
# 12 TRACEABILITY
# =========================================================

elif page == "12 · Traceability":

    page_header(
        "12",
        "Requirements Traceability",
        "Demonstrating how business problems connect to requirements, delivery and testing.",
    )

    st.subheader("End-to-End Traceability")

    st.markdown(
        """
        **Business Problem → Business Requirement → Functional Requirement → User Story → UAT**
        """
    )

    st.dataframe(
        traceability,
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        "Download Traceability Matrix",
        traceability.to_csv(index=False),
        file_name="spa_crm_traceability.csv",
        mime="text/csv",
    )

    st.subheader("Example")

    st.code(
        """
P03
Inconsistent appointment follow-up
        ↓
BR-04
Reduce manual appointment communication
        ↓
FR-15
Automatically send appointment reminders
        ↓
US-04
As a receptionist, I want reminders
to be automatically generated...
        ↓
UAT-04
Verify reminder workflow
        ↓
Expected Result
Reminder sent according to configured rule
        """,
        language=None,
    )

    st.success(
        """
        Traceability demonstrates that the project does not contain disconnected
        documents. Each proposed CRM capability can be traced back to a business
        problem and forward to implementation and validation.
        """
    )

    footer()
