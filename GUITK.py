import tkinter as tk
from tkinter import messagebox

def confirm_values():
    confirmation_message = f"""Confirm Input Values:

Current Pension Value: {current_value_entry.get()}
Annual Return (%): {annual_return_entry.get()}
Interest Period: {interest_period_entry.get()}
Years Until Retirement: {years_till_retire_entry.get()}
Additional Monthly Contributions: {additional_contributions_entry.get()}"""

    confirmation = messagebox.askyesno("Confirmation", confirmation_message)
    if confirmation:
        calculate_compound_interest()

def calculate_compound_interest():
    try:
        current_value = float(current_value_entry.get())
        annual_return = float(annual_return_entry.get()) / 100
        interest_period = int(interest_period_entry.get())
        years_till_retire = int(years_till_retire_entry.get())
        additional_contributions = float(additional_contributions_entry.get())

        # Calculations
        interest_period_calc = (1 + annual_return / interest_period)
        topower = (interest_period * years_till_retire)
        interest_plus_principal = current_value * (interest_period_calc ** topower)

        oneplus = (1 + (annual_return / interest_period))
        topower2 = (interest_period * years_till_retire)
        period_rate = annual_return / interest_period
        halfdone = (((oneplus ** topower2) - 1) / period_rate)
        future_value_with_deposits = additional_contributions * halfdone

        total_amount = interest_plus_principal + future_value_with_deposits

        # Display result
        total_amount_label.config(text=f"Expected pension amount: £{total_amount:,.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create main application window
app = tk.Tk()
app.title("Compound Interest Calculator")

# Create entry fields
current_value_label = tk.Label(app, text="Current Pension Value:")
current_value_label.grid(row=0, column=0)
current_value_entry = tk.Entry(app)
current_value_entry.grid(row=0, column=1)

annual_return_label = tk.Label(app, text="Annual Return (%):")
annual_return_label.grid(row=1, column=0)
annual_return_entry = tk.Entry(app)
annual_return_entry.grid(row=1, column=1)

interest_period_label = tk.Label(app, text="Interest Payments (Per Year):")
interest_period_label.grid(row=2, column=0)
interest_period_entry = tk.Entry(app)
interest_period_entry.grid(row=2, column=1)

years_till_retire_label = tk.Label(app, text="Years Untill Retirement:")
years_till_retire_label.grid(row=3, column=0)
years_till_retire_entry = tk.Entry(app)
years_till_retire_entry.grid(row=3, column=1)

additional_contributions_label = tk.Label(app, text="Additional Monthly Contributions:")
additional_contributions_label.grid(row=4, column=0)
additional_contributions_entry = tk.Entry(app)
additional_contributions_entry.grid(row=4, column=1)

# Create 'Confirm' button
confirm_button = tk.Button(app, text="Confirm", command=confirm_values)
confirm_button.grid(row=5, column=0, columnspan=2)

# Result label
total_amount_label = tk.Label(app, text="")
total_amount_label.grid(row=6, column=0, columnspan=2)

app.mainloop()
