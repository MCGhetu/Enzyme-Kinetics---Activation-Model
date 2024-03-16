import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Function to extract the number of seconds from text data
def extract_seconds(text):
    pattern = r'(\d+)\s*min(?:ute)?(?:s)?(?:\s*(\d+)\s*s(?:ec(?:ond)?s?)?)?'
    
    matches = re.findall(pattern, text)
    
    total_seconds = 0
    for match in matches:
        minutes = int(match[0]) if match[0] else 0
        seconds = int(match[1]) if match[1] else 0
        total_seconds += minutes * 60 + seconds

    return total_seconds

# Function defining a linear equation
def linear_func(x, m, c):
    return m * x + c

# Function to calculate R-squared value
def r_squared(y_true, y_pred):
   
    y_mean = np.mean(y_true)
    ss_tot = np.sum((y_true - y_mean) ** 2)
    ss_res = np.sum((y_true - y_pred) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared

# Activation mechanism model function
def activation_mechanism(c, vmax, KM):
    return vmax * (c + 2.13 * c**2 / 17.7) / (KM + c + c**2 / 17.7)

def main():

     # Read data from an Excel file
    df = pd.read_excel("example.xlsx")
    
    # Extract ox data from excel file
    ox_data = df.iloc[11, 2:]
    if ox_data.dtype == 'object':  # If ox_data is text
        ox_data = ox_data.astype(str)
        if ox_data.str.match(r'\d+ min \d+ s').any():
            ox_data = ox_data.apply(extract_seconds).tolist()
        else:
            ox_data = ox_data.astype(float).tolist()
            
    # Extract oy data and perform unit conversions (absorbance to concentration)
    oy_data = df.iloc[12:25, 2:].astype(float).values
    oy_data = oy_data * (10**6) / 6220 / 0.58

    # Extract legend labels
    legend_labels = df.iloc[12:25, 0].tolist()

    TON = []
    vmax_values = []
    KM_values = []
    pg_TON_data = []

    # Removing data points from the end of the graph until the linear fit achieves the highest R-squared value
    for i in range(oy_data.shape[0]):
        x_data = np.array(ox_data[:len(oy_data[i])]) 
        y_data = oy_data[i]

        popt, _ = curve_fit(linear_func, x_data, y_data)
        y_fit = linear_func(x_data, *popt)
        r_squared_val = r_squared(y_data, y_fit)

        while len(y_data) > 3 and r_squared_val < 0.999:
            x_data = x_data[:-1]
            y_data = y_data[:-1]
            popt, _ = curve_fit(linear_func, x_data, y_data)
            y_fit = linear_func(x_data, *popt)
            r_squared_val = r_squared(y_data, y_fit)

        plt.plot(x_data, y_data, label=f'Data {i+1}')

        # Extracting the slope value for each graph and convert it 
        slope = abs(popt[0] * 1000) / 5
        TON.append(slope)
        
    # Plot the cut data
    plt.xlabel('Time (s)')
    plt.ylabel('[NADH] (uM)')
    plt.legend(legend_labels)
    plt.show()
    
    # Substracting the value of the last slope from all the other values
    last_slope = TON[-1]
    TON = [slope - last_slope for slope in TON[:-1]]

    # Plot the extracted and converted slope values (TON) against [S] concentration and fit it with the modified version
    pg_values = [50, 35, 25, 12.5, 6.25, 2, 1, 0.5, 0.25, 0.125, 0.0625]

    popt, _ = curve_fit(activation_mechanism, pg_values, TON)

    popt, _ = curve_fit(activation_mechanism, pg_values, TON, bounds=(0, [1000, 1000]))
    vmax, KM = popt
    c_values = np.linspace(min(pg_values), max(pg_values))
    plt.plot(c_values, activation_mechanism(c_values, *popt), linestyle='--', color='red', label='Michaelis-Menten Fit')
    vmax_values.append(vmax)
    KM_values.append(KM)

    pg_TON_df = pd.DataFrame({'[3PG] (mM)': pg_values, 'TON (1/s)': [round(val, 2) for val in TON]})
    
    # Print a table containing the [S] values and the corresponding TON value 
    print("Slope Table:")
    print(pg_TON_df)
    
    # Print the graph of [S] vs TON
    plt.scatter(pg_values, TON)
    plt.xlabel('[3PG] (mM)')
    plt.ylabel('TON (1/s)')
    plt.title('Enzymatic activity')
    plt.show()
    
    # Extract the desired parameters (vmax, KM)
    print("vmax value:")
    print(vmax.round(2))
    print("KM value:")
    print(KM.round(2))

if __name__ == "__main__":
    main()
