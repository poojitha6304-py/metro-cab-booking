import streamlit as st
st.set_page_config(
    page_title="Metro+Cab Booking",
    layout="centered")
st.title("Metro and Cab Booking Application")
st.divider()
name=st.text_input("Enter your Name")
stations=["Select","JNTUH","MYP","LB NAGAR","KPHB"]
from_station=st.selectbox("From Station",stations)
to_station=st.selectbox("To Station",stations)
tickets=st.number_input("No of Tickets",min_value=1,max_value=10,value=1)
st.divider()
need_cab=st.radio("Do you need a cab ?",
["Yes","NO"],index=None)
cab_destination=""
if need_cab=="Yes":
    cab_destination=st.text_input("Enter the Location")
st.divider()
if st.button("Generate Bill",use_container_width=True):
    if name.strip()=="":
        st.error("Please entre your name")
    elif from_station=="Select":
        st.error("Please select the from station")
    elif to_station=="Select":
        st.error("Please select the to station")
    elif from_station==to_station:
        st.error("Both stations cannot be the same")
    elif need_cab=="Yes" and cab_destination.strip()=="":
        st.error("Please enter the cab destination")
    else:
        metro_fare=40
        metro_total=metro_fare*tickets
        #cab fare
        if need_cab=="Yes":
            cab_fare=150
        else:
            cab_fare=0
        final_total=metro_total+cab_fare
        st.success("Booking details Generated!")
        st.subheader("Metro Ticket Information")
        st.write(f"Name:{name}")
        st.write(f"From Station:{from_station}")
        st.write(f"To Station:{to_station}")
        st.write(f"Tickets:{tickets}")
        st.write(f"Total{metro_total}")
        if need_cab=="Yes":

            st.subheader("Cab information")
            st.write(f"Cab from:{to_station} ")
            st.write(f"Drop :To {cab_destination}")
            st.write(f"Cab bill:{cab_fare}")
        else:
            st.write("No Cab selected")
        st.divider()
        st.subheader("Final Bill")
        st.write(f"Metro Fare:{metro_total}")
        if need_cab=="Yes":
            st.write("Cab Fare : 150")
        st.markdown(f"Total:{final_total}")