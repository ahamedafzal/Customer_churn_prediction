#import necessary libraries
import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
#create an object for scaling
scaler=MinMaxScaler()
#loading the model
loaded_model=pickle.load(open("model.csv","rb"))
#creating prediction function
def prediction(input):
    input_data = np.asarray(input)
    input_data = input_data.reshape(1, -1)
    prediction = loaded_model.predict(scaler.transform(input_data))
    # print(prediction)
    if prediction==0:
        return "The customer is a valid customer"
    else:
        return "The customer is a churn"

#creatin main function
def main():

    st.title("Customer Churn Prediction")
    columns=['Tenure', 'PreferredLoginDevice', 'CityTier',
       'WarehouseToHome', 'PreferredPaymentMode', 'Gender', 'HourSpendOnApp',
       'NumberOfDeviceRegistered', 'PreferedOrderCat', 'SatisfactionScore',
       'MaritalStatus', 'NumberOfAddress', 'Complain', 'OrderCount',
       'DaySinceLastOrder', 'CashbackAmount']
    login_device=["Mobile Phone","Computer"]
    payment_mode=["Debit Card","Credit Card","E wallet","Cash on Delivery","UPI"]
    gender=["Female","Male"]
    order_category=["Laptop & Accessory","Mobile Phone","Fashion","Grocery","Others"]
    marital_status=["Married","Single","Divorced"]

    Tenure=st.number_input("Enter tenure period")
    PreferredLoginDevice = st.selectbox("Select login device",login_device)
    CityTier = st.number_input("Enter city tier")
    WarehouseToHome = st.number_input("Enter distance from ware house")
    PreferredPaymentMode = st.selectbox("Select payment mode",payment_mode)
    Gender = st.selectbox("Select your gender",gender)
    HourSpendOnApp = st.number_input("Enter hours spend on app")
    NumberOfDeviceRegistered = st.number_input("Enter number of device registered")
    PreferedOrderCat = st.selectbox("Select category",order_category)
    SatisfactionScore = st.number_input("Enter satisfactory score")
    MaritalStatus = st.selectbox("Select marital status",marital_status)
    NumberOfAddress = st.number_input("Enter no of addresses")
    Complain = st.number_input("Enter no of complains")
    OrderCount = st.number_input("Enter order count")
    DaySinceLastOrder = st.number_input("Enter the no of days since your last order")
    CashbackAmount = st.number_input("Enter the cash back amount recieved")

#initialising customer variable
    customer=""
#create a button
    if st.button("Predict"):
        #PreferredLoginDevice
        if PreferredLoginDevice=="computer":
            PreferredLoginDevice=0
        else:
            PreferredLoginDevice=1
        #PreferredPaymentMode
        if PreferredPaymentMode=="Debit Card":
            PreferredPaymentMode=2
        elif PreferredPaymentMode=="Credit Card":
            PreferredPaymentMode=1
        elif PreferredPaymentMode=="E wallet":
            PreferredPaymentMode=3
        elif PreferredPaymentMode=="Cash on Delivery":
            PreferredPaymentMode=0
        else:
            PreferredPaymentMode=4

        #Gender
        if Gender=="Female":
            Gender=0
        else:
            Gender=1

        #PreferredOrderCat
        if PreferedOrderCat=="Laptop & Accessory":
            PreferedOrderCat=3
        elif PreferedOrderCat=="Mobile Phone":
            PreferedOrderCat=2
        elif PreferedOrderCat=="Fashion":
            PreferedOrderCat=0
        elif PreferedOrderCat=="Grocery":
            PreferedOrderCat=1
        else:
            PreferedOrderCat=4

        #MartialStatus
        if MaritalStatus=="Married":
            MaritalStatus=1
        elif MaritalStatus=="Single":
            MaritalStatus=2
        else:
            MaritalStatus=0

        customer=prediction([Tenure,PreferredLoginDevice,CityTier,WarehouseToHome,PreferredPaymentMode,Gender,HourSpendOnApp,
       NumberOfDeviceRegistered,PreferedOrderCat,SatisfactionScore,MaritalStatus,NumberOfAddress,Complain,OrderCount,
       DaySinceLastOrder,CashbackAmount])

    st.success(customer)

if __name__=="__main__":
    main()