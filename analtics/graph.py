import matplotlib.pyplot as plt
import numpy as np

def redistribute_sales(sales_data, old_time_range, new_time_range):
    """
    Redistribute sales data to fit a new time range.

    Parameters:
    - sales_data (list): List containing the number of sales for each time point.
    - old_time_range (list): List containing the old time points.
    - new_time_range (list): List containing the new time points.

    Returns:
    - list: Redistributed sales data.

    Example:
    new_sales_data = redistribute_sales([10, 20, 15, 25], ['Day 1', 'Day 2', 'Day 3', 'Day 4'], ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'])
    """
    # Check if the length of sales_data and old_time_range is the same
    if len(sales_data) != len(old_time_range):
        raise ValueError("Length of sales_data and old_time_range must be the same")

    # Use numpy's interpolation to redistribute sales data
    old_indices = np.arange(len(old_time_range))
    new_indices = np.linspace(0, len(old_time_range) - 1, len(new_time_range))
    
    redistributed_sales = np.interp(new_indices, old_indices, sales_data)

    return redistributed_sales.tolist()

def display_sales_graph(sales_data, time_range, time_scale):
    """
    Display a line graph of sales over a variable time range.

    Parameters:
    - sales_data (list): List containing the number of sales for each time point.
    - time_range (list): List containing the time points.
    - time_scale (str): Time scale for the x-axis, e.g., 'Days', 'Months', 'Years'.

    Example:
    display_sales_graph([10, 20, 15, 25], ['Day 1', 'Day 2', 'Day 3', 'Day 4'], 'Days')
    """
    # Check if the length of sales_data and time_range is the same
    if len(sales_data) != len(time_range):
        raise ValueError("Length of sales_data and time_range must be the same")

    # Create a line graph
    plt.plot(time_range, sales_data, marker='o', linestyle='-')

    # Add labels and title
    plt.xlabel(time_scale)
    plt.ylabel('Number of Sales')
    plt.title('Sales Over Time')

    # Show the graph
    plt.show()

# Example usage
sales_data = [10, 20, 15, 25]
time_range_days = ['Day 1', 'Day 2', 'Day 3', 'Day 4']

# Example time ranges for months and years
time_range_weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
time_range_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
time_range_years = ['2021', '2022', '2023', '2024', '2025']

# Menu to choose time scale
print("Select time scale:")
print("1. Days")
print("2. Weeks")
print("3. Months")
print("4. Years")

choice = input("Enter the number of your choice: ")

if choice == '1':
    time_scale = 'Days'
    time_range = time_range_days
elif choice == '2':
    time_scale = 'Weeks'
    time_range = time_range_weeks
elif choice == '3':
    time_scale = 'Months'
    time_range = time_range_months
elif choice == '4':
    time_scale = 'Years'
    time_range = time_range_years
else:
    print("Invalid choice. Using default time scale (Days).")
    time_scale = 'Days'
    time_range = time_range_days

# Redistribute sales data based on the chosen time scale
new_time_range = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']

# Ensure the new time range has the same length as sales data
new_time_range = new_time_range[:len(sales_data)]

# Redistribute sales data
redistributed_sales = redistribute_sales(sales_data, time_range, new_time_range)

# Display the graph with redistributed sales data
display_sales_graph(redistributed_sales, new_time_range, time_scale)
