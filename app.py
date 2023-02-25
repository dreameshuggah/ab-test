import streamlit as st
import pandas as pd
from utils.functions import plot_chart, run_ab_test

st.set_page_config(
    page_title="A/B Testing App",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

st.write(
    """
    # A/B Testing App
    Upload your experiment results to see the significance of your A/B test.
    """
)

uploaded_file = st.file_uploader("Upload CSV", type=".csv")

use_example_file = st.checkbox(
    "Use example file", False, help="Use in-built example file to demo the app"
)

ab_default, result_default = None, None
conversions_a, conversions_b = 0, 0
visitors_a, visitors_b = 0, 0
submit_button = False

# If CSV is not uploaded and checkbox is filled, use values from the example file
# and pass them down to the next if block
if use_example_file:
    uploaded_file = "data/Website_Results.csv"
    ab_default = ["variant"]
    result_default = ["converted"]

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### Data preview")
    st.dataframe(df.head())

    st.markdown("### Select columns for analysis")
    with st.form(key="my_form"):
        ab = st.multiselect(
            "A/B column",
            options=df.columns,
            help="Select which column refers to your A/B testing labels.",
            default=ab_default,
        )

        if ab:
            control = df[ab[0]].unique()[0]
            treatment = df[ab[0]].unique()[1]
            decide = st.radio(
                f"Is *{treatment}* Group B?",
                options=["Yes", "No"],
                help="Select yes if this is group B (or the treatment group) from your test.",
            )
            if decide == "No":
                control, treatment = treatment, control
            visitors_a = df[ab[0]].value_counts()[control]
            visitors_b = df[ab[0]].value_counts()[treatment]

        result = st.multiselect(
            "Result column",
            options=df.columns,
            help="Select which column shows the result of the test.",
            default=result_default,
        )

        if result:
            conversions_a = (
                df[[ab[0], result[0]]].groupby(ab[0]).agg("sum")[result[0]][control]
            )
            conversions_b = (
                df[[ab[0], result[0]]].groupby(ab[0]).agg("sum")[result[0]][treatment]
            )

        with st.expander("Adjust test parameters"):
            st.markdown("### Parameters")
            st.radio(
                "Hypothesis type",
                options=["One-sided", "Two-sided"],
                index=0,
                key="hypothesis",
                help="A one-sided hypothesis test tests whether a parameter of interest is significantly greater than or less than the test static.\nA two-sided hypothesis test tests whether there is a significant difference between a parameter of interest and the test statistic, regardless of direction.",
            )
            st.slider(
                "Significance level (α)",
                min_value=0.01,
                max_value=0.10,
                value=0.05,
                step=0.01,
                key="alpha",
                help="The probability of mistakenly rejecting the null hypothesis, if the null hypothesis is true. This is also called false positive and type I error. ",
            )
        submit_button = st.form_submit_button(label="Submit")

    if not ab or not result:
        st.warning("Please select both an **A/B column** and a **Result column**.")
        st.stop()

    if submit_button:

        run_ab_test(uploaded_file, conversions_a, conversions_b, visitors_a, visitors_b)

        if st.session_state['name'] != '':
            st.write("")
            st.write("## Results for A/B test from ", st.session_state['name'])
            st.write("")

        [m_col1, m_col2] = st.columns(2)

        # Use st.metric to display difference in conversion rates
        if st.session_state['m_col1'] != '':
            with m_col1:
                st.metric(
                    "Delta",
                    value=f"{(st.session_state['m_col1']):.3g}%",
                    delta=f"{(st.session_state['m_col1']):.3g}%",
                )

        # Display whether A/B test result is statistically significant
        if st.session_state['m_col2'] != '':
            with m_col2:
                st.metric("Significant?", value=st.session_state.significant)

        if 'plot' in st.session_state:
            st.write("")
            st.write("")
            # Plot bar chart of conversion rates
            plot_chart(st.session_state['plot'])

        # conversions and stat-sig tables
        n_col1, n_col2 = st.columns([2, 1])
        if st.session_state['table1'] != '':
            n_col1.write(st.session_state['table1'])

        if st.session_state['table2'] != '':
            n_col1.write(st.session_state['table2'])
