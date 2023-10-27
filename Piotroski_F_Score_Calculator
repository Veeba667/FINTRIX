import streamlit as st


def calculatePiotroski_F_score(net_income, operating_cash_flow, total_assets, long_term_debt, current_assets, current_liabilities, shares_outstanding):
    criteria = [
        net_income > 0,
        operating_cash_flow > 0,
        net_income / total_assets > 0 if total_assets > 0 else False,
        operating_cash_flow > net_income,
        long_term_debt / total_assets < 1 if total_assets > 0 else False,
        current_assets / current_liabilities > 1 if current_liabilities > 0 else False,
        shares_outstanding > 0
    ]
    
    fscore = sum(criteria)
    return fscore

def main():
    st.set_page_config(
    page_title="Piotroski's F-score Calculator",
    page_icon="💯",
    layout="wide",
    initial_sidebar_state="expanded"
    )

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.title("Piotroski F-Score Calculator")
    
    net_income = st.number_input("Net Income")
    operating_cash_flow = st.number_input("Operating Cash Flow")
    total_assets = st.number_input("Total Assets")
    long_term_debt = st.number_input("Long-term Debt")
    current_assets = st.number_input("Current Assets")
    current_liabilities = st.number_input("Current Liabilities")
    shares_outstanding = st.number_input("Shares Outstanding")
    
    if st.button("Calculate"):
        try:
            fscore = calculatePiotroski_F_score(net_income, operating_cash_flow, total_assets, long_term_debt, current_assets, current_liabilities, shares_outstanding)
        except Exception as ex:
            print('Exception:', ex)
        
        st.write("### Piotroski F-Score:")
        st.write(f"The calculated Piotroski F-Score is: {fscore}")

if __name__ == "__main__":
    main()
