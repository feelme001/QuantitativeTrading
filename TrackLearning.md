### 12/12/2023
- DailyPy
- read https://www.researchgate.net/profile/Lisa-Goldberg-5/publication/267791427_The_Barra_Equity_Volatility_Futures_Model_EVX1/links/5506f6ea0cf2d7a281228541/The-Barra-Equity-Volatility-Futures-Model-EVX1.pdf
- read https://d1wqtxts1xzle7.cloudfront.net/60249823/Barras_risk_model20190809-8329-u0l1rd-libre.pdf?1565404030=&response-content-disposition=inline%3B+filename%3DBARRAs_Risk_Models.pdf&Expires=1702461739&Signature=AjG-FbK5HAngNX4414RYr~HUKiU9IFUGOswVL2GDzdy3rTiSyASEOu3EI2TPIzpiToDn4SBvAglz7buDgkqYlOqlYoeuN~qkuG5Zb5V5886b3pRABxga7DOSHzLLSFHIlJ5vb880e~W-gJgJmiBei8lOlv4rg6uWaQ9urBB5nyrh1h4eP~rL1XdAi2xdlQDMKoLqkm4mGVYnAmMPK6x6C~yd5WYZvlkLJEb-zSPhynCrLfVzVdYGbYFPOwF08c3yTSFIHg4ygkPub-PFTBqB6T-~vdIBJkYGjdboggw5s5IK8O9rvCNM3VKjtdCmopULUkzfTWCzo~YcBpyIfe0aZg__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA

### 12/11/2023
- coding practice

### 12/8/2023
- Reading https://app2.msci.com/products/analytics/models/
  - 4 levels, industry
    - 10 industory factor
- VaR model

### 12/7/2023
- CheckModel EDA and Data Reprocessing section learning 

### 12/6/2023
- planning to watch this [video](https://www.youtube.com/watch?v=ro07evEWbCE&t=1946s) related to barra factor model
- pratice pandas https://pandas.pydata.org/docs/user_guide/index.html 
- reading https://app2.msci.com/products/analytics/models/
 

### 12/5/2023
- watch three factor model youtube [video](https://www.youtube.com/watch?v=HwXX_JBM8_4)
- three factor model 
  - ![Alt Text](https://drive.google.com/uc?id=1BK9RIWnS9cR_LZbexDrK_y7SoZSTx0xs) 
- My excel example [worksheet](https://docs.google.com/spreadsheets/d/1l7z_KihejnZNjK_LfhpxPQ4hu5JhFTax/edit?usp=drive_link&ouid=117366340446730717038&rtpof=true&sd=true)
- Get the three factor data library here: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
- CAPM model beta is market return s&p500 daily return coefficient with a single price daily return
  - watch youtube [video](https://www.youtube.com/watch?v=Gu8zUxgU2vA)
  - calculation [formular](https://drive.google.com/file/d/1rQIwmtcZos9HD9z0EEsTP2QYRZbz8ls-/view?usp=drive_link)
   - ![capm](https://drive.google.com/uc?id=1rQIwmtcZos9HD9z0EEsTP2QYRZbz8ls-) 
  - intercept is alpha
  - s&p500 coefficients is the beta
  - beta p-value: is it significant driving this related to confident level
  - alpha p-value: 
  - Expected-Return(Asset) = Risk-Free-Rate  +  β  ×  (Market Return  −  Risk-Free-Rate)
  - FORMULATEXT function in excel show what the formular is been used
  - ![capm](https://drive.google.com/uc?id=146uPBN7ZnVfDzY_cWus3_x5-NfEFBy-1)
- run regression model
  - Definition: R2 is a measure of the goodness of fit of a regression model. It ranges from 0 to 1
    - R2=0 indicates that the model does not explain any variability in the dependent variable.
    - R2=1 indicates that the model perfectly explains the variability in the dependent variable.
  - Interpretation
    - R2 is interpreted as the proportion of the variance in the dependent variable that can be explained by the independent variable(s) in the model.
    - For example, if R2=0.75, it means that 75% of the variance in the dependent variable is explained by the independent variable(s) in the model.
  - Calculation and more details
    - [link](https://drive.google.com/file/d/1ADHGiW462b4l4x8g3loDRHtNIGAMoymK/view?usp=drive_link)
    - ![Alt Text](https://drive.google.com/uc?id=1ADHGiW462b4l4x8g3loDRHtNIGAMoymK)
- show image in md
  - ```![Alt Text](https://drive.google.com/uc?id=your-file-id)```
  - Replace Alt Text with a descriptive text for the image, and replace your-file-id with the actual file ID.
  - example
    - ```
      https://drive.google.com/file/d/1ADHGiW462b4l4x8g3loDRHtNIGAMoymK/view?usp=drive_link
      https://drive.google.com/uc?id=1ADHGiW462b4l4x8g3loDRHtNIGAMoymK
- graph the efficient frontier and capital allocation line in excel, youtube [video](https://www.youtube.com/watch?v=dJipa0K64HI)



### 12/4/2023
- Using GPT to learn the github Barra model [barra](https://github.com/hansihuang2016/Barra-Multiple-factor-risk-model) create_filter.py and finance.py
  - ```
    np.where()

    Purpose: Returns the indices where a specified condition is true.
    
    Usage in the script:
    template = np.where(close.values[-reserve_row] != 0)[0]
    
    Example:
    import numpy as np
    arr = np.array([1, 0, 3, 0, 5])
    indices = np.where(arr != 0)[0]
    print(indices)
    # Output: [0 2 4]
  - ```
    np.delete()
    
    Purpose: Deletes elements along a specified axis.
    
    Usage in the script:
    template = np.delete(template, 1)
    
    Example:
    import numpy as np

    arr = np.array([1, 2, 3, 4, 5])
    new_arr = np.delete(arr, 2)  # Delete element at index 2
    print(new_arr)
    # Output: [1 2 4 5]
  - ```
    pd.read_excel()

    Purpose: Read an Excel file into a Pandas DataFrame.

    Usage in the script:
    data = pd.read_excel(tech_fname, tecnical_index_list)

    Example
    import pandas as pd
    df = pd.read_excel("example.xlsx", sheet_name="Sheet1")
    Get excel data from sheet1
  - ```
    // only get close colomn from sheet1
    close = data['close']

    // use reserve_row
    reserve_row = 192
    close.values[-reserve_row]: Here, it is using array indexing to get the row at index -reserve_row. The negative index -reserve_row means counting from the end of the array, similar to how negative indices work in Python. In this context, it's retrieving the row that is 192 positions from the end.

    template = np.where(close.values[-reserve_row] != 0)[0]:
    This line involves NumPy operations:
    close.values: Converts the 'close' column to a NumPy array.
    close.values[-reserve_row]: Selects the row at index -reserve_row from the bottom (i.e., 192nd row from the end).
    close.values[-reserve_row] != 0: Creates a boolean array where each element is True if the corresponding closing price is not equal to 0.
    np.where(...): Returns the indices where the condition is True.
    np.where(close.values[-reserve_row] != 0)[0]: Retrieves the indices of non-zero closing prices in the selected row.
  - ```
    pd.read_excel(fname).iloc[2:, :]: Read the Excel file, starting from the third row (index 2) to skip header rows.
  - ```
    temp = pd.concat([temp, pd.read_excel(fname).iloc[2:, :]], axis=0)
    df.iloc[row_indexer, column_indexer]
    row_indexer: The integer-based index or slice to select rows.
    column_indexer: The integer-based index or slice to select columns.
    Example 1: Select Specific Rows and Columns
    
    import pandas as pd

    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)

    # Select the first two rows and the first two columns
    subset = df.iloc[0:2, 0:2]
    print(subset)
    
    output
       A  B
    0  1  4
    1  2  5

    in pandas, when using the iloc indexer, the indexing starts from 0. This includes both rows and columns. Therefore, the header row is considered row 0.

    So, when you see df.iloc[2:, :], it means selecting all rows starting from row 2 (the third row) onward and all columns.
  - ```
    In pandas, the term "axis" refers to either the rows or columns of a DataFrame. The axis parameter is commonly used in many pandas functions to specify whether the operation should be performed along the rows (axis 0) or columns (axis 1). 
      
      import pandas as pd

      data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
      df = pd.DataFrame(data)

      # Sum along axis 0 (sum each column)
      column_sums = df.sum(axis=0)
      print(column_sums)

      A     6
      B    15
      C    24
      dtype: int64

      # Sum along axis 1 (sum each row)
      row_sums = df.sum(axis=1)
      print(row_sums)
      0    12
      1    15
      2    18
      dtype: int64

      column_sums is not a DataFrame; it's a pandas Series. When you apply the sum function along a specific axis, the result is a Series.
      # Sum along axis 0 (sum each column)
      column_sums = df.sum(axis=0)
      print(column_sums)

      column_sums_df = column_sums.to_frame(name='Sum')
      print(column_sums_df)
         Sum
      A    6
      B   15
      C   24
  - ```
    // This line sets the 'Accper' column as the index of the DataFrame a. The drop=False parameter ensures that the 'Accper' column is kept as a regular column as well.
    a = a.set_index('Accper', drop=False)

    // This line filters the DataFrame a based on the half-yearly time series hfyr. It selects only the rows where the 'Accper' column matches the values in hfyr. Note that ix is an older method for selection; you might want to consider using loc for label-based indexing or iloc for integer-location based indexing.
    a = a.ix[hfyr]

    // Finally, this line sets a multi-level index using both 'Stkcd' and 'Accper'. The resulting DataFrame a has a hierarchical index based on the stock code and the accounting period.
    a = a.set_index(['Stkcd', 'Accper'])
  - ```
    Multi-Level Index:
              |  A  |  B  |  C
    --------------------------------
    Level 1   |           |
    Level 2   |           |
    ----------------------------
      row1    | 10  | 20  | 30
      row2    | 40  | 50  | 60
      row3    | 70  | 80  | 90
      
    # Access data for 'Stkcd' = 2 and 'Accper' = '2020-01'
    value_2020_01 = df_multi_index.loc[(2, '2020-01'), 'Value']
    print("Value for Stkcd=2 and Accper='2020-01':", value_2020_01)

    Value for Stkcd=2 and Accper='2020-01': 20


















  
- Reading [pdf](https://github.com/hansihuang2016/Barra-Multiple-factor-risk-model/blob/master/Multiple-factor-risk-model.pdf) 

### 12/3/2023
- Barra 
  - Read [link](https://www.investopedia.com/terms/b/barra-risk-factor-analysis.asp)
    - The Barra Risk Factor Analysis is a multi-factor model, incorporates over 40 data metrics, including earnings growth, share turnover, and senior debt rating.
  - Learning [barra](https://github.com/hansihuang2016/Barra-Multiple-factor-risk-model) from github
  - GPT
    - Step 1: Understand the Basics
      - Before diving into the details, make sure you have a solid understanding of basic financial concepts, factor models, and risk management. Familiarize yourself with terms like alpha, beta, risk factors, and portfolio risk.
        - Risk and Volatility:
          - Risk refers to the uncertainty or variability of returns. 
          - Volatility is a measure of how much the price of an asset fluctuates.
        - Alpha and Beta:
          - Alpha measures the excess return of an investment compared to its expected return.
          - Beta measures the sensitivity of an asset's returns to market movements.
    - Step 2: Define the Universe
    - Step 3: Select Risk Factors
    - Step 4: Gather Data
    - Step 5: Estimate Factor Exposures
    - Step 6: Calculate Factor Returns
    - Step 7: Build the Risk Model
    - Step 8: Analyze Portfolio Risk
    - Step 9: Portfolio Optimization
    - Step 10: Monitor and Update