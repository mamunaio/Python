import tkinter as tk

def show_name():
    # ১. ইনপুট বক্স থেকে লেখাটা নিচ্ছি
    name = entry_box.get()

    # ২. যদি নাম খালি না থাকে
    if name:
        # ৩. result_label এর লেখা পরিবর্তন করছি (.config দিয়ে)
        result_label.config(text=f"Hello, {name}! Welcome to GUI.")
    else:
        result_label.config(text="Please enter your name first!")

root = tk.Tk()
root.title("Name Greeter App")
root.geometry("400x300")

# --- উইজেট সাজানো ---

# ১. সাধারণ লেখা
label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
label.pack(pady=10)

# ২. ইনপুট বক্স (Entry)
entry_box = tk.Entry(root, font=("Arial", 14))
entry_box.pack(pady=5)

# ৩. বাটন
btn = tk.Button(root, text="Submit", font=("Arial", 12), bg="lightblue", command=show_name)
btn.pack(pady=10)

# ৪. ফলাফল দেখানোর জন্য একটি খালি লেবেল
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="green")
result_label.pack(pady=20)

root.mainloop()