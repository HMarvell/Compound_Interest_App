import customtkinter as ctk
from tkinter import messagebox

def confirm_values():
    confirmation_message = f"""Confirm Input Values:

Current Pension Pot: {current_value_entry.get()}
Expected Annual Return (%): {annual_return_entry.get()}
Interest Period: {interest_period_entry.get()}
Years Until Retirement: {years_to_retire_entry.get()}
Additional Monthly Contributions: {additional_contributions_entry.get()}"""

    confirmation = messagebox.askyesno("Confirmation", confirmation_message)
    if confirmation:
        calculate_compound_interest()

def calculate_compound_interest():
    try:
        current_value = float(current_value_entry.get())
        annual_return = float(annual_return_entry.get()) / 100
        interest_period = int(interest_period_entry.get())
        years_to_retire = int(years_to_retire_entry.get())
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

        # Hide input fields and confirmation button
        for widget in input_widgets:
            widget.grid_remove()

        confirm_button.grid_remove()

        # Display result
        total_amount_label.configure(text=f"Expected pension amount: £{total_amount:,.2f}")
        total_amount_label.grid(row=5, column=0, columnspan=2)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create main application window
app = ctk.CTk()

# Create entry fields
current_value_label = ctk.CTkLabel(app, text="Current Pension Value:")
current_value_label.grid(row=0, column=0)
current_value_entry = ctk.CTkEntry(app)
current_value_entry.grid(row=0, column=1)

annual_return_label = ctk.CTkLabel(app, text="Annual Return (%):")
annual_return_label.grid(row=1, column=0)
annual_return_entry = ctk.CTkEntry(app)
annual_return_entry.grid(row=1, column=1)

interest_period_label = ctk.CTkLabel(app, text="Interest Payments (Per Year):")
interest_period_label.grid(row=2, column=0)
interest_period_entry = ctk.CTkEntry(app)
interest_period_entry.grid(row=2, column=1)

years_to_retire_label = ctk.CTkLabel(app, text="Years Until Retirement:")
years_to_retire_label.grid(row=3, column=0)
years_to_retire_entry = ctk.CTkEntry(app)
years_to_retire_entry.grid(row=3, column=1)

additional_contributions_label = ctk.CTkLabel(app, text="Additional Monthly Contributions:")
additional_contributions_label.grid(row=4, column=0)
additional_contributions_entry = ctk.CTkEntry(app)
additional_contributions_entry.grid(row=4, column=1)

# Store input widgets for easier management
input_widgets = [
    current_value_label, current_value_entry,
    annual_return_label, annual_return_entry,
    interest_period_label, interest_period_entry,
    years_to_retire_label, years_to_retire_entry,
    additional_contributions_label, additional_contributions_entry
]

# Create 'Confirm' button
confirm_button = ctk.CTkButton(app, text="Confirm", command=confirm_values)
confirm_button.grid(row=5, column=0, columnspan=2)

# Result label
total_amount_label = ctk.CTkLabel(app, text="")
# total_amount_label.grid(row=6, column=0, columnspan=2)

app.mainloop()
