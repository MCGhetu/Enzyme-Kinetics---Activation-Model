# Enzyme Kinetics - Activation Model

The Enzymatic Activity Analysis and Plotting Tool is a Python script designed to facilitate the analysis of enzymatic activity data obtained from experimental assays. Leveraging the power of libraries such as pandas, numpy, and matplotlib, this tool enables researchers to efficiently process and visualize their data, gaining valuable insights into enzyme kinetics.
The model used in this tool is a modified version of the classic Michaelis-Menten equation, incorporating additional terms to account for specific experimental conditions.

## Michaelis-Menten Equation
The Michaelis-Menten equation describes the rate of enzymatic reactions based on the concentration of substrate [S].

$v = \frac{V_{max} \cdot [S]}{K_M + [S]}$

Where:
- $\( v \)$ is the reaction rate,
- $\( V_{max} \)$ is the maximum reaction rate,
- $\( K_M \)$ is the Michaelis constant,
- $\( [S] \)$ is the substrate concentration.

## Modified Model Equation
The modified model equation is an extension of the classic Michaelis-Menten equation, incorporating additional terms to account for specific experimental conditions.

$v = \frac{V_{max} \cdot ([S] + 2.13 \cdot [S]^2 / 17.7)}{K_M + [S] + [S]^2 / 17.7}$

Where:
- $\( v \)$ is the reaction rate,
- $\( V_{max} \)$ is the maximum reaction rate,
- $\( K_M \)$ is the Michaelis constant,
- $\( [S] \)$ is the substrate concentration.

# Key Features:

Data Import: The tool seamlessly imports experimental data from Excel files, providing flexibility in data storage and organization.

Data Processing: It offers robust data processing capabilities, including the extraction of time data represented in text format to numerical values using regular expressions.

Curve Fitting: Utilizing the curve fitting functionality from scipy.optimize, the tool fits linear models to the data points, allowing researchers to assess the goodness of fit through the calculation of the R-squared value.

Enzyme Kinetics Modeling: Researchers can model enzyme activation mechanisms using the provided mathematical model, enabling the estimation of key parameters such as vmax and KM. 

Interactive Visualization: The tool generates interactive plots, allowing researchers to visualize the experimental data, fitted models, and enzyme kinetics parameters.

# User-friendly:

Users can simply run the script and provide the path to their Excel file containing the experimental data. The tool will then process the data, perform analysis, and generate informative plots for visualization. Additionally, researchers can customize the tool according to their specific experimental setups and requirements.

# Advantages:

Streamlined Data Analysis: Eliminates manual data processing tasks, saving time and reducing errors.
Insightful Visualizations: Provides clear and intuitive visualizations of experimental data and model fits, aiding in data interpretation.
Parameter Estimation: Enables researchers to estimate important parameters related to enzyme kinetics, facilitating further analysis and understanding of enzymatic activity.
Future Enhancements:

Future enhancements to the tool may include support for additional data formats, integration with statistical analysis libraries for advanced data processing, and optimization of plotting features for enhanced visualization.

