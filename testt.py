import streamlit as st

st.set_page_config(
    page_title="Spa CRM | BA Case Study",
    page_icon="💼",
    layout="wide"
)

st.title("Spa CRM Implementation")
st.subheader("Business Analyst Case Study")

st.write("""
A business analysis project exploring the selection and implementation
of a CRM solution for a spa services business.
""")

st.divider()

st.header("The Business Problem")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Customer Data", "Fragmented")
    st.write("Customer information is stored across multiple channels.")

with col2:
    st.metric("Booking Process", "Manual")
    st.write("Appointment confirmations and follow-ups rely on staff.")

with col3:
    st.metric("Reporting", "Limited")
    st.write("Management has limited visibility into retention and service performance.")

st.divider()

st.header("Project Approach")

st.write("""
**Discover → Analyse → Define Requirements → Evaluate CRM → Implement → Measure**
""")

if st.button("Explore the Case Study"):
    st.success("Streamlit is working!")
