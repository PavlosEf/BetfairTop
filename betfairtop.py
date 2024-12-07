import streamlit as st

def calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission):
    """
    Calculate lay stake, liability, and profit for a back and lay bet.
    """
    # Calculate the lay stake
    lay_stake = (back_stake * back_odds) / lay_odds

    # Calculate the liability
    liability = lay_stake * (lay_odds - 1)

    # Calculate potential outcomes
    back_bet_win = (back_stake * (back_odds - 1)) - liability
    lay_bet_win = lay_stake * (1 - commission / 100)

    return {
        "Lay Stake": round(lay_stake, 2),
        "Liability": round(liability, 2),
        "Profit if Back Bet Wins": round(back_bet_win, 2),
        "Profit if Lay Bet Wins": round(lay_bet_win, 2),
    }

# Streamlit app layout
st.title("Back & Lay Betting Calculator")

st.write("This calculator helps you calculate lay stakes, liabilities, and profits for matched betting scenarios.")

# Input fields
st.sidebar.header("Input Parameters")
back_stake = st.sidebar.number_input("Back Stake (£):", min_value=0.0, value=10.0, step=1.0)
back_odds = st.sidebar.number_input("Back Odds (decimal):", min_value=1.01, value=2.5, step=0.01)
lay_odds = st.sidebar.number_input("Lay Odds (decimal):", min_value=1.01, value=2.4, step=0.01)
commission = st.sidebar.slider("Exchange Commission (%):", min_value=0.0, max_value=100.0, value=5.0)

# Calculate results
if st.sidebar.button("Calculate"):
    results = calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission)

    # Results Display
    st.subheader("Calculation Results")
    st.write(f"### Lay Stake: £{results['Lay Stake']}")
    st.write(f"### Liability: £{results['Liability']}")
    st.write(f"### Profit if Back Bet Wins: £{results['Profit if Back Bet Wins']}")
    st.write(f"### Profit if Lay Bet Wins: £{results['Profit if Lay Bet Wins']}")

    # Summary Table
    st.table(
        {
            "Outcome": ["Back Bet Wins", "Lay Bet Wins"],
            "Profit (£)": [results["Profit if Back Bet Wins"], results["Profit if Lay Bet Wins"]],
        }
    )
else:
    st.write("Please input values and click the **Calculate** button to see results.")

# Footer
st.markdown("---")


      
#  Initial commit for betting calculator
