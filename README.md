**This project predicts total monthly rent** for apartments in the cities of Mumbai, Nagpur, Pune, Bangalore and New Delhi, based on location choice, your area requirements and monthly INR/SQFT budget.
***
<h1>Dataset Preperation:</h1>
Downloaded and saved Rent data of 5 Indian cities of Mumbai, Nagpur, Pune, Bangalore, New Delhi, in ‘cities_magicbricks_rental_prices.csv’ via Kaggle.
In a **Jupyter Notebook**- Imported NumPy and Pandas library,

Followed by the CSV file via pandas’ ‘read_csv’.

Checked data’s head, shape and info 

![image](https://github.com/user-attachments/assets/58dd2ce5-3207-47a7-8dc5-8c5106712591)

Data consists of 7691 rows 10 Columns (house_type, locality, city, area, beds, bathrooms, balconies, furnishing, area_rate, rent).
After checking for empty values, dropped the columns ‘house_type', 'bathrooms', 'balconies', 'furnishing’. Data now consists of 7691 rows 6 Columns (locality, city, area, beds, area_rate, rent)
Checked for non-null values and saved the data as ‘usable_data.csv’
***
<h1>Applying ML:</h1>

Defined x as data from columns ‘locality’, ‘city’, ‘area’, ‘beds’, ‘area_rate’ and y as ‘rent’ column.

Installed Scikit-learn
_From sklearn.model_selection_ imported train_test_split;
_From sklearn.linear_model_ imported LinearRegression, Lasso, Ridge;
_From sklearn.preprocessing_ imported OneHotEncoder, StandardScaler;
_From sklearn.compose_ imported make_column_transformer;
_From sklearn.pipeline_ imported make_pipeline;
_From sklearn.metrics_ imported r2_score.

Defined and split, test and train sets at 20:80 ratio with random state as 42 (Answer to the Ultimate Question of Life, the Universe, and Everything).
Checked shape of training and testing data, then made a Column Transformer with One hot Encoder with sparse output devised for dense arrays and retaining ‘locality’ and ‘city’ columns, rest of the columns to be passthrough, then applied Linear Regression and Standard Scaler.

Defined a pipe with Column Transformer, Linear Regression and Standard Scaler. Then fitted training data through the pipe.
Saved prediction of x’s testing data through the pipe as y_pred_lr then checked the r2 score of y’s testing data with y_pred_lr.

![image](https://github.com/user-attachments/assets/21a6286f-54ca-4829-8140-e5a04d0e06bd)

Followed the same steps for applying LASSO (L1 Regularization) followed by Ridge (L2 Regularization)
Since the R2 score returned similar values, imported Pickle and saved the Linear Regression Model as 'rent_predictor.pkl’
***

<h1>Frontend development:</h1>

In a python file via an IDE, imported Streamlit, Pandas, NumPy, and Pickle.
Saved data as CSV file via pandas’ ‘read_csv’ then saving it in a data frame as df.
Added Webpage title ‘Rent Predictor’

In an ‘if’ statement defined ‘city’ and ‘locality’ in df’s columns:
Made a selection box of ‘city_option’ titled ‘City’ with concatenated option consisting of the button’s dropdown button label 'Select City...’ alongside sorted column of ‘city’ with unique values.
Repeated the same for ‘Locality_option’ titled 'Locality’ with dropdown label 'Enter Locality...’


![image](https://github.com/user-attachments/assets/71f464ad-bb96-49a0-8986-5cb99eb5926c)


‘beds’ with ‘Beds_option’ titled as ‘Bedrooms’ with dropdown label ‘Enter Bedrooms…’.
Followed by ‘area’ & ‘area_rate’ titled as as ‘Area’ & ‘Budget’ with 'Enter required area in square feet...’ & 'Enter INR per square feet...’ as  dropdown labels.


![image](https://github.com/user-attachments/assets/413ac250-7e2a-4ecc-9daf-3bd3700d7d22)


Defined Predict function with x’s columns, created dataframe from the same with columns placed in a single row so to match with the feature names expected by the ML model.
Loaded pre-trained 'rent_predictor.pkl' model into the memory using rb (read binary) mode, deserealized using pickle.load.

'rent_predictor.pkl' is used to make predictions on the input data by the user, which is then rounded to 2 decimal places.

Defined another ‘if’ statement so to pass all the input values from city_option, Locality_option, Area_option, Beds_option, Budget_option to the predict function, then ‘write’ the displayed result.

![image](https://github.com/user-attachments/assets/c548da68-14f5-4522-9da7-a24f7c75d00e)

Added three exceptions for error handling.
