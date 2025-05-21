# Menu App

## Creator  
**Bron Whitten**

---

## Project Structure  
```
├── resources/        # Contains application assets (e.g., .ico file)
├── src/              # Contains the main Python source code
│   └── menu_app.py   # Primary GUI application file
└── README.md         # Project overview and instructions
```

---

## Build Information  
- **Language:** Python  
- **GUI Framework:** Tkinter  

---

## Overview  
![MenuApp Screenshot](https://github.com/user-attachments/assets/e20bb6d8-e3f7-48c9-9853-8aa76d487a18)

The **Menu App** is a graphical ordering system created using Python and Tkinter. It allows users to place multiple orders from a defined menu, calculates tax, and generates a detailed receipt saved as a `.txt` file in the same directory.

---

## Features  
- Multi-order support within one transaction  
- Subtotal and sales tax calculation  
- Receipt generation in plain text format  
- Clean and intuitive GUI  
- Custom icon for window branding

---

## Usage Instructions  

### 1. Launch the Application  
Navigate to the `src/` folder and run the `MenuApp.py` file.

```bash
cd src
python menu_app.py
```

### 2. Add an Order  
Click the **“Add an Order”** button to open the menu interface.  
Select one or more items using the checkboxes and click **“Add to Order”**.

### 3. Submit Order  
- Continue adding items or click **“Submit Order”** to finalize.  
- A `receipt.txt` file is saved in the current directory.
- A confirmation message will appear on-screen.

### 4. Quit  
Use the **“Quit”** button at any point to exit the application.

---

## Configuration  

- **Menu Items, Prices, and Tax Rate** are defined as constants in the source code (`menu_app.py`) and can be modified as needed.  
- **Window Icon** is specified using a `.ico` file located in the `resources/` folder.

---

## File Summary  
- `src/menu_app.py` – Main application logic and GUI interface  
- `resources/app_icon.ico` – Application icon (must be in the specified path)

---

## Status  
**Archived** — This project is no longer actively maintained.

---

## License  
This project is open for educational use. Attribution appreciated.
