# 🧠 Low-Level Design (LLD) Practice — FAANG-Style

Welcome to my **Low-Level Design** preparation repository. This repo contains detailed, production-style implementations of classic **Object-Oriented Design** problems that are frequently asked in interviews at companies like Amazon, Uber, Microsoft, and Atlassian.

Each problem lives in its own folder (or branch) with:
- a dedicated **README** explaining assumptions, UML, patterns, and class diagrams;
- a **modular Python implementation** following SOLID principles;
- optional **tests** and CLI demos;  
- a **commit roadmap** (8–10 green pushes) showing my iteration process.

---

## Learning Goals
- Strengthen understanding of **OOP concepts** (Encapsulation, Inheritance, Composition, Polymorphism).  
- Apply **Design Patterns** (Strategy, Factory, Observer, Singleton).  
- Build scalable and extensible designs with **clear responsibilities** and **maintainable abstractions**.  
- Prepare for FAANG-style **LLD interviews** and system design discussions.

---

## Problems Covered (so far)

| # | Problem | Key Concepts | Status |
|---|----------|---------------|---------|
| 1️⃣ | [Parking Lot](./ParkingLot/) | Multi-floor design, Allocation, Strategy pattern | 🚧 In progress |
| 2️⃣ | Vending Machine | State machine, Factory pattern | ⏳ Planned |
| 3️⃣ | Splitwise | Expense sharing, Observer pattern | ⏳ Planned |
| 4️⃣ | Elevator System | State + Command patterns | ⏳ Planned |
| 5️⃣ | Library Management | Aggregation, Search APIs | ⏳ Planned |
| 6️⃣ | Chess/Tic-Tac-Toe | Rules engine, Strategy pattern | ⏳ Planned |

---

## Repo Structure
```

LLD/
│
├── README.md               # (this file)
│
├── ParkingLot/             # each problem in its own subfolder or branch
│   ├── README.md
│   ├── parking_lot/
│   ├── tests/
│   └── requirements.txt
│
├── VendingMachine/
│   └── ...
│
└── Splitwise/
└── ...

````

---

## Tech Stack
- **Language:** Python 3.10+
- **Patterns:** SOLID, GoF Design Patterns
- **Testing:** pytest
- **Versioning:** One branch per problem (e.g., `feature/parking-lot`)
- **Docs:** Markdown diagrams + ASCII UML

---

## Setup (for any design)
```bash
# clone and move to specific problem folder
git clone https://github.com/<your_username>/LLD.git
cd LLD/ParkingLot

# run tests
pytest -v
````

---

## Next Up

→ Start with [Parking Lot](./ParkingLot/) — the foundational LLD problem that touches every OOP concept.
You’ll find:

* detailed design docs,
* UML,
* patterns,
* and full Python code walkthroughs with tests.

---

## Created by **Rishabh Agarwal** and **Priya Sisodia** — two CS students exploring large-scale design and OOP mastery.
<!-- Connect on [LinkedIn](https://linkedin.com/in/...) or explore more on [GitHub](https://github.com/...). -->

---

