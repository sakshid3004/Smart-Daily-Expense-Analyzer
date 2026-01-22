import streamlit as st
import datetime

# page configuration
st.set_page_config(page_title="Expense Analyzer", page_icon="💸")

st.title("💸 Smart Daily Expense Analyzer")
st.write("This app helps students track daily expenses and analyze spending habits.")

st.markdown("---")

# initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# input form
st.subheader("➕ Add New Expense")

with st.form("expense_form"):
    date = st.date_input("Date", datetime.date.today())
    category = st.selectbox("Category", ["Food", "Travel", "Education", "Shopping", "Other"])
    amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
    note = st.text_input("Note (optional)")
    submit = st.form_submit_button("Add Expense")

    if submit:
        st.session_state.expenses.append({
            "date": date,
            "category": category,
            "amount": amount,
            "note": note
        })
        st.success("Expense added successfully!")

st.markdown("---")

# display expenses
st.subheader("📋 Expense List")

if st.session_state.expenses:
    total = 0
    for i, exp in enumerate(st.session_state.expenses, start=1):
        st.write(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['note']}")
        total += exp['amount']

    st.markdown("---")
    st.subheader("📊 Summary")
    st.write(f"**Total Spending:** ₹{total}")

    # simple analysis
    if total > 3000:
        st.warning("Your spending is high. Try to control unnecessary expenses.")
    else:
        st.success("Good job! Your spending is under control.")
else:
    st.info("No expenses added yet.")



