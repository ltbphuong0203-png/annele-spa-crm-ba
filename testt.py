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
# CUSTOM CSS
# =========================================================

# =========================================================
# CUSTOM CSS / THEME
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

    /* Cards */
    .card {
        padding: 1.3rem;
        border: 1px solid var(--border-color);
        border-radius: 14px;
        height: 100%;
        background-color: #ffffff;
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

    [data-testid="stSidebar"] [aria-checked="true"] + div {
        color: var(--primary-color);
        font-weight: 700;
    }

    /* Info / success / warning boxes */
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
        color: #66736f;
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
                Customer information, appointments, and interactions are currently
                managed through
                <strong>Excel and disconnected communication channels</strong>,
                making it difficult for staff to access complete customer histories
                and for management to track performance.
            </p>

            <p>
                Over the past two years,
                <strong>
                    missed bookings, late reminders, and inconsistent communication
                </strong>
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
        Identify the business needs, evaluate suitable CRM solutions and define
        an implementation approach that improves customer information management,
        appointment communication and management reporting.
        """
    )

    st.header("Project Lifecycle")

    st.markdown(
        """
        **Discover**  
        Business Problem → Stakeholders → Current-State Analysis

        ↓

        **Define**  
        Requirements → Prioritisation → Evaluation Criteria

        ↓

        **Select**  
        CRM Comparison → Weighted Evaluation → Recommendation

        ↓

        **Design & Implement**  
        To-Be Process → User Stories → Migration → Configuration

        ↓

        **Validate**  
        Testing → UAT → Training → Go-Live

        ↓

        **Measure**  
        Adoption → Benefits → Post-Implementation Review
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
        "Understanding why change is required before evaluating a technology solution.",
    )

    st.subheader("Problem Statement")

    st.markdown(
        """
        > The spa currently manages customer information and interactions across
        > multiple channels, resulting in fragmented customer records and limited
        > visibility of customer history.
        >
        > Booking confirmations and follow-ups are handled inconsistently, which may
        > contribute to missed appointments and lost revenue. Management also has
        > limited access to customer-retention and service-performance reporting,
        > making it difficult to identify trends and support data-driven decisions.
        """
    )

    st.subheader("Observed Business Problems")

    st.dataframe(
        business_problems,
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Root Cause Themes")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### RC01")
        st.markdown("**Fragmented customer data**")
        st.write(
            "Customer information is stored across multiple channels and is not connected into one customer view."
        )

    with c2:
        st.markdown("### RC02")
        st.markdown("**Manual communication processes**")
        st.write(
            "Booking confirmations, reminders and follow-ups depend heavily on staff actions."
        )

    with c3:
        st.markdown("### RC03")
        st.markdown("**Limited reporting capability**")
        st.write(
            "Customer, appointment and service information is difficult to consolidate for management reporting."
        )

    st.subheader("Root Cause Relationship")

    st.code(
        """
CURRENT ENVIRONMENT
       |
       +---------------------------+--------------------------+
       |                           |                          |
       v                           v                          v
Fragmented Systems          Manual Processes          Limited Data /
and Channels                and Workflows             KPI Structure
       |                           |                          |
       v                           v                          v
No Central Customer         No Standardised           Difficult to
Record                      Reminder Process          Consolidate Data
       |                           |                          |
       v                           v                          v
Incomplete Customer         Inconsistent              Limited
History                     Follow-Ups                Reporting
       |                           |                          |
       v                           v                          v
Lower Staff Efficiency      Possible Contribution     Limited Management
and Personalisation         to No-Shows               Decision Support
        """,
        language=None,
    )

    footer()


# =========================================================
# 03 CURRENT STATE
# =========================================================

elif page == "03 · Current-State Analysis":

    page_header(
        "03",
        "Current-State Analysis",
        "Understanding how customer enquiries and appointment booking currently operate.",
    )

    st.subheader("As-Is Process")

    st.code(
        """
CUSTOMER               RECEPTIONIST / STAFF              CURRENT SYSTEMS
   |                           |                                |
   | Contact spa               |                                |
   |-------------------------->|                                |
   | Phone / Social / Walk-in  |                                |
   |                           |                                |
   |                           | Search customer information    |
   |                           |------------------------------->|
   |                           |                                |
   |                           | Search spreadsheet / booking   |
   |                           | records / message history      |
   |                           |<-------------------------------|
   |                           |                                |
   |                           | Is customer found?             |
   |                           |       /       \\               |
   |                           |      Yes       No              |
   |                           |       |         |              |
   |                           |       |       Create customer   |
   |                           |       |       record manually   |
   |                           |       |         |              |
   |                           |       +---------+              |
   |                           |            |                   |
   |                           | Check availability             |
   |                           |------------------------------->|
   |                           |<-------------------------------|
   |                           |                                |
   |<--------------------------| Offer available times          |
   |                           |                                |
   | Select appointment        |                                |
   |-------------------------->|                                |
   |                           |                                |
   |                           | Create booking manually        |
   |                           |------------------------------->|
   |                           |                                |
   |<--------------------------| Confirm appointment            |
   |                           |                                |
  END
        """,
        language=None,
    )

    st.subheader("Pain Points Within the Process")

    painpoints = pd.DataFrame(
        [
            ["Search customer", "P01", "Staff search several channels and records."],
            ["Review customer history", "P02", "No single source of customer history."],
            ["Create booking", "P03", "Communication and confirmation rely on manual action."],
            ["Appointment follow-up", "P04", "No-show risks are difficult to proactively manage."],
            ["Management reporting", "P05", "Data must be manually consolidated."],
        ],
        columns=["Process Step", "Problem", "Observation"],
    )

    st.dataframe(painpoints, hide_index=True, use_container_width=True)

    st.subheader("Current-State Findings")

    st.warning(
        """
        The analysis indicates that the main issue is not a single booking step.
        The broader problem is fragmentation between customer information,
        appointment management, communications and reporting.
        """
    )

    footer()


# =========================================================
# 04 REQUIREMENTS
# =========================================================

elif page == "04 · Requirements Gathering":

    page_header(
        "04",
        "Requirements Gathering",
        "Translating stakeholder needs and process findings into structured CRM requirements.",
    )

    st.subheader("Stakeholders")

    c1, c2, c3, c4, c5 = st.columns(5)

    stakeholder_cards = [
        ("Spa Manager", "Reporting, retention, operational visibility"),
        ("Receptionist", "Customer lookup, booking, less manual work"),
        ("Therapist", "Customer history, treatment notes, preferences"),
        ("Marketing", "Segmentation, retention, targeted campaigns"),
        ("Customer", "Easy booking, confirmation, reminders, privacy"),
    ]

    for col, card in zip([c1, c2, c3, c4, c5], stakeholder_cards):
        with col:
            st.markdown(f"### {card[0]}")
            st.write(card[1])

    st.subheader("Elicitation Methods")

    e1, e2, e3 = st.columns(3)

    with e1:
        st.markdown("### Interviews")
        st.write("Understand stakeholder goals, frustrations, information needs and expectations.")

    with e2:
        st.markdown("### Process Walkthrough")
        st.write("Observe the current customer enquiry and appointment-booking workflow.")

    with e3:
        st.markdown("### Data Review")
        st.write("Review customer records, booking information, reporting and communication data.")

    st.subheader("From Insight to Requirement")

    st.markdown(
        """
        **Stakeholder insight**

        > “I have to search several places to find a customer's information.”

        ↓

        **Business need**

        Staff need one reliable view of customer information.

        ↓

        **BR-01**

        Centralise customer information to provide staff with a consistent customer view.

        ↓

        **FR-02 / FR-03 / FR-04**

        Search customers quickly, display a central profile and provide appointment history.
        """
    )

    st.subheader("Requirements Catalogue")

    type_filter = st.multiselect(
        "Requirement Type",
        options=requirements["Type"].unique(),
        default=list(requirements["Type"].unique()),
    )

    priority_filter = st.multiselect(
        "Priority",
        options=["Must", "Should", "Could", "Won't"],
        default=["Must", "Should"],
    )

    filtered = requirements[
        requirements["Type"].isin(type_filter)
        & requirements["Priority"].isin(priority_filter)
    ]

    st.dataframe(filtered, hide_index=True, use_container_width=True)

    st.download_button(
        "Download Requirements CSV",
        requirements.to_csv(index=False),
        file_name="spa_crm_requirements.csv",
        mime="text/csv",
    )

    st.subheader("MoSCoW Prioritisation")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown("### Must")
        st.write(
            """
            Customer profile  
            Customer search  
            Appointment booking  
            Therapist availability  
            Confirmation  
            Reminders
            """
        )

    with m2:
        st.markdown("### Should")
        st.write(
            """
            Retention reporting  
            Customer segmentation  
            Communication status  
            Duplicate detection
            """
        )

    with m3:
        st.markdown("### Could")
        st.write(
            """
            Birthday campaigns  
            Advanced promotions  
            Loyalty automation
            """
        )

    with m4:
        st.markdown("### Won't — Phase 1")
        st.write(
            """
            AI recommendations  
            Customer mobile app  
            Advanced predictive analytics
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
        "Comparing shortlisted solutions using requirements-driven evaluation criteria.",
    )

    st.subheader("Evaluation Approach")

    st.markdown(
        """
        Requirements  
        ↓  
        Define Evaluation Criteria  
        ↓  
        Shortlist Solutions  
        ↓  
        Requirements Fit Analysis  
        ↓  
        Weighted Decision Matrix  
        ↓  
        Recommendation
        """
    )

    st.subheader("Shortlisted Solution Types")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### CRM A")
        st.markdown("**General-Purpose CRM**")
        st.write(
            "Strong customer management, automation and reporting. May require appointment integration."
        )

    with c2:
        st.markdown("### CRM B")
        st.markdown("**Spa-Specific Platform**")
        st.write(
            "Strong appointment, therapist and service functionality with lower configuration effort."
        )

    with c3:
        st.markdown("### CRM C")
        st.markdown("**Configurable CRM**")
        st.write(
            "Flexible workflows and integration capability but requires more implementation effort."
        )

    st.subheader("Interactive Weighted Decision Matrix")

    st.caption(
        "Adjust the criterion weights to explore how different business priorities influence the recommendation."
    )

    criteria_defaults = {
        "Customer Management": 20,
        "Appointment Management": 20,
        "Automation & Reminders": 15,
        "Reporting & Analytics": 15,
        "Usability": 10,
        "Integration": 5,
        "Security & Privacy": 5,
        "Implementation Effort": 5,
        "Cost": 5,
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
            )

    total_weight = sum(weights.values())

    if total_weight != 100:
        st.warning(
            f"Current total weighting is {total_weight}%. "
            "For formal evaluation, weights should total 100%."
        )
    else:
        st.success("Weights total 100%.")

    crm_scores = {
        "CRM A": {
            "Customer Management": 5,
            "Appointment Management": 2,
            "Automation & Reminders": 5,
            "Reporting & Analytics": 5,
            "Usability": 3,
            "Integration": 5,
            "Security & Privacy": 5,
            "Implementation Effort": 2,
            "Cost": 2,
        },
        "CRM B": {
            "Customer Management": 4,
            "Appointment Management": 5,
            "Automation & Reminders": 4,
            "Reporting & Analytics": 4,
            "Usability": 5,
            "Integration": 3,
            "Security & Privacy": 4,
            "Implementation Effort": 5,
            "Cost": 4,
        },
        "CRM C": {
            "Customer Management": 5,
            "Appointment Management": 3,
            "Automation & Reminders": 5,
            "Reporting & Analytics": 4,
            "Usability": 3,
            "Integration": 5,
            "Security & Privacy": 5,
            "Implementation Effort": 3,
            "Cost": 3,
        },
    }

    matrix_rows = []

    for criterion in weights:
        matrix_rows.append(
            {
                "Criterion": criterion,
                "Weight %": weights[criterion],
                "CRM A": crm_scores["CRM A"][criterion],
                "CRM B": crm_scores["CRM B"][criterion],
                "CRM C": crm_scores["CRM C"][criterion],
            }
        )

    matrix_df = pd.DataFrame(matrix_rows)

    st.dataframe(matrix_df, hide_index=True, use_container_width=True)

    results = {}

    for crm in crm_scores:
        weighted_total = 0

        for criterion, weight in weights.items():
            weighted_total += crm_scores[crm][criterion] * weight

        if total_weight > 0:
            results[crm] = weighted_total / total_weight
        else:
            results[crm] = 0

    result_df = pd.DataFrame(
        {
            "CRM": results.keys(),
            "Weighted Score / 5": [round(x, 2) for x in results.values()],
        }
    ).sort_values("Weighted Score / 5", ascending=False)

    st.subheader("Evaluation Result")
    st.dataframe(result_df, hide_index=True, use_container_width=True)

    winner = result_df.iloc[0]["CRM"]
    score = result_df.iloc[0]["Weighted Score / 5"]

    st.success(f"Current recommended solution: {winner} — {score}/5")

    st.caption(
        "Scores are illustrative for the portfolio project. In a real selection exercise, each score would be supported by vendor research, demonstrations and stakeholder validation."
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

    st.success("CRM B — Spa-Specific Management Platform")

    st.write(
        """
        CRM B was selected because it provides the strongest alignment with the
        spa's operational requirements, particularly appointment scheduling,
        therapist availability, customer records, automated communication and ease of use.

        Although general-purpose CRM platforms may provide stronger traditional
        CRM and reporting capabilities, they require additional configuration or
        integration to support spa-specific appointment workflows.
        """
    )

    st.subheader("Decision Rationale")

    decision = pd.DataFrame(
        [
            ["Appointment Management", "Strong native capability", "Critical"],
            ["Customer Records", "Meets central-profile requirements", "Critical"],
            ["Automated Communication", "Supports confirmations and reminders", "Critical"],
            ["Usability", "Suitable for operational staff", "High"],
            ["Implementation Effort", "Lower than heavily configurable CRM options", "High"],
            ["Reporting", "Meets core requirements with some configuration", "Medium"],
        ],
        columns=["Factor", "Finding", "Importance"],
    )

    st.dataframe(decision, hide_index=True, use_container_width=True)

    st.subheader("Fit-Gap Analysis")

    gap = pd.DataFrame(
        [
            ["Customer Profile", "Supported", "None", "Standard configuration"],
            ["Appointment Scheduling", "Supported", "None", "Standard configuration"],
            ["Reminder Automation", "Supported", "Minor", "Configure reminder rules"],
            ["Retention Reporting", "Partial", "Moderate", "Configure/customise reports"],
            ["Existing Customer Data", "Not migrated", "Major", "Data cleansing and migration"],
            ["Staff Knowledge", "New system", "Major", "Training and SOP"],
            ["Operating Process", "Current manual steps", "Moderate", "Process redesign and adoption"],
        ],
        columns=["Requirement Area", "Capability", "Gap", "Response"],
    )

    st.dataframe(gap, hide_index=True, use_container_width=True)

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

    st.subheader("To-Be Process")

    st.code(
        """
CUSTOMER                RECEPTIONIST                    CRM SYSTEM
   |                          |                              |
   | Contact spa              |                              |
   |------------------------->|                              |
   |                          |                              |
   |                          | Search customer              |
   |                          |----------------------------->|
   |                          |                              |
   |                          |<-----------------------------|
   |                          | Customer found?              |
   |                          |     /       \\               |
   |                          |   Yes        No              |
   |                          |    |          |              |
   |                          |    |       Create profile     |
   |                          |    |------------------------->|
   |                          |    |                          |
   |                          |<---+--------------------------|
   |                          |                              |
   |                          | Open central customer profile |
   |                          |----------------------------->|
   |                          |<-----------------------------|
   |                          | Customer + history displayed  |
   |                          |                              |
   | Discuss required service |                              |
   |------------------------->|                              |
   |                          |                              |
   |                          | Select service               |
   |                          |----------------------------->|
   |                          |                              |
   |                          | CRM checks availability      |
   |                          |<-----------------------------|
   |                          |                              |
   |<-------------------------| Offer available times        |
   |                          |                              |
   | Select appointment       |                              |
   |------------------------->|                              |
   |                          |                              |
   |                          | Create appointment           |
   |                          |----------------------------->|
   |                          |                              |
   |                          | CRM validates conflict       |
   |                          | CRM creates booking          |
   |                          | CRM links customer record    |
   |                          |                              |
   |<-------------------------------------------------------|
   | Automatic confirmation                                  |
   |                                                         |
   |                 APPOINTMENT CONFIRMED                    |
  END
        """,
        language=None,
    )

    st.subheader("As-Is vs To-Be")

    comparison = pd.DataFrame(
        [
            ["Customer Search", "Search multiple sources", "Search central CRM profile"],
            ["Customer History", "Fragmented", "Single customer view"],
            ["Appointment Availability", "Manual checking", "CRM availability view"],
            ["Booking", "Manual record", "CRM-linked appointment"],
            ["Confirmation", "Dependent on staff", "Automatically generated"],
            ["Reporting", "Manual consolidation", "Central reporting"],
        ],
        columns=["Area", "As-Is", "To-Be"],
    )

    st.dataframe(comparison, hide_index=True, use_container_width=True)

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
            ["1", "Preparation", "Confirm scope, roles, risks and implementation schedule"],
            ["2", "Configuration", "Configure customer fields, booking rules, reminders and permissions"],
            ["3", "Data Migration", "Clean, map, import and validate customer data"],
            ["4", "Testing", "System testing and defect resolution"],
            ["5", "UAT", "Business-user validation of critical workflows"],
            ["6", "Training", "Train reception, therapists, manager and marketing users"],
            ["7", "Go-Live", "Deploy CRM and provide hypercare"],
            ["8", "Review", "Measure adoption, KPIs and improvement opportunities"],
        ],
        columns=["Phase", "Activity", "Outcome"],
    )

    st.dataframe(phases, hide_index=True, use_container_width=True)

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
        columns=["Epic", "Name"],
    )

    st.dataframe(epics, hide_index=True, use_container_width=True)

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
            ["R01", "Poor data quality", "High", "Clean and validate data before migration"],
            ["R02", "Staff resistance to new process", "Medium", "Early engagement, training and feedback"],
            ["R03", "Incorrect configuration", "Medium", "Configuration review and UAT"],
            ["R04", "Migration data loss", "High", "Backup, test migration and reconciliation"],
            ["R05", "Low user adoption", "High", "Usage monitoring and post-go-live support"],
        ],
        columns=["Risk", "Description", "Impact", "Mitigation"],
    )

    st.dataframe(risks, hide_index=True, use_container_width=True)

    footer()


# =========================================================
# 09 UAT
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

    st.dataframe(uat, hide_index=True, use_container_width=True)

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
# 10 GO LIVE
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
            ["Receptionist", "Customer search, booking, cancellation, reminders", "Workshop + Quick Guide"],
            ["Therapist", "Customer history, treatment notes", "Short Workshop + SOP"],
            ["Manager", "Dashboard, reporting, user oversight", "Manager Training"],
            ["Marketing", "Segments, customer lists and campaign workflows", "Workshop"],
        ],
        columns=["Audience", "Training Content", "Method"],
    )

    st.dataframe(training, hide_index=True, use_container_width=True)

    st.subheader("Go-Live Plan")

    st.markdown(
        """
        **T-7 Days**  
        Final data migration rehearsal and user communication

        **T-3 Days**  
        Complete staff training and confirm support contacts

        **T-1 Day**  
        Final backup and production migration preparation

        **Go-Live Day**  
        CRM available for operational use

        **Week 1**  
        Hypercare, issue tracking and daily user feedback

        **Weeks 2–4**  
        Adoption monitoring and configuration improvements
        """
    )

    st.subheader("Adoption Measures")

    adoption = pd.DataFrame(
        [
            ["Active User Rate", "% of expected staff regularly accessing CRM"],
            ["CRM Booking Rate", "% of appointments recorded through new process"],
            ["Customer Profile Completeness", "% of required customer fields completed"],
            ["Reminder Automation Rate", "% of eligible appointments receiving reminders"],
            ["User Feedback", "Staff satisfaction and reported usability issues"],
        ],
        columns=["Measure", "Purpose"],
    )

    st.dataframe(adoption, hide_index=True, use_container_width=True)

    footer()


# =========================================================
# 11 BENEFITS
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
        columns=["Original Problem", "CRM Response", "Expected Benefit"],
    )

    st.dataframe(benefit_map, hide_index=True, use_container_width=True)

    st.subheader("Benefits Realisation Targets")

    targets = pd.DataFrame(
        [
            ["Customer profile lookup time", "3 minutes", "< 30 seconds"],
            ["Follow-up completion", "40%", "> 90%"],
            ["Appointment no-show rate", "12%", "< 7%"],
            ["Repeat booking rate", "45%", "60%"],
            ["Manual report preparation", "3 hours", "< 30 minutes"],
        ],
        columns=["KPI", "Illustrative Baseline", "Target"],
    )

    st.dataframe(targets, hide_index=True, use_container_width=True)

    st.caption(
        "These figures are illustrative project targets for the simulated case study and should not be presented as actual measured business results."
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

    st.dataframe(traceability, hide_index=True, use_container_width=True)

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
