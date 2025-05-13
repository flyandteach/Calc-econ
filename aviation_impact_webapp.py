
import streamlit as st

# Define aviation multipliers
economic_multiplier = 1.8  # Output multiplier

# Streamlit App
st.title("✈️ Aviation Infrastructure Economic Impact Calculator")

st.header("Section A: Airport Budgets")
capital_budget = st.number_input("Capital Budget ($/year)", min_value=0.0, value=5000000.0)
operating_budget = st.number_input("Operating Budget ($/year)", min_value=0.0, value=2000000.0)
other_capital = st.number_input("Other Capital Expenditures ($/year)", min_value=0.0, value=1000000.0)

st.header("Section B: Commercial Aviation Passenger Activity")
annual_enplanements = st.number_input("Annual Enplanements (#)", min_value=0, value=100000)
visitor_percentage = st.number_input("Visitor Percentage (%)", min_value=0.0, max_value=100.0, value=60.0)

st.header("Section C: General Aviation Operations")
ga_operations = st.number_input("Annual GA Operations (#)", min_value=0, value=50000)
transient_percentage = st.number_input("Transient Operations Percentage (%)", min_value=0.0, max_value=100.0, value=30.0)
avg_persons_per_op = st.number_input("Average Persons per Operation", min_value=0.0, value=1.5)

st.header("Section D: Visitor Spending per Trip")
lodging = st.number_input("Lodging ($)", min_value=0.0, value=150.0)
restaurant = st.number_input("Restaurant/Bar ($)", min_value=0.0, value=100.0)
transport = st.number_input("Local Transportation ($)", min_value=0.0, value=50.0)
retail = st.number_input("Retail Purchases ($)", min_value=0.0, value=75.0)
entertainment = st.number_input("Entertainment ($)", min_value=0.0, value=50.0)

if st.button("Calculate Economic Impact"):
    commercial_visitors = annual_enplanements * (visitor_percentage / 100)
    ga_visitors = ga_operations * (transient_percentage / 100) * avg_persons_per_op
    total_visitors = commercial_visitors + ga_visitors

    total_spending_per_visitor = lodging + restaurant + transport + retail + entertainment
    total_visitor_spending = total_visitors * total_spending_per_visitor

    total_airport_expenditures = capital_budget + operating_budget + other_capital
    direct_impact = total_airport_expenditures + total_visitor_spending
    total_economic_impact = direct_impact * economic_multiplier

    st.subheader("Results:")
    st.write(f"**Total Commercial Visitors:** {commercial_visitors:,.0f}")
    st.write(f"**Total GA Visitors:** {ga_visitors:,.0f}")
    st.write(f"**Total Visitors:** {total_visitors:,.0f}")
    st.write(f"**Total Visitor Spending:** ${total_visitor_spending:,.2f}")
    st.write(f"**Total Airport Expenditures:** ${total_airport_expenditures:,.2f}")
    st.write(f"**Direct Economic Impact:** ${direct_impact:,.2f}")
    st.success(f"**Total Economic Output (Direct x 1.8): ${total_economic_impact:,.2f}**")
