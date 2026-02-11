# Mobilier & Office Inventory System (MVP)

## Overview
This repository contains the **Functional Minimum Viable Product (MVP)** for an inventory management system designed for **Mobilier & Office Lara 2015 C.A.** The project focuses on validating the interdepartmental workflow between **Sales** and **Warehouse**, optimizing request traceability and stock control through a modern, user-centric interface.

## Tech Stack
* **Language:** Python 3.13
* **GUI Framework:** `customtkinter` (Modern UI/UX)
* **Additional Libraries:** `tkcalendar`, `babel` (Date management)
* **Architecture Pattern:** **MVC (Model-View-Controller)** - Decoupled logic for high scalability.
* **Persistence:** In-memory state simulation (MVP stage).

## Key Features
* **Multi-Role Authentication:** Integrated login system with Role-Based Access Control (RBAC).
* **Sales Dashboard:** Full interface for creating and tracking furniture requests.
* **Warehouse Dashboard:** Control panel for stock dispatch and inventory lookup.
* **Modern UI:** Responsive and dark-themed components using CustomTkinter.
* **Input Validation:** Real-time feedback for user credentials and form entries.

## Installation & Setup
To run this prototype locally, ensure you have Python installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Petters26/mobilier-inventory-system.git
   cd mobilier-inventory-system

2. **Install Dependencies**
This project uses a `requirements.txt` file for automated setup:

    ```bash
    pip install -r requirements.txt

3. **Run the Application:**
     ```bash
     python main.py

## Demo Credentials (MVP Access)
To test the different workflows and role-based dashboards, use the following credentials:

| Role | Username | Password |
| :--- | :--- | :--- |
| **Warehouse Manager** | `almacen` | `123` |
| **Sales Representative** | `ventas` | `123` |

## Roadmap & Future Enhancements
This project is currently in the **UI/UX Validation Phase**. Future development cycles include:

- [ ] **RESTful API Integration:** Transitioning from in-memory state to a robust backend service.
- [ ] **Database Persistence:** Integration with PostgreSQL for secure data storage.
- [ ] **Report Engine:** Automated PDF generation for invoices and inventory audits.
- [ ] **Enhanced Security:** Implementation of `.env` variables and password hashing (**Bcrypt**).

## License
This project is licensed under the **MIT License**.
