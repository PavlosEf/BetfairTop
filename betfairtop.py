import streamlit as st

# Function for calculation
def calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission):
    lay_stake = (back_stake * back_odds) / lay_odds
    liability = lay_stake * (lay_odds - 1)
    back_bet_win = (back_stake * (back_odds - 1)) - liability
    lay_bet_win = lay_stake * (1 - commission / 100)

    market_profit = back_stake * (back_odds - 1) - liability
    commission_paid = lay_stake * (commission / 100)
    net_profit = market_profit - commission_paid
    yield_percent = (net_profit / back_stake) * 100

    return {
        "Lay Stake": round(lay_stake, 2),
        "Liability": round(liability, 2),
        "Profit if Back Bet Wins": round(back_bet_win, 2),
        "Profit if Lay Bet Wins": round(lay_bet_win, 2),
        "Market Profit": round(market_profit, 2),
        "Commission Paid": round(commission_paid, 2),
        "Net Profit": round(net_profit, 2),
        "Yield": round(yield_percent, 2),
    }

# Layout
st.title("Top Price / Betfair Calculator")
st.markdown("This calculator helps you calculate lay stakes, liabilities, and profits for matched betting scenarios.")

# Input Fields
st.markdown("### Input Parameters")
col1, col2 = st.columns(2)

with col1:
    back_odds = st.number_input("Back Odds (decimal):", min_value=1.01, value=2.5, step=0.01)
    lay_odds = st.number_input("Lay Odds (decimal):", min_value=1.01, value=2.4, step=0.01)

with col2:
    back_stake = st.number_input("Back Stake (£):", min_value=0.0, value=100.0, step=1.0)
    commission = st.slider("Exchange Commission (%):", min_value=0.0, max_value=100.0, value=5.0)

# Calculation Button
if st.button("Calculate"):
    results = calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission)

    # Display Results
    st.markdown("### Results")

    result_cols = st.columns([1, 1])
    with result_cols[0]:
        st.markdown("#### Wins")
        st.markdown(f"Back Bet Profit: **£{results['Profit if Back Bet Wins']}**")
        st.markdown(f"Market Profit: **£{results['Market Profit']}**")
        st.markdown(f"Commission Paid: **£{results['Commission Paid']}**")
        st.markdown(f"Net Profit: **£{results['Net Profit']}**")
        st.markdown(f"Yield: **{results['Yield']}%**")

    with result_cols[1]:
        st.markdown("#### Loses")
        st.markdown(f"Lay Bet Profit: **£{results['Profit if Lay Bet Wins']}**")
        st.markdown(f"Liability: **£{results['Liability']}**")
        st.markdown(f"Net Profit: **£{results['Net Profit']}**")
        st.markdown(f"Yield: **{results['Yield']}%**")

# Style the Page
st.markdown(
    """
    <style>
        /* Align input boxes and layout */
        div.stButton {text-align: center;}
        div.stNumberInput > label {
            font-weight: bold;
        }
        div[data-testid="stMetricValue"] {
            font-size: 1.25em;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
