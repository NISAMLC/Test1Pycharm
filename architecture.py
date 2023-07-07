import streamlit as st


st.title('BillDusk Architecture')

st.graphviz_chart("""

digraph{
Admin -> SuperDistributor -> MasterDistributor -> Distributor 

Admin -> Retailer

SuperDistributor -> Retailer
MasterDistributor -> Retailer
Distributor -> Retailer 

} """)