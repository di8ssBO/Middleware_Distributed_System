## Installation and Setup (Windows)

Follow the steps below to set up and run the project on Windows.

### 1. Create a Virtual Environment

Open Command Prompt in the project root folder and run:

```
python -m venv .venv
```

This creates a virtual environment named `.venv` to manage project dependencies separately.

---

### 2. Activate the Virtual Environment

Run:

```
venv\Scripts\activate
```

After activation, your terminal should indicate that the virtual environment is active.

---

### 3. Install Required Dependencies

Install all required Python packages:

```
pip install -r requirements.txt
```

This installs all libraries listed in `requirements.txt`.

---

### 4. Generate gRPC Files

Create a folder for generated files:

```
mkdir generated
```

Then compile the `.proto` file:

```
python -m grpc_tools.protoc -I=proto --python_out=generated --grpc_python_out=generated proto/school.proto
```

This command generates the required Python gRPC files inside the `generated` folder.

---

### 5. Start the Servers

Run the following commands (each in a separate terminal window):

```
python servers/math_server.py
python servers/student_server.py
python servers/system_server.py
```

These commands start the backend services of the system.

---

### 6. Run the Main Application

After all servers are running, start the application:

```
python app.py
```

---

## Important

Make sure to select the correct Python Interpreter that points to the `.venv` virtual environment in your IDE. This ensures the project uses the correct installed dependencies.
