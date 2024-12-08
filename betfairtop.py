import streamlit as st

# Function for calculation
def calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission):
    lay_stake = (back_stake * back_odds) / lay_odds
    liability = lay_stake * (lay_odds - 1)
    back_bet_profit = (back_stake * (back_odds - 1)) - liability
    lay_bet_profit = lay_stake * (1 - commission / 100)

    market_profit_back = (back_stake * (back_odds - 1)) - liability
    commission_paid = lay_stake * (commission / 100)
    net_profit_back = market_profit_back - commission_paid
    yield_back = (net_profit_back / back_stake) * 100

    net_profit_lay = lay_bet_profit - liability
    yield_lay = (net_profit_lay / back_stake) * 100

    return {
        "Lay Stake": round(lay_stake, 2),
        "Liability": round(liability, 2),
        "Back Bet Profit": round(back_bet_profit, 2),
        "Lay Bet Profit": round(lay_bet_profit, 2),
        "Market Profit": round(market_profit_back, 2),
        "Commission Paid": round(commission_paid, 2),
        "Net Profit (Back)": round(net_profit_back, 2),
        "Yield (Back)": round(yield_back, 2),
        "Net Profit (Lay)": round(net_profit_lay, 2),
        "Yield (Lay)": round(yield_lay, 2),
    }

# Layout
st.title("Back & Lay Betting Calculator")
st.markdown("Calculate stakes, profits, and yield for matched betting scenarios.")

# Input Fields
st.markdown("### Input Parameters")
col1, col2 = st.columns(2)

with col1:
    back_odds = st.number_input("Back Price:", min_value=1.01, value=2.5, step=0.01)
    lay_odds = st.number_input("Lay Price:", min_value=1.01, value=2.4, step=0.01)

with col2:
    back_stake = st.number_input("Stake (Back):", min_value=0.0, value=100.0, step=1.0)
    commission = st.number_input("Commission (%):", min_value=0.0, max_value=100.0, value=5.0)

# Calculation Button
if st.button("Calculate"):
    results = calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission)

    # Display Results
    st.markdown("### Results Breakdown")

    st.markdown("#### Input Summary")
    st.write(f"**Back Odds:** {back_odds}, **Lay Odds:** {lay_odds}, **Back Stake:** €{back_stake}, **Commission:** {commission}%")

    st.markdown("#### Profit Breakdown")
    result_cols = st.columns([1, 1])

    with result_cols[0]:
        st.markdown("**Wins**")
        st.write(f"Back Bet Profit: €{results['Back Bet Profit']}")
        st.write(f"Market Profit: €{results['Market Profit']}")
        st.write(f"Commission Paid: €{results['Commission Paid']}")
        st.write(f"Net Profit: €{results['Net Profit (Back)']}")
        st.write(f"Yield: {results['Yield (Back)']}%")

    with result_cols[1]:
        st.markdown("**Loses**")
        st.write(f"Lay Bet Profit: €{results['Lay Bet Profit']}")
        st.write(f"Liability: €{results['Liability']}")
        st.write(f"Net Profit: €{results['Net Profit (Lay)']}")
        st.write(f"Yield: {results['Yield (Lay)']}%")

# Footer
st.markdown("---")
st.markdown("Designed for matched betting scenarios.")
