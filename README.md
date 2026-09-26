# Digital Marketing Request Processing Using Queueing Theory and FPGA

## Project Overview

This project develops a queueing-model-based request processing system for analyzing and managing digital marketing workloads.

Digital marketing platforms receive a continuous flow of requests such as:

- Advertisement clicks
- Website visits
- Customer inquiries
- Product searches
- Campaign interactions
- Notification requests

When many requests arrive simultaneously, they form queues and experience waiting time before processing.

This project uses **queueing theory** to model this behavior.

The current implementation uses:

- **M/M/1 Queueing Model**
- **FCFS (First-Come-First-Served) Queue**
- **Python-based reference implementation**

The future goal is to implement the system on a **PYNQ-Z2 FPGA**, process real application data, and extend the system from **M/M/1 to M/M/N**.

---

# Project Objectives

The main objectives of this project are:

- Develop a mathematical queueing model for request processing.
- Implement an M/M/1 queueing model using Python.
- Implement FCFS scheduling for request ordering.
- Generate and verify test cases.
- Develop a hardware-compatible fixed-point model.
- Implement the queueing model on FPGA.
- Compare FPGA results with Python reference results.
- Extend the single-server M/M/1 model to a multi-server M/M/N model.

---

# System Concept

The proposed system represents a digital marketing request processing environment.

```text
Digital Marketing Requests
            |
            ↓
    Request Collector
            |
            ↓
        FCFS Queue
            |
            ↓
       M/M/1 Model
            |
            ↓
    Processing Server
            |
            ↓
        Results
```

The FCFS queue determines the order of request processing.

The M/M/1 model mathematically analyzes the behavior of the queue.

---

# Queueing Model

## M/M/1 Model

M/M/1 represents:

### First M
Poisson arrival process.

### Second M
Exponential service time.

### 1
Single processing server.

The main parameters are:

```text
λ = Arrival rate
μ = Service rate
ρ = Utilization
n = Number of customers
```

The system is stable when:

\[
\lambda < \mu
\]

---

# M/M/1 Mathematical Equations

## Utilization

\[
\rho=\frac{\lambda}{\mu}
\]

## Probability of Zero Customers

\[
P_0=1-\rho
\]

## Probability of n Customers

\[
P_n=(1-\rho)\rho^n
\]

## Average Number of Customers in System

\[
L=\frac{\lambda}{\mu-\lambda}
\]

## Average Queue Length

\[
L_q=\frac{\lambda^2}{\mu(\mu-\lambda)}
\]

## Average Time in System

\[
W=\frac{1}{\mu-\lambda}
\]

## Average Waiting Time

\[
W_q=\frac{\lambda}{\mu(\mu-\lambda)}
\]

The model also verifies:

\[
L=\lambda W
\]

\[
L_q=\lambda W_q
\]

---

# FCFS Queue

FCFS stands for:

**First-Come-First-Served**

It ensures that requests are processed in the same order they arrive.

Example:

Arrival order:

```text
R1 → R2 → R3 → R4
```

Processing order:

```text
R1 → R2 → R3 → R4
```

The FCFS queue represents how real systems handle incoming requests before assigning processing resources.

---

# Current Software Implementation

The current software implementation is developed using Python.

The system includes:

- M/M/1 mathematical calculations
- Input generation
- FCFS queue handling
- Request management
- Test generation
- Automated verification

---

# Repository Structure

```text
os-queueing-project/

│
├── main.py
├── inputs.py
├── mm1.py
├── queue_fcfs.py
├── request.py
├── generate_tests.py
├── verify_tests.py
├── test_fcfs.py
├── mm1_test_vectors.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

# File Description

| File | Description |
|---|---|
| main.py | Executes the M/M/1 queueing model |
| inputs.py | Generates λ, μ and n values |
| mm1.py | Contains M/M/1 mathematical calculations |
| queue_fcfs.py | Implements FCFS queue operations |
| request.py | Defines request information |
| generate_tests.py | Generates M/M/1 test vectors |
| verify_tests.py | Verifies calculated results |
| test_fcfs.py | Tests FCFS queue operation |
| mm1_test_vectors.csv | Stores generated test cases |
| requirements.txt | Python dependency information |
| README.md | Project documentation |

---

# Installation and Setup

## Requirements

- Python 3.x
- Git

No external Python libraries are required currently.

---

## Clone Repository

```bash
git clone https://github.com/sujaykarthi/os-queueing-project.git
```

Enter the project folder:

```bash
cd os-queueing-project
```

---

# Running the Project

## Run M/M/1 Model

```bash
python main.py
```

This generates:

- Arrival rate (λ)
- Service rate (μ)
- Number of customers (n)

and calculates:

- Utilization
- Probabilities
- Queue length
- Waiting time

---

## Generate Test Vectors

```bash
python generate_tests.py
```

This creates:

```text
mm1_test_vectors.csv
```

---

## Verify Results

```bash
python verify_tests.py
```

This compares calculated values with expected results.

---

## Test FCFS Queue

```bash
python test_fcfs.py
```

This verifies that requests are processed in the correct order.

---

# Test Vector Generation

The project currently contains:

```text
Total Test Cases : 100

Stable Cases     : 80

Unstable Cases   : 20
```

The test vectors include:

- λ
- μ
- n
- Stability condition
- ρ
- P0
- Pn
- L
- Lq
- W
- Wq

These test cases act as the software reference dataset for future FPGA verification.

---

# Verification

The system verifies:

- Queue stability
- Utilization (ρ)
- Probability values
- Average queue length
- Waiting time

The following relationships are checked:

```text
L = λW

Lq = λWq
```

This ensures mathematical consistency.

---

# Sample Output

Example:

```text
========== M/M/1 QUEUE ==========

Arrival rate (λ) : 3.39
Service rate (μ) : 17.22
Number (n)       : 5

---------------------------------

Queue status     : STABLE

ρ                : 0.196864
P0               : 0.803136
Pn               : 0.000237
L                : 0.245119
Lq               : 0.048255
W                : 0.072307
Wq               : 0.014235

=================================
```

---

# Current Project Status

## Completed

✅ M/M/1 mathematical model  
✅ Python implementation  
✅ FCFS queue implementation  
✅ Request model  
✅ 100 test cases  
✅ Stable and unstable testing  
✅ Verification system  
✅ GitHub repository  

---

## In Progress

🔄 Fixed-point conversion  
🔄 Verilog implementation  
🔄 FPGA testbench development  
🔄 Hardware FIFO queue  

---

# FPGA Implementation Plan

Target hardware:

```text
PYNQ-Z2 FPGA Board
```

The planned hardware architecture:

```text
Incoming Requests

        |
        ↓

    Hardware FIFO

        |
        ↓

 M/M/1 Accelerator

        |
        ↓

 Processed Output
```

Hardware modules:

- Fixed-point M/M/1 accelerator
- FIFO request queue
- Verification testbench

Python results will be used as the reference for FPGA output comparison.

---

# Future Development Roadmap

The planned development stages are:

```text
Python M/M/1 Model
          |
          ↓
Fixed-Point Conversion
          |
          ↓
Verilog M/M/1 Accelerator
          |
          ↓
Hardware FIFO Queue
          |
          ↓
PYNQ-Z2 FPGA Implementation
          |
          ↓
Real Digital Marketing Data
          |
          ↓
M/M/N Multi-Server Model
```

---

# Real Data Integration

Currently:

```text
Random λ and μ values
```

are used for testing.

In the future:

```text
Digital Marketing Events
          |
          ↓
Request Arrival Data
          |
          ↓
Calculate Arrival Rate λ
          |
          ↓
Queueing Model
```

Real application requests will replace simulated inputs.

---

# M/M/N Extension

The current system uses:

```text
M/M/1
```

with one server.

Future development will extend it to:

```text
M/M/N
```

where multiple servers process requests.

Example:

```text
              Server 1
             /
Requests → Queue → Server 2
             \
              Server N
```

The existing FCFS and request architecture will be preserved while replacing the single-server model with a multi-server system.

---

# Conclusion

This project establishes a queueing-based request processing system for digital marketing applications.

The current stage provides:

- A verified Python M/M/1 model
- FCFS request scheduling
- Automated testing
- Reference results for hardware comparison

The next stage focuses on converting the model into fixed-point hardware and implementing it on the PYNQ-Z2 FPGA platform.