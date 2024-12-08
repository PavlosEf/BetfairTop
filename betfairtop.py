import streamlit as st

# Function for calculation
def calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission):
    lay_stake = (back_stake * back_odds) / lay_odds
    liability = lay_stake * (lay_odds - 1)
    back_bet_profit = (back_stake * (back_odds - 1)) - liability
    lay_bet_profit = lay_stake * (1 - commission / 100)

    market_profit = back_bet_profit
    commission_paid = lay_stake * (commission / 100)
    net_profit = market_profit - commission_paid
    yield_percent = (net_profit / back_stake) * 100

    return {
        "Lay Stake": round(lay_stake, 2),
        "Liability": round(liability, 2),
        "Back Bet Profit": round(back_bet_profit, 2),
        "Lay Bet Profit": round(lay_bet_profit, 2),
        "Market Profit": round(market_profit, 2),
        "Commission Paid": round(commission_paid, 2),
        "Net Profit": round(net_profit, 2),
        "Yield": round(yield_percent, 2),
    }


# Layout
st.title("Lay Bet Calculator")
st.markdown("Calculate lay stakes, liabilities, and profits for betting scenarios.")

# Input Fields
st.markdown("### Input Parameters")
with st.container():
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        back_odds = st.number_input("Back Odds", min_value=1.01, value=2.5, step=0.01)
    with col2:
        lay_odds = st.number_input("Lay Odds", min_value=1.01, value=2.4, step=0.01)
    with col3:
        back_stake = st.number_input("Back Stake (€)", min_value=0.0, value=100.0, step=1.0)
    with col4:
        commission = st.number_input("Commission (%)", min_value=0.0, max_value=100.0, value=5.0)

# Calculation Button
if st.button("Calculate"):
    results = calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission)

    # Display Results
    st.markdown("### Results Breakdown")
    st.markdown(
        """
        <style>
        .result-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 10px;
        }
        .result-box {
            background-color: #F8F9FA;
            border: 1px solid #DEE2E6;
            border-radius: 8px;
            padding: 15px;
            margin: 10px;
            width: 200px;
            text-align: center;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="result-container">
            <div class="result-box">
                <div>Lay Stake</div>
                <div>€{results['Lay Stake']}</div>
            </div>
            <div class="result-box">
                <div>Liability</div>
                <div>€{results['Liability']}</div>
            </div>
            <div class="result-box">
                <div>Net Profit</div>
                <div>€{results['Net Profit']}</div>
            </div>
            <div class="result-box">
                <div>Yield</div>
                <div>{results['Yield']}%</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Detailed Breakdown
    st.markdown("### Detailed Profit Breakdown")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Wins")
        st.write(f"Back Bet Profit: €{results['Back Bet Profit']}")
        st.write(f"Market Profit: €{results['Market Profit']}")
        st.write(f"Commission Paid: €{results['Commission Paid']}")
        st.write(f"Net Profit: €{results['Net Profit']}")
        st.write(f"Yield: {results['Yield']}%")

    with col2:
        st.markdown("#### Loses")
        st.write(f"Lay Bet Profit: €{results['Lay Bet Profit']}")
        st.write(f"Liability: €{results['Liability']}")
        st.write(f"Net Profit: €{results['Net Profit']}")
        st.write(f"Yield: {results['Yield']}%")

# Footer
st.markdown("---")
st.markdown("Designed for betting calculations.")
