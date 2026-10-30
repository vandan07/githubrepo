<div align="center">

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- 🏟️ HERO BANNER: STADIUM COMMAND CENTER                             -->
<!-- ═══════════════════════════════════════════════════════════════════ -->
<img src="./assets/hero-banner.svg" alt="Vandan Mahajan — Systems × Product × AI" width="100%"/>

<br/><br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- ⚡ QUICK MATCH TELEMETRY (CONNECT & BADGES)                         -->
<!-- ═══════════════════════════════════════════════════════════════════ -->
<a href="https://linkedin.com/in/vandan-mahajan"><img src="https://img.shields.io/badge/LinkedIn-D31427?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=0B0D13" alt="LinkedIn"/></a>
<a href="mailto:vandanmahajan@example.com"><img src="https://img.shields.io/badge/Email-E2B755?style=for-the-badge&logo=gmail&logoColor=0B0D13&labelColor=0B0D13" alt="Email"/></a>
<a href="https://github.com/vandan-mahajan"><img src="https://img.shields.io/badge/GitHub-D31427?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=0B0D13" alt="GitHub"/></a>
<a href="#"><img src="https://img.shields.io/badge/Base-Bengaluru%2C_IN-0B0D13?style=for-the-badge&logo=googlemaps&logoColor=E2B755&labelColor=171B26" alt="Location"/></a>

<br/><br/>

<img src="./assets/match-divider.svg" alt="Seam divider" width="100%"/>

</div>

<br/>

## 🏏 THE PLAYBOOK // 01: FIRST-PRINCIPLES ENGINEERING

> *"In cricket, you don't step out to swing blindly at every delivery. You read the pitch, feel the bounce, study the field placements, and select the precise shot. Engineering is identical.*
>
> **Good engineering isn't about writing more code. It's about making better decisions.**"

<div align="center">
  <img src="./assets/think-first.svg" alt="The First-Principles Decision Engine" width="100%"/>
</div>

<br/>

Most software engineering failures don't originate from syntax errors or framework limitations—they come from **faulty reasoning, uninspected assumptions, and premature complexity**.

Before writing a single line of code, my mental compiler runs through this decision tree:

```yaml
1. The Pitch (Root Diagnosis):
   - What is the actual, unadorned problem?
   - Why does it exist right now?
   - What hidden assumptions are masquerading as requirements?

2. The Field (System Boundaries & Risk):
   - Where will this fail when traffic multiplies 10x?
   - Where are the database lock contentions, serialization bottlenecks, and network hops?
   - If this dependency dies at 03:00 AM, how gracefully does the system degrade?

3. The Shot (Radical Simplicity):
   - What is the absolute simplest architecture that permanently solves this?
   - Can we avoid introducing a new distributed component?
   - Does this solution make sound, practical sense?

4. The Delivery (Execution & Measurement):
   - Write clean, idiomatic, test-backed code.
   - Benchmark with real workloads (p99 latency, heap allocation, throughput).
   - Zero clever hacks; maximum long-term readability.
```

---

<div align="center">
  <img src="./assets/match-divider.svg" alt="Seam divider" width="100%"/>
</div>

## 🛡️ THE PLAYING XI // TECHNICAL ARSENAL

Every technology in my lineup has earned its place through trial by production. **Zero bench warmers. No buzzword inflation.**

<div align="center">
  <img src="./assets/playing-xi.svg" alt="The Playing XI Lineup" width="100%"/>
</div>

<br/>

<table>
  <thead>
    <tr style="border-bottom: 2px solid #D31427;">
      <th align="left" width="22%">Tactic</th>
      <th align="left" width="38%">Technologies &amp; Engines</th>
      <th align="left" width="40%">Engineering Judgment &amp; Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Top Order<br/>(Core Backend)</b></td>
      <td>
        <code>Java (17 / 21)</code> <code>Spring Boot</code><br/>
        <code>Spring MVC</code> <code>JPA / Hibernate</code><br/>
        <code>Virtual Threads</code> <code>Concurrency</code>
      </td>
      <td>
        The bedrock anchors. Chosen for strong type safety, memory model predictability, mature concurrency primitives, and massive enterprise throughput.
      </td>
    </tr>
    <tr>
      <td><b>Middle Order<br/>(State &amp; Cache)</b></td>
      <td>
        <code>PostgreSQL</code> <code>MySQL</code><br/>
        <code>Redis (Cluster / PubSub)</code> <code>MongoDB</code>
      </td>
      <td>
        Architecting clean relational schemas, rigorous query-plan analysis, index tuning, and distributed locking to prevent cache stampedes.
      </td>
    </tr>
    <tr>
      <td><b>Pace Attack<br/>(Event &amp; Infra)</b></td>
      <td>
        <code>Apache Kafka</code> <code>RabbitMQ</code><br/>
        <code>Docker</code> <code>AWS</code> <code>Jenkins</code> <code>Linux</code>
      </td>
      <td>
        Asynchronous decoupling, partition-keyed event streaming, fault-tolerant consumer groups, containerized CI/CD, and repeatable deployments.
      </td>
    </tr>
    <tr>
      <td><b>The Finisher<br/>(Generative AI)</b></td>
      <td>
        <code>LLMs Architecture</code> <code>RAG Pipelines</code><br/>
        <code>ChromaDB</code> <code>Vector Embeddings</code> <code>Ollama</code>
      </td>
      <td>
        Bridging deterministic backend systems with non-deterministic probabilistic models. Chunking strategies, hybrid vector + lexical search, and context optimization.
      </td>
    </tr>
    <tr>
      <td><b>Fielding Unit<br/>(Interface)</b></td>
      <td>
        <code>React</code> <code>Vite</code> <code>TypeScript</code> <code>JavaScript</code>
      </td>
      <td>
        Clean, functional UI surfaces and operator dashboards built to observe, control, and consume backend systems.
      </td>
    </tr>
  </tbody>
</table>

---

<div align="center">
  <img src="./assets/match-divider.svg" alt="Seam divider" width="100%"/>
</div>

## 🏆 MATCH HIGHLIGHTS // INNINGS BREAKDOWN

Real engineering problems, architectural decisions, and measurable production impact.

<br/>

### 01. Distributed Transaction & Real-Time Event Ledger Engine
> **High-Throughput Ingestion Architecture // Core Backend & Messaging**

<details open>
<summary><b>View Tactical Breakdown &amp; Metrics</b></summary>
<br/>

* **The Problem:** Direct database writes during burst traffic spikes ($>3,500\text{ req/s}$) choked PostgreSQL connection pools. Row-level lock contention on account balances resulted in frequent deadlocks and inflated p99 latency beyond $1,200\text{ms}$.
* **The Engineering Decision:** Decoupled ingress from persistence. Replaced synchronous HTTP database mutations with an event-driven architecture using **Kafka partitioned topics** keyed by `accountId` to guarantee strict sequential ordering per tenant. Implemented a **Redis write-back buffer** with Lua-scripted atomic validations.
* **The Architecture:**
  ```text
  [Client Requests] 
         │ 
         ▼
  [Spring Boot Gateway] ──(Produce Event)──► [Kafka Topic: ledger-inbound] (Key: account_id)
                                                    │
                                                    ▼
                                           [Consumer Pool] ◄──► [Redis Atomic State]
                                                    │
                                           (Batched Flushes)
                                                    ▼
                                           [PostgreSQL Database]
  ```
* **Key Challenge Solved:** Handled consumer group rebalances without processing duplicate ledger events by enforcing idempotent deduplication keys inside Redis with automated 10-minute expiry windows.
* **Measurable Results:**
  - Ingestion Throughput: **$850\text{ req/s} \to 5,400+\text{ req/s}$** ($6.3\times$ improvement)
  - p99 Latency: **$1,200\text{ms} \to 38\text{ms}$**
  - Database Deadlocks: **$14\%\text{ under peak load} \to 0\%$**
* **Stack:** `Java 21` `Spring Boot` `Apache Kafka` `PostgreSQL` `Redis` `Docker`

</details>

---

### 02. Enterprise Hybrid RAG & Context Intelligence Gateway
> **Knowledge Retrieval Pipeline // Generative AI & Vector Search**

<details open>
<summary><b>View Tactical Breakdown &amp; Metrics</b></summary>
<br/>

* **The Problem:** Engineers querying complex technical documentation, architectural decision records (ADRs), and internal API specifications suffered from severe LLM hallucinations and unacceptable retrieval latency ($15.2\text{s}$) caused by naive brute-force semantic vector chunking.
* **The Engineering Decision:** Abandoned fixed-token chunking in favor of **AST-aware recursive character chunking** that preserves code block and heading hierarchy. Introduced **Hybrid Search (BM25 Lexical + Cosine Vector Embeddings)** merged via **Reciprocal Rank Fusion (RRF)** before feeding context into local Ollama models.
* **The Architecture:**
  ```text
  [Technical Documents] ──► [AST/Hierarchy Chunker] ──► [Dense Vectors] ──► [ChromaDB]
                                                    ──► [Sparse Lexical] ──► [BM25 Index]
                                                                                │
  [User Prompt] ──────────────────► [Reciprocal Rank Fusion] ◄──────────────────┘
                                             │
                                     (Top-K Filtered)
                                             ▼
                               [Ollama LLM Streaming Engine] ──► [Precise Answer + Citations]
  ```
* **Key Challenge Solved:** Hallucinations on specific function signatures and config parameters were eliminated by introducing strict provenance citations and setting dynamic cross-entropy thresholding on retrieved chunks.
* **Measurable Results:**
  - Query-to-Answer Latency: **$15.2\text{s} \to 0.85\text{s}$** ($94\%$ faster)
  - Context Retrieval Precision: **$58\% \to 94.2\%$**
  - Hallucination Rate on Technical Entities: **Near-Zero (Strict Provenance Enforced)**
* **Stack:** `Python` `Spring AI / Java` `ChromaDB` `Ollama` `Vector Embeddings` `FastAPI`

</details>

---

### 03. Apex Distributed Cache & Thundering Herd Defense
> **Resilient Systems Topology // In-Memory Caching & Concurrency**

<details open>
<summary><b>View Tactical Breakdown &amp; Metrics</b></summary>
<br/>

* **The Problem:** In high-concurrency microservices, whenever heavily-accessed cached entities expired simultaneously, thousands of threads immediately missed cache and hammered the downstream database in a classic **Cache Stampede (Thundering Herd)**, causing cascade connection pool starvation.
* **The Engineering Decision:** Engineered a two-tier caching topology: local in-memory L1 cache backed by a distributed Redis L2 cluster. Combined distributed mutex locks with the **XFetch probabilistic early expiration algorithm** to asynchronously recompute hot cache entries *before* they officially expire.
* **Measurable Results:**
  - Cache Hit Ratio: **$71.4\% \to 98.7\%$**
  - Database Load Reduction: **$86\%\text{ CPU} \to 18\%\text{ CPU}$** under identical 10,000 QPS load
  - p99 Latency during mass invalidations: **Remained stable at $< 25\text{ms}$**
* **Stack:** `Java` `Spring Boot` `Redis Cluster` `Resilience4j` `MySQL` `AWS`

</details>

---

<div align="center">
  <img src="./assets/match-divider.svg" alt="Seam divider" width="100%"/>
</div>

## 📊 LIVE MATCH TELEMETRY // SCOREBOARD

<div align="center">
  <img src="./assets/scoreboard.svg" alt="Digital Stadium Scorecard" width="100%"/>
</div>

<br/>

<div align="center">

### 🏟️ The 3D Contribution Arena

*Every commit raises another brick in the pavilion — updated automatically every night.*

<img src="./profile-3d-contrib/profile-night-view.svg" alt="3D Contribution Arena" width="100%"/>

</div>

---

<div align="center">
  <img src="./assets/match-divider.svg" alt="Seam divider" width="100%"/>
</div>

## 🎯 CURRENT FORM & UPCOMING FIXTURES

What I'm actively researching, testing, and building in the engineering nets:

* 🔬 **Virtual Threads & Structured Concurrency:** Profiling carrier thread pinning, lock contention patterns, and zero-overhead non-blocking I/O in Java 21 / Project Loom.
* 🤖 **Autonomous Multi-Agent Systems:** Building self-correcting agent loops with deterministic verification harnesses to eliminate LLM hallucinations in system ops.
* ⚡ **Zero-Copy Serialization:** Benchmarking Protobuf and FlatBuffers over gRPC to minimize garbage collection pauses in distributed event pipelines.
* 📖 **Reading & Deconstructing:** Designing Data-Intensive Applications (Kleppmann) & Database Internals (Petrov).

---

<div align="center">

## 🤝 THE PAVILION // MATCH CREDENTIALS & CONNECT

*Always open to discuss distributed systems, backend architecture, high-performance Java, or impactful engineering opportunities.*

<br/>

<a href="https://linkedin.com/in/vandan-mahajan"><img src="https://img.shields.io/badge/LinkedIn-D31427?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=0B0D13" alt="LinkedIn"/></a>
<a href="mailto:vandanmahajan@example.com"><img src="https://img.shields.io/badge/Email-E2B755?style=for-the-badge&logo=gmail&logoColor=0B0D13&labelColor=0B0D13" alt="Email"/></a>
<a href="https://github.com/vandan-mahajan"><img src="https://img.shields.io/badge/GitHub-D31427?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=0B0D13" alt="GitHub"/></a>

<br/><br/>

<img src="./assets/match-divider.svg" alt="Seam divider" width="60%"/>

<br/>

**PLAY BOLD. THINK FIRST. EXECUTE PRECISE.** 🏏

<sub>Engineered with first-principles reasoning &amp; craftsmanship · Bengaluru, India</sub>

</div>
