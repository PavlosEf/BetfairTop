import streamlit as st

# Function for calculation
def calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission):
    lay_stake = (back_stake * back_odds) / lay_odds
    liability = lay_stake * (lay_odds - 1)
    back_bet_profit_win = back_stake * (back_odds - 1) - liability
    back_bet_profit_lose = -back_stake
    lay_bet_profit_win = lay_stake * (1 - commission / 100)
    lay_bet_profit_lose = -liability

    market_profit_win = back_bet_profit_win + lay_bet_profit_win
    market_profit_lose = lay_bet_profit_lose + back_bet_profit_lose

    commission_paid = lay_stake * (commission / 100)
    net_profit_win = market_profit_win - commission_paid
    net_profit_lose = market_profit_lose - commission_paid

    return {
        "Lay Stake": round(lay_stake, 2),
        "Liability": round(liability, 2),
        "Back Bet Profit Win": round(back_bet_profit_win, 2),
        "Back Bet Profit Lose": round(back_bet_profit_lose, 2),
        "Lay Bet Profit Win": round(lay_bet_profit_win, 2),
        "Lay Bet Profit Lose": round(lay_bet_profit_lose, 2),
        "Market Profit Win": round(market_profit_win, 2),
        "Market Profit Lose": round(market_profit_lose, 2),
        "Commission Paid": round(commission_paid, 2),
        "Net Profit Win": round(net_profit_win, 2),
        "Net Profit Lose": round(net_profit_lose, 2),
    }

# Layout
st.title("Minimal Lay Bet Calculator")
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
        commission = st.number_input("Commission (%)", min_value=0.0, max_value=100.0, value=2.5, step=0.1)

# Calculate Lay Stake on Input
lay_stake = round((back_stake * back_odds) / lay_odds, 2)
total_stake = round(back_stake + lay_stake, 2)
st.markdown(f"### Calculated Lay Stake: €{lay_stake} (Total Stake: €{total_stake})")

# Calculation Button
if st.button("Calculate"):
    results = calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission)

    # Display Results
    st.markdown("### Results Breakdown")

    # Simplified Display
    st.markdown(
        f"""
        <style>
        .result-box {{
            background-color: #F8F9FA;
            border: 1px solid #DEE2E6;
            border-radius: 8px;
            padding: 15px;
            margin: 10px;
            text-align: left;
        }}
        </style>
        <div class="result-box">
            <b>If Win:</b>
            <ul>
                <li>Back Bet Profit: €{results['Back Bet Profit Win']}</li>
                <li>Lay Bet Profit: €{results['Lay Bet Profit Win']}</li>
                <li>Market Profit: €{results['Market Profit Win']}</li>
                <li>Commission Paid: €{results['Commission Paid']}</li>
                <li>Net Profit: €{results['Net Profit Win']}</li>
            </ul>
            <b>If Lose:</b>
            <ul>
                <li>Back Bet Profit: €{results['Back Bet Profit Lose']}</li>
                <li>Lay Bet Profit: €{results['Lay Bet Profit Lose']}</li>
                <li>Market Profit: €{results['Market Profit Lose']}</li>
                <li>Commission Paid: €{results['Commission Paid']}</li>
                <li>Net Profit: €{results['Net Profit Lose']}</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown("---")
st.markdown("Designed for minimalistic and effective betting calculations.")
