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
        topower = (interest_period * years_to_retire)
        interest_plus_principal = current_value * (interest_period_calc ** topower)

        oneplus = (1 + (annual_return / interest_period))
        topower2 = (interest_period * years_to_retire)
        period_rate = annual_return / interest_period
        halfdone = (((oneplus ** topower2) - 1) / period_rate)
        future_value_with_deposits = additional_contributions * halfdone

        total_amount = interest_plus_principal + future_value_with_deposits

        # Hide input fields and confirmation button
        for widget in input_widgets:
            widget.pack_forget()

        confirm_button.pack_forget()

        # Display result
        total_amount_label.configure(text=f"Expected pension amount: £{total_amount:,.2f}")
        total_amount_label.pack()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create application
app = ctk.CTk()

# Create a frame for window
main_frame = ctk.CTkFrame(app)
main_frame.pack(padx=20, pady=20)

# Create entry fields
current_value_label = ctk.CTkLabel(main_frame, text="Current Pension Value:")
current_value_label.pack()
current_value_entry = ctk.CTkEntry(main_frame)
current_value_entry.pack()

annual_return_label = ctk.CTkLabel(main_frame, text="Annual Return (%):")
annual_return_label.pack()
annual_return_entry = ctk.CTkEntry(main_frame)
annual_return_entry.pack()

interest_period_label = ctk.CTkLabel(main_frame, text="Interest Payments (Per Year):")
interest_period_label.pack()
interest_period_entry = ctk.CTkEntry(main_frame)
interest_period_entry.pack()

years_to_retire_label = ctk.CTkLabel(main_frame, text="Years Until Retirement:")
years_to_retire_label.pack()
years_to_retire_entry = ctk.CTkEntry(main_frame)
years_to_retire_entry.pack()

additional_contributions_label = ctk.CTkLabel(main_frame, text="Additional Monthly Contributions:")
additional_contributions_label.pack()
additional_contributions_entry = ctk.CTkEntry(main_frame)
additional_contributions_entry.pack()

# Store input widgets
input_widgets = [
    current_value_label, current_value_entry,
    annual_return_label, annual_return_entry,
    interest_period_label, interest_period_entry,
    years_to_retire_label, years_to_retire_entry,
    additional_contributions_label, additional_contributions_entry
]

# Create 'Confirm' button
confirm_button = ctk.CTkButton(main_frame, text="Confirm", command=confirm_values)
confirm_button.pack(pady=20)

# Result label
total_amount_label = ctk.CTkLabel(main_frame, text="")
# total_amount_label.pack()

app.mainloop()
