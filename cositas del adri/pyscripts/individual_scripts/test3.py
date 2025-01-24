import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    filename='invalid_values.log',  # Log file
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_integers_with_logging(df):
    """
    Validates that all values in the DataFrame (excluding column 0) are integers.
    Logs any non-integer values using Python's logging module.

    Parameters:
        df (pd.DataFrame): The DataFrame to validate.
    """
    # Iterate over all columns starting from column 1
    for col in df.columns[1:]:
        for idx, value in enumerate(df[col]):
            try:
                # Check if the value can be converted to an integer
                int(value)
            except (ValueError, TypeError):
                # Log the invalid value
                logging.warning(f"Invalid value '{value}' at row {idx}, column '{col}'")

    print("Validation complete. Check 'invalid_values.log' for details.")

# Dataframe from CSV
df = pd.read_csv('/pyscripts/data_sample/precip.P3.MIROC5.RCP60.2006-2100.REGRESION.dat', skiprows=2, sep=r'\s+', engine='python')

print("Original DataFrame:")
print(df)

# Validate the DataFrame
validate_integers_with_logging(df)


