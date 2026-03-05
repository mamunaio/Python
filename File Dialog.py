import tkinter as tk
from tkinter import filedialog # ফাইল খোঁজার বক্স ওপেন করার জন্য

def select_pdf():
    # এই লাইনটি কম্পিউটারের ফাইল সিলেক্ট করার উইন্ডো ওপেন করবে
    filenames = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    # কনসোলে দেখাবে আপনি কয়টি ফাইল সিলেক্ট করেছেন
    print(f"User selected: {filenames}")

    # লেবেলে দেখাবে কয়টি ফাইল সিলেক্ট করা হলো
    status_label.config(text=f"Selected {len(filenames)} files")

# --- GUI Setup ---
root = tk.Tk()
root.title("My PDF Merger")
root.geometry("400x200")

# ১. নির্দেশনা
label = tk.Label(root, text="Select PDF files to merge", font=("Arial", 14))
label.pack(pady=20)

# ২. বাটন (ফাইল সিলেক্ট করার জন্য)
btn = tk.Button(root, text="Select PDFs", bg="orange", command=select_pdf)
btn.pack(pady=10)

# ৩. স্ট্যাটাস দেখার জন্য লেবেল
status_label = tk.Label(root, text="No file selected", fg="gray")
status_label.pack(pady=10)

root.mainloop()