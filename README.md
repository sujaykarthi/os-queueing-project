# Digital Marketing Request Processing Using Queueing Theory

A queueing-model-based system for analyzing and managing incoming digital marketing requests using **M/M/1 queueing theory** and a **First-Come, First-Served (FCFS)** queue.

The project is currently implemented and verified in **Python**. The long-term goal is to implement the queueing model on a **Zynq FPGA**, integrate it with real application requests, and extend the system from **M/M/1 to M/M/N**.

## Project Overview

Digital marketing platforms can receive a large number of events and requests, such as:

* Advertisement clicks
* Website visits
* Lead and form submissions
* Product inquiries
* Purchase events
* Campaign interactions
* Email/SMS notification requests

When multiple requests arrive and compete for processing resources, they can form a queue.

This project models that behavior using queueing theory.

The current system uses:

```text
Digital Marketing Requests
          ↓
    Request Collector
          ↓
      FCFS Queue
          ↓
  Single Processing Server
          ↓
    Processed Requests
```

The **FCFS queue** determines the order in which requests are processed, while the **M/M/1 model** mathematically analyzes the behavior of the single-server queue.

---

## Current Implementation

The current version contains:

### 1. M/M/1 Queueing Model

The mathematical model uses:

* `λ` — arrival rate
* `μ` — service rate
* `ρ` — utilization
* `P0` — probability of zero customers
* `Pn` — probability of `n` customers
* `L` — average number of customers in the system
* `Lq` — average number of customers in the queue
* `W` — average time in the system
* `Wq` — average waiting time in the queue

The system is stable when:

```text
λ < μ
```

The implemented equations are:

```text
ρ  = λ / μ

P0 = 1 - ρ

Pn = (1 - ρ) × ρ^n

L  = λ / (μ - λ)

Lq = λ² / [μ(μ - λ)]

W  = 1 / (μ - λ)

Wq = λ / [μ(μ - λ)]
```

The implementation also verifies the relationships:

```text
L  = λW

Lq = λWq
```

---

## 2. FCFS Queue

The project implements a **First-Come, First-Served (FCFS)** queue using Python's `deque`.

Requests are processed in the same order in which they enter the queue.

Example:

```text
R1 → R2 → R3 → R4 → R5
```

Processing order:

```text
R1
R2
R3
R4
R5
```

The queue implementation supports:

* Enqueue
* Dequeue
* Peek
* Empty check
* Queue size

---

## 3. Request Model

Each incoming request is represented by a `Request` object.

A request contains:

```text
Request ID
Arrival Time
Service Time
Queue Entry Time
Service Start Time
Service Completion Time
Waiting Time
Status
```

The request status progresses through the processing lifecycle:

```text
WAITING → PROCESSING → COMPLETED
```

---

## Project Structure

```text
os-queueing-project/
│
├── main.py
├── inputs.py
├── mm1.py
├── queue_fcfs.py
├── request.py
├── test_fcfs.py
├── generate_tests.py
├── verify_tests.py
├── mm1_test_vectors.csv
├── .gitignore
└── README.md
```

### File Description

| File                   | Purpose                                                                 |
| ---------------------- | ----------------------------------------------------------------------- |
| `main.py`              | Main program that connects the queueing model, requests, and FCFS queue |
| `inputs.py`            | Generates input parameters for M/M/1 testing                            |
| `mm1.py`               | Implements the M/M/1 mathematical calculations                          |
| `queue_fcfs.py`        | Implements the FCFS queue                                               |
| `request.py`           | Defines the request object and request lifecycle                        |
| `test_fcfs.py`         | Tests FCFS queue ordering                                               |
| `generate_tests.py`    | Generates 100 M/M/1 test vectors                                        |
| `verify_tests.py`      | Verifies calculated results against the reference model                 |
| `mm1_test_vectors.csv` | Stores generated test cases and expected M/M/1 results                  |
| `.gitignore`           | Prevents Python cache files from being committed                        |
| `README.md`            | Project documentation                                                   |

---

## Testing and Verification

The project currently contains **100 M/M/1 test vectors**.

```text
Total Tests    : 100
Stable Cases   : 80
Unstable Cases : 20
```

The test cases include both normal stable queues and unstable conditions where:

```text
λ ≥ μ
```

The verification program checks:

* Queue stability
* Utilization `ρ`
* `P0`
* `Pn`
* `L`
* `Lq`
* `W`
* `Wq`
* `L = λW`
* `Lq = λWq`

This provides a controlled software reference before moving toward hardware implementation.

---

## Example M/M/1 Output

Example input:

```text
λ = 3.39
μ = 17.22
n = 5
```

Example output:

```text
========== M/M/1 MODEL ==========
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
```

---

## Example FCFS Output

For five incoming requests:

```text
R1: Arrival=0, Service=3
R2: Arrival=1, Service=2
R3: Arrival=2, Service=4
R4: Arrival=3, Service=1
R5: Arrival=4, Service=2
```

The processing results are:

```text
R1: Start=0  Completion=3  Waiting=0
R2: Start=3  Completion=5  Waiting=2
R3: Start=5  Completion=9  Waiting=3
R4: Start=9  Completion=10 Waiting=6
R5: Start=10 Completion=12 Waiting=6
```

The processing order remains:

```text
R1 → R2 → R3 → R4 → R5
```

This demonstrates the FCFS behavior of the implemented queue.

---

## Technologies Used

* **Python**
* Queueing Theory
* M/M/1 Mathematical Model
* FCFS Queue
* CSV Test Vectors
* Automated Verification
* Git / GitHub

---

## Current Project Status

| Component                  | Status    |
| -------------------------- | --------- |
| M/M/1 mathematical model   | Completed |
| Python implementation      | Completed |
| FCFS queue                 | Completed |
| Request model              | Completed |
| 100 test vectors           | Completed |
| Automated verification     | Completed |
| GitHub repository          | Completed |
| Fixed-point implementation | Planned   |
| Verilog implementation     | Planned   |
| FPGA simulation            | Planned   |
| Zynq integration           | Planned   |
| Real application requests  | Planned   |
| M/M/N extension            | Planned   |

---

## Future Development

The project will be developed in stages.

### Stage 1 — Current

```text
M/M/1 Mathematical Model
        ↓
Python Implementation
        ↓
FCFS Queue
        ↓
Testing & Verification
```

### Stage 2 — Fixed-Point Model

The floating-point Python model will be converted into a fixed-point representation suitable for digital hardware.

The proposed representation is:

```text
Q16.16
32-bit fixed-point
```

The fixed-point model will first be compared against the existing floating-point reference implementation.

### Stage 3 — FPGA Implementation

After numerical verification, the model will be implemented using hardware description logic and tested through simulation.

The target platform is a **Zynq FPGA**.

The planned hardware interface will include:

```text
Inputs:
    λ
    μ
    n
    start
    clock
    reset

Outputs:
    done
    stable
    ρ
    P0
    Pn
    L
    Lq
    W
    Wq
```

### Stage 4 — Real Application Integration

The eventual system will accept real application events:

```text
Website / Application
        ↓
Incoming Marketing Events
        ↓
Request Collector
        ↓
FCFS Queue
        ↓
Queueing Model
        ↓
Processing Servers
        ↓
Completed Requests
```

### Stage 5 — M/M/N Extension

The current M/M/1 system uses one server.

The long-term goal is to extend the model to **M/M/N**, allowing multiple processing servers:

```text
                 ┌── Server 1
                 │
Requests → Queue ├── Server 2
                 │
                 ├── Server 3
                 │
                 └── Server N
```

The overall system architecture will remain similar; the single-server queueing model will be extended to support multiple servers.

---

## Project Goal

The final goal is to develop a queueing-based request-processing system that can:

1. Receive incoming digital marketing requests.
2. Maintain request order using FCFS.
3. Analyze queue behavior using queueing theory.
4. Process requests using multiple processing resources.
5. Implement the computational model on Zynq FPGA hardware.
6. Eventually support an M/M/N queueing model for multiple servers.

---

## Repository

GitHub repository:

**os-queueing-project**

The repository contains the current Python implementation, test generation, verification framework, and project documentation.
